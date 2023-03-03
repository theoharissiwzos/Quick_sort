def quick_sort(arr):
    """
 
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)


# Read numbers from the file
with open("num_list.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# Sort the numbers using Quick Sort
sorted_numbers = quick_sort(numbers)

# Print the sorted numbers
print(sorted_numbers)
