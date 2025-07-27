from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    role: str  
    content: str

class QueryRequest(BaseModel):
    messages: List[ChatMessage]

class QueryResponse(BaseModel):
    response: str
