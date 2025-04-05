from typing import List
import re
from collections import Counter
import sys

def extract_emails(filepath) -> List[str]:
    email_list = []
    with open(filepath) as f:
        for line in f:
            emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", line)
            email_list += emails

    
    
    return email_list            

def top_n_emails(email_list, n):
    counts = Counter(email_list)
    sorted_emails = sorted(
        counts.items(), key=lambda x: (-x[1], x[0])
    )
    for email, count in sorted_emails:
        print(f"{email}: {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python main.py <filename>')
        sys.exit(1)
    filepath = sys.argv[1]
    
    email_list = extract_emails(filepath)
    top_n_emails(email_list, n=10)