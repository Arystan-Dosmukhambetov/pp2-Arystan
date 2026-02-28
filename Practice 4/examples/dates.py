from datetime import datetime, timedelta


# 1. Subtract five days from current date
now = datetime.now()
five_days_ago = now - timedelta(days=5)

print("1) Subtract five days from current date")
print("Today:", now)
print("Five days ago:", five_days_ago)
print()


# 2. Print yesterday, today, tomorrow
today = now.date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("2) Yesterday, Today, Tomorrow")
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
print()


# 3. Drop microseconds from datetime
no_microseconds = now.replace(microsecond=0)

print("3) Datetime without microseconds")
print("Original:", now)
print("Without microseconds:", no_microseconds)
print()


# 4. Calculate difference between two dates in seconds
date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 15, 30, 0)

difference = date2 - date1
seconds = int(difference.total_seconds())

print("4) Difference between two dates in seconds")
print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", seconds)
