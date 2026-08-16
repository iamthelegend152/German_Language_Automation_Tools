# Parent-Monitored Portfolio Track - CEFR A1 German Article Matcher
import random

# Database matrix storing nouns with their required grammar tags
noun_vault = {
    "Computer": "der",
    "Handy": "das",
    "Schule": "die",
    "Buch": "das",
    "Tasche": "die",
    "Lehrer": "der"
}

def run_article_matcher_quiz():
    print("==================================================")
    print("     CEFR A1 GERMAN ARTICLE MATCHING ENGINE       ")
    print("==================================================")
    
    # Pick a random noun from the database vault keys
    selected_noun = random.choice(list(noun_vault.keys()))
    correct_article = noun_vault[selected_noun]
    
    print(f"Target Vocabulary Token: '___ {selected_noun}'")
    user_input = input("Enter the correct article (der / die / das): ").strip().lower()
    
    print("\n--- Validation Engine Output ---")
    if user_input == correct_article:
        print(f"🚀 SUCCESS: Match verified! It is correctly '{correct_article} {selected_noun}'.")
    else:
        print(f"❌ ERROR: Grammatical mismatch. The correct form is '{correct_article} {selected_noun}'.")

# Initialize quiz loop execution
run_article_matcher_quiz()
