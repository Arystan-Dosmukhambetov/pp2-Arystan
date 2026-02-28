import json

a = json.loads(input())
b = json.loads(input())

def lit(x):
    if x == "<missing>":
        return "<missing>"
    return json.dumps(x, separators=(",", ":"), sort_keys=True)

diffs = []

def walk(x, y, path):
    if isinstance(x, dict) and isinstance(y, dict):
        keys = set(x.keys()) | set(y.keys())
        for k in keys:
            p = k if not path else path + "." + k
            if k not in x:
                diffs.append((p, "<missing>", y[k]))
            elif k not in y:
                diffs.append((p, x[k], "<missing>"))
            else:
                walk(x[k], y[k], p)
    else:
        if x != y:
            diffs.append((path, x, y))

walk(a, b, "")

diffs.sort(key=lambda t: t[0])

if not diffs:
    print("No differences")
else:
    for p, old, new in diffs:
        print(f"{p} : {lit(old)} -> {lit(new)}")