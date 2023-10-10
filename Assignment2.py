import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FuncFormatter

# Load the dataset from the URL
dataset_url = "https://raw.githubusercontent.com/Houssem-Chbcihib/Assignment2/main/Coronavirus_Tunisia.csv"
df = pd.read_csv(dataset_url)

# Streamlit Sidebar Widgets
st.sidebar.title("COVID-19 Data Visualization")
chart_type = st.sidebar.selectbox("Select Chart Type", ["3D Scatter Plot", "Line Chart"])

# Insert images in the sidebar
st.sidebar.image("https://www.worldbank.org/content/dam/photos/780x439/2017/apr-4/Tunisia-COVID19-780.jpg", use_column_width=True)
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
            yaxis=dict(title=dict(text='Day', font=dict(color='black')), tickfont=dict(color='black')),  # Black title and numbers for Y-axis
            zaxis=dict(title=dict(text='Cases', font=dict(color='black')), tickfont=dict(color='black'))  # Black title and numbers for Z-axis
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
    st.markdown("<hr style='border:2px solid black'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1f77b4;'>Description:</h3>", unsafe_allow_html=True)
    st.markdown("<ul style='color: #1f77b4; list-style-type: disc;'>", unsafe_allow_html=True)
    st.markdown("<li>Animate bullet point 1</li>", unsafe_allow_html=True)
    st.markdown("<li>Animate bullet point 2</li>", unsafe_allow_html=True)
    st.markdown("<li>Animate bullet point 3</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1f77b4;'>This 3D scatter plot illustrates the distribution of COVID-19 cases in Tunisia during 2020.</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #1f77b4;'>The color scale represents case numbers, with <span style='color: red;'>red</span> indicating higher counts.</p>", unsafe_allow_html=True)
    st.mark
