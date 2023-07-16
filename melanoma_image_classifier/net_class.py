import torch
import torch.nn as nn
import torch.nn.functional as F
import sys

# statquest explanation video
# https://www.youtube.com/watch?v=HGwBXDKFk9I



# 50x50 pixels
img_size = 50


class Net(nn.Module):

    # constructor
    def __init__(self):

        super().__init__()

        self.conv1 = nn.Conv2d(1,32,kernel_size=5)
        self.conv2 = nn.Conv2d(32,64,kernel_size=5)
        self.conv3 = nn.Conv2d(64,128,kernel_size=5)

        self.fc1 = nn.Linear(128*2*2, 512)
        self.fc2 = nn.Linear(512, 2)

    def forward(self,x):

        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))
        # print(f"shape after conv1: {x.shape} ")


        x = F.max_pool2d(F.relu(self.conv2(x)), (2,2))
        # print(f"shape after conv2: {x.shape} ")

        x = F.max_pool2d(F.relu(self.conv3(x)), (2,2))
        # print(f"shape after conv3: {x.shape} ")

        # sys.exit("trying to get shape for linear layer")

        x = x.view(-1,128*2*2)

        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        x = F.softmax(x)

        return(x)





# net = Net()


# test_img = torch.randn(img_size,img_size).view(-1,1,img_size,img_size)
# output = net(test_img)