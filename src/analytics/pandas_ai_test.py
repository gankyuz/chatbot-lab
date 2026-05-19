from src.analytics.dataframes import clientes_dataframes
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

from dotenv import load_dotenv
import os 

load_dotenv()

df = clientes_dataframes()

llm = OpenAI(
    api_token=os.getenv("OPENAI_API_KEY")
)

sfd = SmartDataframe(df, config={"llm":llm})

resposta = sfd.chat("Qual cidade possui mais clientes que mais gastam?")

print(resposta)