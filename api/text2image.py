from __future__ import annotations
import torch
from PIL.Image import Image
from pathlib import Path

from diffusers import StableDiffusionPipeline
import config


token = open("./token.txt", "r").readlines()[0].strip()

pipeline = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    revision="fp16",
    torch_dtype=torch.float16,
    use_auth_token=token,
)

pipeline.to(config.DEVICE)


def obtain_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_interface_steps: int = 51,
    guidance_scale: float = 7.5,
):
    generator = None if seed is None else torch.Generator("cpu").manual_seed(42)
    print(f"Using Device: {pipeline.device}")
    image: Image = pipeline(
        prompt=prompt,
        guidance_scale=guidance_scale,
        num_inference_steps=num_interface_steps,
        generator=generator,
    ).images[0]
    return image
