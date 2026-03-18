num=1
for i in range(1,5):
    for j in range (4-i):
        print(" ",end="")
    for k in range (i):
        print(f"{num}",end="")
        num+=1
    print()
# num = 1

# for i in range(1,5):

#     for space in range(4-i):
#         print("  ", end="")

#     for j in range(i):
#         print(num, end=" ")
#         num += 1

#     print()