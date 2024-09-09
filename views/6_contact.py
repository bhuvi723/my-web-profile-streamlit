import streamlit as st
import re
import time
from utils.mail import *

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex,email) is not None

@st.dialog(" ")
def contact_me():
    with st.form("my_form"):
        st.write('<h1>Contact me via mail :</h1><hr style="border-top: 1px solid white;">',unsafe_allow_html=True)
        # st.write()
        name = st.text_input("Name : ")
        email = st.text_input("Email : ")
        message = st.text_area("Your Message : ")
        submitted = st.form_submit_button("submit")
        if submitted:
            # st.success("Sent Succesfully!")
            if not name:
                st.error("Please give name.",icon="😒")
                st.stop()
            
            if not email:
                st.error("Please give email address.",icon="🤔")
                st.stop()
                
            if not is_valid_email(email):
                st.error("Please give valid email address.",icon="😫")
                st.stop()
                
            if not message:
                st.error("Please give message!",icon="😣")
                st.stop()
                
            if send_email(name,email,message) == "Message Sent!":
                st.success("Your Email Successfully Sent!",icon="🤩")
                time.sleep(4)
                st.rerun()
            else:
                st.error("There is an issue. Come back later!",icon="😣")

def contact():
    st.title(":red[Contact :]")
    
    st.markdown('<hr style="border-top: 3px solid red;">',unsafe_allow_html=True)
    
    # st.markdown("""
    #         <div style="display: flex; align-items: center;">
    #             <span style="font-size: 24px; font-weight: bold; margin-right: 10px;">Email :</span>
    #             <span><a href="#" style="font-size: 20px;">salvajibhuvan@gmail.com</span>
    #         </div>
    #         """, unsafe_allow_html=True
    #     )
    
    col1,col2 = st.columns([1,3],gap="small",vertical_alignment="center")
            
    st.markdown("""
            <div style="display: flex; align-items: center;">
                <span style="font-size: 24px; font-weight: bold; margin-right: 10px;">Linkedin :</span>
                <span><a href="https://linkedin.com/in/s-bhuvan-7a0544275" style="font-size: 20px;">https://linkedin.com/in/s-bhuvan-7a0544275</span>
            </div>
            """, unsafe_allow_html=True
    )
    
    st.markdown("""
            <div style="display: flex; align-items: center;">
                <span style="font-size: 24px; font-weight: bold; margin-right: 10px;">Git Hub :</span>
                <span><a href="https://github.com/bhuvi723" style="font-size: 20px;">https://github.com/bhuvi723...</span>
            </div>
            """, unsafe_allow_html=True
    )
        
    with st.container():
        st.write("")
        if st.button("Contact via mail"):
            contact_me()

contact()