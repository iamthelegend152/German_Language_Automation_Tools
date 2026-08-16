# Parent-Monitored Portfolio Track - Bubble Sort Simulation Engine
print("==================================================")
print("       BUBBLE SORT ARRAY OPTIMIZATION ENGINE      ")
print("==================================================")

def execute_bubble_sort(data_list):
    n = len(data_list)
    print(f"Initial Unsorted Matrix: {data_list}")
    print("--------------------------------------------------")
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if data_list[j] > data_list[j + 1]:
                # Swapping mechanism node
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                
    return data_list

# Simulated test dataset (e.g., student grade scores or index tokens)
scrambled_metrics = [95, 88, 100, 60, 75, 92]
sorted_output = execute_bubble_sort(scrambled_metrics)
print(f"🚀 SUCCESS: Fully Sorted Target Matrix: {sorted_output}")
