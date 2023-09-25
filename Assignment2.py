import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D from mpl_toolkits.mplot3d
from matplotlib.ticker import FuncFormatter

# I extracted the URL of a dataset that I uploaded in Github repository
dataset_url = "https://raw.githubusercontent.com/Houssem-Chbcihib/Assignment2/main/Coronavirus_Tunisia.csv"
# Load the dataset from the URL
df = pd.read_csv(dataset_url)

# Streamlit Sidebar Widgets
st.sidebar.title("COVID-19 Data Visualization")
chart_type = st.sidebar.selectbox("Select Chart Type", ["3D Scatter Plot", "Line Chart"])

# Main content
st.title("COVID-19 Data Visualization App")

if chart_type == "3D Scatter Plot":
    st.header("3D Scatter Plot of COVID-19 Cases in Tunisia (2020)")

    # Create a filter for data points with cases above or equal to a certain threshold
    threshold = st.slider("Select a Cases Threshold", min_value=0, max_value=10000, value=500)
    filtered_data = df[df['cases'] >= threshold]

    # Create a 3D scatter plot using Matplotlib
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Extract data
    x = filtered_data['month']
    y = filtered_data['day']
    z = filtered_data['cases']

    # Create the scatter plot
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', marker='o', s=50)

    # Add labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Day')
    ax.set_zlabel('Cases')
    ax.set_title(f'3D Scatter Plot of COVID-19 Cases in Tunisia (2020) (Cases >= {threshold})')

    # Create a color scale legend
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Cases', rotation=270, labelpad=20)

    # Format axis labels as integers
    ax.xaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))
    ax.zaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))

    # Set fixed limits for axes to prevent zooming in
    ax.set_xlim(left=df['month'].min(), right=df['month'].max())
    ax.set_ylim(bottom=df['day'].min(), top=df['day'].max())
    ax.set_zlim(bottom=df['cases'].min(), top=df['cases'].max())

    # Show the 3D scatter plot
    st.pyplot(fig)

elif chart_type == "Line Chart":
    st.header("Monthly COVID-19 Cases and Deaths in Tunisia (2020)")

    monthly_data = df.groupby('month')[['cases', 'deaths']].sum()

    # Create a line chart for monthly cases and deaths
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index, monthly_data['cases'], label='Cases', marker='o')
    plt.plot(monthly_data.index, monthly_data['deaths'], label='Deaths', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Monthly COVID-19 Cases and Deaths in Tunisia (2020)')
    plt.legend()
    plt.grid(True)

    # Format the y-axis label as an integer
    plt.gca().get_yaxis().set_major_formatter(FuncFormatter(lambda val, _: int(val)))

    # Show the line chart
    st.pyplot()
