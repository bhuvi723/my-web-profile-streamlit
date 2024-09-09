import streamlit as st 
from PIL import Image

def about_me():
    col1, col2 = st.columns(2,gap="large", vertical_alignment= "center")
    
    with col1:
        
        st.title(":red[Salvaji Bhuvan]")
        
        st.subheader("About Me :")
        
        st.write("""<p style="font-size: 18px;">
                Iam a big enthusiast of learning data science, machine learning and leveraging data to
                drive impactful insights and solutions.
                also working on backend of web application, buidling logics.</p>
                """,unsafe_allow_html=True)
        
        # download button
        with open("Resume.pdf","rb") as file:
            resume = file.read()
            
        st.download_button(label = "Download Resume",
                  data = resume,
                  file_name = "Resume.pdf",
                  mime = "application/pdf"                  
                )
    
    with col2:
    
        img_path = r"images/my_pho.jpg"
        img = Image.open(img_path)
        img = img.resize((300,300))
        st.image(img,use_column_width=True)
    
    # horizontal line
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    
    # Education
    st.header(":red[Education Qualification :]")
    edu = {
        1 : {
            # title
            "title" : "Hyderabad Institute of Technology and Management,Hyderabad",
        
            # description1
            "desc1" : "- Bachelor of technology in specialization Data Science.",
            
            # description2
            "desc2" : "- Currently holding academic aggregate of 8.7 CGPA."
            
        },
        2 : {
            "title" : "Kendriya Vidyalaya Sangatan, NTPC RDM",
            
            "desc1" : "- Studied +1 and +2 in Computer Science.",
            
            "desc2" : "- Academic aggregate in 11th - 83% and 12th - 85%."
        }
    }
    
    for ind,ed in edu.items():
        st.markdown(f"""
                <dl>
                    <dt style="font-size: 21px;">{ed['title']}</dt>
                    <dd style="font-size: 18px;">{ed['desc1']}</dd>
                    <dd style="font-size: 18px;">{ed['desc2']}</dd>
                </dl>
            """,unsafe_allow_html=True)

    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    # tech - skills
    st.header(":red[Technical Skills :]")
    
    tech = {
        
        1 : {
            # title
            "title" : "Languages :",
        
            # description1
            "tech_stack" : "- C++, Python."
        },
        2 : {
            "title" : "Web Technologies :",
            
            "tech_stack" : "- Python-Flask, SQLAlchemy , Mysql, SQlite, Html, CSS."
        },
        3 : {
            "title" : "Additional Tech-Stack :",
            
            "tech_stack" : "- Problem Solving-Data structures, Algorithms, Oops."
        }
    }
    
    for ind,tech in tech.items():
        st.markdown(f"""
                <dl>
                    <dt style="font-size: 21px;">{tech['title']}</dt>
                    <dd style="font-size: 18px;">{tech['tech_stack']}</dd>
                </dl>
            """,unsafe_allow_html=True)
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
   #------------------------------------------------
   # projects
    st.header(":red[Projects :]")
    projects = {
        
        1 : {
            # title
            "title" : "Social Network Data Analysis :",
        
            # description1
            "description" : '''- The "Social Network Data Analyzer" project leverages a Facebook dataset to analyze social media interactions
                                using an Ordinary Least Squares (OLS) regression algorithm. Implemented in Python, the project employs libraries such as scikit
                                -learn for regression modeling, pandas and numpy for data manipulation, and matplotlib for visualization''',
            
            #tech stack
            "tech_stack" : "- Used OLS machine learning algo, scikit learn libraries, pandas ,numpy and matplotlib."
        },
        2 : {
            "title" : "SMS/Email Spam Classification",
            
            "description" : '''- The "SMS/Email Spam Classification" project involves developing a system to automatically classify
                                messages as spam or not spam using the Naive Bayes algorithm.''',
            
            "tech_stack" : "- Used Naive Bayes Supervised machine learning Algo, pandas, numpy, matplotlib, scikit-learn libraries and wordcloud."
        },
        3 : {
            "title" : "TAAZA KHABHAR : The Trending News App",
            
            "description" : '''- Taaza Khabar is a dynamic and trending web application developed using Streamlit, 
                                designed to keep users informed with the latest news across various domains such as business, 
                                sports, entertainment, and health.''',
            
            "tech_stack" : "- Used streamlit, media stack api, html and css."
        },
        4 : {
            "title" : "Flight Price Prediction",
            
            "description" : '''- The "Flight Price Prediction" project involves predicting flight ticket prices using a comprehensive
                                flight dataset. The solution employs the XGBoost algorithm, known for its high performance in regression tasks.''',
            
            "tech_stack" : "- Used XG boost algo, Scikit Learn and Feature Engine libraries, pandas, numpy, matplotlib and seaborn."
        }
    }
    
    for ind,proj in projects.items():
        st.markdown(f"""
                <dl>
                    <dt style="font-size: 21px;">{ind}. {proj['title']}</dt>
                    <dd style="font-size: 18px;">{proj['description']}</dd>
                    <dd style="font-size: 18px;">{proj['tech_stack']}</dd>
                </dl>
            """,unsafe_allow_html=True)
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    # trainings and certifications
    st.header(":red[Trainings and Certifications :]")
    
    certis = {
        1 : {
            # title
            "title" : "Nptel Online Certification on DataBase Management System.",
            
            #cdescription
            "desc" : "- Certified from Swayam Govt of india!",
            
        },
        2 : {
            # title
            "title" : "Training and Certification on Machine Learning.",
            
            # description
            "desc" : "- Certified by Internshala!",
        },
        3 : {
            # title
            "title" : "Hacker Rank - Bacics Python Certificate.",
            
            # description
            "desc" : "- Certified by Hacker rank!",
        }
    }
    
    for ind,certi in certis.items():
        st.markdown(f"""
                <dl>
                    <dt style="font-size: 21px;">{ind}. {certi['title']}</dt>
                    <dd style="font-size: 18px;">{certi['desc']}</dd>
                </dl>
            """,unsafe_allow_html=True)
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    # Internships
    st.header(":red[Internships :]")
    
    intern = {
        1 : {
            # title
            "title" : "Currently Working At Robokalam Technologies As An AI/ML Intern.",
            
            #cdescription
            "duration" : "1-AUG-2024 to .....",
        }
    }
    
    for ind,inte in intern.items():
        st.markdown(f'''
                    <dl>
                        <dt style="font-size: 21px;">{ind}. {inte['title']}</dt>
                        <dd style="font-size: 18px;">{inte['duration']}</dd>
                    </dl>
                ''',unsafe_allow_html=True
        )
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    # intrests
    st.header(":red[ Intrests :]")
    
    intrests = {
        1 : {
            "title" : "Iam very much intrested in working on real world projects of data science and machine learning."          
        },
        2 : {
            "title" : "Data Structures Problem Solving using python."
        },
        3 : {
            "title" : "Knowing about startups and also intrested inspiring stories of big players in the market."
        }
    }
    
    for ind,inn in intrests.items():
        st.markdown(f'''
                    <dl>
                        <dt style="font-size: 21px;">{ind}. {inn['title']}</dt>
                    </dl>
                ''',unsafe_allow_html=True
        )
    
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    # Hobbies
    st.header(":red[Hobbies :]")
    
    hbs = {
        1 : {
            "title" : "Playing Chess and FootBall."          
        },
        2 : {
            "title" : "Exploring new technologies which are trending in the market."
        },
        3 : {
            "title" : "coding :)"
        }
    }
    
    for ind,hb in hbs.items():
        st.markdown(f'''
                    <dl>
                        <dt style="font-size: 21px;">{ind}. {hb['title']}</dt>
                    </dl>
                ''',unsafe_allow_html=True
        )
    
    
    st.markdown(
        """
        <hr style="border-top: 3px solid red;">
        """,
        unsafe_allow_html=True
    )
    #------------------------------------------------
    
about_me()