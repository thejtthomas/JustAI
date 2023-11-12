import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie file from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 1. Sidebar menu
with st.sidebar:
    st.title("Just AI")
    selected_sidebar = option_menu("Main Menu", ["Home", 'Client', 'Lawyer', 'Dashboard', 'History', 'Contact'], 
        icons=['house', 'people-fill', 'bank', 'chat-dots', 'clock-history', 'telephone'], menu_icon="cast", default_index=0)
    st.write("Selected Sidebar Option:", selected_sidebar)

# 2. Horizontal menu
st.title("Just AI")
selected_horizontal = option_menu(None, ["Home", "Client", "Lawyer", "Dashboard", "History", 'Contact'], 
    icons=['house', 'people-fill', 'bank', 'chat-dots', 'clock-history', 'telephone'], 
    menu_icon="cast", default_index=0, orientation="horizontal")


# Load Lottie file for animation (replace with your actual Lottie URL)
lottie_hello = load_lottieurl("https://lottie.host/6729af09-07c8-4adb-a768-3a2f366834b3/WO1501fN3r.json")

# Content based on selected option
if selected_horizontal == "Home":
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium; high
        height=300,
        width=300,
        key=None,
    )

    st.header("Overview")
    st.markdown("""
        Introducing "JUST AI," a product dedicated to revolutionizing legal assistance. By leveraging artificial intelligence, we aim to democratize access to legal information, fostering a more inclusive and efficient legal support system.
    """)

    st.header("Our Mission")

    st.markdown("""
        Dedicated to equitable legal support, our mission is to leverage advanced AI technologies for inclusive, accessible, and ethical assistance, ensuring individuals navigate the legal landscape with confidence and fairness.
    """)

    st.header("Our Services")

    st.markdown("""
        - Legal Consultation: Access on-demand legal consultation through an intuitive chat interface, providing users with timely and personalized advice.
        - Document Assistance: Generate and review legal documents efficiently, ensuring accuracy and compliance with relevant legal standards.
        - AI-Driven Case Analysis: Benefit from AI-driven case analysis for enhanced insights and recommendations tailored to specific legal situations.
        - User Advocacy: Advocate for users by providing information on legal rights, potential legal recourse, and strategies for navigating legal challenges.
    """)
elif selected_horizontal == 'Contact':
    st.header("Contact Us")

    contacts = [
        {"name": "Samyuktha Sudheer", "phone": "+123456789", "email": "abc@example.com"},
        {"name": "Rose Mary P John", "phone": "+987654321", "email": "ghi@example.com"},
        {"name": "Riya Derose Micheal", "phone": "+111223344", "email": "yui@example.com"},
        {"name": "Thej T Thomas", "phone": "+555666777", "email": "ert@example.com"}
    ]

    phone_icon = "📞"
    mail_icon = "✉️"

    for contact in contacts:
        st.subheader(contact["name"])
        st.write(f"{phone_icon} Phone: {contact['phone']}")
        st.write(f"{mail_icon} Email: {contact['email']}")
        st.write("---")

