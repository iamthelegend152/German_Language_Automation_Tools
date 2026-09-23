# Parent-Monitored Portfolio Track - Aeronautical Mach Speed Calculator
print("==================================================")
print("     AERONAUTICAL MACH FLIGHT VELOCITY ENGINE     ")
print("==================================================")

def calculate_mach_number(airspeed_kmh, air_temperature_celsius):
    # Physics formula simulation for speed of sound based on atmospheric temperature
    speed_of_sound_kmh = 1225.0 + (air_temperature_celsius * 2.1)
    mach_number = airspeed_kmh / speed_of_sound_kmh
    
    print(f"Current Aircraft Airspeed: {airspeed_kmh} km/h")
    print(f"Ambient Temperature Node : {air_temperature_celsius}°C")
    print(f"Calculated Speed of Sound: {round(speed_of_sound_kmh, 2)} km/h")
    print("--------------------------------------------------")
    print(f"🚀 SUCCESS: Flight Mach Vector: {round(mach_number, 2)}")
    
    # Structural flight regime tracking boundaries
    if mach_number < 0.8:
        print("Flight Regime Status: 🟢 SUBSONIC CRUISING PROFILE")
    elif 0.8 <= mach_number <= 1.2:
        print("Flight Regime Status: 🟡 TRANSONIC BOUNDARY LAYER ALERT")
    else:
        print("Flight Regime Status: 🔴 SUPERSONIC SHOCKWAVE WAVEFRONT ENGINED")
        
    return mach_number

# Simulated flight metrics (e.g., standard jet aircraft cruising at high velocity)
calculate_mach_number(950.0, -15.0)
