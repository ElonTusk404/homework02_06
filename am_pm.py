hour = int(input("Enter hour: "))
am_or_pm = input("am or pm: ")
ahead = int(input("How many hours ahead? "))

new_hour = (hour + ahead) % 12
if new_hour == 0:
    new_hour = 12

if am_or_pm == 'am' and hour + ahead >= 12:
    am_or_pm = "pm"
if am_or_pm == 'pm' and hour >= 12:
    am_or_pm = "am"

print(f"New hour: {new_hour} {am_or_pm}")
