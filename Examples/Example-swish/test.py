
import swish
import torch



x = torch.randn(5, 3)
y = swish.forward(x)
print(y)
