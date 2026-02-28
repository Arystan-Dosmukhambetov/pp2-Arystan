import json
import re

data = json.loads(input())
q = int(input())

token_re = re.compile(r'([A-Za-z_][A-Za-z0-9_]*)|\[(\d+)\]')

def resolve(value, query):
    pos = 0
    current = value
    for m in token_re.finditer(query):
        if m.start() != pos:
            if query[pos] == '.':
                pos += 1
                if m.start() != pos:
                    return None, False
            else:
                return None, False
        pos = m.end()

        key = m.group(1)
        idx = m.group(2)

        if key is not None:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None, False
        else:
            i = int(idx)
            if isinstance(current, list) and 0 <= i < len(current):
                current = current[i]
            else:
                return None, False

    if pos != len(query):
        return None, False
    return current, True

for _ in range(q):
    query = input().strip()
    val, ok = resolve(data, query)
    if not ok:
        print("NOT_FOUND")
    else:
        print(json.dumps(val, separators=(",", ":"), sort_keys=True))