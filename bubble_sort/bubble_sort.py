def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    for i in range(len(unsorted_list)):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

print(bubble_sort([4, 5, 3, 4]))
