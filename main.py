# sorting

# 1. find max value in the list below 

list = [74, 50, 30, 10, 23, 112, 39, 20, 23, 42, 3]
# max value is 112, min value is 3. 
length = len(list)
min = 100000
for i in list:
  if i < min:
    min = i

max = 1
for i in list:
  if i > max:
    max = i 

print(f' max value is {max}, min value is {min}')