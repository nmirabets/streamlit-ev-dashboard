import streamlit as st
from functions import load_ev_data

# Set up the page
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="expanded" # or expanded
)

# Load the ev data
ev_sales, ev_sales_share = load_ev_data()

# Page title
st.title("📊 EV Adoption Dashboard")

# Subheader
st.subheader("🌍 World EV Sales Summary")

# Expander with info on the datasource
with st.expander("About the data"):
    st.markdown("The data for this dashboard is sourced from the IEA [International Energy Agency](https://www.iea.org).")

# Add three metric cards, side-by-side
col1, col2, col3 = st.columns(3)

col1.metric("Total EV Sales", value="40M", delta="0.4M", border=True)
col2.metric("Total EV Sales Share", value="20%", delta="0.4%", border=True)
col3.metric("Total EV Sales Share", value="30%", delta="0.1%", border=True)

# Add a divider
st.divider()

# Add a chart title
st.subheader("🔍 EV World Sales")

# Add a bar chart of the EV world sales
# Filter for the world region
world_ev_sales = ev_sales[ev_sales["region"] == "World"]
# Convert units to millions
world_ev_sales["value"] = world_ev_sales["value"] / 1000000

st.bar_chart(world_ev_sales, x="year", y="value", color="powertrain", x_label="Year", y_label="Sales (M)")