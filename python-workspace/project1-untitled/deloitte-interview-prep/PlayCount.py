def pacman(dayOfweek, dayOfMonth):
    if "T" in dayOfweek:
        return "Inky"
    elif dayOfMonth % 4 == 0:
        return "Pinky"
    elif dayOfweek == "Sunday":
        return "Blinky"
    elif dayOfweek == "Monday":
        return "Blinky"
    else:
        return "Clyde"
def incDay(day):
    daysOfWeek= [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
    return daysOfWeek[(daysOfWeek.index(day) + 1) % len(daysOfWeek)]
def playCount(startingDay, daysInMonth):
    daysOfWeek = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
    month=[]
    week={}
    lo=1
    weeks=0
    i=0


    while weeks <=int(daysInMonth/7):
        while i<=len(daysOfWeek):
            week[startingDay]=lo
            startingDay = incDay(startingDay)
            i+=1
            lo+=1
        weeks+=1



        month.append(week)
    print(month)








playCount("Sunday", 31)
