response = input('Would it be 2 people or 1 person?') #get input (input should be 1 or 2 here)
#end if/else statement
if response == '1': #for one singular volunteer
    print ('Dear volunteer,')
    one = ('Perfect! Please make sure to bring')
    answer = input('Will you be willing to bring food for the food drive this month?')
    if answer == 'yes':
        import random
        names = ["cheese", "meat", "chicken", "cookies", "donuts", "cake", "plates", "fruits", "vegetables", "fish"]
        guests = names[random.randint(0, len(names)-1)]
        import random
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        time = days[random.randint(0, len(days)-1)]
        print (one + ' ' + guests + ' ' + 'every' + ' ' + time)
    elif answer == 'no':
        response = input('Sorry to hear that. What about next month?')
        if response == 'yes':
            print('Thank you! We will get back to you in a few days on what to bring')
        elif response == 'no':
            print('No problem. Thank you for taking the time to answer.')
        elif response == 'maybe':
            print('Let us know.')
    elif answer == 'maybe':
        print ('Let me know before Wednesday')
    else:
        print ('Try again')
    print ('Regards, JB')
elif response == '2':
    print ('Dear volunteers,')
    one = ('Perfect! Please make sure to bring')
    three = ('Let me know before Wednesday')

    answer = input('Will you be willing to bring food for the food drive this month?')#user input again
    if answer == 'yes':
        import random
        names = ["cheese", "meat", "chicken", "cookies", "donuts", "cake", "plates", "fruits", "vegetables", "fish"]
        guests = names[random.randint(0, len(names)-1)]#random food selection of name
        import random
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        time = days[random.randint(0, len(days)-1)] #random date selection of day
        secondtime = days[random.randint(0, len(time))] #additional time for the second person
        print (one + ' ' + guests + ' ' + 'every' + ' ' + time + ' ' + 'and' + ' ' + secondtime)
    elif answer == 'no':
        response = input('Sorry to hear that. What about next month?')
        if response == 'yes':
            print('Thank you! We will get back to you in a few days on what to bring')
        elif response == 'no':
            print('No problem. Thank you for taking the time to answer.')
        elif response == 'maybe':
            print('Let us know.')
    elif answer == 'maybe':
        print (three)
    else:
        print ('Try again')
    print ('Regards, JR')
else:
    print ('Try writing it in number form')
