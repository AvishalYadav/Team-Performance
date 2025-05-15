# Team Performance Dashboard

A Streamlit dashboard for tracking team performance and resource utilization metrics.

## Features

- Real-time data visualization from Google Sheets
- Team performance metrics
- Resource utilization tracking
- Project status monitoring
- Budget and hours tracking

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Google Sheets API credentials
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment

This app is deployed on Streamlit Community Cloud. Visit the [dashboard](https://avishalyadav-team-performance.streamlit.app/) to view the live version.

## Data Source

The dashboard pulls data from a [Google Sheet]([url](https://docs.google.com/spreadsheets/d/14C8o2dzUF5eUpUvjgzSlebpma0m-Zqh_tnOqD4JGGyY/edit?gid=0#gid=0)) that contains:
- Team information
- Project status
- Hours allocated and spent
- Budget information
