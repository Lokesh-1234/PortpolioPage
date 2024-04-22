import streamlit as st
import os

# Set up the static folder
static_dir = 'static'

# Define the index route
def index():
    st.title('Lokesh Rachuri Portfolio')
    st.header('Machine Learning Engineer')

    # About Me section
    st.header('About Me')
    st.markdown("""
        🎓 Hey there! I'm Lokesh Rachuri,
        
        💻 As a highly skilled and diligent individual, I am actively seeking an opportunity to establish a rewarding career in the dynamic field of data science. 
        
        🚀 With a passion for leveraging analytical tools, statistics, and machine learning techniques, I am eager to contribute my expertise to drive actionable insights and innovation within the organization where I work.
        
        🎯 My goal is to utilize my proficiency in data analysis, exploratory data visualization, and predictive modeling to tackle complex challenges, optimize processes, and drive business growth.
        
        I am committed to continuous learning and growth, aiming to make meaningful contributions to the field of data science while advancing both personal and organizational objectives.
    """)

    # Download resume link
    st.header('Resume')
    st.markdown('[Download my resume](http://localhost:8501/download_resume)')

    # Contact section
    st.header('Contact')
    st.markdown("""
        - Email: lokeshrachuri177@email.com
        - Phone: +91 6303212724
    """)

# Define the download_resume route
def download_resume():
    resume_path = os.path.join(static_dir, 'resume.pdf')
    st.download_button('Download Resume', resume_path, 'resume.pdf', 'application/pdf')

# Main function to run the application
def main():
    index()

# Entry point of the application
if __name__ == '__main__':
    main()
