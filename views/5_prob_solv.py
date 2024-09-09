import streamlit as st 

def prob():
    st.title(":red[Problem Solving Platforms :]")
    
    st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
    )
    
    st.markdown("""
            <style>
                .pro_sty{
                    color: #FA603E;
                }
            </style>
            """,unsafe_allow_html=True
    )
    
    # code 360
    st.markdown("""
    <div style="border: 2px solid red; padding: 10px; border-radius: 5px;">
        <b class="pro_sty" style="font-size: 30px">Code 360</b>
        <details>
            <summary style="font-size: 1.2em; font-weight: bold;">Expand for My Profile Link</summary>
            <hr style="border-top: 2px solid;">
            <p style="font-size: 20px;">My Code 360 link : </p>
            <a href="https://www.naukri.com/code360/profile/bhuvan_2307" style="font-size: 18px;">https://www.naukri.com/code360/profile/bhuvan_2307</a>
        </details>
    </div><br><br>
    """, unsafe_allow_html=True)

    # leet code
    st.markdown("""
    <div style="border: 2px solid red; padding: 10px; border-radius: 5px;">
        <b class="pro_sty" style="font-size: 30px">Leet Code</b>
        <details>
            <summary style="font-size: 1.2em; font-weight: bold;">Expand for My Profile Link</summary>
            <hr style="border-top: 2px solid;">
            <p style="font-size: 20px;">My Leetcode link : </p>
            <a href="https://leetcode.com/u/Bhuvi_leet_2307/" style="font-size: 18px;">https://leetcode.com/u/Bhuvi_leet_2307/</a>
        </details>
    </div><br><br>
    """, unsafe_allow_html=True)

    # hacker rank
    st.markdown("""
    <div style="border: 2px solid red; padding: 10px; border-radius: 5px;">
        <b class="pro_sty" style="font-size: 30px">Hacker Rank</b>
        <details>
            <summary style="font-size: 1.2em; font-weight: bold;">Expand for My Profile Link</summary>
            <hr style="border-top: 2px solid;">
            <p style="font-size: 20px;">My Hacker Rank link : </p>
            <a href="https://www.hackerrank.com/profile/Bhuvi_2307" style="font-size: 18px;">https://www.hackerrank.com/profile/Bhuvi_2307</a>
        </details>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(
            """
            <hr style="border-top: 3px solid red;">
            """,
            unsafe_allow_html=True
    )

    
prob()