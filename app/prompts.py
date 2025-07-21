from langchain.prompts import PromptTemplate

# Prompt para LinkedIn
linkedin_prompt = PromptTemplate.from_template(
    """Escribe una publicación profesional para LinkedIn sobre el tema "{tema}".
Debe ser informativa, con tono cercano y profesional, pensada para una audiencia de {audiencia}.
Escríbelo en primera persona si es posible."""
)

# Prompt para Instagram
instagram_prompt = PromptTemplate.from_template(
    """Crea una publicación para Instagram sobre el tema "{tema}".
Usa un tono creativo, emocional y visual. Dirígete a una audiencia de {audiencia}.
Hazlo breve y directo. Incluye emojis si es natural."""
)

# Función para obtener el prompt adecuado
def get_prompt_template(plataforma: str):
    plataforma = plataforma.lower()
    if plataforma == "linkedin":
        return linkedin_prompt
    elif plataforma == "instagram":
        return instagram_prompt
    else:
        raise ValueError(f"No hay plantilla de prompt para la plataforma: {plataforma}")
