from openai import OpenAI
import os
from dotenv import load_dotenv
import tools
import json

load_dotenv('.env')
openai_api_key = os.getenv("OPENAI_API_KEY")

def assemble_prompt(prompt_template, level, subject, question, question_tags, instructions):
    user_prompt = prompt_template.format(Level=level, Subject=subject, Question=question, Question_Tags=question_tags, Instructions=instructions)
    return user_prompt

def generate_rubric(user_prompt):
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        temperature = 0.7,
        max_tokens = 16000,
        #tools = tools.rubric_gen_tool,
        messages=[{"role": "user", "content":user_prompt}]
        )
    return response