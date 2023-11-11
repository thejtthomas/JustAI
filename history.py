import openai
import os
import streamlit as st
from dotenv import load_dotenv
from deta import Deta

# Load environment variables
load_dotenv()

# Set up OpenAI API key
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set up Deta
DETA_KEY = os.getenv('DETA_KEY')
deta = Deta(DETA_KEY)
db = deta.Base('History')

# Chat-based language model system messages
system_messages = f"""Act as an AI Legal Advisor. Do not mention you are not an actual lawyer. 
Give legal advice based on the constitution of India in the following steps.

1: Check whether the issue is an actual legal issue.
2: Give legal advice
3: Explain the steps for how to and where to register a complaint as a list.
4: Cite the necessary articles and sections under the law with brief explanations about each with context to the problem.

Provide a response in the following format
Legal advice: <step 2 reasoning>

Steps for registering a complaint: <step 3 reasoning>

Citations: <step 4 reasoning>
"""

# Function to get legal advice
def get_legal_advice(prompt):
    # Call OpenAI API for legal advice
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_messages},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message.content
    
    # Store the prompt and response in Deta



    db.update({'Response': f"""{prompt}, 'response': {response}"""}, "kzr40aulnoeo")

    return response

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
            
            if legal_advice:
                st.success("Legal Advice:")
                st.write(legal_advice)
            else:
                st.warning("Error getting legal advice. Please try again.")
        else:
            st.warning("Please enter a legal query.")

# Run the Streamlit app
if __name__ == "__main__":
    dashboard()
