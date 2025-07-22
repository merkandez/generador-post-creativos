from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(token=os.getenv("HF_API_KEY"))

def generate_image(prompt: str, output_path="generated_image.png"):
    """
    Genera una imagen usando Hugging Face InferenceClient y Stable Diffusion.
    Devuelve la ruta de la imagen guardada.
    """
    img = client.text_to_image(prompt)
    img.save(output_path)
    return output_path

if __name__ == "__main__":
    prompt = "ilustración moderna sobre inteligencia artificial creativa en redes sociales"
    try:
        path = generate_image(prompt)
        print(f"\n✅ Imagen generada y guardada en: {path}")
    except Exception as e:
        print("❌ Error:", e)
