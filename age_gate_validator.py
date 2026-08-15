# Parent-Monitored Academic Tracker - Goethe Age System Check
def check_enrollment_clearance(age, school_node):
    print(f"--- Processing Profile Roster Node: Age {age} at {school_node} ---")
    
    if age >= 16:
        return "✅ Direct Webshop Access Granted: Standard Adult Cohort Approved."
    elif school_node == "HPS Begumpet":
        return "🚀 Special Route Activated: Requesting Parental Waiver / External Fit in Deutsch Track!"
    else:
        return "❌ Roster Error: Wait for next local Youth Learner schedule release."

# Execute simulation variables
my_current_age = 11
my_school = "HPS Begumpet"

result_string = check_enrollment_clearance(my_current_age, my_school)
print(result_string)
