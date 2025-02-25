import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title='Dynamic Web App', layout='wide', page_icon='🌟')

# Sidebar navigation
st.sidebar.title("Navigation")
tab_choice = st.sidebar.radio("Go to", ["Home", "Data Visualization", "About"])

# Home Tab
if tab_choice == "Home":
    st.title("🌟 Welcome to the Dynamic Streamlit Web App")
    st.write("This is a modern and interactive web application built with Streamlit.")
    
    st.image("https://media.licdn.com/dms/image/C4E03AQEbUWdZxS_8ig/profile-displayphoto-shrink_200_200/0/1638368405671?e=2147483647&v=beta&t=r3vSYgmD8glAVDaE4aehBJmJaqrw-qWAqLx0YCs8leM", use_container_width=True)
    st.markdown("### Features:")
    st.write("- Interactive sidebar navigation")
    st.write("- Beautiful data visualizations with Plotly")
    st.write("- Responsive and dynamic UI")

# Data Visualization Tab
elif tab_choice == "Data Visualization":
    st.title("📊 Data Visualization")
    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Dataset Preview:")
        st.dataframe(df.head())
        
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        if numeric_columns:
            x_axis = st.selectbox("Select X-axis", numeric_columns)
            y_axis = st.selectbox("Select Y-axis", numeric_columns)
            
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"Scatter Plot of {x_axis} vs {y_axis}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No numeric columns found in the dataset!")

# About Tab
elif tab_choice == "About":
    st.title("ℹ️ About")
    st.write("This web application is built using **Streamlit**, a powerful Python framework for creating data-driven apps.")
    st.write("#### Developed by: Your Name")
    st.write("🚀 Connect with me on [LinkedIn](https://www.linkedin.com) or [GitHub](https://github.com)")
