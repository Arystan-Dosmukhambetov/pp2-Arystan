from datetime import datetime, timedelta

def to_utc(line):
    d, t, tz = line.split()
    dt = datetime.strptime(d + " " + t, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz[3] == '+' else -1
    hh, mm = map(int, tz[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm) * sign
    return dt - offset

start_utc = to_utc(input().strip())
end_utc = to_utc(input().strip())

print(int((end_utc - start_utc).total_seconds()))