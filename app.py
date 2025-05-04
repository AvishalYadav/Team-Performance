import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import plotly.express as px

# ---- STREAMLIT PAGE CONFIG ----
st.set_page_config(page_title="Team Performance Dashboard", layout="wide")

# ---- GOOGLE SHEET SETUP ----
SCOPE = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive",
         "https://www.googleapis.com/auth/drive.file"]

SERVICE_ACCOUNT_FILE = 'E:\CVs\Latest Resumes\Product\KPI dashboard\streamlit-dashboard-457409-c1afa8bf27ec.json'
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/14C8o2dzUF5eUpUvjgzSlebpma0m-Zqh_tnOqD4JGGyY/edit?gid=0#gid=0"

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPE)

client = gspread.authorize(creds)

spreadsheet = client.open_by_url(SPREADSHEET_URL)
sheet = spreadsheet.worksheet("Data")

data = pd.DataFrame(sheet.get_all_records())

# ---- STREAMLIT DASHBOARD ----
st.title("📊 Team Performance & Resource Utilization Dashboard")

# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filter Projects")
    team_options = st.multiselect("Select Team:", options=data['Team'].unique(), default=data['Team'].unique())
    status_options = st.multiselect("Select Status:", options=data['Status'].unique(), default=data['Status'].unique())

filtered_data = data[
    (data['Team'].isin(team_options)) &
    (data['Status'].isin(status_options))
]

# KPIs
total_projects = len(filtered_data)
completed_projects = len(filtered_data[filtered_data['Status'] == 'Completed'])
total_hours_allocated = filtered_data['Hours Allocated'].sum()
total_hours_spent = filtered_data['Hours Spent'].sum()
total_budget_allocated = filtered_data['Budget Allocated (USD)'].sum()
total_budget_spent = filtered_data['Budget Spent (USD)'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Projects", total_projects)
col2.metric("Completed Projects", completed_projects)
col3.metric("In Progress", len(filtered_data[filtered_data['Status'] == 'In Progress']))

col4, col5, col6 = st.columns(3)
col4.metric("Hours Allocated", total_hours_allocated)
col5.metric("Hours Spent", total_hours_spent)
col6.metric("Budget Spent / Allocated", f"${total_budget_spent:,} / ${total_budget_allocated:,}")

st.markdown("---")

# Charts
col7, col8 = st.columns(2)

# ...existing code...

with col7:
    status_count = filtered_data['Status'].value_counts().reset_index()
    status_count.columns = ['Status', 'count']  # Rename columns for clarity
    fig_status = px.pie(status_count, names='Status', values='count',
                        title='Project Status Distribution', hole=0.4)
    st.plotly_chart(fig_status, use_container_width=True)

with col8:
    team_hours = filtered_data.groupby('Team')[['Hours Spent']].sum().reset_index()
    fig_hours = px.bar(team_hours, x='Team', y='Hours Spent',
                       title='Hours Spent by Team', color='Team', text='Hours Spent')
    st.plotly_chart(fig_hours, use_container_width=True)

# ...existing code...

# Table View
st.subheader("📋 Project Details")
st.dataframe(filtered_data, use_container_width=True)

