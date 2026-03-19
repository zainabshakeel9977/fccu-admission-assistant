from fastapi import APIRouter
from app.models.schema import QueryRequest, QueryResponse
from app.services.retriever import retrieve_chunks, build_context
from app.services.llm import generate_answer

# Create a router instance to group related endpoints
router = APIRouter()

# Define a POST endpoint at /query
# response_model ensures the output follows QueryResponse schema
@router.post("/query", response_model=QueryResponse)

def query_endpoint(request: QueryRequest):
    """
    Handles user queries by retrieving relevant context
    and generating an answer using an LLM.
    """
    
    # Step 1: Retrieve relevant document chunks
    # based on the user's question and program
    results = retrieve_chunks(request.question, request.program)
    
    # Step 2: Handle case when no relevant information is found
    if not results: 
        return {
            "answer":"I could not find relevant information. Please contact FCCU Admission Office",
            "sources":[]
        }
    
    # Step 3: Build LLM-ready context and extract source references
    context, sources = build_context(results.points)
    # Step 4: Generate an answer using the LLM
    answer = generate_answer(request.question, context)
    
    # Step 5: Return the final structured response
    return {
        "answer": answer,
        "sources":sources
    }

