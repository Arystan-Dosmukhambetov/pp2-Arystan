import importlib

q = int(input())
for _ in range(q):
    mod_name, attr = input().split()
    try:
        mod = importlib.import_module(mod_name)
    except Exception:
        print("MODULE_NOT_FOUND")
        continue

    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
        continue

    val = getattr(mod, attr)
    print("CALLABLE" if callable(val) else "VALUE")