#Liam Collins
#5/10/18
#howManyWords.py

file = open('engmix.txt')

L = [0]*22
for item in file:
    L[len(item)-1] = L[len(item)-1] + 1

i = 1
while i<=21:
    print(i,'-letter words: ',L[i])
    i+=1
