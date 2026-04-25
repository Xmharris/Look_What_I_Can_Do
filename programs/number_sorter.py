def number_sorter():
    print("\n--- Number Sorter ---")
    nums = input("Enter numbers separated by spaces: ").split()
    nums = [int(n) for n in nums]
    print("Sorted:", sorted(nums))
