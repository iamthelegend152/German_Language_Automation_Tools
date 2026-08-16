# Parent-Monitored Portfolio Track - Cryptographic Prime Verification Filter
print("==================================================")
print("     CRYPTOGRAPHIC PRIME VERIFICATION FILTER      ")
print("==================================================")

def verify_prime_status(number_token):
    # Base validation constraints
    if number_token <= 1:
        return False
    if number_token == 2:
        return True
        
    # Optimization Loop: Check factors up to the square root of the number
    # This is a highly efficient O(sqrt(n)) algorithm structure
    for i in range(2, int(number_token**0.5) + 1):
        if number_token % i == 0:
            return False # Factor found, not a prime number
            
    return True # No factors found, verified prime node

# Test array execution sequence
test_numbers = [11, 23, 97, 100, 103]
print("Running System Diagnostic Matrix Scan:")
print("-----------------------------------------")

for target in test_numbers:
    is_prime = verify_prime_status(target)
    if is_prime:
        print(f"🚀 Token {target}: VERIFIED PRIME NODE (Secure Encryption Element)")
    else:
        print(f"❌ Token {target}: COMPOSITE NODE (Standard Data Block)")
