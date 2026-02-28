import json

source = json.loads(input())
patch = json.loads(input())

def apply_patch(src, pat):
    for k, v in pat.items():
        if v is None:
            if k in src:
                del src[k]
        else:
            if isinstance(v, dict) and isinstance(src.get(k), dict):
                apply_patch(src[k], v)
            else:
                src[k] = v
    return src

result = apply_patch(source, patch)
print(json.dumps(result, separators=(",", ":"), sort_keys=True))