# Parent-Monitored Portfolio Track - HPSB Term Grade Analytics Engine
print("==================================================")
print("       HPSB TERM GRADE ANALYTICS ENGINE NODE       ")
print("==================================================")

def analyze_term_performance(subject_marks_dict):
    total_max_marks = len(subject_marks_dict) * 100.0
    total_secured_marks = sum(subject_marks_dict.values())
    
    # Calculate real-time dynamic aggregate float metric
    aggregate_percentage = (total_secured_marks / total_max_marks) * 100.0
    
    print("Logged Subject Performance Grid Matrix:")
    print("--------------------------------------------------")
    for subject, marks in subject_marks_dict.items():
        print(f"🔹 {subject:<15} ➔  {marks} / 100")
        
    print("--------------------------------------------------")
    print(f"Calculated Aggregate Metric : {round(aggregate_percentage, 2)}%")
    
    # Strict 95% TUM Admission baseline tracking logic parameters
    if aggregate_percentage >= 95.0:
        print("🚀 STATUS: EXCELLENT. Grade tracking aligns perfectly with TUM prerequisites!")
        return True
    else:
        print("⚠️ STATUS: CRITICAL NODES DETECTED. Increase study block parameters to hit 95%+ matrix.")
        return False

# Simulated current academic input array mapping out 5 core subjects
current_scores = {
    "Mathematics": 97,
    "Physics": 96,
    "Chemistry": 95,
    "German": 100,
    "Computers": 98
}

analyze_term_performance(current_scores)
