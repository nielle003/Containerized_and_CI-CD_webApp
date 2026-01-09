from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {"message": "Hello from simple web app!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}