from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def hello() -> dict[str, str]:
    return {"message": "hello FastAPI!"}
