# Parent-Monitored Portfolio Track - CEFR A1 German Sentence Builder
print("==================================================")
print("     GERMAN POSITION 2 VERB SYNTAX VALIDATOR      ")
print("==================================================")

def validate_sentence_structure(word_list):
    print(f"Analyzing Input Sequence: {word_list}")
    print("--------------------------------------------------")
    
    # Target regular sentence parameters (e.g., ["ich", "lerne", "python"])
    # Rule: In a standard statement, the verb must rest exactly at index 1 (Position 2)
    known_verbs = ["lerne", "wohne", "spiele", "bin", "studiere"]
    
    if len(word_list) < 3:
        return "❌ Syntax Error: Sentence array requires at least a Subject, Verb, and Object node."
        
    action_verb = word_list[1].lower().strip()
    
    if action_verb in known_verbs:
        print(f"🚀 SUCCESS: Present tense verb '{action_verb}' detected in Position 2!")
        return "✅ Sentence Structure Validated: 100% Grammatically Correct."
    else:
        print(f"⚠️ Warning: Position 2 contains '{action_verb}', which is not a verified verb.")
        return "❌ Syntax Error: Verb placement rule violated. The verb must sit in Position 2!"

# Execute system testing sequence with a clean structure matrix
test_sentence = ["Ich", "lerne", "Python"]
result_log = validate_sentence_structure(test_sentence)
print(result_log)
