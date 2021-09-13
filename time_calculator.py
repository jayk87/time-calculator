def add_time(start, duration, weekday = None):
    weekdays = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
    time = ''
    dow = ''
    days = ''

    hour = int(start[0:start.find(":")])
    if start[-2:] == "PM":
        hour += 12

    min = int(start[start.find(":") + 1:start.find(":") + 3])

    add_hour = int(duration[0:duration.find(":")])

    add_min = int(duration[duration.find(":") + 1:duration.find(":") + 3])

    if min + add_min > 59:
        add_hour += 1
    hour += add_hour
    print(hour)
    add_day = int(hour/24)

    print(add_day)
    print(type(add_day))
    print(add_day == 1)
    if add_day == 1:
        days = " (next day)"
    elif add_day >= 2:
        days = " (" + str(add_day) + " days later)"
    else:
        days = ""

    hour = hour % 24

    if hour >= 12:
        ampm = "PM"
    else:
        ampm = "AM"

    hour = hour % 12
    min = ((min + add_min) % 60)

    if hour == 0:
        hour = 12

    if weekday != None:
        dow = weekdays[((weekdays.index(weekday.lower()) + 1 + add_day) % 7) -1]
        dow = ", " + dow.capitalize()

    time = str(hour) + ":" + str(min).rjust(2, '0') + " " + ampm

    new_time = "{}{}{}".format(time, dow, days).rstrip()
    return new_time