def tip_calculator():
    print("\n--- Tip Calculator ---")

    def get_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                return value / 100 if value > 1 else value
            except:
                print("Invalid input.")

    meal = get_float("Meal price: ") * 100  # undo % conversion
    tax = get_float("Tax rate (% or decimal): ")
    discount = get_float("Discount (% or decimal): ")
    tip = get_float("Tip (% or decimal): ")

    tax_amount = meal * tax
    discount_amount = (meal + tax_amount) * discount
    tip_amount = meal * tip
    total = meal + tax_amount - discount_amount + tip_amount

    print(f"Subtotal: ${meal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Discount: ${discount_amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")
