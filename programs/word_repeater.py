def word_repeater():
    print("\n--- Word Repeater ---")
    word = input("Word to repeat: ")
    times = int(input("How many times? "))
    print(" | ".join([word] * times) + " 🎉")
