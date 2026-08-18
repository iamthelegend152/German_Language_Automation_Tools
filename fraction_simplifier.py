# Parent-Monitored Portfolio Track - HPSB Math Fraction Simplifier
print("==================================================")
print("     CLASS 6 MATHEMATICS FRACTION SIMPLIFIER      ")
print("==================================================")

def find_greatest_common_divisor(a, b):
    # Implementing Euclid's classic subtraction algorithm for GCD
    while b != 0:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        return "❌ Error: Denominator cannot be zero."
        
    gcd = find_greatest_common_divisor(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    
    print(f"Original Input Fraction: {numerator}/{denominator}")
    print(f"Greatest Common Divisor: {gcd}")
    print(f"🚀 SUCCESS: Lowest Terms Fraction: {simplified_numerator}/{simplified_denominator}")
    return simplified_numerator, simplified_denominator

# Test execution node using standard school metrics (e.g., reducing 18/24)
simplify_fraction(18, 24)
