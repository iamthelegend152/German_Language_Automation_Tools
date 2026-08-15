# Parent-Monitored Academic Tracker - Advanced Vocabulary Engine
import random

# Core language matrix structured with gender nodes
vocabulary_database = {
    "Level 1 (Nouns)": {
        "der Computer": "the computer",
        "das Handy": "the mobile phone",
        "die Schule": "the school",
        "das Haus": "the house"
    },
    "Level 2 (Verbs)": {
        "programmieren": "to program",
        "studieren": "to study",
        "lernen": "to learn",
        "fahren": "to drive"
    }
}

def run_language_matrix():
    print("--- TUM Munich Engineering Prep: Language Engine Active ---")
    print("Select Core Data Track:\n1. Nouns\n2. Verbs")
    track_choice = input("Enter choice (1 or 2): ").strip()
    
    if track_choice == "1":
        selected_matrix = "Level 1 (Nouns)"
    elif track_choice == "2":
        selected_matrix = "Level 2 (Verbs)"
    else:
        print("❌ Invalid input matrix node.")
        return

    # Select a random entry from the chosen database map
    german_token, english_target = random.choice(list(vocabulary_database[selected_matrix].items()))
    
    print(f"\nTarget Track: {selected_matrix}")
    user_input = input(f"Translate the German term '{german_token}': ").strip().lower()
    
    if user_input == english_target:
        print("🚀 Code Execution Verified: Correct translation matrix node!")
    else:
        print(f"❌ Logic Error: Target definition is '{english_target}'")

# Execute the runtime system
run_language_matrix()
