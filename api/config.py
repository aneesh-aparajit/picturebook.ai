import torch

DEVICE = torch.device("cuda" if torch.has_cuda else "mps" if torch.has_mps else "cpu")
