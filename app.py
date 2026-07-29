import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="EduPro Analytics", layout="wide")
st.title("Learner Demographics and Course Enrollment")
uploaded_file = st.file_uploader("Upload your dataset (Excel)", type=["xlsx"])
if uploaded_file:
    users = pd.read_excel(uploaded_file, sheet_name='Users')
    courses = pd.read_excel(uploaded_file, sheet_name='Courses')
    transactions = pd.read_excel(uploaded_file, sheet_name='Transactions')
    # Merge them and proceed with analysis...