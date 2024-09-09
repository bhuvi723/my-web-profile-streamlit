import streamlit as st 
from PIL import Image

# @st.dialog("Certificate :")
# def box(img):
#     img = Image.open(img)
#     resized_img = img.resize((2400,2000))
#     st.image(resized_img)#,use_column_width=True)

def certi():
    st.title(":red[Trainings and Certifications :]")
    
    st.markdown(f'<hr style="border-top: 3px solid red;">',unsafe_allow_html=True)
    
    certis = {
        1 : {
            # title
            "title" : "Nptel Online Certification on DataBase Management System.",
            
            #cdescription
            "desc" : "Certified from Swayam Govt of india!",
            
            # certificate
            "cert" : r"images/dbms.jpg"
        },
        2 : {
            # title
            "title" : "Training and Certification on Machine Learning.",
            
            # description
            "desc" : "Certified by Internshala!",
            
            # certificate
            "cert" : r"images/machine_learning.jpg"
        },
        3 : {
            # title
            "title" : "Hacker Rank - Bacics Python Certificate.",
            
            # description
            "desc" : "Certified by Hacker rank!",
            
            # certificate
            "cert" : r"images/hackerrank.png"
        }
    }
    
    st.markdown("""
            <style>
                .pro_sty{
                    color: #FA603E;
                }
            </style>
            """,unsafe_allow_html=True
    )
    
    for ind, certi in certis.items():        
        st.markdown(f"""
                    <h3>{ind}. {certi['title']}</h3> 
                   """,
                    unsafe_allow_html=True)
        
        with st.expander("Certificate :"):
            st.write(certi['desc'])
            st.image(certi['cert'])
            # if st.button("view certificate",key=ind,help="Click here to view the certificate!"):
            #     box(certi['cert'])
                
        st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
        )
    
certi()