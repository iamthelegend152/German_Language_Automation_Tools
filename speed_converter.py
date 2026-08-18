# Parent-Monitored Portfolio Track - Bavarian Speed Unit Converter
print("==================================================")
print("     BAVARIAN METRIC TRANSIT CONVERSION ENGINE     ")
print("==================================================")

def convert_kmh_to_mph(kmh_input):
    # Metric physics constant factor ratio rule (1 km/h = 0.621371 mph)
    conversion_factor = 0.621371
    
    mph_output = kmh_input * conversion_factor
    
    print(f"Input German Rail Velocity  : {kmh_input} km/h")
    print("--------------------------------------------------")
    print(f"🚀 SUCCESS: Converted Output String : {round(mph_output, 2)} mph")
    return mph_output

# Simulated train vector tracking (e.g., standard German ICE train operating speed of 250 km/h)
ice_train_velocity = 250.0
convert_kmh_to_mph(ice_train_velocity)
