'''
You’re given a large text file (like a log, book, or dump).
Write a program to:

Read the file

Count how many times each word appears

Print the top N most frequent words
'''
import re
from collections import Counter
def extract_words(filepath):
    with open(filepath, "r") as f:
        text = f.read().lower()
        lst = re.findall(r'\b\w+\b', text)
    return lst

def top_n(lst, n):
    counter = Counter(lst)
    new_lst = sorted([(word, count) for word, count in counter.items()], key=lambda x: (-x[1],x[0]))
    return new_lst[:n]