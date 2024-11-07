# EnviroMonitor

**EnviroMonitor** is an environmental monitoring and data visualization dashboard that provides real-time insights into temperature, humidity, soil moisture, and CO₂ levels. The project aims to help users make informed decisions by presenting environmental data in an intuitive and interactive way.

## Features

- **Real-Time Data Monitoring**: Continuously update and display data for environmental metrics such as temperature, humidity, soil moisture, and CO₂.
- **Traffic Light System**: Visual indication for soil moisture levels using red, yellow, and green indicators to represent low, moderate, and optimal moisture.
- **Interactive Visualizations**: Plotly-powered charts for data analysis, including bar charts, scatter plots, and treemaps.
- **REST API Integration**: Collects data from IoT sensors or other sources through a Flask server with SQLite database integration.
- **Ngrok Integration**: Easily expose the local server to the internet for remote access and monitoring.

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: Flask
- **Database**: SQLite
- **Visualization**: Plotly, Matplotlib
- **Deployment**: Ngrok for secure tunneling

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/EnviroMonitor-Dashboard.git
    cd EnviroSuite
    ```

2. Install the required packages:

    ```bash
    pip install streamlit pyngrok pandas matplotlib plotly flask
    ```

3. Start the Flask server:

    ```bash
    python server.py
    ```

4. Start the Streamlit app in a separate terminal:

    ```bash
    streamlit run app.py
    ```

5. Expose the application using Ngrok:

    ```python
    from pyngrok import ngrok
    ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
    flask_tunnel = ngrok.connect(5000)
    print("Flask server running on:", flask_tunnel.public_url)
    
    streamlit_tunnel = ngrok.connect(8501)
    print("Streamlit app running on:", streamlit_tunnel.public_url)
    ```

6. The app should now be accessible from the printed Ngrok URLs.

## Usage

### Dashboard Features

- **Summary Statistics**: Displays minimum, maximum, and average values for temperature, humidity, soil moisture, and CO₂.
- **Visualization Charts**: Various types of charts and graphs to track changes over time.
- **Traffic Light Indicator**: Provides a visual indicator for soil moisture levels, helping users quickly interpret whether moisture is within a safe range.
  
### REST API

The Flask server includes a REST API endpoint to receive data from IoT devices or other sources.

- **Endpoint**: `/data` (POST request)
- **Data Format**:
  ```json
  {
    "temperature": 25.3,
    "humidity": 45.6,
    "soil_moisture": 400,
    "CO2": 800
  }
