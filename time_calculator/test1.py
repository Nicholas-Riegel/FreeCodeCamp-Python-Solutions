# need to make sure times and ampms are formatted correctly

def add_time(start, add, startDay=None):

    # days dictionary
    days = {
        0: 'sunday',
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
    }
    
    # find number of start day
    startDayNumber = None
    
    def find_day_number(startDay):
        for k, v in days.items():
            if v == startDay:
                return k
    
    if startDay != None and startDay.lower() in days.values():
        startDay = startDay.lower()
        startDayNumber = find_day_number(startDay)
    elif startDay != None and startDay.lower() not in days.values():
        return 'Error: Improper day input.'

    #starts
    start = start.replace(':', ' ')
    start = start.split(' ')
    startHours = int(start[0])
    if startHours > 12 or startHours < 1:
        return 'Error: Hours outside range.'
    startMins = int(start[1])
    if startMins < 0 or startMins > 59:
        return 'Error: Minutes outside range.'
    startAMPM = start[2]
    if startAMPM != 'AM' and startAMPM != 'PM':
        return 'Error: Time must be either AM or PM'

    #convert time to 24hr
    if startAMPM == 'AM' and startHours == 12:
        startHours = 0
    if startAMPM == 'PM' and startHours < 12:
        startHours += 12
    
    #adds
    add = add.split(':')
    addHours = int(add[0])
    addMins = int(add[1])
    if addMins > 59:
        return 'Error: Minutes outside range.'
   
    #add minutes => endMins
    endMins = startMins + addMins
    
    #add mins to hours
    if endMins > 59:
        startHours += 1
        endMins -= 60

    #add hours
    endHours = startHours
    if endHours > 23:
        endHours = 0
        if startDayNumber != None:
            startDayNumber += 1
        if startDayNumber != None and startDayNumber > 6:
            startDayNumber = 0
    count = 0
    while count < addHours:
        endHours += 1
        count += 1
        if endHours > 23:
            if startDayNumber != None:
                startDayNumber += 1
            if startDayNumber != None and startDayNumber > 6:
                startDayNumber = 0
            endHours = 0

    # convert back to 12 hour time

    endAMPM = None
    if endHours < 12:
        endAMPM = 'AM'
    else:
        endAMPM = 'PM'

    if endHours == 0:
        endHours = 12
    
    if endHours > 12:
        endHours -= 12

    result = str(endHours) + ':' + str(endMins).zfill(2) + ' ' + endAMPM

    if startDay != None:
        endDay = days[startDayNumber]
        result += ' '+ endDay.capitalize()

    return result

print(
    add_time('12:30 AM', '3:30', 'tuesday')
)