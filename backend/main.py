from fastapi import FastAPI, HTTPException
from schemas import QueryRequest, QueryResponse
from services import get_llm_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Medical Symptom Checker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query", response_model=QueryResponse)
def check_symptoms(request: QueryRequest):
    try:
        response = get_llm_response(request.messages)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
