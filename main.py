import io
from fastapi import FastAPI
from fastapi.responses import FileResponse
import converter
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/image")
def image(image_url: str):
    image = converter.text_to_image(image_url)
    return FileResponse(image)


@app.get("/text", response_class=FileResponse)
def text(image_url: str):
    ascii_file = converter.image_to_ascii(image_url)
    return ascii_file


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(levelname)s - %(message)s"
    uvicorn.run("main:app", host="0.0.0.0", port=8080,
                reload=True, log_level="info", log_config=log_config)
