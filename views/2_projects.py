import streamlit as st
# from streamlit_option_menu import option_menu

def projects():

    st.title(":red[Projects :]")

    st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
        )
    
    projects = {
        1 : {
            # title
            "title" : "TAAZA KHABHAR : The Trending News App",
            
            # description
            "description" : """Taaza Khabar is a dynamic and trending web application developed using Streamlit, 
            designed to keep users informed with the latest news across various domains such as business, 
            sports, entertainment, and health. This innovative app not only aggregates news from multiple 
            sources but also supports four different languages and pulls content from various countries, 
            ensuring comprehensive coverage and efficiency.The application leverages the powerful Mediastack 
            API to fetch real-time news updates, ensuring users receive accurate and up-to-date information. 
            Python libraries like Streamlit and Requests are utilized for seamless integration and data handling, 
            while custom HTML and CSS enhance the user interface, providing a visually appealing and intuitive experience. 
            With its robust functionality and elegant design, Taaza Khabar stands out as a highly efficient and user-friendly
            news aggregator.""",
            
            # tech_stack
            "tech_stack" : "Used streamlit, media stack api, html and css.",
            
            #git hub link
            "git_hub" : "https://github.com/bhuvi723/streamlit-news-app"
        },
        2 :{
            #title
            "title" : "SMS/Email Spam Classification",
            
            #description
            "description" : """The "SMS/Email Spam Classification" project involves developing a system to automatically classify
            messages as spam or not spam using the Naive Bayes algorithm. This machine learning approach is implemented in a Jupyter
            Notebook environment, utilizing Python libraries such as scikit-learn for model training and evaluation, pandas and numpy
            for data manipulation and analysis, and matplotlib for visualizing results. The project preprocesses text data by removing
            stop words and employing the Porter stemmer to normalize words. Additionally, techniques to handle imbalanced data are applied
            to ensure robust model performance. The Naive Bayes algorithm is chosen for its effectiveness in text classification tasks,
            providing a reliable solution for filtering unwanted spam messages in SMS and emails.""",
            
            #tech_stack
            "tech_stack" : "Used Naive Bayes Supervised machine learning Algo, pandas, numpy, matplotlib, scikit-learn libraries and wordcloud.",
            
            #git hub link
            "git_hub" : "https://github.com/bhuvi723/Email-Sms-classification-naive-bayes-algo"
        },
        3 : {
            #title
            "title" : "Social Network Data Analyser",
            
            #description
            "description" : """The "Social Network Data Analyzer" project leverages a Facebook dataset to analyze social media interactions
            using an Ordinary Least Squares (OLS) regression algorithm. Implemented in Python, the project employs libraries such as scikit
            -learn for regression modeling, pandas and numpy for data manipulation, and matplotlib for visualization. The analysis focuses on
            predicting the number of likes a particular user is expected to receive within a specified year range. By examining patterns and
            trends in the dataset, the project draws valuable insights into user engagement and interaction metrics, helping to forecast future
            social media activity and optimize content strategies.""",
            
            #tech_stack
            "tech_stack" : "Used OLS machine learning algo, scikit learn libraries, pandas ,numpy and matplotlib.",
            
            #git hub link
            "git_hub" : "https://github.com/bhuvi723/social-nw-data-analysis-ols-algo"
        },
        4 :{
            #title
            "title" : "Flight Price Prediction",
            
            #description
            "description" : """The "Flight Price Prediction" project involves predicting flight ticket prices using a comprehensive
            flight dataset. The solution employs the XGBoost algorithm, known for its high performance in regression tasks. The analysis
            is carried out in a Python environment using libraries such as scikit-learn and Feature-engine for model training and
            feature engineering, along with pandas and numpy for data manipulation and matplotlib for visualization. The project
            includes thorough data analysis to derive insights and improve model accuracy. Hypothesis testing is performed to validate
            assumptions and ensure robustness. After hyperparameter tuning to optimize the model, it is deployed on AWS SageMaker for
            scalable and reliable predictions. This approach combines advanced machine learning techniques with best practices in data
            handling and deployment.""",
            
            #tech_stack
            "tech_stack" : "Used XG boost algo, Scikit Learn and Feature Engine libraries, pandas, numpy, matplotlib and seaborn.",
            
            #git hub link
            "git_hub" : ""
            
        },
    }
    st.markdown("""
            <style>
                .pro_sty{
                    color: #FA603E;
                }
            </style>
                """,unsafe_allow_html=True)
                
    for ind, proj in projects.items():
        st.markdown(f"""
                    <h3 class="pro_sty">{ind}. {proj['title']}</h3> 
                    <dl type="">
                        <h4>🔶 Description : </h4><dd><h6>👉 {proj['description']}</h6></dd><br>
                        <h4>🔶 Tech Stack : </h4><dd><h6>👉 {proj['tech_stack']}</h6></dd><br>
                        <h4>🔶 Git-Hub Link : </h4><dd><h6>👉<a href="{proj['git_hub']}"> {proj['git_hub']}</a></h6></dd><br>
                    </dl>""",
                    unsafe_allow_html=True)

        st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
        )

projects()
    