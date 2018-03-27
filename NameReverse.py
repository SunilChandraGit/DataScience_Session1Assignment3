#Read first name
firstName = input('Enter your first name : ');

#Read last name
lastName = input('Enter your last name : ');

#Reverse and concatenate first and last name
print(str(firstName[::-1])+' '+str(lastName[::-1]));
