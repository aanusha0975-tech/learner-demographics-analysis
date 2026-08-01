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
    st.subheader("Users Data")
st.dataframe(users)  # st.dataframe(user)

st.subheader("Age Distribution")

fig = px.histogram(
    users,
    x="Age",
    title="Age Distribution of Learners"
)

st.plotly_chart(fig)
merged = transactions.merge(users, on='UserID')
merged = merged.merge(courses, on='CourseID')
st.subheader("Course Enrolment by Age Group")

age_course = merged.groupby(["Age", "CourseName"]).size().reset_index(name="Enrollments")

fig2 = px.bar(
    age_course,
    x="Age",
    y="Enrollments",
    color="CourseName",
    title="Course Enrolment by Age Group"
)

st.plotly_chart(fig2)
st.subheader("Gender-based Difference in Course Enrollments")

gender_course = merged.groupby(["Gender", "CourseName"]).size().reset_index(name="Enrollments")

fig3 = px.bar(
    gender_course,
    x="CourseName",
    y="Enrollments",
    color="Gender",
    barmode="group",
    title="Gender-based Difference in Course Enrollments"
)

st.plotly_chart(fig3)
st.subheader("Course Categories with Highest Enrollments")

category = merged.groupby("CourseCategory").size().reset_index(name="Enrollments")

fig4 = px.bar(
    category,
    x="CourseCategory",
    y="Enrollments",
    color="CourseCategory",
    title="Course Categories with Highest Enrollments"
)

st.plotly_chart(fig4)
st.subheader("Preferred Course Types")

course_type = merged.groupby("CourseType").size().reset_index(name="Enrollments")

fig5 = px.pie(
    course_type,
    names="CourseType",
    values="Enrollments",
    title="Preferred Course Types"
)

st.plotly_chart(fig5)
st.subheader("Preferred Course Levels")

course_level = merged.groupby("CourseLevel").size().reset_index(name="Enrollments")

fig6 = px.bar(
    course_level,
    x="CourseLevel",
    y="Enrollments",
    color="CourseLevel",
    title="Preferred Course Levels"
)

st.plotly_chart(fig6)