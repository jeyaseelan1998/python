import re
text = "CAT caret crt cgt cmt"

# raw string with dot wildcard
print(re.search(r"c.t", text))
print(re.search(r"c.t", text, re.IGNORECASE))

print(re.search(r"c", text))
