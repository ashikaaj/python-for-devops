import re

text = "The quick brown fox"
pattern = r"brown"

search = re.findall(pattern, text)
if search:
    print("Pattern found:", search[0])
else:
    print("Pattern not found")
