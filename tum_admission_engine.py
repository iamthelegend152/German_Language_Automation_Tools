# Parent-Monitored Portfolio Track - TUM Admission Calculation Platform
import datetime

# Central Database Module: Converted Bavarian Grade Formula
def calculate_bavarian_gpa(indian_percentage):
    # Nmax = 100% (Perfect score), Nmin = 60% (Minimum passing standard for calculation)
    if indian_percentage > 100 or indian_percentage < 0:
        return None
    
    # Standard Bavarian Formula: 1 + 3 * ((Nmax - Nd) / (Nmax - Nmin))
    # In Germany, 1.0 is perfect, 4.0 is minimum pass, 5.0 is fail
    if indian_percentage >= 60:
        german_gpa = 1.0 + 3.0 * ((100.0 - indian_percentage) / (100.0 - 60.0))
        return round(german_gpa, 2)
    else:
        return 5.0 # Fail status entry

# Core Verification Engine: TUM Aptitude Scoring Algorithm
def run_admission_assessment(german_gpa, target_stream, code_portfolio_commits, language_level):
    score = 0
    
    # Parameter 1: Academic Converted GPA Matrix (Max 45 Points)
    if german_gpa <= 1.5:
        score += 45
    elif german_gpa <= 2.0:
        score += 35
    elif german_gpa <= 3.0:
        score += 20
        
    # Parameter 2: HPS Begumpet High School Stream Check
    if target_stream.upper() in ["MPC", "PCMC"]:
        score += 25
        
    # Parameter 3: GitHub Portfolio Activity (Proving Multi-Year Engineering Tracking)
    if code_portfolio_commits >= 10:
        score += 15 # Secret baseline point multiplier!
        
    # Parameter 4: Language Proficiency Node
    if language_level.upper() in ["B2", "C1"]:
        score += 15
    elif language_level.upper() == "B1":
        score += 10
        
    return score

def main_runtime():
    print("==================================================")
    print("      TUM INFORMATICS APTITUDE ASSESSMENT MATRIX  ")
    print("==================================================")
    
    # 1. Capture and validate high school academic metrics
    try:
        user_pct = float(input("Enter targeted Class 12 Board Percentage (e.g., 95): ").strip())
        gpa = calculate_bavarian_gpa(user_pct)
        
        if gpa is None:
            print("❌ Input Out of Bounds: Percentage must rest between 0 and 100.")
            return
            
        print(f"📊 Bavarian Formula Output: Converted Converted GPA = {gpa}")
    except ValueError:
        print("❌ Data Format Error: You must type a valid numerical sequence.")
        return

    # 2. Capture profile trajectory variables
    stream = input("Enter high school stream track (MPC / Commerce / Arts): ").strip()
    commits = int(input("Enter total active developer profile GitHub commits: ").strip())
    language = input("Enter current target German language certificate (A1/A2/B1/B2): ").strip()

    # 3. Process data array through the evaluation matrix
    final_score = run_admission_assessment(gpa, stream, commits, language)
    
    print("\n=========================================")
    print("      APPLICATION PORTAL RESULTS SEARCH  ")
    print("=========================================")
    print(f"Total Evaluated Points: {final_score} out of 100")
    
    if final_score >= 70:
        print("🚀 STATUS: DIRECT ADMISSION APPROVED (Stage 1 Waiver Granted)!")
    elif final_score >= 50:
        print("⚠️ STATUS: STAGE 2 APTITUDE INTERVIEW REQUIRED.")
    else:
        print("❌ STATUS: PROFILE REJECTED. Under threshold criteria coordinates.")

if __name__ == "__main__":
    main_runtime()
