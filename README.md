Certainly, here's an improved version of your README.md with a more professional appearance and formatting:

---

# HackAI_Hack-230466

## Temperature Alert Agent

The Temperature Alert Agent is a robust tool built using the uAgent library, designed to empower users by providing real-time weather updates for their chosen locations. This project offers a personalized temperature monitoring system, ensuring users receive timely alerts when the weather conditions fall outside their preferred temperature range.

## Features

### 1. Real-time Temperature Data
The agent seamlessly connects to the free openweather API to fetch up-to-date temperature information for the specified location.

### 2. Customizable Temperature Preferences
Users enjoy the flexibility of setting their preferred temperature range by specifying minimum and maximum thresholds. This feature allows them to tailor alerts to match their comfort and safety requirements.

### 3. Location-Based Alerts
Users can select their desired location for weather monitoring, whether it's their current location or a place they plan to visit. The agent provides location-based alerts, ensuring relevant and accurate weather updates.

### 4. Alerts and Notifications
The Temperature Alert Agent actively monitors temperature changes in the chosen location. If the current temperature falls below the user's set minimum or rises above the maximum threshold, the agent sends immediate alerts and notifications to keep the user well-informed.

## How It Works

The Temperature Alert Agent harnesses the power of the uAgent library, simplifying the process of fetching weather data and sending alerts. Here's a brief overview of its functionality:

1. **User Configuration**: Users specify their preferred temperature range and the location they want to monitor.

2. **Weather Data Retrieval**: The agent seamlessly connects to the openweather API to obtain real-time temperature information for the specified location.

3. **Continuous Monitoring**: The agent continually tracks temperature changes in the chosen location, ensuring users are promptly notified if conditions go beyond their set thresholds.

4. **Alerts and Notifications**: When the current temperature falls below the minimum or exceeds the maximum threshold, the agent triggers instant alerts or notifications, keeping the user informed and prepared.

## How to Use

Follow these steps to effectively utilize the Temperature Alert Agent:

1. **Obtain an API Key from OpenWeather**: Sign in or create an account at [OpenWeather](https://openweathermap.org/api) to generate your API Key.

2. **API Key Configuration**: Replace the placeholder in the following line found in `src/agents/Scripts/APICall.py` with your API Key:

   ```python
   API_KEY = "ENTER_YOUR_API_KEY"
   ```

3. **Run the Scripts**: Execute the two scripts located in `src/agents/Alert.py` and `src/agents/client.py` in separate dedicated terminals. If you're using VSCode, consider installing the "Code Runner" extension to run the codes in dedicated terminals.

4. **Start the Agent**: After the agents have successfully registered on the Almanac, run `src/starter.py` in a dedicated terminal.

5. **Configuration Prompt**: You'll be greeted with a message prompting you to enter your location details in the terminal. You will need to specify the city you want to find the location of, as well as the maximum and minimum temperature thresholds.

6. **Temperature Check**: The terminal will then display whether the current temperature in the specified location falls within the entered range of maximum and minimum temperatures.

7. **Repeat the Process**: The process will restart, allowing you to enter new or the same location and adjust the maximum and minimum values as needed. The cycle will continue every 8 seconds.

Enjoy accurate and timely weather updates with the Temperature Alert Agent!
If you want to know more about openweather, uagents, visit the links below
1. For OpenWeather: https://openweathermap.org/
2. For Uagents: https://fetch.ai/docs
