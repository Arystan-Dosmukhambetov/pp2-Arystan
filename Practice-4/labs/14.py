from datetime import datetime, timedelta

def parse(line):
    date_part, tz_part = line.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if '+' in tz_part else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm) * sign
    return dt - offset

d1 = parse(input().strip())
d2 = parse(input().strip())

diff = abs((d1 - d2).total_seconds()) // 86400
print(int(diff))