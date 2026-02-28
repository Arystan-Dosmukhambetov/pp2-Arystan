from datetime import datetime, timedelta

def parse(line):
    date_part, tz_part = line.split()
    y, m, d = map(int, date_part.split("-"))
    sign = 1 if tz_part[3] == '+' else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm) * sign
    utc = datetime(y, m, d) - offset
    return (m, d), offset, utc, y

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

(bm, bd), b_off, _, _ = parse(input().strip())
(_, _), _, cur_utc, cy = parse(input().strip())

def birthday_utc(year):
    m, d = bm, bd
    if m == 2 and d == 29 and not is_leap(year):
        d = 28
    return datetime(year, m, d) - b_off

cand = birthday_utc(cy)
if cand < cur_utc:
    cand = birthday_utc(cy + 1)

t = (cand - cur_utc).total_seconds()
if t < 0:
    print(0)
else:
    print(int((t + 86399) // 86400))