import streamlit as st
from gps_tracker import log_gps_ping
from map_replay import display_replay
from heatmap_generator import generate_heatmap
from reverse_route_analyzer import analyze_reverse_route
from motion_alerts import monitor_speed_and_alert
from google_sheets_logger import log_to_sheets

st.set_page_config(page_title="ScalpX Tracker Suite", layout="wide")
st.title("🚘 ScalpX GPS Intelligence Dashboard")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📍 Live Tracker", "🕹️ Replay", "🔥 Heatmap", "🔄 Reverse Route", "📊 Logs"])

with tab1:
    st.header("📍 Live GPS Ping")
    log_gps_ping()

with tab2:
    st.header("🕹️ Replay Viewer")
    display_replay()

with tab3:
    st.header("🔥 Heatmap Generator")
    generate_heatmap()

with tab4:
    st.header("🔄 Reverse Route Analyzer")
    analyze_reverse_route()

with tab5:
    st.header("📊 Motion Alerts + Sheet Logs")
    monitor_speed_and_alert()
    log_to_sheets()