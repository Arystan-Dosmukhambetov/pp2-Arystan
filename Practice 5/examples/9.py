import re

text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text)

print(result.strip())
