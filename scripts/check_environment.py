import sys
import platform
print("Python:", sys.version.split()[0])
print("Platform:", platform.platform())
try:
    import torch
    print("PyTorch:", torch.__version__)
    print("CUDA available locally:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
    else:
        print("No local CUDA GPU detected. Use Colab for GPU training.")
except ImportError:
    print("PyTorch is not installed in this environment.")
