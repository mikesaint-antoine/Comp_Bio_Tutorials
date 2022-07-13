import random



test_array = [4,1,7,3]


def bubble_sort(array_in):

    swaps = True

    while (swaps):

        swaps = False

        for i in range(len(array_in)-1):
            if array_in[i] > array_in[i+1]:
                tmp = array_in[i+1]
                array_in[i+1] = array_in[i]
                array_in[i] = tmp
                swaps = True

    return(array_in)

# print(test_array)
# test_array = bubble_sort(test_array)
# print(test_array)


randlist = random.sample(range(0, 10000), 100)


print(randlist)
randlist = bubble_sort(randlist)
print()
print(randlist)
