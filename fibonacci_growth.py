# Parent-Monitored Portfolio Track - Fibonacci Mathematical Growth Engine
print("==================================================")
print("     FIBONACCI MATRIX SEQUENCE CALCULATOR         ")
print("==================================================")

def generate_fibonacci_sequence(iterations):
    print(f"Initializing calculation array for {iterations} loops:")
    print("-----------------------------------------")
    
    # Set the initial baseline sequence variables
    sequence = [0, 1]
    
    if iterations <= 0:
        return []
    elif iterations == 1:
        return [0]
    elif iterations == 2:
        return sequence
        
    # Execute the addition loops to grow the matrix values
    while len(sequence) < iterations:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        
    return sequence

# Execute validation sequence up to 12 iterations (Matching your total commits tracking)
target_iterations = 12
result_array = generate_fibonacci_sequence(target_iterations)
print(f"Operational Array Output: {result_array}")
