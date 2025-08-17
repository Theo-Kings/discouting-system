def calculate_discount(price, discount_percent):
    """
    Calculates and returns the final price after applying the discount,
    only if the discount is 20% or higher. Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discounted_amount = price * (discount_percent / 100)
        return price - discounted_amount
    else:
        return price  # No discount applied

def main():
    try:
        price_input = input("Enter the original price of the item: ")
        price = float(price_input)
        
        discount_input = input("Enter the discount percentage: ")
        discount_percent = float(discount_input)

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(f"Discount applied! Final price: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price: {price:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values for price and discount.")

if __name__ == "__main__":
    main()
