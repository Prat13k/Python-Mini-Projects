import datetime,random
def GetBirthday(numberofbirthdays):
    birthdays = []
    for i in range(numberofbirthdays):
        startofyear = datetime.date(199,1,1)
        randomdays = datetime.timedelta(random.randint(0,364))
        birthday = startofyear + randomdays
        birthdays.append(birthday)
    return birthdays
def getmatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a, birthdaya in enumerate(birthdays):
        for b, birthdayb in enumerate(birthdays[a+1:]):
            if birthdaya == birthdayb:
                return birthdaya
print("Birthday Paradox")
months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')
while True:
    print('How many birthdays shall i generate (not more than 100)')
    response = input('>')
    if(response.isdecimal()) and (0<int (response)<=100):
        numbdays = int(response)
        break
print()
print("Here are ",numbdays," Birthdays")
birthdays = GetBirthday(numbdays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        print(',',end = '')
    monthname = months[birthday.month-1]
    datetext = '{}{}'.format(monthname,birthday.day)
    print(datetext,end = '')
print()
print()
match = getmatch(birthdays)
print('In this simulation',end = '')
if match!= None:
    monthname = months[match.months-1]
    datetext = '{}{}'.format(monthname,match.day)
    print('Multiple people have a birthday on ',datetext)
else:
    print("There is no matching birthday")
print()
print("Generating ",numbdays,'random bdays 1L times' )
input('Press Enter to Begin')
print('Lets run amother 1L simulation')
simmatch = 0
for i in range(100_000):
    if i%10_000 == 0:
        print(i ,'stimulation run......')
    birthdays = GetBirthday(numbdays)
    if getmatch(birthdays)!= None:
        simmatch = simmatch+1
print('100000 Simulation Run')
probability = round(simmatch/100_000*100,2)
print('Out of 100,000 simulations of', numbdays, 'people, there was a')
print('matching birthday in that group', simmatch, 'times. This means')
print('that', numbdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')