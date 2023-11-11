import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# 1. Sidebar menu
with st.sidebar:
    st.title("Legal AI Platform")
    selected_sidebar = option_menu("Main Menu", ["Home", 'User Login', 'Lawyer Login', 'Dashboard'], 
        icons=['house', 'user', 'lawyer', 'chart-line'], menu_icon="cast", default_index=0)
    st.write("Selected Sidebar Option:", selected_sidebar)

# 2. Horizontal menu
st.title("Legal AI Platform")
selected_horizontal = option_menu(None, ["Home", "User Login", "Lawyer Login", 'Dashboard'], 
    icons=['house', 'user', 'lawyer', 'chart-line'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.write("Selected Horizontal Option:", selected_horizontal)

# Content based on selected option
if selected_horizontal == "Home":
    st.write("Welcome to the Legal AI Platform Home Page!")
elif selected_horizontal == "User Login":
    st.write("User Login Page - Enter your credentials.")
elif selected_horizontal == "Lawyer Login":
    st.write("Lawyer Login Page - Enter your credentials.")
elif selected_horizontal == "Dashboard":
    st.write("Dashboard - View legal analytics and insights.")