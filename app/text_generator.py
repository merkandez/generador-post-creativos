
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from app.prompts import get_prompt_template
from dotenv import load_dotenv
import os

load_dotenv()

def generate_text(tema: str, audiencia: str, plataforma: str) -> str:
    prompt = get_prompt_template(plataforma)

    llm = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",  # Modelo de OpenRouter
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run({
        "tema": tema,
        "audiencia": audiencia
    })

    return output


# text_generator.py para Ollama (comentado porque no se usa en este momento)

# from langchain.llms import Ollama
# from langchain.chains import LLMChain
# from app.prompts import get_prompt_template

# def generate_text(tema: str, audiencia: str, plataforma: str) -> str:
#     """
#     Genera un texto usando LangChain + Ollama en función de la plataforma y tema.
#     """
#     # 1. Obtener el prompt adecuado
#     prompt = get_prompt_template(plataforma)

#     # 2. Crear el modelo (asegúrate de haber ejecutado: `ollama run mistral`)
#     llm = Ollama(model="mistral")

#     # 3. Crear la cadena LangChain
#     chain = LLMChain(llm=llm, prompt=prompt)

#     # 4. Ejecutar el modelo con las variables necesarias
#     output = chain.run({
#         "tema": tema,
#         "audiencia": audiencia
#     })

#     return output

