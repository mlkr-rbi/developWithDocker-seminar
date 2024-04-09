import torch

def check_gpu():
    # Check if CUDA is available
    if torch.cuda.is_available():
        # Get the number of available GPUs
        num_gpus = torch.cuda.device_count()
        print(f"Number of GPUs available: {num_gpus}")

        # Print information about each GPU
        for i in range(num_gpus):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_ram = torch.cuda.get_device_properties(i).total_memory
            gpu_ram_gb = round(gpu_ram / (1024 ** 3), 2)  # Convert bytes to GB
            print(f"GPU {i+1}: {gpu_name}, RAM: {gpu_ram_gb} GB")
    else:
        print("No GPU available.")

if __name__ == "__main__":
    check_gpu()
