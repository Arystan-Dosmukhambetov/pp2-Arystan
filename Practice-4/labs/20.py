g = 0

def outer():
    n = 0

    def inner(cmds):
        nonlocal n
        global g
        local_var = 0
        for scope, val in cmds:
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            else:
                local_var += val

    m = int(input())
    cmds = []
    for _ in range(m):
        s, v = input().split()
        cmds.append((s, int(v)))

    inner(cmds)
    return n

n = outer()
print(g, n)