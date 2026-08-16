# Parent-Monitored Portfolio Track - CEFR A1 Verb Conjugation Engine
print("==================================================")
print("     GERMAN REGULAR VERB CONJUGATION ENGINE       ")
print("==================================================")

# Structural database storing standard regular verb stems
verb_vault = {
    "lernen": "lern",
    "programmieren": "programmier",
    "wohnen": "wohn",
    "studieren": "studier"
}

# Standard grammar endings for regular present tense verbs in Germany
conjugation_rules = {
    "ich": "e",    # I learn -> ich lerne
    "du": "st",    # You learn -> du lernst
    "er/sie/es": "t", # He/She/It learns -> er lernt
    "wir": "en",   # We learn -> wir lernen
    "ihr": "t",    # You all learn -> ihr lernt
    "sie/Sie": "en" # They/You (formal) learn -> sie lernen
}

def execute_conjugation_matrix(verb_token):
    verb_token = verb_token.lower().strip()
    
    if verb_token in verb_vault:
        stem = verb_vault[verb_token]
        print(f"Target Verb: '{verb_token}' (Stem Node: '{stem}')")
        print("--------------------------------------------------")
        
        # Loop through the grammar dictionary to print the correct combinations
        for pronoun, ending in conjugation_rules.items():
            print(f"🔹 {pronoun:<10} ➔  {stem}{ending}")
    else:
        print("❌ Registry Alert: Specified verb rests outside regular conjugation maps.")

# Execute system testing sequence with your primary target verb
execute_conjugation_matrix("programmieren")
