import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# Uses NVDIA GPU, else uses cpu - remind me to add amd gpu support
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Hyper-parameters - input_size = the number of features in the input data. hidden_size = number of neurons in the hidden layer. num_classes = number of classes you want to predict.
input_size = 784
hidden_size = 100
num_classes = 10
num_epochs = 2

# not sure what these 2 parameters are below
learning_rate = 0.001
batch_size = 100

# MNIST 
train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True,
        transform=transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False,
        transform=transforms.ToTensor())


train_loader = torch.utils.data.DataLoader(dataset=train_dataset,batch_sampler=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset,batch_sampler=batch_size, shuffle=False)

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

class ConvNet(nn.Module):
    def __init__(self):
        pass
    def forward(self, x):
        pass
