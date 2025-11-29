"""
Streamlit Dashboard - A simple data visualization dashboard
Run with: streamlit run streamlit_dashboard.py
"""

import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta


def generate_sample_data():
    """Generate sample data for the dashboard."""
    # Generate dates for last 30 days
    dates = [datetime.now() - timedelta(days=i) for i in range(30)]
    dates.reverse()

    data = {
        "Date": dates,
        "Sales": [random.randint(100, 500) for _ in range(30)],
        "Revenue": [random.randint(1000, 5000) for _ in range(30)],
        "Customers": [random.randint(50, 200) for _ in range(30)],
        "Products_Sold": [random.randint(20, 100) for _ in range(30)]
    }
    return pd.DataFrame(data)


def main():
    """Main function to run the Streamlit dashboard."""
    # Page configuration
    st.set_page_config(
        page_title="Streamlit Dashboard",
        page_icon="📊",
        layout="wide"
    )

    # Title
    st.title("📊 Streamlit Dashboard")
    st.markdown("---")

    # Generate sample data
    df = generate_sample_data()

    # Sidebar
    st.sidebar.header("Dashboard Controls")
    selected_metric = st.sidebar.selectbox(
        "Select Metric to Display",
        ["Sales", "Revenue", "Customers", "Products_Sold"]
    )

    date_range = st.sidebar.slider(
        "Select Date Range (last N days)",
        min_value=7,
        max_value=30,
        value=30
    )

    # Filter data based on date range
    filtered_df = df.tail(date_range)

    # Key Metrics
    st.header("📈 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_sales = filtered_df["Sales"].sum()
        st.metric(
            label="Total Sales",
            value=f"{total_sales:,}",
            delta=f"{filtered_df['Sales'].iloc[-1] - filtered_df['Sales'].iloc[-2]:+d}"
        )

    with col2:
        total_revenue = filtered_df["Revenue"].sum()
        st.metric(
            label="Total Revenue",
            value=f"${total_revenue:,}",
            delta=f"${filtered_df['Revenue'].iloc[-1] - filtered_df['Revenue'].iloc[-2]:+,}"
        )

    with col3:
        total_customers = filtered_df["Customers"].sum()
        st.metric(
            label="Total Customers",
            value=f"{total_customers:,}",
            delta=f"{filtered_df['Customers'].iloc[-1] - filtered_df['Customers'].iloc[-2]:+d}"
        )

    with col4:
        total_products = filtered_df["Products_Sold"].sum()
        st.metric(
            label="Products Sold",
            value=f"{total_products:,}",
            delta=f"{filtered_df['Products_Sold'].iloc[-1] - filtered_df['Products_Sold'].iloc[-2]:+d}"
        )

    st.markdown("---")

    # Charts
    st.header("📊 Data Visualization")

    # Line chart
    st.subheader(f"{selected_metric} Over Time")
    st.line_chart(filtered_df.set_index("Date")[selected_metric])

    # Two column layout for charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Bar Chart - Daily Comparison")
        st.bar_chart(filtered_df.set_index("Date")[selected_metric])

    with col2:
        st.subheader("Area Chart - Cumulative View")
        st.area_chart(filtered_df.set_index("Date")[selected_metric])

    st.markdown("---")

    # Data Table
    st.header("📋 Data Table")

    show_full_data = st.checkbox("Show full dataset")
    if show_full_data:
        st.dataframe(filtered_df)
    else:
        st.dataframe(filtered_df[["Date", selected_metric]])

    # Statistics
    st.header("📊 Statistical Summary")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Summary Statistics")
        st.write(filtered_df[[selected_metric]].describe())

    with col2:
        st.subheader("Additional Info")
        st.write(f"**Mean:** {filtered_df[selected_metric].mean():.2f}")
        st.write(f"**Median:** {filtered_df[selected_metric].median():.2f}")
        st.write(f"**Std Dev:** {filtered_df[selected_metric].std():.2f}")
        st.write(f"**Max:** {filtered_df[selected_metric].max()}")
        st.write(f"**Min:** {filtered_df[selected_metric].min()}")

    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ using Streamlit | "
        f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )


if __name__ == "__main__":
    main()
