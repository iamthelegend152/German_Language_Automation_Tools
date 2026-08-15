# Parent-Monitored Academic Tracker - Munich Student Survival Dashboard
import datetime
import random

# Data Module 1: Comprehensive Vocabulary Vault
vocabulary_vault = {
    "Nouns": {
        "der Computer": "the computer",
        "das Handy": "the mobile phone",
        "die Universität": "the university",
        "das Haus": "the house"
    },
    "Verbs": {
        "programmieren": "to program",
        "studieren": "to study",
        "lernen": "to learn",
        "fahren": "to drive"
    }
}

# Data Module 2: Suburb Transit Mapping
transit_matrix = {
    "Garching": "🚄 Take Bus 230 or Subway U6 straight to the TUM Campus.",
    "Ismaning": "🚄 Take S-Bahn S8 to Johanneskirchen, switch to Bus 230.",
    "Haar": "🚄 Take S-Bahn S4 to East Station, switch to Subway U5/U6."
}

def calculate_time_vectors():
    target_date = datetime.date(2032, 7, 15) # Targeted post-Class 12 departure
    current_date = datetime.date.today()
    delta = (target_date - current_date).days
    return delta

def run_language_trainer():
    print("\n--- [MODULE A: GOETHE LANGUAGE TESTING NODE] ---")
    category = random.choice(["Nouns", "Verbs"])
    german_word, english_meaning = random.choice(list(vocabulary_vault[category].items()))
    
    print(f"Category Group: {category}")
    user_guess = input(f"Translate the German term '{german_word}': ").strip().lower()
    
    if user_guess == english_meaning:
        print("🚀 Success: Translation matrix validated.")
        return True
    else:
        print(f"❌ Error: Correct definition target is '{english_meaning}'")
        return False

def run_transit_router():
    print("\n--- [MODULE B: BAVARIAN SUBURBAN ROUTER] ---")
    print("Available standalone house suburbs:")
    for suburb in transit_matrix.keys():
        print(f"- {suburb}")
        
    choice = input("Enter a suburb to trace the commute back to TUM: ").strip()
    if choice in transit_matrix:
        print(f"\nRoute Parameters for {choice}: {transit_matrix[choice]}")
    else:
        print("❌ Location out of grid boundaries.")

def master_runtime():
    print("==================================================")
    print("   TUM MUNICH STRATEGIC DEV DASHBOARD OPERATIONAL ")
    print("==================================================")
    
    days_left = calculate_time_vectors()
    print(f"📍 Relocation Matrix: {days_left} days remaining until Class 12 departure.")
    
    while True:
        print("\nSelect Executive Action Vector:")
        print("1. Execute German A1 Vocabulary Trainer")
        print("2. Run Suburban Transit Routing Simulation")
        print("3. Shutdown Station")
        
        selection = input("Enter vector option (1-3): ").strip()
        
        if selection == "1":
            run_language_trainer()
        elif selection == "2":
            run_transit_router()
        elif selection == "3":
            print("\nStation shutting down safely. Auf Wiedersehen!")
            break
        else:
            print("❌ Input validation error. Reselect.")

# Initialize system execution
if __name__ == "__main__":
    master_runtime()
