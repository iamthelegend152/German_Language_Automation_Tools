# Parent-Monitored Portfolio Track - High-Efficiency Binary Search Engine
print("==================================================")
print("     BINARY SEARCH DATA OPTIMIZATION ENGINE       ")
print("==================================================")

def execute_binary_search(sorted_array, target_element):
    low = 0
    high = len(sorted_array) - 1
    steps = 0
    
    print(f"Target Token to Locate: {target_element}")
    print(f"Searching Matrix Array: {sorted_array}")
    print("--------------------------------------------------")
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = sorted_array[mid]
        
        print(f"Step {steps}: Inspecting index {mid} (Value: {guess})")
        
        if guess == target_element:
            print(f"🚀 SUCCESS: Element located at array index: {mid}")
            print(f"Total Computational Cycles: {steps}")
            return mid
        if guess > target_element:
            high = mid - 1  # Target is in the lower half, chop off the upper half
        else:
            low = mid + 1   # Target is in the upper half, chop off the lower half
            
    print("❌ ERROR: Target token sits completely outside this database.")
    return -1

# Simulated sorted database registry (e.g., student ID tokens)
id_database = [102, 204, 308, 415, 527, 631, 742, 859, 973]

# Execute validation search query
search_target = 742
execute_binary_search(id_database, search_target)
