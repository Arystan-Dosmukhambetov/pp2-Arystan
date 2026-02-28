import math

r = float(input())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

dx = bx - ax
dy = by - ay
seg_len = math.hypot(dx, dy)

if seg_len == 0.0:
    print(f"{0.0:.10f}")
else:
    a = dx * dx + dy * dy
    b = 2.0 * (ax * dx + ay * dy)
    c = ax * ax + ay * ay - r * r

    disc = b * b - 4.0 * a * c

    if disc < 0.0:
        if c <= 0.0:
            ans = seg_len
        else:
            ans = 0.0
    else:
        s = math.sqrt(max(0.0, disc))
        t1 = (-b - s) / (2.0 * a)
        t2 = (-b + s) / (2.0 * a)
        if t1 > t2:
            t1, t2 = t2, t1

        lo = max(0.0, t1)
        hi = min(1.0, t2)
        ans = seg_len * max(0.0, hi - lo)

    print(f"{ans:.10f}")