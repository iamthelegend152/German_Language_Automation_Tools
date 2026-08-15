# Parent-Monitored Academic Tracker - Munich Flight Matrix
import datetime

# Define the targeted departure vector (e.g., July 15, 2032 after Class 12 boards)
target_date = datetime.date(2032, 3, 15)
current_date = datetime.date.today()

days_remaining = (target_date - current_date).days

print("--- TUM Munich Timeline Terminal Node ---")
print(f"Current Date Logged: {current_date}")
print(f"Target Relocation Matrix Date: {target_date}")
print("-----------------------------------------")
print(f"🚀 Days remaining until the Munich Master Plan activates: {days_remaining} days!")
