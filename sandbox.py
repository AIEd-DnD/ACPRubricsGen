import llm_functions as ACP
import prompts
import tools

user_prompt = ACP.assemble_prompt(
    prompts.rubric_gen_prompt_v1,
    level="Year 10",
    subject="History",
    question="How did the Industrial Revolution impact society?",
    question_tags="Industrial Revolution, Society, Impact",
    instructions="Create a rubric for a Year 10 history assessment."
)

response = ACP.generate_rubric(user_prompt)
print(response.choices[0].message.content)