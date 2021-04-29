def add_time(start, add, startDay=None):

#times are all messed up: this is too complicated and ad hoc. 1. change everything to 24 hour time. Only change back at the end.

    #starts
    start = start.replace(':', ' ')
    start = start.split(' ')
    startHours = int(start[0])
    startMins = int(start[1])
    startAMPM = start[2]

    #dealing with PM hours
    if startAMPM == 'PM' and startHours != 12:
        startHours += 12

    #dealing with 12 AM
    if startHours == 12 and startAMPM == 'AM':
        startHours = 0

    #adds
    add = add.split(':')
    addHours = int(add[0])
    addMins = int(add[1])

    #ends
    endAMPM = None
    endMins = startMins + addMins

    #mins to hours
    if startMins + addMins > 59:
        startHours += 1
        endMins -= 60

    #add hours
    endHours = startHours
    count = 0
    while count < addHours:
        endHours += 1
        count += 1
        if endHours > 23: endHours = 0

    #AM/PM
    if endHours > 11:
        endAMPM = 'PM'
    else:
        endAMPM = 'AM'
    
    #12 hour time-period
    if endHours > 12:
        endHours -= 12

    #0==12
    if endHours == 0:
        endHours = 12

    #result
    result = str(endHours) + ':' + str(endMins).zfill(2) + ' ' + endAMPM
    
    #below to be changed
    if startDay != None:
        result += ' '+startDay

    print(result)

add_time('11:30 PM', '12:35', 'Mon')