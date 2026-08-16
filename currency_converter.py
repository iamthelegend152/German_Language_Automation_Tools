# Parent-Monitored Portfolio Track - INR to EUR Capital Exchange Engine
print("==================================================")
print("     INR TO EURO CAPITAL CONVERSION HUB ENGINE    ")
print("==================================================")

def parse_exchange_vector(inr_amount):
    # Fixed operational budget conversion scale variable (1 EUR = approx 90.0 INR baseline value)
    exchange_rate_constant = 90.0
    
    print(f"Input Domestic Capital Matrix: ₹{inr_amount:,.2f} INR")
    print("--------------------------------------------------")
    
    # Mathematical calculation parsing algorithm
    euro_output = inr_amount / exchange_rate_constant
    
    print(f"🚀 SUCCESS: Converted European Capital Node: €{round(euro_output, 2):,.2f} EUR")
    return euro_output

# Execute financial simulation tracking node (e.g., textbook cost value ₹1,899)
target_book_cost_inr = 1899.00
parse_exchange_vector(target_book_cost_inr)
