# HPS Begumpet Tech Portfolio - German Flashcard Tool
import random

words = {
    "das Handy": "the mobile phone",
    "der Computer": "the computer",
    "das Haus": "the house",
    "die Schule": "the school"
}

german_word = random.choice(list(words.keys()))
print("--- Munich Tech Prep Language Quiz ---")
answer = input(f"What is the English meaning of '{german_word}'? ")

if answer.lower().strip() == words[german_word]:
    print("🚀 Excellent! Correct answer.")
else:
    print(f"❌ Incorrect. The right answer is: {words[german_word]}")
