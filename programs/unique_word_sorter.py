def unique_word_sorter():
    print("\n--- Unique Word Sorter ---")
    punct = ".,!?"
    sentence = input("Enter a sentence: ").lower()
    words = [w.strip(punct) for w in sentence.split()]
    unique = sorted(set(words))

    print("Unique words:")
    for w in unique:
        print(w)
    print("Total:", len(unique))
