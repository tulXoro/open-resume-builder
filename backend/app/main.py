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
        prompt = f"""You are an expert resume writer. Generate bullet points for job experience based on the following details:

The user's current or previous job title is "{request.user_job_title}", and their responsibilities include:
{request.user_job_description}

The target job title is "{request.target_job_title}", and the job description is as follows:
{request.target_job_description}

Focus on highlighting transferable skills and tailoring the bullet points to match the target job. Use industry-specific keywords from the target job description to maximize ATS compatibility. Emphasize relevant achievements and skills, quantify results where possible, and use professional, action-oriented language. Ensure the bullet points align with the key responsibilities and qualifications of the target job."""

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
                        "error": f"Ollama API ({request.model}) failed to generate bullet points.",
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