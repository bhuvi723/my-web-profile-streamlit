import streamlit as st 

home_page = st.Page(
    page = "views/1_home.py",
    title="About Me",
    icon="🏠",
    default = True
)

project_2_page = st.Page(
    page="views/2_projects.py",
    title="Projects",
    icon="📚"
)

project_3_page = st.Page(
    page = "views/3_certifications.py",
    title="Certifications",
    icon="📃"
)

project_4_page = st.Page(
    page="views/4_intern.py",
    title="Internships",
    icon="🧩"
)

project_5_page = st.Page(
    page="views/5_prob_solv.py",
    title="Problem solving",
    icon="🚀"
)

project_6_page = st.Page(
    page="views/6_contact.py",
    title="Contact",
    icon="📚"
)

pg = st.navigation(pages=[home_page,project_2_page,project_3_page,project_4_page,project_5_page,project_6_page])
pg.run()

