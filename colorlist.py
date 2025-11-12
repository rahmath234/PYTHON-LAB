list1=input("enter list1:").split(',')
list2=input("enter list2:").split(',')
for color in list1:
    if color not in list2:
        print(color)