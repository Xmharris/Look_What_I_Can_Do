# notes/lists_examples.py

def basic_operations():
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    nums.insert(0, 0)
    popped = nums.pop()          # 6
    return nums, popped

def comprehensions_and_filters():
    nums = range(10)
    squares = [n * n for n in nums]
    evens = [n for n in nums if n % 2 == 0]
    pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
    return squares, evens, pairs

def slicing_examples():
    s = list("abcdefghij")
    first_three = s[:3]
    last_two = s[-2:]
    every_other = s[::2]
    reversed_list = s[::-1]
    return first_three, last_two, every_other, reversed_list

if __name__ == "__main__":
    print("Basic:", basic_operations())
    print("Comps:", comprehensions_and_filters())
    print("Slices:", slicing_examples())
