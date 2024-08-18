n = int(input()) #Input in Integer form
 
l = [] #Empty list to append the values 
l.append(n)

while(n > 1): #loop it till n value is greater than 1
    if(n % 2 == 0): # if n is even then divide it by 2
        n = n / 2
        l.append(n) # append the n value to list
    else: # if n is off then multiply n with 3 and add 1 to it
        n = (n * 3) + 1
        l.append(n) # append the n value to list

for i in l: # for-each loop
    print(int(i))  