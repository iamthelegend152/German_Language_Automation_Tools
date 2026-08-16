# Parent-Monitored Portfolio Track - Unified TUM Strategic Suite Engine
import random
import datetime

# Comprehensive multi-level vocabulary data matrix
language_matrix = {
    "A1 Nouns": {
        "der Computer": "the computer",
        "das Handy": "the mobile phone",
        "die Schule": "the school",
        "das Haus": "the house",
        "der Lehrer": "the teacher"
    },
    "A1 Verbs": {
        "programmieren": "to program",
        "studieren": "to study",
        "lernen": "to learn",
        "sprechen": "to speak",
        "wohnen": "to live"
    }
}

def check_tum_countdown():
    print("\n--- [MODULE 1: RE-LOCATION TIME VECTOR CLOCK] ---")
    target_date = datetime.date(2032, 7, 15) # Post-Class 12 departure vector
    current_date = datetime.date.today()
    days_left = (target_date - current_date).days
    print(f"📍 System Log Date: {current_date}")
    print(f"📍 Target Departure: {target_date}")
    print(f"🚀 Vector Remaining: {days_left} days until Munich relocation.")

def run_hpsb_academic_check():
    print("\n--- [MODULE 2: HPS BEGUMPET SCORE TRACKER] ---")
    print("Enter your target score for current school mathematics:")
    try:
        score_input = float(input("Target Percentage (e.g., 95): ").strip())
        if score_input >= 95.0:
            print("🚀 Status Verified: Grade trajectory matches TUM baseline entry protocols!")
        else:
            print("⚠️ Status Alert: Increase study block parameters to secure 95%+ matrix.")
    except ValueError:
        print("❌ Data Format Error: Please enter a valid numerical sequence.")

def execute_language_drill():
    print("\n--- [MODULE 3: SYSTEMIC VOCABULARY TESTING HUB] ---")
    category = random.choice(["A1 Nouns", "A1 Verbs"])
    german_token, english_target = random.choice(list(language_matrix[category].items()))
    
    print(f"Active Dictionary Node: {category}")
    user_response = input(f"Translate the German term '{german_token}': ").strip().lower()
    
    if user_response == english_target:
        print("🚀 Code Execution Verified: Correct entry node locked.")
    else:
        print(f"❌ Logic Error: Target definition is '{english_target}'")

def main_system_loop():
    while True:
        print("\n==================================================")
        print("      TUM MUNICH UNIFIED ADVANCED MASTER RUNTIME  ")
        print("==================================================")
        print("Select Executive Operations Vector:")
        print("1. Launch Relocation Countdown Clock")
        print("2. Check HPSB Math Score Alignments")
        print("3. Execute German A1 Vocabulary Tester")
        print("4. Terminate Station Terminal")
        
        vector_choice = input("\nEnter system option (1-4): ").strip()
        
        if vector_choice == "1":
            check_tum_countdown()
        elif vector_choice == "2":
            run_hpsb_academic_check()
        elif vector_choice == "3":
            execute_language_drill()
        elif vector_choice == "4":
            print("\nShutting down master processing array safely. Auf Wiedersehen!")
            break
        else:
            print("❌ Validation Error: Input outside operational parameters.")

if __name__ == "__main__":
    main_system_loop()
