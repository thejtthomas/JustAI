import openai
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Chat-based language model system messages
system_messages = f"""Act as an AI Legal Advisor. Do not mention you are not an actual lawyer. 
Give legal advises based on the constitution of India in the following steps.

1: Check whether the issue is an actual legal issue.
2: Give legal advise
3: Explain the steps for how to and where to register complaint as a list.
4: Cite the necessary articles and sections under law with brief explainations about each with contect to the problem.


Provide response in the  following format
Legal advise :<step 2 reasoning>

Steps for registering complaint: <step 3 reasoning>

Citations <step 4 reasoning>
"""

def get_legal_advice(prompt):
    # Call OpenAI API for legal advice
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_messages},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# Main part of the Streamlit app
def dashboard():
    st.header("Legal Advisor Chatbot")
    st.subheader("Ask for Legal Advice")

    # User input for legal advice
    user_prompt = st.text_area("Enter your legal query:")
    
    if st.button("Get Legal Advice"):
        if user_prompt:
            # Get legal advice from OpenAI
            legal_advice = get_legal_advice(user_prompt)
            st.success("Legal Advice:")
            st.write(legal_advice)
        else:
            st.warning("Please enter a legal query.")

# Run the Streamlit app
if __name__ == "__main__":
    dashboard()
