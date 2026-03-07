import re

text = "hello_world test_example"

result = re.findall(r"[a-z]+_[a-z]+", text)

print(result)
