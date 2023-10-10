import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D  # Import Axes3D from mpl_toolkits.mplot3d
from matplotlib.ticker import FuncFormatter

# I extracted the URL of a dataset that I uploaded in Github repository
dataset_url = "https://raw.githubusercontent.com/Houssem-Chbcihib/Assignment2/main/Coronavirus_Tunisia.csv"
# Load the dataset from the URL
df = pd.read_csv(dataset_url)

# Streamlit Sidebar Widgets
st.sidebar.title("COVID-19 Data Visualization")
chart_type = st.sidebar.selectbox("Select Chart Type", ["3D Scatter Plot", "Line Chart"])

# Insert the image in the sidebar
st.sidebar.image("https://www.worldbank.org/content/dam/photos/780x439/2017/apr-4/Tunisia-COVID19-780.jpg", use_column_width=True)

# Insert the image in the sidebar
st.sidebar.image("https://www.amnesty.ie/wp-content/uploads/2020/04/www.amnesty.org180tunis02gettyimages-1209367433.jpg", use_column_width=True)

# Main content
st.title("COVID-19 Data Visualization App")

# Disable Python Notification
st.set_option('deprecation.showPyplotGlobalUse', False)

if chart_type == "3D Scatter Plot":
    st.header("3D Scatter Plot of COVID-19 Cases in Tunisia (2020)")

    # Create a filter for data points with cases above or equal to a certain threshold
    threshold = st.slider("Select a Cases Threshold", min_value=0, max_value=6000, value=0)
    filtered_data = df[df['cases'] >= threshold]

    # Create an interactive 3D scatter plot using Plotly Express with custom settings
    fig = px.scatter_3d(
        filtered_data, x='month', y='day', z='cases',
        color='cases', opacity=0.7,
        labels={'month': 'Month', 'day': 'Day', 'cases': 'Cases'},
        title=f'3D Scatter Plot of COVID-19 Cases in Tunisia (2020) (Cases >= {threshold})'
    )

    # Customize the figure's appearance
    fig.update_layout(
        scene=dict(
            xaxis_title='<b>Month</b>',  # Bold title for X-axis
            yaxis_title='<b>Day</b>',    # Bold title for Y-axis
            zaxis_title='<b>Cases</b>',  # Bold title for Z-axis
            bgcolor='white',  # Set background color to white
            xaxis=dict(title=dict(text='Month', font=dict(color='black')), tickfont=dict(color='black')),  # Black title and numbers for X-axis
            yaxis=dict(title=dict(text='Day', font=dict(color='black')), tickfont=dict(color='black')),    # Black title and numbers for Y-axis
            zaxis=dict(title=dict(text='Cases', font=dict(color='black')), tickfont=dict(color='black'))    # Black title and numbers for Z-axis
        ),
        coloraxis=dict(
            colorscale='RdYlGn_r',  # Use the reversed RdYlGn color scale (green to red)
            cmin=0,  # Set the minimum value for color mapping
            cmax=6000  # Set the maximum value for color mapping
        )
    )

    # Increase the size of the figure
    fig.update_layout(height=600, width=800)

    # Show the 3D scatter plot using st.plotly_chart
    st.plotly_chart(fig)

    # Text under the 3D Scatter Plot
    st.markdown("**Description**:")
    st.write("This 3D scatter plot shows the distribution of COVID-19 cases in Tunisia in 2020.")
    st.write("The color scale represents the number of cases, with red indicating higher cases.")
    st.write("We can see a noticeable increase in cases from month 8 onwards, possibly due to changes in policies or public behavior.")

elif chart_type == "Line Chart":
    st.header("Monthly COVID-19 Cases and Deaths in Tunisia (2020)")

    # Allow users to select which data series to display
    selected_data = st.multiselect("Select Data Series", ["Cases", "Deaths"], default=["Cases", "Deaths"])

    if "Cases" in selected_data:
        st.subheader("Cases")
        monthly_data_cases = df.groupby('month')['cases'].sum().tolist()
    if "Deaths" in selected_data:
        st.subheader("Deaths")
        monthly_data_deaths = df.groupby('month')['deaths'].sum().tolist()

    plt.figure(figsize=(12, 6))

    if "Cases" in selected_data:
        plt.plot(df['month'].unique(), monthly_data_cases, label='Cases', marker='o', color='blue')

    if "Deaths" in selected_data:
        plt.plot(df['month'].unique(), monthly_data_deaths, label='Deaths', marker='o', color='red')

    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.title('Monthly COVID-19 Cases and Deaths in Tunisia (2020)')
    plt.legend()
    plt.grid(True)
    plt.gca().get_yaxis().set_major_formatter(FuncFormatter(lambda val, _: int(val)))

    st.pyplot()

    # Text under the Line Chart
    st.markdown("**Description**:")
    st.write("This line chart displays the monthly count of COVID-19 cases and deaths in Tunisia for the year 2020.")
    st.write("Users can select specific data series (Cases, Deaths) to visualize.")
    st.write("The chart provides insights into the trends of cases and deaths over time.")
