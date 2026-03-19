from fastapi import FastAPI
from app.routes.query import router


# Create a FastAPI application instance
app = FastAPI(title="FCCU Admission Assistant")
app.include_router(router)

# # Define a GET endpoint at the root path "/"
# @app.get("/")
# def health_check():
#     # Return a simple JSON response confirming the server is running
#     return {"status":"ok"}


#############################################################
#An API is a mechanism that enables two software programs to interact and exchange information
#Route is the internal mapping in the server that connects a URL path and HTTP method to a function.
#Endpoint is the actual URL that a client uses to access the API.
#A route handler is the function that gets executed when a specific route is accessed in a web application.
#############################################################