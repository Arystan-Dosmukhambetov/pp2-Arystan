import math

r = float(input())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

def dist(x, y):
    return math.hypot(x, y)

def dist_to_segment_origin(ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay
    d2 = dx*dx + dy*dy
    if d2 == 0.0:
        return dist(ax, ay)
    t = -(ax*dx + ay*dy) / d2
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    px = ax + t*dx
    py = ay + t*dy
    return dist(px, py)

def ang(x, y):
    return math.atan2(y, x)

def ang_ccw(a, b):
    d = b - a
    while d < 0:
        d += 2 * math.pi
    while d >= 2 * math.pi:
        d -= 2 * math.pi
    return d

ab = math.hypot(bx - ax, by - ay)
min_d = dist_to_segment_origin(ax, ay, bx, by)

eps = 1e-12
if min_d >= r - eps:
    print(f"{ab:.10f}")
else:
    da = dist(ax, ay)
    db = dist(bx, by)

    phi_a = ang(ax, ay)
    phi_b = ang(bx, by)

    ga = 0.0 if da <= r else math.acos(r / da)
    gb = 0.0 if db <= r else math.acos(r / db)

    la = 0.0 if da <= r else math.sqrt(max(0.0, da*da - r*r))
    lb = 0.0 if db <= r else math.sqrt(max(0.0, db*db - r*r))

    a_angles = [phi_a + ga, phi_a - ga]
    b_angles = [phi_b + gb, phi_b - gb]

    best = float("inf")
    for ta in a_angles:
        for tb in b_angles:
            d1 = ang_ccw(ta, tb)
            d2 = 2 * math.pi - d1
            arc = min(d1, d2)
            best = min(best, la + lb + r * arc)

    print(f"{best:.10f}")