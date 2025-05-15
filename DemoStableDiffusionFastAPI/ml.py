from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline
from PIL.Image import Image


token_path = Path("token.txt")
token = token_path.read_text().strip()

model_id = "CompVis/stable-diffusion-v1-4"

#get token at http://huggingface.co/settings/tokens

pipe = StableDiffusionPipeline.from_pretrained(model_id,
                                               use_safetensors=True,
                                               use_auth_token=token)

pipe.to("cuda" if torch.cuda.is_available() else "cpu")

prompt = "A photograph of an astronaut riding a horse"

#image = pipe(prompt)["sample"][0]

def obtain_image(
        prompt: str,
        *,
        seed: int | None = None,
        num_inference_steps: int = 50,
        guidance_scale: float = 7.5
) -> Image:
    generator = torch.Generator("cpu").manual_seed(seed) if seed is not None else None
    print(f"Using device: {pipe.device}")
    image: Image = pipe(
        prompt,
        guidance_scale=guidance_scale,
        num_inference_steps=num_inference_steps,
        generator=generator,
    ).images[0]
    return image

#image = obtain_image(prompt, num_inference_steps=5, seed=1024)