# notes/string_examples.py
import re

def formatting_examples(name, score):
    s1 = "Name: {}, Score: {}".format(name, score)
    s2 = f"Name: {name}, Score: {score}"
    s3 = "Name: {n:>10} | Score: {s:^5}".format(n=name, s=score)
    return s1, s2, s3

def regex_find_emails(text):
    # very simple email regex for demo purposes
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

def split_and_join(text):
    parts = text.split()
    return "-".join(parts)

if __name__ == "__main__":
    print(formatting_examples("Alice", 92))
    print("Emails:", regex_find_emails("Contact me at test@example.com or admin@site.org"))
    print("Joined:", split_and_join("look what I can do"))
