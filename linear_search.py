# Parent-Monitored Portfolio Track - Linear Search Array Traversal Engine
print("==================================================")
print("     LINEAR SEARCH & REGISTRY DATABASE ENGINE     ")
print("==================================================")

def execute_linear_search(data_array, target_element):
    print(f"Scanning data matrix for target token: '{target_element}'")
    print("--------------------------------------------------")
    
    # Loop through the list index by index to find the element
    for index in range(len(data_array)):
        if data_array[index] == target_element:
            return f"🚀 SUCCESS: Token found at operational database index location: {index}"
            
    return "❌ ERROR: Target token sits completely outside the database array."

# Database registry catalog array
munich_suburb_registry = ["Garching", "Ismaning", "Haar", "Schwabing", "Freising"]

# Run system diagnostic scan query
search_query = "Ismaning"
result_log = execute_linear_search(munich_suburb_registry, search_query)
print(result_log)
