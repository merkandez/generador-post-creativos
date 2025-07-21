from langchain.prompts import PromptTemplate

# Directrices de estilo universales
extra_estilo = """
Mantén el mensaje y la estructura general, pero:
– Agrega emociones sutiles, expresiones humanas y un lenguaje más conversacional.
– Usa frases con ritmos variados: combina oraciones cortas y largas.
– Evita un tono demasiado perfecto o robótico.
– Sustituye palabras genéricas por otras más específicas o con carga emocional.
– Añade conectores suaves y naturales como: “además”, “la verdad es que”, “y es que”, etc.
– Siempre que sea posible, incluye ejemplos, analogías o detalles que hagan el texto más cercano.
– No utilices estructuras repetitivas, frases perfectamente simétricas o un lenguaje excesivamente neutro.
"""

# Prompt para LinkedIn
linkedin_prompt = PromptTemplate.from_template(
    f"""Escribe una publicación profesional para LinkedIn sobre el tema "{{tema}}".
Debe ser informativa, con tono cercano y profesional, pensada para una audiencia de {{audiencia}}.

{extra_estilo}
"""
)

# Prompt para Instagram
instagram_prompt = PromptTemplate.from_template(
    f"""Crea una publicación para Instagram sobre el tema "{{tema}}".
Usa un tono creativo, emocional y visual. Dirígete a una audiencia de {{audiencia}}.
Hazlo breve y directo. Incluye emojis si es natural.

{extra_estilo}
"""
)

# Prompt para blog
blog_prompt = PromptTemplate.from_template(
    f"""Escribe un artículo de blog sobre: "{{tema}}".
Debe estar optimizado para SEO y ser claro y estructurado.
El público objetivo es: {{audiencia}}. Usa subtítulos y llamadas a la acción.

{extra_estilo}
"""
)

# Prompt para Twitter/X
twitter_prompt = PromptTemplate.from_template(
    f"""Escribe un tuit o hilo corto sobre: "{{tema}}".
Debe ser claro, provocador y dirigido a una audiencia de {{audiencia}}.
Usa hashtags relevantes si aplica. Límite: 280 caracteres por mensaje.

{extra_estilo}
"""
)

# Prompt para infantil
infantil_prompt = PromptTemplate.from_template(
    f"""Explica el tema "{{tema}}" de forma divertida y sencilla para niños de entre 7 y 10 años.
Usa ejemplos, emojis y un lenguaje accesible para esa edad.

{extra_estilo}
"""
)

# Función para obtener el prompt adecuado
def get_prompt_template(plataforma: str):
    plataforma = plataforma.lower()
    if plataforma == "linkedin":
        return linkedin_prompt
    elif plataforma == "instagram":
        return instagram_prompt
    elif plataforma == "blog":
        return blog_prompt
    elif plataforma == "twitter":
        return twitter_prompt
    elif plataforma == "infantil":
        return infantil_prompt
    else:
        raise ValueError(f"No hay plantilla de prompt para la plataforma: {plataforma}")
