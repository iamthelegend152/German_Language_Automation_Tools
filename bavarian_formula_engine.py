# Parent-Monitored Academic Tracker - Bavarian Formula Simulation Module
def convert_to_bavarian_scale(percentage_score):
    # Absolute ceiling constraints for Indian school boards
    n_max = 100.0
    n_min = 60.0
    
    if percentage_score > n_max or percentage_score < 0:
        return "❌ Logic Error: Percentage input out of operational bounds."
        
    if percentage_score >= n_min:
        # Standard German Federal formula implementation
        german_grade = 1.0 + 3.0 * ((n_max - percentage_score) / (n_max - n_min))
        return f"🎯 Converted German Grade: {round(german_grade, 2)}"
    else:
        return "❌ Academic Alert: Grade sits below minimum technical threshold."

# Test validation parameters
test_input_percentage = 95.5
print("--- Initializing Bavarian Formula Conversion Check ---")
print(f"Input Data Node: {test_input_percentage}%")
print(convert_to_bavarian_scale(test_input_percentage))
