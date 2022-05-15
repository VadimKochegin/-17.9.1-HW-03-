print("Enter numbers separate by space: ")
input_int_array = [int(x) for x in input().split()]
print("sortin list and deleting the duplication....")
input_int_array.sort()
input_int_array = list(dict.fromkeys(input_int_array))
print(input_int_array)

print("Enter a number: ")
value = int(input())
mid = len(input_int_array) // 2
low = 0
high = len(input_int_array) - 1
if len(input_int_array) == 0:
    print("Your list is empty")
    quit()
if value < input_int_array[0]:
    print("Number is out of the list.\nIndex of the bigger neighbour value in list is: 0")
    quit()
elif value > input_int_array[high]:
    print("Number is out of the list.\nIndex of the smaller neighbour value in list is: ", high)
    quit()
while low <= high and input_int_array[mid] != value:
    if input_int_array[mid] < value:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if input_int_array[mid] == value:
    if input_int_array[0] == value:
        print("Entered number is the first value in the list. Its index is: 0")
        print("Index of the bigger neighbour value in list is: 1")
    elif input_int_array[len(input_int_array)-1] == value:
        print("Entered number is the last value in the list. Its index is: ", len(input_int_array)-1)
        print("Index of the smaller neighbour value in list is: ", len(input_int_array)-2)
    else:
        print("Index of the smaller neighbour value in list is: ", mid - 1)
        print("Index of the bigger neighbour value in list is: ", mid + 1)
elif low > high:
    print("Index of the smaller neighbour value in list is: ", high)
    print("Index of the bigger neighbour value in list is: ", low)
else:
    print("Element is out of the list")
