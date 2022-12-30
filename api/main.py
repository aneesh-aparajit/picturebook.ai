from fastapi import FastAPI
from pydantic import BaseModel
from text2image import obtain_image
from fastapi.responses import StreamingResponse
from translate import Translator
import io


description = """This API has two parts:
1. Text to Text
    - This is the text generation model which generates new text
2. Text to Image
    - This uses the text generated in the previous endpoint and generates images.
    """

app = FastAPI(
    title="picturebook.ai",
    description=description,
    version="1.0.0",
    contact={"name": "Aneesh Aparajit G", "url": "https://github.com/aneesh-aparajit"},
)

translator = Translator(from_lang="English", to_lang="Tamil")


class TextInput(BaseModel):
    prompt: str
    seed: int = 42
    num_iterface_steps: int = 51
    guidance_scale: float = 7.5


@app.post("/english/text2text", tags=["English"])
def generate_text(inputs: TextInput):
    return {"status": "To be completed..."}


@app.post("/english/text2img", tags=["English"])
def generate_img(inputs: TextInput):
    image = obtain_image(**inputs.dict())
    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")


@app.post("/tamil/text2text", tags=["Tamil"])
def generate_text(inputs: TextInput):
    return {"status": "To be completed..."}


@app.post("/tamil/text2img", tags=["Tamil"])
def generate_img(inputs: TextInput):
    args = inputs.dict()
    args["prompt"] = translator.translate(inputs.prompt)
    image = obtain_image(**args)
    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")
