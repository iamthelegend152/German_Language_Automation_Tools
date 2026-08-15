# Parent-Monitored Portfolio Track - Munich Student Apartment Selector
print("==================================================")
print("     MUNICH HOUSING & ANMELDUNG VALIDATION NODE   ")
print("==================================================")

print("Select your monthly Euro allocation tier:")
print("1. €400 - €600 (Budget)")
print("2. €650 - €950 (Premium Student Studio)")
print("3. €1200+ (Luxury Serviced Aparthotel)")

budget_tier = input("\nEnter your budget option number (1-3): ").strip()

print("\n--- Housing Market Analysis Engine ---")
if budget_tier == "1":
    print("⚠️ Strategy Alert: Standard tourist hotels are legally banned for long-term stays.")
    print("📍 Route: You must apply early to the 'Studierendenwerk München' dormitory rosters.")
elif budget_tier == "2":
    print("✅ Target Locked: Private Student Accommodations (e.g., Neon Wood, Student One).")
    print("🛡️ Legal Clearance: Landlord form (Wohnungsgeberbestätigung) is 100% guaranteed for your Anmeldung!")
elif budget_tier == "3":
    print("👑 Premium Route: High-tech Serviced Business Apartments (e.g., Revo München, Residence Inn).")
    print("🛡️ Legal Clearance: Full 24/7 reception desk, personal workspace, and immediate town hall registration.")
else:
    print("❌ Input verification error. Please select a valid capital tier.")
