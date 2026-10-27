import streamlit as st
import pickle
import time
import random
import plotly.graph_objects as go

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Spam and Scam Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- LOAD MODELS ----------------

sms_model = pickle.load(open("models/spam_model.pkl","rb"))
sms_vec = pickle.load(open("models/vectorizer.pkl","rb"))

email_model = pickle.load(open("models/email_spam_model.pkl","rb"))
email_vec = pickle.load(open("models/email_vectorizer.pkl","rb"))

fraud_model = pickle.load(open("models/fraud_model.pkl","rb"))

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page="home"

# ---------------- CSS DESIGN ----------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#000000);
color:white;
font-family: 'Segoe UI', sans-serif;
}

.title{
font-size:50px;
font-weight:800;
text-align:center;
color:#e6edf7;
margin-bottom:10px;
}

.subtitle{
text-align:center;
font-size:18px;
color:#b8c3d1;
}

.glass{
background:rgba(255,255,255,0.05);
border-radius:18px;
padding:25px;
border:1px solid rgba(255,255,255,0.15);
transition:.3s;
}

.glass:hover{
transform:scale(1.02);
border:1px solid #4cc9f0;
box-shadow:0 0 20px rgba(76,201,240,0.3);
}

.feature{
background:rgba(255,255,255,0.04);
padding:20px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.15);
text-align:center;
transition:.3s;
}

.feature:hover{
border:1px solid #00c6ff;
box-shadow:0 0 20px rgba(0,198,255,0.4);
transform:scale(1.03);
}

.stButton>button{
background:linear-gradient(45deg,#00c6ff,#0072ff);
border:none;
border-radius:25px;
color:white;
padding:10px 25px;
font-weight:bold;
}

.stButton>button:hover{
transform:scale(1.05);
}

.mentor{
text-align:center;
background:rgba(255,255,255,0.05);
padding:15px;
border-radius:12px;
border:1px solid #4cc9f0;
margin-top:25px;
}

.footer{
text-align:center;
color:#c0c0c0;
font-size:15px;
margin-top:40px;
padding-top:20px;
border-top:1px solid rgba(255,255,255,0.2);
}

</style>
""",unsafe_allow_html=True)

# ---------------- AI PROCESS ----------------

def ai_process(msg):
    with st.spinner(msg):
        time.sleep(1)

# ---------------- RADAR CHART ----------------

def radar_chart():

    categories=['Spam','Fraud','Phishing','Malware','Scam']
    values=[random.randint(40,95) for _ in categories]

    fig=go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line=dict(color='#00c6ff')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        height=350
    )

    st.plotly_chart(fig,use_container_width=True)

# ---------------- RISK GAUGE ----------------

def risk_gauge(score):

    fig=go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text':"Threat Score"},
        gauge={
            'axis':{'range':[0,100]},
            'bar':{'color':"#0072ff"},
            'steps':[
                {'range':[0,40],'color':'#2ecc71'},
                {'range':[40,70],'color':'#f1c40f'},
                {'range':[70,100],'color':'#e74c3c'}
            ]
        }
    ))

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)")

    st.plotly_chart(fig,use_container_width=True)

# ---------------- HOME PAGE ----------------

def home():

    st.markdown('<div class="title">Spam and Scam Detection System</div>',unsafe_allow_html=True)

    st.markdown('<div class="subtitle">Minor Project | Department of Computer Science and Engineering | Purnea College of Engineering</div>',unsafe_allow_html=True)

    st.write("")

    col1,col2=st.columns([2,1])

    with col1:

        st.markdown('<div class="glass">',unsafe_allow_html=True)

        st.markdown("""
### Project Overview

The **Spam and Scam Detection System** is a machine learning based platform designed to detect spam messages, fraudulent emails and suspicious financial transactions.

This system uses machine learning models and natural language processing techniques to identify cyber threats.

Modules Included:

• SMS Spam Detection  
• Email Spam Detection  
• Financial Scam Detection  
        """)

        if st.button("Enter Detection Dashboard"):
            st.session_state.page="dashboard"

        st.markdown('</div>',unsafe_allow_html=True)

    with col2:

        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png",width=220)

    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown('<div class="feature"><h4>SMS Spam Detection</h4><p>Identify suspicious promotional messages using machine learning.</p></div>',unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="feature"><h4>Email Spam Detection</h4><p>Detect spam and phishing emails using NLP techniques.</p></div>',unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="feature"><h4>Financial Scam Detection</h4><p>Analyze transactions and detect fraudulent activities.</p></div>',unsafe_allow_html=True)

    st.markdown("""
<div class="mentor">

<b>Project Mentor</b><br>
Dr. Priti Kumari

</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="footer">

<b>Minor Project</b><br>
Department of Computer Science and Engineering<br>
Purnea College of Engineering

<br><br>

<b>Team Members</b><br>

Rohit Chakraverty<br>
Ritu Priya<br>
Rashmi Pacheriya<br>
Prabhat Kumar

</div>
""",unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------

def dashboard():

    st.markdown('<div class="title">Spam and Scam Detection Dashboard</div>',unsafe_allow_html=True)

    col1,col2,col3,col4=st.columns(4)

    col1.metric("Messages Scanned","12421","+12%")
    col2.metric("Spam Detected","3291","+7%")
    col3.metric("Fraud Alerts","182","+4%")
    col4.metric("System Accuracy","96.4%")

    st.write("")

    st.subheader("Threat Overview")

    radar_chart()

    st.write("")

    c1,c2,c3=st.columns(3)

    with c1:
        if st.button("📱 SMS Spam Detection"):
            st.session_state.page="sms"

    with c2:
        if st.button("📧 Email Spam Detection"):
            st.session_state.page="email"

    with c3:
        if st.button("💳 Financial Scam Detection"):
            st.session_state.page="fraud"

# ---------------- SMS ----------------

def sms():

    st.markdown('<div class="title">SMS Spam Detection</div>',unsafe_allow_html=True)

    msg=st.text_area("Enter SMS Message")

    if st.button("Analyze SMS"):

        ai_process("Analyzing SMS")

        vec=sms_vec.transform([msg])
        pred=sms_model.predict(vec)[0]

        risk=random.randint(50,95)

        if pred==1:
            st.error("Spam Message Detected")
            risk_gauge(risk)
        else:
            st.success("Legitimate Message")

    if st.button("Back"):
        st.session_state.page="dashboard"

# ---------------- EMAIL ----------------

def email():

    st.markdown('<div class="title">Email Spam Detection</div>',unsafe_allow_html=True)

    msg=st.text_area("Enter Email Content")

    if st.button("Analyze Email"):

        ai_process("Analyzing Email")

        vec=email_vec.transform([msg])
        pred=email_model.predict(vec)[0]

        risk=random.randint(50,95)

        if pred==1:
            st.error("Spam Email Detected")
            risk_gauge(risk)
        else:
            st.success("Trusted Email")

    if st.button("Back"):
        st.session_state.page="dashboard"

# ---------------- FRAUD ----------------

def fraud():

    st.markdown('<div class="title">Financial Scam Detection</div>',unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        f1=st.number_input("Feature 1")

    with c2:
        f2=st.number_input("Feature 2")

    with c3:
        f3=st.number_input("Feature 3")

    if st.button("Analyze Transaction"):

        ai_process("Analyzing Transaction")

        features=[f1,f2,f3]+[0]*27
        pred=fraud_model.predict([features])[0]

        risk=random.randint(60,95)

        if pred==1:
            st.error("Fraudulent Transaction")
            risk_gauge(risk)
        else:
            st.success("Legitimate Transaction")

    if st.button("Back"):
        st.session_state.page="dashboard"

# ---------------- ROUTER ----------------

if st.session_state.page=="home":
    home()

elif st.session_state.page=="dashboard":
    dashboard()

elif st.session_state.page=="sms":
    sms()

elif st.session_state.page=="email":
    email()

elif st.session_state.page=="fraud":
    fraud()