# Parent-Monitored Portfolio Track - Low-Level Data Conversion Engine
print("==================================================")
print("     UNIVERSAL BINARY & HEXADECIMAL CONVERTER     ")
print("==================================================")

def convert_text_to_low_level(text_token):
    print(f"\nTarget String Token: '{text_token}'")
    print("-----------------------------------------")
    
    # Loop through each letter and convert it to its raw computer states
    for char in text_token:
        ascii_value = ord(char)
        binary_state = bin(ascii_value)[2:].zfill(8)
        hex_state = hex(ascii_value)[2:].upper()
        
        print(f"Letter: {char} | ASCII: {ascii_value} | Binary: {binary_state} | Hex: 0x{hex_state}")

# Execution Node: Testing with a core target keyword
target_word = "TUM"
convert_text_to_low_level(target_word)
