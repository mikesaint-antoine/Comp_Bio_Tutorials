
import random

test_array = [4,1,3,7]

def selection_sort(array_in):

    for starting_index in range(len(array_in)-1):

        min_index = starting_index

        for i in range(starting_index, len(array_in)):

            if array_in[i] < array_in[min_index]:
                min_index = i 

        tmp = array_in[starting_index]
        array_in[starting_index] = array_in[min_index]
        array_in[min_index] = tmp

    return(array_in)


# print(test_array)
# test_array = selection_sort(test_array)
# print(test_array)



def check_if_sorted(array_in):
    for i in range(len(array_in)-1):
        if array_in[i] > array_in[i+1]:
            return(False)
    return(True)

randlist = random.sample(range(0, 10000), 100)

print("Check if sorted:")
print(check_if_sorted(randlist))
print("sorting...")
randlist = selection_sort(randlist)
print()
print("Check if sorted:")
print(check_if_sorted(randlist))



