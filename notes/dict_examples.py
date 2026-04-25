# notes/dict_examples.py

def create_and_update():
    d = {"a": 1, "b": 2}
    d["c"] = 3
    d.update({"b": 20, "d": 4})
    return d

def comprehension_and_merge():
    keys = ["x", "y", "z"]
    values = [10, 20, 30]
    comp = {k: v for k, v in zip(keys, values)}
    defaults = {"y": 0, "w": 99}
    merged = {**defaults, **comp}   # comp overrides defaults
    return comp, merged

def safe_lookup(d, key, default=None):
    return d.get(key, default)

if __name__ == "__main__":
    print("Create:", create_and_update())
    print("Comp & Merge:", comprehension_and_merge())
    print("Lookup:", safe_lookup({"a": 1}, "b", 0))
