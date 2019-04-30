import re

patterns = ['term1','term2']

text = "This is a sting with term1"

for pat in patterns:

    if re.search(pat,text):
        print("Match")
    else:
        print("No match")
