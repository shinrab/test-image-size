import kagglehub

# Download latest version
path = kagglehub.dataset_download("pengcw1/market-1501", output_dir="./data/market1501")

print("Path to dataset files:", path)
