###
# Converts time in 24-hour format (hh:mm) to 12-hour format
#
time_24 = input("Enter time (24-hour format): ")

hours = int(time_24[:2])
minutes = time_24[3:]

if hours == 0:
    hours_12 = 12
    period = "am"
elif hours < 12:
    hours_12 = hours
    period = "am"
elif hours == 12:
    hours_12 = 12
    period = "pm"
else:
    hours_12 = hours - 12
    period = "pm"

print(f"Time in 12-hour format: {hours_12}:{minutes}{period}")
