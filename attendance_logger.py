# Parent-Monitored Portfolio Track - HPSB Attendance & Recovery Tracker
print("==================================================")
print("     HPSB ATTENDANCE & MEDICAL RECOVERY LEDGER    ")
print("==================================================")

def evaluate_attendance_safety(total_working_days, days_present):
    # Calculate attendance percentage metrics using floating point values
    attendance_percentage = (days_present / total_working_days) * 100.0
    
    print(f"Total Term Operational Days : {total_working_days}")
    print(f"Verified Days Attended      : {days_present}")
    print(f"Current Attendance Metric   : {round(attendance_percentage, 2)}%")
    print("--------------------------------------------------")
    
    # Strict 75% HPS Begumpet academic safety threshold parameters
    if attendance_percentage >= 75.0:
        print("🚀 STATUS: SAFE. Clearance parameters within school guidelines.")
        return "PASS"
    else:
        print("⚠️ STATUS: CRITICAL ALERT! Attendance sits below the 75% baseline.")
        print("📝 Action: Deploy official medical leave certificate node to clear profile rules.")
        return "ALERT"

# Simulation variables (e.g., 40 total days, 34 days present due to knee recovery rest)
total_days_in_term = 40
days_actually_present = 34

evaluate_attendance_safety(total_days_in_term, days_actually_present)
