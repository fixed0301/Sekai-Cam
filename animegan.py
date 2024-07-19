import torch
from PIL import Image

# 사진기에 따라 바꿀 것
n = 720

model = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
model = model.to(torch.device('cpu')) # Change to your device!
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=720)
img = Image.open(r"image2.png").crop((0, 0, 1080, 1080)).resize((1920, 1080)).convert("RGB")
out = face2paint(model, img)
out.show()
