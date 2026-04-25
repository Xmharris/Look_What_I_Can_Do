from programs.password_system import password_system
from programs.tip_calculator import tip_calculator
from programs.word_repeater import word_repeater
from programs.calculator import calculator
from programs.task_list import task_list
from programs.number_sorter import number_sorter
from programs.reverse_word import reverse_word
from programs.unique_word_sorter import unique_word_sorter  
from programs.year_check import year_check

def header(name):
    print("~" * 44)
    print(f"        Welcome {name} to my portfolio!")
    print("~" * 44)
    print("These are the programs I’ve created:")
    print("1. Password System")
    print("2. Tip Calculator")
    print("3. Word Repeater")
    print("4. Calculator")
    print("5. Task List")
    print("6. Number Sorter")
    print("7. Reverse Word")
    print("8. Unique Word Sorter")
    print("9. Year Check")
    print("0. Exit")
    print("~" * 44)

def main():
    name = input("What is your name? ")
    while True:
        header(name)
        choice = input("Choose an option: ")

        if choice == "1": password_system()
        elif choice == "2": tip_calculator()
        elif choice == "3": word_repeater()
        elif choice == "4": calculator()
        elif choice == "5": task_list()
        elif choice == "6": number_sorter()
        elif choice == "7": reverse_word()
        elif choice == "8": unique_word_sorter()
        elif choice == "9": year_check()
        elif choice == "0":
            print("Thanks for visiting!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
