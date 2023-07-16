import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from net_class import Net

# 50x50 pixels
img_size = 50


training_data = np.load("melanoma_training_data.npy", allow_pickle=True)



# for row in training_data:
#     print(row[0])
#     print(row[1])
#     print()
#     print()
#     input()


# putting all the image arrays into this tensor
train_X = torch.Tensor( [item[0] for item in training_data]  )
train_X = train_X / 255

# for row in train_X:
#     print(row)
#     print()
#     input()


# one-hot vector labels tensor
train_y = torch.Tensor( [item[1] for item in training_data]  )


net = Net()


optimizer = optim.Adam(net.parameters(), lr=0.001)

loss_function = nn.MSELoss()
# mean squared error loss function



batch_size = 100
# how many images you're passing through at once



epochs = 2

for epoch in range(epochs):

    for i in range(0,len(train_X), batch_size):

        print(f"EPOCH {epoch+1}, fraction complete: {i/len(train_X)}")

        batch_X = train_X[i: i+batch_size].view(-1, 1, img_size, img_size)
        batch_y = train_y[i: i+batch_size]

        optimizer.zero_grad()
        # reset gradients of model parameters to zero before this pass


        outputs = net(batch_X)


        loss = loss_function(outputs,batch_y)
        # calculates loss between predicted outputs and actually image one-hot vector labels
        # real label (example):
        # [0,1]
        # model guess (example):
        # [0.34,0.66]

        loss.backward()
        # backpropagation is done to calculate gradients of the loss with respect to model params

        optimizer.step()
        # optimizer updates the model params based on the gradient we just calculated





torch.save(net.state_dict(), "saved_model.pth")








