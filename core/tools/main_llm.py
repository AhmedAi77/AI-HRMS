from crewai import LLM
from django.conf import settings

basic_llm = LLM(
    model=settings.OPENAI_MODEL,
    temperature=settings.OPRNAI_DEFAULT_TEMPERATURE,
    apikey=settings.OPENAI_APIKEY,
)