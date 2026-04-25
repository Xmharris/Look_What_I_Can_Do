def calculator():
    print("\n--- Calculator ---")
    a = float(input("First number: "))
    op = input("Operation (+ - * / // %): ")
    b = float(input("Second number: "))

    ops = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b,
        "//": a // b,
        "%": a % b
    }

    print(f"{a} {op} {b} = {ops.get(op, 'Invalid operator')}")
