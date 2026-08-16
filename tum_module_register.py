# Parent-Monitored Portfolio Track - TUM Academic Module Registrar Simulation Engine
print("==================================================")
print("     TUM INFORMATICS COURSE REGISTRATION NODE      ")
print("==================================================")

# Comprehensive Nested University Database Array
course_catalog = {
    "IN0001": {
        "Name": "Introduction to Informatics & Systems Architecture",
        "ECTS_Credits": 6,
        "Difficulty": "Core Foundational",
        "Language Requirement": "German (CEFR B2 Target Alignment)"
    },
    "IN0002": {
        "Name": "Data Structures, Algorithm Design & Sorting Matrices",
        "ECTS_Credits": 8,
        "Difficulty": "Advanced Engineering",
        "Language Requirement": "German (CEFR B2 Target Alignment)"
    },
    "IN0006": {
        "Name": "Discrete Mathematics & Functional Linear Structures",
        "ECTS_Credits": 8,
        "Difficulty": "Theoretical Elite Tier",
        "Language Requirement": "German / English Dual Code"
    }
}

print("Operational University Modules Indexed for Review:")
for course_id, details in course_catalog.items():
    print(f"🔹 Module ID: {course_id} | {details['Name']} ({details['ECTS_Credits']} ECTS)")

print("\nEnter a target Module ID to trace its engineering requirements:")
user_selection = input("Target Key (e.g., IN0002): ").strip().upper()

print("\n--- Processing Database Query Node ---")
if user_selection in course_catalog:
    target_data = course_catalog[user_selection]
    print(f"✅ MODULE FOUND: {target_data['Name']}")
    print(f"📍 Academic Weight: {target_data['ECTS_Credits']} European Credit Transfer Tokens")
    print(f"📍 Complexity Tier: {target_data['Difficulty']}")
    print(f"📍 Language Validation Wall: {target_data['Language Requirement']}")
    print("\n🚀 Strategy Alignment Checklist:")
    print("- Ensure your HPS Begumpet math baseline maintains a 95%+ grade status matrix.")
    print("- Keep logging weekly green squares onto your parent-managed GitHub portfolio dashboard.")
else:
    print("❌ Query Validation Error: Specified Module ID does not exist in the catalog grid.")
