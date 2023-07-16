import numpy as np
import torch
from net_class import Net


# 50x50 pixels
img_size = 50


net = Net()
net.load_state_dict(torch.load('saved_model.pth'))
net.eval()


testing_data = np.load("melanoma_testing_data.npy", allow_pickle=True)


# for row in testing_data:
#     print(row[0])
#     print(row[1])
#     print()
#     print()
#     input()


# putting all the image arrays into this tensor
test_X = torch.Tensor( [item[0] for item in testing_data]  )
test_X = test_X / 255

# for row in test_X:
#     print(row)
#     print()
#     input()


# one-hot vector labels tensor
test_y = torch.Tensor( [item[1] for item in testing_data]  )



correct = 0
total = 0


with torch.no_grad():
    # tells pytorch not to automatically keep track of gradients

    for i in range(len(test_X)):

        # real label (example):
        # [0,1]
        # model guess (example):
        # [0.34,0.66]


        output = net(test_X[i].view(-1, 1, img_size, img_size))[0]

        if output[0] >= output[1]:
            guess = "B"
        else:
            guess = "M"

        real_label = test_y[i]

        if real_label[0] >= output[1]:
            real_class = "B"
        else:
            real_class = "M"

        if guess == real_class:
            correct += 1

        total += 1


print(f"Accuracy: {round(correct/total,3)}")