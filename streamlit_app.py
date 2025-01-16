import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and description
st.title("EnviroMonitor Dashboard")
st.write("This dashboard provides insights into environmental data trends and metrics.")

# Sidebar for file upload
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load the data
    data = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.write(data.head())

    # Display data statistics
    if st.checkbox("Show dataset statistics"):
        st.write("### Dataset Statistics")
        st.write(data.describe())

    # Select column for visualization
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_columns) > 0:
        st.sidebar.header("Visualization Settings")

        chart_type = st.sidebar.selectbox(
            "Choose chart type", ["Line Plot", "Bar Plot", "Histogram", "Heatmap"]
        )

        column = st.sidebar.selectbox("Select a column", numeric_columns)

        if chart_type == "Line Plot":
            st.write(f"### Line Plot for {column}")
            fig, ax = plt.subplots()
            ax.plot(data[column])
            st.pyplot(fig)

        elif chart_type == "Bar Plot":
            st.write(f"### Bar Plot for {column}")
            fig, ax = plt.subplots()
            ax.bar(data.index, data[column])
            st.pyplot(fig)

        elif chart_type == "Histogram":
            st.write(f"### Histogram for {column}")
            fig, ax = plt.subplots()
            ax.hist(data[column], bins=20)
            st.pyplot(fig)

        elif chart_type == "Heatmap":
            st.write("### Heatmap of Numeric Data")
            fig, ax = plt.subplots()
            sns.heatmap(data[numeric_columns].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    else:
        st.write("No numeric columns available for visualization.")

else:
    st.write("Please upload a CSV file to get started.")
