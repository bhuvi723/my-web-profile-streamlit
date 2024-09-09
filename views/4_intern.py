import streamlit as st 

def intern():
    st.title(":red[Internships :]")
    
    st.markdown('<hr style="border-top: 3px solid red">',unsafe_allow_html=True)
    
    internships = {
        1 : {
            # title of internship
            "title" : "AI/ML Intern At Robokalam Technologies :",
            
            #duration
            "duration" : "1-Aug-2024 to ....",
            
            "desc_exp1" : "Iam very much excited that i got an intership offer as AI/ML from robokalam technologies!",
            
            "desc_exp2" : "soon......",
            
            # projects
            "projects" : "",
            
            #offer letter
            "offer_letter" : r"images\offer_robo.jpg",
            
            # internship certificate
            "certificate" : r""
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
    
    for ind, keys in internships.items():        
        st.markdown(f"""
                    <h3 class="pro_sty">{ind}. {keys['title']} {keys['duration']}</h3> 
                    <dl type="">
                        <h5>🔶 Projects : </h5><dd><h6>👉 {keys['projects']}</h6></dd><br>
                    </dl>""",
                    unsafe_allow_html=True)
        
        # offer letter
        st.markdown(f"""
                    <dl type="">
                        <h5>🔶 Offer-letter : </h5>
                    </dl>""",
                    unsafe_allow_html=True)
        exp1 = st.expander("Offer-letter :")
        exp1.write(keys['desc_exp1'])
        exp1.image(keys["offer_letter"])
        st.markdown("<br>",unsafe_allow_html=True)
        
        # certificate
        st.markdown(f"""
                    <dl type="">
                        <h5>🔶 Certificate :</h5>
                    </dl>""",
                    unsafe_allow_html=True)
        exp2 = st.expander("Certificate :")
        exp2.write(keys['desc_exp2'])
        # exp2.image(keys['certificate'])
        st.markdown("<br>",unsafe_allow_html=True)
        

        st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
        )

intern()
