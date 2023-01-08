while True:
    try:
        n= int(input("Enter N: "))
        k= int(input("Enter K: "))
        break
    except:
        print("No valid integer, please enter a number !")
print("You've successfully entered an integer.")

list1= []
list2=[]

for i in range(n):
    number= int(input())
    
    if n > k:
        list1.append(number)
    elif n<= k and number >0 :
        list2.append(number)

print(list1)
print(list2)

total=1
for i in range(len(list1)):
    if i % 2 == 1:
        total *= list1[i]
if len(list1) >0 :
    min_value_one = min(list1)
    min_value_index= list1.index(min_value_one)

if len(list2) >0:
    min_value_two = min(list2)
    max_value_two = max(list2)

diff = max_value_two - min_value_two
print(diff)