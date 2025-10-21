import torch

if torch.cuda.is_available():
    current_device = torch.cuda.current_device()
    print(f"Current CUDA device: {current_device}")
    print(f"Device name: {torch.cuda.get_device_name(current_device)}")
else:
    print("CUDA is not available, using CPU.")

# import torch
print("检查 PyTorch 版本中 CUDA 的支持")
print(torch.version.cuda)  # 检查 PyTorch 版本中 CUDA 的支持

# import torch
print("查看 cuDNN 是否可用")
print(torch.backends.cudnn.is_available())  # 查看 cuDNN 是否可用
print("查看 cuDNN 版本")
print(torch.backends.cudnn.version())       # 查看 cuDNN 版本

# import torch
print("torch.__version")
print(torch.__version__)
print("CUDA 安裝成功")
print(torch.cuda.is_available())  # True 表示 CUDA 安裝成功

gpu_count = torch.cuda.device_count()
print(f"可用的 GPU 数量：{gpu_count}")

# import argparse
# import torch

# # 定義argparse參數
# parser = argparse.ArgumentParser(description='Your script description')
# parser.add_argument('--rand_seed', action='store_true', help='Use a random seed for each sample.')
# parser.add_argument('--seed', type=int, default=12345, help='Set the seed manually.')

# # 解析參數
# args = parser.parse_args()

# # 如果使用 --rand_seed，則生成隨機的seed
# if args.rand_seed:
#     args.seed = torch.randint(1, 999999, (1,)).item()

# # 生成攻擊者使用的rand_seed，並確保與 args.seed 不同
# rand_seed = args.seed
# while rand_seed == args.seed:
#     rand_seed = torch.randint(1, 999999, (1,)).item()

# print(f"Main seed: {args.seed}, Random seed for attacker: {rand_seed}")
