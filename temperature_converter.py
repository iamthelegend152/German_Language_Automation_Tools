# Parent-Monitored Portfolio Track - Bavarian Thermal Conversion Matrix
print("==================================================")
print("     BAVARIAN THERMAL CONVERSION SYSTEM ENGINE    ")
print("==================================================")

def run_thermal_conversion(celsius_input):
    print(f"Initializing calculation array for Base Metric: {celsius_input}°C")
    print("--------------------------------------------------")
    
    # 🌡️ Calculate Fahrenheit Scale: (C * 9/5) + 32
    fahrenheit = (celsius_input * 9.0 / 5.0) + 32.0
    
    # 🌡️ Calculate Kelvin Scale: C + 273.15 (Standard Physics Constant)
    kelvin = celsius_input + 273.15
    
    print(f"🔹 Metric Output Fahrenheit: {round(fahrenheit, 2)}°F")
    print(f"🔹 Metric Output Kelvin    : {round(kelvin, 2)}K")
    return {"F": fahrenheit, "K": kelvin}

# Execute system testing sequence with a baseline sample
room_temperature_hyderabad = 28.5
run_thermal_conversion(room_temperature_hyderabad)
