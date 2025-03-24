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

class ResumeRequest(BaseModel):
    background: str
    job_description: str
    model: str = "mixtral"

@app.post("/api/generate-resume")
async def generate_resume(request: ResumeRequest):
    # Validate model
    allowed_models = ['mixtral', 'llama3', 'phi3', 'llama2']
    if request.model not in allowed_models:
        raise HTTPException(status_code=400, detail="Invalid model selected")
    
    try:
        prompt = f"""Create a professional resume based on this background:
{request.background}

Tailor it specifically for this job description:
{request.job_description}

Include these sections:
- Professional Summary
- Core Competencies
- Technical Skills
- Professional Experience
- Education

Format requirements:
- Use bullet points for achievements
- Quantify results where possible
- Use industry-specific keywords"""
        
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
                        "error": "Ollama API !",
                        "status_code": response.status_code,
                        "response": error_details
                    }
                )
            
            # Return the generated resume
            return {"resume": response.json()["response"]}
    
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