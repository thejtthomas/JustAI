import streamlit as st
from streamlit_option_menu import option_menu

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
elif selected_horizontal == "Lawyer":
    st.write("Lawyer Login Page - Enter your credentials.")
elif selected_horizontal == "Dashboard":
    st.write("Dashboard - View legal analytics and insights.")
elif selected_horizontal == "History":
    st.write("History - View previous legal analytics and insights.")
elif selected_horizontal == "Contact":
    st.write("Contact- For any help contact us")

# You can add more content and logic based on the selected options.
