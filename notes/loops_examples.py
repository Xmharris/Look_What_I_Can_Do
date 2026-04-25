# notes/loops_examples.py

def enumerate_example(items):
    return [(i, v) for i, v in enumerate(items)]

def zip_example(keys, values):
    return dict(zip(keys, values))

def while_example(limit):
    i = 0
    total = 0
    while i < limit:
        total += i
        i += 1
    return total

def generator_example(n):
    # simple generator that yields squares
    for i in range(n):
        yield i * i

if __name__ == "__main__":
    print("Enumerate:", enumerate_example(["a","b","c"]))
    print("Zip:", zip_example(["x","y"], [1,2]))
    print("While sum:", while_example(5))
    print("Generator:", list(generator_example(6)))
