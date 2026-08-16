# Parent-Monitored Academic Tracker - HPSB School Class 6-8 Training Node
print("==================================================")
print("     HPS BEGUMPET GERMAN A1 CURRICULUM TRACKER    ")
print("==================================================")

print("Select your target academic review node:")
print("1. Class 6 (Current Baseline Vocab)")
print("2. Class 7 (Intermediate Grammar Matrices)")
print("3. Class 8 (Official Goethe A1 Exam Prep)")

current_class = input("\nEnter your current class tier (1-3): ").strip()

print("\n--- School Curriculum Study Route ---")
if current_class == "1":
    print("📍 Status: Building base vocabulary blocks.")
    print("📝 Action: Master pronouns (ich, du, er, sie) and classroom objects on your MacBook Pro!")
elif current_class == "2":
    print("📍 Status: Advancing to sentence structures.")
    print("📝 Action: Practice verb conjugations (kommen, wohnen, heißen) and number strings up to 100.")
elif current_class == "3":
    print("📍 Status: GOETHE FIT IN DEUTSCH 1 EXAM ARENA!")
    print("🚀 Action: Run complete mock listening sheets, reading sets, and situational speaking drills with your teacher.")
else:
    print("❌ Input validation error. Select a valid school class tier.")
