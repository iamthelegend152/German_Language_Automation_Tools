# Parent-Monitored Portfolio Track - TUM Campus Explorer Module
def scan_university_module(module_id):
    # Core structural university database array
    tum_database = {
        "IN0001": "Introduction to Informatics | 6 ECTS | Language: German B2",
        "IN0002": "Data Structures & Algorithm Design | 8 ECTS | Language: German B2",
        "MA0001": "Discrete Mathematics for Computer Science | 8 ECTS | Language: Dual Code"
    }
    
    print(f"--- Querying TUM Database Node: {module_id} ---")
    if module_id in tum_database:
        return f"✅ MODULE MATCH: {tum_database[module_id]}"
    else:
        return "❌ Registry Alert: Specified Module ID rests outside current catalog limits."

# Execute validation check
target_node = "IN0002"
print(scan_university_module(target_node))
