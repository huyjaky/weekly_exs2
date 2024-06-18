import torch
import softmax

data = torch.Tensor([1, 2, 3])
softmax1 = softmax.Softmax()
print(softmax1.calc(data))
