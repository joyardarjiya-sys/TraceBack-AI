from fastapi import FastAPI
app = FastAPI(
    title =" TraceBack-AI",
    description = " Intelligent digital trust and fraud detection system ",
    version =" 1.0.0"
)
@app.get("/")
def home():
    return{
        "project": "TraceBack-AI",
        "status" : "ONLINE",
        "message" : "Digital investigation system is running"
    }

@app.get("/health")
def health():
    return{
    "status" : " Healthy"
}

