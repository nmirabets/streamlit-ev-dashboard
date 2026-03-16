import pandas as pd

def load_ev_data():
    ev_url = "https://api.iea.org/evs?parameters=EV%20sales&category=Historical&mode=Cars&csv=true"
    ev_df = pd.read_csv(ev_url)
    # Split the data into ev_sales and ev_sales_share
    ev_sales = ev_df[ev_df["parameter"] == "EV sales"]
    ev_sales_share = ev_df[ev_df["parameter"] == "EV sales share"]
    # For ev_sales, drop the columns: category, parameter, mode, unit
    ev_sales = ev_sales.drop(columns=["category", "parameter", "mode", "unit"])
    # For ev_sales_share, drop the columns: category, parameter, mode, unit
    ev_sales_share = ev_sales_share.drop(columns=["category", "parameter", "powertrain", "mode", "unit"])
    return ev_sales, ev_sales_share

