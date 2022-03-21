from os import path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import converter
import uvicorn

app = FastAPI()

app.mount(
    "/static",
    # StaticFiles(directory=Path(__file__).absolute() / "static"),
    StaticFiles(directory=path.join(path.dirname(__file__), "static")),
    name="static",
)

templates = Jinja2Templates(directory="static")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/image")
def image(url: str):
    image = converter.text_to_image(url)
    return FileResponse(image)


@app.get("/text", response_class=FileResponse)
def text(url: str):
    ascii_file = converter.image_to_ascii(url)
    return ascii_file


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(levelname)s - %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(levelname)s - %(message)s"
    uvicorn.run("main:app", host="0.0.0.0", port=8080,
                reload=True, log_level="info", log_config=log_config)
