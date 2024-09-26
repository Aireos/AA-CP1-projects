


staff = int(input("how many staff are attending?"))
students = int(input("How many students are being awarded?"))
guests = students * 2
changes = input("do you want any changes?: ")
changes = changes.lower()
type = ''

if changes == 'yes':
    type = input('what do you need to change?: ')
    type = type.lower()




    if type == 'staff':
        staff = int(input('How many staff are able to come?: '))






    if type == 'students':
        students = int(input('How many students are being awarded?: '))





    if type == 'guests':
        guests = (guests - int(input('how many guests will not be able to come?: ')))






    numberoftables = ((staff + guests + students) / 12)
    print('The total number of tables needed will be:', numberoftables)
elif changes == 'no':
    numberoftables = ((staff + guests + students) / 12)
    print('The total number of tables needed will be:', numberoftables)
