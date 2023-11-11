import openai
import os
import streamlit as st
from dotenv import load_dotenv
import datetime
import bcrypt
from streamlit_option_menu import option_menu
from deta import Deta

# Load environment variables
load_dotenv()

# Set up OpenAI API key
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set up Deta
DETA_KEY = os.getenv('DETA_KEY')
deta = Deta(DETA_KEY)
db = deta.Base('StreamlitAuth')

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

# Function to hash the password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')  # Decode bytes to string

# Function to insert a new user
def insert_user(email, username, password):
    date_joined = str(datetime.datetime.now())
    hashed_password = hash_password(password)

    return db.put({'key': username, 'username': username, 'password': hashed_password, 'date_joined': date_joined})

# Function to authenticate a user
def authenticate_user(username, password):
    user = db.get(username)
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        return user
    return None

# Function to sign up a new user
def sign_up():
    with st.form(key='signup', clear_on_submit=True):
        st.subheader(':green[Sign Up]')
        email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
        password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')

        if st.form_submit_button('Sign Up'):
            if password1 == password2:
                result = insert_user(email, username, password1)
                st.success(f"User {username} successfully created! Date joined: {result['date_joined']}")
            else:
                st.error("Passwords do not match. Please try again.")

# Function to log in a user
def login():
    with st.form(key='login', clear_on_submit=True):
        st.subheader(':green[Log In]')
        username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
        password = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')

        if st.form_submit_button('Log In'):
            user = authenticate_user(username, password)
            if user:
                # Set the state variable to indicate successful login
                st.session_state.is_authenticated = True
                st.success(f"Welcome back, {user['username']}! Last login: {datetime.datetime.now()}")
            else:
                st.error("Authentication failed. Please check your username and password.")

# Function to display the legal advice chatbot
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

# Function to display the dashboard
def dashboard():
    st.title("Just AI Dashboard")
    st.header("Welcome to the Dashboard!")

    # Add your dashboard content here

# Main part of the Streamlit app
if __name__ == "__main__":
    # Display the login or sign-up page based on the selected navigation
    selected_page = st.sidebar.radio("Navigation", ["Home", "Sign Up", "Log In", "Legal Advice", "Dashboard"])
    # 1. Sidebar menu
with st.sidebar:
    st.title("Just AI")
    selected_sidebar = option_menu("Main Menu", ["Home", 'Client', 'Lawyer', 'Dashboard','History','Contact'], 
        icons=['house', 'people-fill', 'bank', 'chat-dots','clock-history','telephone'], menu_icon="cast", default_index=0)
    st.write("Selected Sidebar Option:", selected_sidebar)

# 2. Horizontal menu
st.title("Just AI")
selected_horizontal = option_menu(None, ["Home", "Client", "Lawyer","Dashboard","History","Contact"], 
    icons=['house', 'people-fill', 'bank', 'chat-dots','clock-history','telephone'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.write("Selected Horizontal Option:", selected_horizontal)

# Content based on selected option
if selected_horizontal == "Home":
    st.write("Welcome to the Just AI Home Page!")
elif selected_horizontal == "Client":
    st.write("Client Login Page - Enter your credentials.")
    sign_up()
    login()
elif selected_horizontal == "Lawyer":
    st.write("Lawyer Login Page - Enter your credentials.")
    sign_up()
    login()
elif selected_horizontal == "Dashboard":
    st.write("Dashboard - View legal analytics and insights.")
    # Check if the user is authenticated
    if hasattr(st.session_state, 'is_authenticated') and st.session_state.is_authenticated:
        user_prompt = st.text_area("Enter your legal query:")
        if st.button("Get Legal Advice"):
            if user_prompt:
                # Get legal advice from OpenAI
                legal_advice = get_legal_advice(user_prompt)
                st.success("Legal Advice:")
                st.write(legal_advice)
            else:
                st.warning("Please enter a legal query.")
    else:
        st.warning("Please log in to access the legal advice chatbot.")
elif selected_horizontal == "History":
    st.write("History - View previous legal analytics and insights.")
elif selected_horizontal == "Contact":
    st.write("Contact- For any help contact us")