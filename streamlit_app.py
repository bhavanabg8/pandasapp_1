
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

# Load CSV data (replace 'data.csv' with your actual CSV file path)
# data = pd.DataFrame({
#     "Category": ["A", "B", "C", "D", "E", "A", "B", "C", "D", "E"],
#     "City": ["City1", "City1", "City1", "City1", "City1", "City2", "City2", "City2", "City2", "City2"],
#     "Sales": [100, 200, 150, 300, 250, 400, 100, 300, 200, 150]
# })
data = pd.read_csv("Supermart_dataset.csv") 

# Streamlit app
st.title("Top 7 Categories by Sales")

# Dropdown filter for City
cities = data['City'].unique()
selected_city = st.selectbox("Select a city:", cities, key='city')

if st.button("Generate Plot"):
    # Filter data based on the selected city
    filtered_data = data[data['City'] == selected_city]

    # Group by Category and sum the sales
    grouped_data = filtered_data.groupby('Category')['Sales'].sum().reset_index()

    # Sort by Sales in descending order and select top 5
    top_7 = grouped_data.sort_values(by='Sales', ascending=False).head(7)

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(top_7['Category'], top_7['Sales'], color='skyblue')
    ax.set_title("Top 7 Categories by Sales")
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")

    # Display the plot
    st.pyplot(fig)


# Add download option for the plot
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    st.download_button(
        label="Download Plot as PNG",
        data=buf,
        file_name="top_7_categories_sales.png",
        mime="image/png"
    )
# gpu-htga-cbp