# better_resume_ai
Make your existing resume **better** with the help of AI: further tailor your existing resume to a specific job posting.

## Description
Human resources often get tons of submitted applications, so they use tools to filter down applications before a human even looks at them. We can improve your chances of getting past these filters and landing you an interview.

## Prerequisites
- `python` version 3
- This program assumes your existing resume is written in markdown format
- You must have an API key on the OpenAI Platform

## Model Used
The app currently uses `gpt-5`. However, feel free to swap out the model within **generate_resume_update_suggestion.py** with other models, like the more cost-effective model `gpt-5-mini`. 

## Estimate OpenAI Costs
[Pricing Located Here](https://developers.openai.com/api/docs/pricing)

Pricing is all about the amount of `tokens` within the input and output.

To get a better estimate of your pricing per API call, use the [OpenAI Tokenizer tool](https://platform.openai.com/tokenizer) to see how many tokens you can expect to use for your **input**.

For example, within the tokenizer tool, plug in all your prompt text. 
- For me, my prompt/input text was a few thousand tokens. 
- Note that the pricings page is per 1 million tokens, so my Input cost of a few thousand tokens will be a fraction of what is listed.

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
