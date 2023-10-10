# HackAI_Hack-230466
Temperature Alert Agent
The Temperature Alert Agent is a versatile tool built using the uAgent library that empowers users to stay informed about real-time weather conditions in their chosen locations. This project is designed to provide users with a personalized temperature monitoring system, ensuring they receive timely alerts when the weather falls outside their preferred temperature range.

# Features
The Temperature Alert Agent offers the following key features:

1. Real-time Temperature Data
The agent connects to a free weather API(openweather) to fetch up-to-date temperature information for the specified location.

3. Customizable Temperature Preferences
Users have the flexibility to set their preferred temperature range by specifying a minimum and maximum temperature. This allows them to tailor the alerts to their specific comfort and safety requirements.

4. Location-Based Alerts
Users can select their desired location for weather monitoring. Whether it's their current location or a place they plan to visit, the agent provides location-based alerts.

5. Alerts and Notifications
The Temperature Alert Agent actively monitors the temperature in the chosen location. If the current temperature falls below the user's set minimum or rises above the maximum threshold, the agent sends an alert or notification to keep the user informed.

# How It Works
The Temperature Alert Agent is powered by the uAgent library, which simplifies the process of fetching weather data and sending alerts. Here's how it works:

User Configuration: Users specify their preferred temperature range and the location they want to monitor.

Weather Data Retrieval: The agent connects to a free weather API(openweather) to obtain real-time temperature information for the specified location.

Continuous Monitoring: The agent continuously monitors the temperature in the chosen location to ensure that users are promptly notified if it goes beyond their set thresholds.

Alerts and Notifications: When the current temperature falls below the minimum or exceeds the maximum threshold, the agent triggers an alert or notification to inform the user.
