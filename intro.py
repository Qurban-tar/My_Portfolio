import streamlit as st

# Page config
st.set_page_config(page_title="My Portfolio", layout="wide")

# Tabs on top
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📂 Projects", "📬 Contact Me"])

# --- HOME TAB ---
with tab1:
    st.title("👋 Welcome to My Portfolio")
    st.subheader("Hi, I'm Qurban Ali")
    st.write("""
    I'm a **Data Scientist** with a passion for building real-world data solutions.

    ### 💼 Skills
    - Python, SQL, Pandas, NumPy  
    - Machine Learning, Data Visualization  
    - Streamlit, Power BI  

    ### 🧠 Currently Learning
    - Deep Learning, Advanced Statistics

    Thanks for visiting my site!
    """)

# --- PROJECTS TAB ---
with tab2:
    st.title("📂 My Projects")

    projects = [
        {"title": "Sales Dashboard", "desc": "Analyzed sales data using Pandas & Power BI.", "link": "https://github.com/yourname/sales-dashboard"},
        {"title": "Customer Segmentation", "desc": "K-means clustering on customer data.", "link": "https://github.com/yourname/customer-segmentation"},
        {"title": "Weather Predictor", "desc": "Used Linear Regression to forecast temperature trends.", "link": "https://github.com/yourname/weather-predictor"},
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(project["desc"])
        st.markdown(f"[🔗 View Project]({project['link']})")
        st.markdown("---")

# --- CONTACT ME TAB ---
with tab3:
    st.title("📬 Contact Me")

    st.write("You can reach me through the following platforms:")

    st.markdown("""
    - 📞 **Phone:** 03133925648  
    - 💬 **WhatsApp:** 03408346162  
    - 💬 **Email:** qurban.girhore@gmail.com 
    - 🌐 **Facebook:** [Visit Profile](https://www.facebook.com/profile.php?id=61567707305145)  
    - 💼 **LinkedIn:** [Visit Profile](https://www.linkedin.com/in/qurban-ali-khaskheli-214bb6345?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    """)
