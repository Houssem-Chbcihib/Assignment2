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

    # Create a separate legend indicating the color scale and values
    color_legend = [0, 3000, 6000]
    st.write("**Color Scale**:")
    st.markdown(
        "- <span style='color:red; text-decoration: underline;'>High Cases</span>"
        "<br>- Moderate Cases"
        "<br>- <span style='color:green;'>Low Cases</span>",
        unsafe_allow_html=True
    )

    # Increase the size of the figure
    fig.update_layout(height=600, width=800)

    # Show the 3D scatter plot using st.plotly_chart
    st.plotly_chart(fig)

    # Text under the 3D Scatter Plot
    st.markdown("<h3>Description:</h3>", unsafe_allow_html=True)
    st.markdown("<ul>"
                "<li>Visualizes the distribution of COVID-19 cases in Tunisia in 2020.</li>"
                "<li><span style='color:red;'>Red color represents higher cases.</span></li>"
                "<li>Notice the increase in cases from month 8, potentially due to policy changes.</li>"
                "</ul>", unsafe_allow_html=True)

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
    st.markdown("<h3>Description:</h3>", unsafe_allow_html=True)
    st.markdown("<ul>"
                "<li>Displays the monthly count of COVID-19 cases and deaths in Tunisia for 2020.</li>"
                "<li>Users can select specific data series (Cases, Deaths) for visualization.</li>"
                "<li>Provides insights into the trends of cases and deaths over time.</li>"
                "</ul>", unsafe_allow_html=True)
