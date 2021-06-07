# This solves the Time Formatter Challenge and adds an extra feature to determine the day of the week
# For days outside of the current week

import re


def addTime(start,duration,dayOfweek=""):
    weekArray=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    #Find day in array
    weekIndex=0
    while weekIndex<len(weekArray):
        if dayOfweek==weekArray[weekIndex]:
            dayFound = weekIndex

            break
        else:
            weekIndex= weekIndex+1


    day =0
    #Splits the start time and duration time into arrays

    splitStart = re.split('\s|:',start)
    splitDuration = re.split(':',duration)

    #Add the hours together and the minutes together
    hours = int(splitStart[0])+int(splitDuration[0])
    minutes =int(splitStart[1])+int(splitDuration[1])

    #turn the time into a 24 hour clock
    if splitStart[2]=="PM":
        hours =hours+12
    else:
        hours =hours
    #If minutes are greater than 59 mod to remaining minutes and add hours
    if minutes >59:
        minutes = minutes %60
        hours = hours+1

    #Determine the number of days
    if hours > 23:
        while hours >23:
            hours = hours-24
            day =day+1
    weekIndex=weekIndex+day
    if weekIndex >6:
        weekIndex =weekIndex%7
    #Determines the message as to how many days later
    if day ==1:
        daysMessage = "(next day)"
    elif day ==0:
        daysMessage = " "
    else:
        daysMessage = "("+(str(day)+" days later")+")"


    #print(hours)
    #print(minutes)
    #print(day)
    #print(daysMessage)

    #Converts to a 12 hour clock
    if hours >12:
        hours =hours-12
        AMorPM ="PM"
    elif hours ==12:
        AMorPM ="PM"
    else:
        hours = hours
        AMorPM ="AM"
    #Adds the 0 before a single digit
    if minutes < 10:
        minutes = "0"+str(minutes)
    #This solves the problem of midnight being 00 and now ses it to 12
    if  hours == 0:
        hours =12
    if dayOfweek != "":
        return (str(hours)+":"+str(minutes)+" "+AMorPM+", "+weekArray[weekIndex])+" "+daysMessage
    else:
        return (str(hours)+":"+str(minutes)+" "+AMorPM+" "+daysMessage)



#Run

print (addTime("11:43 PM","72:00","Friday"))