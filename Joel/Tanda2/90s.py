year = int(input())
last_two_digits = year % 100
if 90 <= last_two_digits <= 99:
    print("SI")
else:
    print("NO")

