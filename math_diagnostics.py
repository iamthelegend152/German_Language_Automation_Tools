# Parent-Monitored Portfolio Track - Academic Math Diagnostic Engine
print("==================================================")
print("     ACADEMIC MATHEMATICS DIAGNOSTIC ENGINE       ")
print("==================================================")

def run_performance_diagnostic(expected_matrix, actual_matrix):
    print("Evaluating Real-Time Calculation Accuracy Logs:")
    print("--------------------------------------------------")
    
    total_equations = len(expected_matrix)
    correct_nodes = 0
    
    # Traverse through both calculation data dictionaries simultaneously
    for equation_id in expected_matrix:
        expected_val = expected_matrix[equation_id]
        actual_val = actual_matrix.get(equation_id, None)
        
        if expected_val == actual_val:
            print(f"🔹 Node {equation_id}: MATCH VERIFIED ({actual_val})")
            correct_nodes += 1
        else:
            print(f"❌ Node {equation_id}: CRITICAL DRIFT! Expected {expected_val}, Got {actual_val}")
            
    # Calculate performance accuracy metric
    accuracy_percentage = (correct_nodes / total_equations) * 100.0
    print("--------------------------------------------------")
    print(f"System Accuracy Diagnostic Rating: {round(accuracy_percentage, 2)}%")
    
    if accuracy_percentage >= 95.0:
        print("🚀 STATUS: UNBROKEN. Performance vector aligns with TUM admissions matrix.")
        return True
    else:
        print("⚠️ STATUS: OPTIMIZATION REQUIRED. Increase textbook review cycles.")
        return False

# Target key answer codes (Expected Master Values)
master_keys = {"EQ01": 144, "EQ02": 25, "EQ03": 81, "EQ04": 400}

# Simulated student calculation runs (Actual Input Values)
student_inputs = {"EQ01": 144, "EQ02": 25, "EQ03": 79, "EQ04": 400}

run_performance_diagnostic(master_keys, student_inputs)
