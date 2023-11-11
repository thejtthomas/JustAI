import streamlit as st
import datetime
from deta import Deta
import bcrypt

DETA_KEY = 'd01xfwtcm2w_vLQsYjQCfDPKijiA8HsUGrSKsfxuf7Aw'

deta = Deta(DETA_KEY)

db = deta.Base('StreamlitAuth')

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

# Function to display the dashboard
def dashboard():
    st.header("Dashboard")
    st.subheader("Chatbot Template")

    # Add your chatbot template or other content here
    # For example, a text input for entering prompts
    prompt = st.text_input("Enter Prompt:")
    if st.button("Submit Prompt"):
        # Add logic to handle prompt submission, e.g., storing in a database
        st.success(f"Prompt submitted: {prompt}")

# Main part of the Streamlit app
if __name__ == "__main__":
    st.title("Just AI")

    # Check if the user is authenticated
    if hasattr(st.session_state, 'is_authenticated') and st.session_state.is_authenticated:
        dashboard()  # Display the dashboard if authenticated
    else:
        # Display the login or sign-up page based on the selected navigation
        selected_page = st.sidebar.radio("Navigation", ["Home", "Sign Up", "Log In"])

        if selected_page == "Home":
            st.header("Welcome to the Home Page!")
            st.write("Navigate to 'Sign Up' or 'Log In' using the sidebar.")

        elif selected_page == "Sign Up":
            sign_up()

        elif selected_page == "Log In":
            login()
