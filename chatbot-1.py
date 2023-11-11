import openai
import os
import streamlit as st
from dotenv import load_dotenv, dotenv_values
load_dotenv()
client = openai.OpenAI(api_key= os.getenv('OPENAI_API_KEY'))
prompt = st.chat_input("Enter your query")
system_messages = f"""Act as an AI Legal Advisor. Do not mention you are not an actual lawyer. 
Give legal advises based on the constitution of India in the following steps.

1: Check whether the issue is an actual legal issue.
2: Give legal advise
3: Explain the steps for how to and where to register complaint as a list.
4: Cite the necessary articles and sections under law with brief explainations about each with contect to the problem.


Provide response in the  following format
Legal advise :<step 2 reasoning>

Steps for registering complaint: <step 3 reasoning>

Citations <step 4 reasoning>
"""


if prompt:
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_messages},
        {"role": "user", "content": prompt}
    ]
    )

    st.write(completion.choices[0].message.content)