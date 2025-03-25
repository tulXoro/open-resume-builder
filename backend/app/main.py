from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx


app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
    
local_models = []

with httpx.Client() as client:
    try:
        response = client.get("http://ollama:11434/api/tags")
        local_models = response.json()
    except httpx.RequestError as e:
        local_models = []  # Fallback to an empty list if the request fails
        print(f"Error fetching models: {str(e)}")

class ResumeRequest(BaseModel):
    user_job_title: str
    user_job_description: str
    target_job_title: str
    target_job_description: str
    model: str = ""
    
@app.get("/api/models")
async def get_models():
    return local_models


@app.post("/api/generate-experience")
async def generate_experience(request: ResumeRequest):

    try:
        prompt = f"""[ROLE] Expert Resume Writer
[TASK] Generate bullet points for job experience
[FOCUS] Highlight transferable skills from the user's experience:
- Job Title: {request.user_job_title}
- Job Description: {request.user_job_description}
[TARGET JOB] Tailor the bullet points to match this target job:
- Job Title: {request.target_job_title}
- Job Description: {request.target_job_description}
[FORMAT] Provide concise bullet points
[REQUIREMENTS]
- Use industry-specific keywords from the target job description to maximize ATS compatibility
- Emphasize relevant achievements and skills
- Quantify results where possible
- Use professional, action-oriented language
- Ensure the bullet points align with the target job's key responsibilities and qualifications"""

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://ollama:11434/api/generate",
                json={
                    "model": request.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.7,
                        "num_ctx": 4096
                    }
                },
                timeout=30.0
            )
            
            # Handle non-200 status codes with detailed error information
            if response.status_code != 200:
                
                try:
                    error_details = response.json()  # Attempt to parse the error response as JSON
                except Exception:
                    error_details = response.text  # Fallback to raw text if JSON parsing fails
                raise HTTPException(
                    status_code=response.status_code,
                    detail={
                        "error": "Ollama API! " + request.model + " failed to generate bullet points",
                        "response": error_details
                    }
                )
            
            # Return the generated bullet points
            return {"bullet_points": response.json()["response"]}
    
    except httpx.RequestError as e:
        # Handle network-related errors (e.g., connection issues, timeouts)
        raise HTTPException(
            status_code=500,
            detail=f"Network error occurred while contacting Ollama API: {str(e)}"
        )
    
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )