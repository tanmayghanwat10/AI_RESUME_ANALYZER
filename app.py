import streamlit as st
from streamlit_lottie import st_lottie
import requests
import base64

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def set_background(video_file):
    video_path = f"data:video/mp4;base64,{base64.b64encode(open(video_file, "rb").read()).decode()}"
    st.markdown(f'''
        <style>
        .stApp {{
            background: url("{"F:\JOB\AI_Project\resume-analyzer-enhanced\background.mp4"}") no-repeat center center fixed;
            background-size: cover;
        }}
        .main-card {{
            backdrop-filter: blur(10px);
            background-color: rgba(0, 0, 0, 0.5);
            border-radius: 20px;
            padding: 2rem;
            color: white;
        }}
        </style>
    ''', unsafe_allow_html=True)

set_background("background.mp4")

lottie_ai = load_lottieurl("https://lottie.host/0c967b42-4e6e-4d53-98ef-8a8efc91c7f1/6WRtIrnx2W.json")
if lottie_ai:
    st_lottie(lottie_ai, height=200)

st.markdown("<h1 style='text-align:center;'>🧠 AI Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Upload your resume and compare it with job descriptions</p>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        resume_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        job_desc = st.text_area("📄 Paste Job Description")
        st.markdown('</div>', unsafe_allow_html=True)