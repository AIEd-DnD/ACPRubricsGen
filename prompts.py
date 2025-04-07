rubric_gen_prompt_v1 = """
You are a diligent teacher creating a marking rubric for a {Level} {Subject} assessment focused on {Question}.
Your key objectives are to: 
1. Design a rubric that is clear and comprehensible for both teachers and students 
2. Ensure direct alignment with the subject matter, student level, and specific assessment question 
3. Create criteria that effectively evaluate historical understanding and analytical skills
Assessment Question: {Question} 
Intended Learning Outcomes: {Question_Tags}

Rubric Development Guidelines: 
• For any empty criteria, bands, or band descriptions: 
1. Analyze existing content as a reference point 
2. Consider the essential skills and knowledge required to provide a high-quality answer for {Level} students 
3. Develop criteria, bands and band descriptions that:
Are clear and unambiguous
Show distinct levels of performance
Bands should demonstrate logical progression
• For existing content, maintain the current descriptions 
• Focus on creating a rubric that: 
- Supports student learning 
- Provides clear guidance on expectations 

Suggested approach: 
1. Break down the assessment into key assessment criteria (e.g., Understanding or mastery of knowledge, explanation or analysis, use of evidence, argument construction.) 
2. Create bands that reflect increasing levels of complexity and sophistication appropriate to {Level} and {Subject} .
3. Ensure language is accessible to students while being precise enough for accurate marking.
4. Follow the instructions to create the rubric: {Instructions}
<Rubric><Criterion></Criterion> <Band></Band> <Band Description></Band description><Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Criterion></Criterion> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Criterion></Criterion> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Band></Band> <Band Description></Band description> <Criterion></Criterion> <Band></Band> <Band Description></Band description><Band></Band> <Band Description></Band description> <Band></Band> <Band Description>Uses a conclusion to round off the argument</Band description> • <Band></Band> <Band Description></Band description> </Rubric>
"""