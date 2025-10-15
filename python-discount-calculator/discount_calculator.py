# Week 3 Assignment: Discount Calculator
# Author: Ifeanyi Ekezie
# Filename: discount_calculator.py

def calculate_discount(price, discount_percent):
    """Calculate final price after discount if discount is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and display the result
    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"🎉 Discount applied! Final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price is: ${final_price:.2f}")

except ValueError:
    print("❌ Invalid input. Please enter numeric values only.")
