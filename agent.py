
import os
import requests
import wikipedia
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.agents import initialize_agent


load_dotenv()

# Configurar Wikipedia en español
wikipedia.set_lang("es")

# 1. Herramienta: API de clima simple
def get_weather(city: str) -> str:
    url = f"https://wttr.in/{city}?format=%C+%t"
    weather = requests.get(url).text
    return weather

weather_tool = Tool(
    name="Weather API",
    func=get_weather,
    description="Obtiene el clima actual de una ciudad"
)

# Herramienta 2: Wikipedia
def search_wikipedia(query: str) -> str:
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Demasiadas opciones: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "No encontré información en Wikipedia."

wikipedia_tool = Tool(
    name="Wikipedia",
    func=search_wikipedia,
    description="Busca información en Wikipedia"
)

# 2. LLM Azure OpenAI (GPT-4o)
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "<TU_ENDPOINT_AZURE_OPENAI>")
api_key = os.getenv("AZURE_OPENAI_API_KEY", "<TU_API_KEY>")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")
model = os.getenv("AZURE_OPENAI_MODEL")
llm = AzureChatOpenAI(
    api_version=api_version,
    azure_endpoint=azure_endpoint,
    api_key=api_key,
    deployment_name=model,
    temperature=0
)

# 3. Inicializar agente con las herramienta
agent = initialize_agent(
    tools=[weather_tool, wikipedia_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 4. Pregunta al agente

# 4. Bucle de preguntas al agente
while True:
    user_query = input("Que queres saber? Escribe tu pregunta para el agente (o 'salir' para terminar): ")
    if user_query.lower() in ["salir", "exit"]:
        print("¡Hasta luego!")
        break
    response = agent.run(user_query)
    print(response)
