import numpy as np


# test_list = [1,3,5,7]
#
# test_array = np.array([4,6,8,2,3,13,16,9,153]).astype(float)
# print(test_array)
# print(type(test_array))
# print(test_array[2])
# print(test_array.shape)


# print(np.max(test_array))
# print(np.min(test_array))
# print(np.mean(test_array))
# print(np.median(test_array))
# print(np.std(test_array))

#
# print(test_list)
# print(type(test_list))
#
# test_list = np.array(test_list)
# print(type(test_list))



# test_array = list(test_array)
# print(test_array)
# print(type(test_array))


# print(test_array)
# print()
# print(test_array * 2)

# print(test_array + test_array*2)

# test_array2 = test_array * 10
#
# print(test_array / test_array2)


# zero_array = np.zeros(shape=(10,))
# print(zero_array)
#
# ones_array = np.ones(shape=(10,))
# print(ones_array)
#
# linspace_test = np.linspace(0,4,num=10)
# print(linspace_test)
#
# arange_test = np.arange(-10,10,2)
# print(arange_test)





test = np.array([[1,2,3,2],
                [5,6,7,7],
                [7,6,5,10]])

# print(test)
# print(type(test))

# print(test.shape)

test = np.transpose(test)
# print(test.shape)
# print(test)

#
# print(test[0,0])
# print(test[1,2])

# print(test[1,:])
#
# print(test[:,2])



# for i in range(test.shape[0]):
#     for j in range(test.shape[1]):
#         print(test[i,j])


# for i in range(test.shape[0]):
#         print(test[i,:])


# print(test)
#
# test[test<5] = 0
# print(test)


# np.save("saved_array.npy",test)



# load_test = np.load("saved_array.npy")
# print(load_test)



# zero_array = np.zeros(shape=(3,4,10))
# print(zero_array)
# print(zero_array.shape)


########################################################################################################

## (Pseudo) Random Number Generation

# rand = np.random.exponential(scale=1,size=(10,2,4))
# print(rand)


rand = np.random.poisson(lam=3,size=(10,2,4))
print(rand)
