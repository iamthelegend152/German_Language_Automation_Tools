# Parent-Monitored Portfolio Track - CEFR A1 German Pronoun Quizzer
import random

# Database matrix storing verbs with their root stems
verb_base = {
    "lernen": "lern",
    "wohnen": "wohn",
    "studieren": "studier",
    "sprechen": "sprech"
}

# Standard grammar rules for regular present tense endings
ending_rules = {
    "ich": "e",
    "du": "st",
    "er/sie/es": "t",
    "wir": "en",
    "ihr": "t",
    "sie/Sie": "en"
}

def run_conjugation_quiz():
    print("==================================================")
    print("     CEFR A1 PRONOUN CONVERSATION QUIZZER ENGINE  ")
    print("==================================================")
    
    # Pick a random verb and pronoun combination parameters
    selected_verb = random.choice(list(verb_base.keys()))
    selected_pronoun = random.choice(list(ending_rules.keys()))
    
    stem = verb_base[selected_verb]
    correct_ending = ending_rules[selected_pronoun]
    correct_full_word = f"{stem}{correct_ending}"
    
    print(f"Infinitiv Verb: '{selected_verb}' (Stem: '{stem}')")
    print(f"Target Pronoun Node: '{selected_pronoun}'")
    
    user_input = input(f"Complete the conjugation for '{selected_pronoun} ___': ").strip()
    
    print("\n--- Syntax Verification System ---")
    if user_input.lower() == correct_full_word:
        print(f"🚀 SUCCESS: Match verified! '{selected_pronoun} {correct_full_word}' is 100% correct.")
    else:
        print(f"❌ ERROR: Grammatical mismatch. The correct answer is '{correct_full_word}'.")

# Initialize runtime execution loop
run_conjugation_quiz()
