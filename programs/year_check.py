def year_check():
    print("\n--- Year Check ---")
    try:
        age = int(input("Your age: "))
        print("Next year you will be:", age + 1)
    except:
        print("Invalid input.")
