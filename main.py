from  fastapi import FastAPI
import uvicorn

app = FastAPI(title="Demo Fast Api",version="1.0.0")

@app.get("/test")
async  def test():
    return {"hello"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)