print()
print("Code to Edit the given list:\n")

num = int(input("Enter the number of elements in the list:\n"))
number = []

# Input
for i in range(num):
    n = int(input(f"Enter the {i+1} element: "))
    number.append(n)

# ✅ Copy AFTER input
org = number.copy()

print("\nThe Given list is :")
print(number)

# 🔹 Remove duplicates
unique = []
for item in number:
    if item not in unique:
        unique.append(item)

# 🔹 Check duplicates
if len(unique) != len(number):
    print("\nDuplicates found → removed\n")
else:
    print("\nNo duplicates found\n")

print("List after removing duplicates:", unique)

print("\nSorting of the list\n")

# 🔹 Bubble Sort
for i in range(len(unique)):
    swapped = False
    for j in range(0, len(unique) - i - 1):
        if unique[j] > unique[j + 1]:
            unique[j], unique[j + 1] = unique[j + 1], unique[j]
            swapped = True
    if not swapped:
        break

print("Sorted list:", unique)

# 🔹 Second largest
print("\nSecond largest element in list is:\n")
if len(unique) < 2:
    print("Not enough elements to find second largest")
else:
    print("Second largest:", unique[-2])

# 🔹 Frequency (use original list)
number = org.copy()

print("\nFinding the frequency of elements in the list:", number)

visited = []

for i in number:
    if i not in visited:
        count = 0
        for j in number:
            if i == j:
                count += 1

        print(f"{i} appears {count} times")
        visited.append(i)