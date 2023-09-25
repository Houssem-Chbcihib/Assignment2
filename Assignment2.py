import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D from mpl_toolkits.mplot3d
from matplotlib.ticker import FuncFormatter

# Load the dataset
file_path = "https://github.com/Houssem-Chbcihib/Assignment2/blob/main/Coronavirus_Tunisia.csv"  # Update with your file path
df = pd.read_csv(dataset_url)

# Streamlit Sidebar Widgets
st.sidebar.title("COVID-19 Data Visualization")
chart_type = st.sidebar.selectbox("Select Chart Type", ["3D Scatter Plot", "Line Chart"])

# Main content
st.title("COVID-19 Data Visualization App")

if chart_type == "3D Scatter Plot":
    st.header("3D Scatter Plot of COVID-19 Cases in Tunisia (2020)")

    # Creating a filter for data points with cases above or equal to a certain threshold
    threshold = st.slider("Select a Cases Threshold", min_value=0, max_value=5000, value=0)
    filtered_data = df[df['cases'] >= threshold]

    # Creating a 3D scatter plot using Matplotlib
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Extracting data
    x = filtered_data['month']
    y = filtered_data['day']
    z = filtered_data['cases']

    # Creating the scatter plot
    scatter = ax.scatter(x, y, z, c=z, cmap='viridis', marker='o', s=50)

    # Adding labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Day')
    ax.set_zlabel('Cases')
    ax.set_title(f'3D Scatter Plot of COVID-19 Cases in Tunisia (2020) (Cases >= {threshold})')

    # Creating a color scale legend
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Cases', rotation=270, labelpad=20)

    # Formating axis labels as integers
    ax.xaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))
    ax.zaxis.set_major_formatter(FuncFormatter(lambda val, _: int(val)))

    # Setting fixed limits for axes to prevent zooming in
    ax.set_xlim(left=df['month'].min(), right=df['month'].max())
    ax.set_ylim(bottom=df['day'].min(), top=df['day'].max())
    ax.set_zlim(bottom=df['cases'].min(), top=df['cases'].max())

    # Showing the 3D scatter plot
    st.pyplot(fig)

elif chart_type == "Line Chart":
    st.header("Monthly COVID-19 Cases and Deaths in Tunisia (2020)")

    monthly_data = df.groupby('month')[['cases', 'deaths']].sum()

    # Creating a line chart for monthly cases and deaths
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_data.index, monthly_data['cases'], label='Cases', marker='o')
    plt.plot(monthly_data.index, monthly_data['deaths'], label='Deaths', marker='o')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Monthly COVID-19 Cases and Deaths in Tunisia (2020)')
    plt.legend()
    plt.grid(True)

    # Formatting the y-axis label as an integer
    plt.gca().get_yaxis().set_major_formatter(FuncFormatter(lambda val, _: int(val)))

    # Showing the line chart
    st.pyplot()
