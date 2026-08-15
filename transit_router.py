# Parent-Monitored Portfolio Track - Bavarian Transit Router
print("--- MVV Munich Public Transit Simulation Hub ---")
print("Available Stations near your 6-room house zones:")
print("1. Ismaning\n2. Central Station (Hauptbahnhof)\n3. Harras")

user_choice = input("\nEnter the station number you are starting from: ").strip()

print("\n--- Routing Engine Output ---")
if user_choice == "1":
    print("📍 Route: Take S-Bahn S8 to Johanneskirchen ➔ Switch to Bus 230 directly to TUM Garching Campus! 🚄")
elif user_choice == "2":
    print("📍 Route: Take Subway U2 to Scheidplatz ➔ Switch to U6 directly to Garching-Forschungszentrum! 🚇")
elif user_choice == "3":
    print("📍 Route: Take Subway U6 straight north all the way to Garching-Forschungszentrum (No switches needed)! 🚀")
else:
    print("❌ Station out of bounds. Please select a valid Munich transit node.")
