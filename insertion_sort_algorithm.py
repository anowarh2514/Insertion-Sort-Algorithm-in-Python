def insertion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index - 1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break
        print("Sorted List = ",list)

list = [6,3,5,4,2,1]
print("Unsorted list = ",list)
insertion_sort(list)
print("Final Sorted List = ",list)