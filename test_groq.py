import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()
print("Les modèles disponibles pour votre compte:")
for m in models.data:
    print("-", m.id)