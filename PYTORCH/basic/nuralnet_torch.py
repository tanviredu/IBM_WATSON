import torch
import torch.nn as nn
import torch.nn.functional as F 
from torchvision import datasets, transforms
import seaborn as sns
sns.set()
import numpy as np 
import matplotlib.pyplot as plt 
import keras 
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(x_test.shape)


## create the nural network