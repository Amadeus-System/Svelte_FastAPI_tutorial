

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Create an instance of FastAPI
# This object will handle all API routes and configurations.
app = FastAPI()


# Define the list of origins (URLs) allowed to access the API.
# This is necessary for enabling Cross-Origin Resource Sharing (CORS),
# which lets the frontend (running on a different port) communicate with this backend.
origins = [
    "http://127.0.0.1:5173", # Local address for the frontend development server
    "http://localhost:5173", # Alternative local address for the frontend
]


# Add the CORS middleware to the FastAPI application
# This middleware automatically adds the appropriate CORS headers to responses.
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,  # Allow incoming requests from these origins
    allow_credentials=True, # Allow sending cookies and authentication headers
    allow_methods=["*"],    # Allow all HTTP methods (e.g. GET, POST, PUT, DELETE)
    allow_headers=["*"],    # Allow all headers in requests
)


@app.get("/hello")
def hello() -> dict:
    """ 
    Handle GET requests at the "/hello" endpoint.
    
    This function is triggered when a client sends a GET request to "/hello".
    It returns a simple JSON message as a greeting for demonstration purposes.

    Args:
        None
    Returns:
        result (dict): A dictionary containing a "message" key with a greeting string.
    """
    return {
        "message": "안녕하세요 파이보!!"
    }