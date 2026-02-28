s = input().strip()

# digit mappings
to_digit = {
    "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8",
    "NIN": "9", "ZER": "0"
}

to_word = {v: k for k, v in to_digit.items()}

# find operator
for op in "+-*":
    if op in s:
        left, right = s.split(op)
        break

# convert left number
num1 = ""
for i in range(0, len(left), 3):
    num1 += to_digit[left[i:i+3]]

# convert right number
num2 = ""
for i in range(0, len(right), 3):
    num2 += to_digit[right[i:i+3]]

# calculate
result = str(eval(num1 + op + num2))

# convert back to triplets
answer = ""
for digit in result:
    answer += to_word[digit]

print(answer)
