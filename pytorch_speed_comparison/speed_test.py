import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import time


## math function to approximate (suggested by ChatGPT):
# f(x) = sum over i of x_i * sin(x_i) + 0.5 * sum over i of x_i^2


# device = torch.device("cpu")
device = torch.device("mps")
# device = torch.device("cuda")

print(f"using device: {device}")


num_samples = 50000
input_dim = 1000
hidden_dim = 4096
output_dim = 1 
batch_size = 128
epochs = 5
learning_rate = 0.001



# f(x) = sum over i of x_i * sin(x_i) + 0.5 * sum over i of x_i^2
X_train = np.random.randn(num_samples, input_dim)
y_train = np.sum(X_train * np.sin(X_train), axis=1) + 0.5 * np.sum(X_train**2, axis=1)



X_train = torch.tensor(X_train, dtype=torch.float32).to(device)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1).to(device)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net().to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(net.parameters(), lr=learning_rate)


print("training...")
start_time = time.time()
for epoch in range(epochs):
    perm = torch.randperm(X_train.size(0))
    X_train = X_train[perm]
    y_train = y_train[perm]

    epoch_loss = 0.0
    net.train()
    for i in range(0, X_train.size(0), batch_size):
        batch_X = X_train[i:i+batch_size]
        batch_y = y_train[i:i+batch_size]

        optimizer.zero_grad()
        outputs = net(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    avg_loss = epoch_loss / (X_train.size(0) / batch_size)
    print(f"epoch: {epoch+1},   loss: {avg_loss:.4f}")

end_time = time.time()
print(f"runtime: {end_time - start_time:.2f} seconds")


