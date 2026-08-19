# Parent-Monitored Portfolio Track - Defensive Input Data Insulation Engine
print("==================================================")
print("     DEFENSIVE INPUT DATA INSULATION FILTER       ")
print("==================================================")

def insulate_user_input(input_token):
    print(f"Analyzing Target Input String: '{input_token}'")
    print("--------------------------------------------------")
    
    # Define a clean list of allowed alphabetic characters (including German umlauts)
    allowed_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZäöüÄÖÜß "
    
    sanitized_output = ""
    malicious_flags_detected = 0
    
    # Loop through every single character in the input string node
    for char in input_token:
        if char in allowed_characters:
            sanitized_output += char
        else:
            # Flag any non-alphabetic symbol, number, or database injection character
            malicious_flags_detected += 1
            
    print("--- Processing Security Matrix Diagnostics ---")
    if malicious_flags_detected > 0:
        print(f"⚠️ SECURITY ALERT: {malicious_flags_detected} unauthorized symbols filtered out.")
        print(f"🛡️ Sanitized Output Stream: '{sanitized_output}'")
        return False
    else:
        print("✅ INPUT VERIFIED: String matches clean structural data parameters.")
        print(f"🚀 Forwarding to System Core: '{sanitized_output}'")
        return True

# Test Execution Sequence 1: Checking clean grammar variables
test_clean = "Ich lerne Python in der Schule"
insulate_user_input(test_clean)

print("\n")

# Test Execution Sequence 2: Checking a dirty input containing dangerous numbers/symbols
test_dirty = "TUM_Admission_100%_SELECT_*_FROM_Database!"
insulate_user_input(test_dirty)
