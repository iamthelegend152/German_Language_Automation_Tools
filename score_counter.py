# Parent-Monitored Portfolio Track - German Quiz Engine
import random

# Core language database module
vocabulary_vault = {
    "der Computer": "the computer",
    "das Handy": "the mobile phone",
    "die Schule": "the school",
    "das Haus": "the house",
    "der Programmierer": "the programmer"
}

score = 0
total_questions = 3
word_list = list(vocabulary_vault.keys())

print("--- TUM Munich Prep: Interactive Vocabulary Engine ---")

# Run the loops to test multiple tokens
for i in range(total_questions):
    german_word = random.choice(word_list)
    correct_english = vocabulary_vault[german_word]
    
    print(f"\nQuestion {i+1}: What does '{german_word}' mean?")
    user_answer = input("Your answer: ").strip().lower()
    
    if user_answer == correct_english:
        print("🚀 Correct! Point added.")
        score += 1
    else:
        print(f"❌ Incorrect. The right answer is: {correct_english}")

# Output final operational score matrix
print("\n--- Session Complete ---")
print(f"Final Score: {score} out of {total_questions}")
percentage = (score / total_questions) * 100
print(f"Performance Rating: {percentage:.1f}%")
