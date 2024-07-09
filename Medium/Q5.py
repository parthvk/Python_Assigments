# You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
def analyze_temperatures(temperatures):
    print("Average temperature: ", sum(temperatures)/len(temperatures))
    print("Highest temperature: ", max(temperatures))
    print("Lowest temperature: ", min(temperatures))
    
temperature_readings = [25, 28, 21, 24, 27]
analyze_temperatures(temperature_readings)