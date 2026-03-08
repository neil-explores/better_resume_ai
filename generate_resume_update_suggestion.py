from openai import OpenAI

client = OpenAI(api_key="ENTER-OPENAI-API-KEY-HERE")


with open("job.txt", "r") as f:
    job_posting_text = f.read()

with open("no_pii_data_resume.md", "r") as f:
    no_pii_data_resume = f.read()

prompt = f"""
You are an expert resume writer.

Your task:
1. Read the job posting.
2. Read the candidate's resume.
3. Rewrite the resume so it better matches the job posting.
4. Emphasize relevant skills and experiences.
5. Keep the resume truthful (do not invent jobs or skills).
6. Output the improved resume in clean Markdown format.

Job Posting:
{job_posting_text}

Candidate Resume:
{no_pii_data_resume}
"""

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a professional resume editor."},
        {"role": "user", "content": prompt}
    ]
)

# Save output to markdown file
output = response.choices[0].message.content

with open("updated_resume.md", "w", encoding="utf-8") as f:
    f.write(output)

print("Updated resume saved to updated_resume.md. Check it out!")