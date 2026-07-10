import accelerate
import diffusers
import huggingface_hub
import torch
import torchvision
import transformers


assert accelerate.__version__ == "0.27.2"
assert diffusers.__version__ == "0.26.3"
assert huggingface_hub.__version__ == "0.20.3"
assert torch.__version__ == "2.5.1+cu121"
assert torchvision.__version__ == "0.20.1+cu121"
assert transformers.__version__ == "4.38.2"

assert torch.cuda.is_available() == True

print("All versions match!")
