# better_resume_ai
Use AI to help further tailor your existing resume to a specific job posting's description.

## Description
Landing Tech interviews is tough, especially with all the AI filters being used by human resources these days. Use AI to help provide you suggestions on tailoring your existing resume to a particular job posting.

## Prerequisites
- `python` version 3
- This program assumes your existing resume is written in markdown format
- You must have an API key on teh OpenAI Platform

## Model Used
- The app currently uses `gpt-5`. However, feel free to swap out the model within **generate_resume_update_suggestion.py** with other models, like the more cost-effective model `gpt-5-mini`. 
- My observation is that `gpt-5` is a ton better at this task and is worth the additional cost (i.e. for a small job posting text and a resume that is a couple of pages: we are talking a difference of a few cents per API call). 

## Process
1. Clone this repo.
2. Within **generate_resume_update_suggestion.py**, replace `"ENTER-OPENAI-API-KEY-HERE"` with your actual OpenAI Platform API key.
3. Copy/Paste the job description text within **job.txt**.
4. Move your resume into this project, and rename the resume file to: **no_pii_data_resume.md**.
5. Remove all your PII information from your resume! We don't want the prompt we send to openai to include your PII information!.
6. Create the virtual environment and install dependencies.
   
       python3 -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt
7. Run the code to generate an updated resume:

        python3 generate_resume_update_suggestion.py
8. Review the updated suggestions. Update your original resume accordingly.
9. Be sure to add back in your PII information at the top.

## Suggestions/Observations
- Good resumes have numbers/metrics to demonstrate effectiveness. Make sure your resume has this. AI can't do this very well because metrics are individualized. 
- It is good to have a resume in both markdown and PDF format. The best markdown-to-pdf conversion tool I've found is the **Markdown PDF** extension by yzane on Visual Studio Code.
