import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Ты — автономный агент, управляющий браузером.
Ты видишь список элементов страницы.
Ты выбираешь следующее действие.
Не выдумывай элементы — используй только переданные.
"""

def decide(goal, elements, memory):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"""
Цель: {goal}

Элементы:
{elements}

Память:
{memory}

Верни JSON строго в формате:
{{
  "action": "click|type|goto|finish",
  "element_id": "...",
  "text": "...",
  "url": "..."
}}
"""}
        ],
        temperature=0
    )

    return response.choices[0].message.content
