from src.ai.llm import client
from src.ai.prompts import SYSTEM_PROMPT

def generate_sql(question):
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash:free",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": SYSTEM_PROMPT
            }
        ]
    )
    
    sql = response.choices[0].message.content
    return sql