import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
originalImage = preprocess(Image.open(r"C:/Users/Ziyad/Downloads/dracula.png").convert('RGB')).unsqueeze(0)
copycatImage = preprocess(Image.open(r"C:/Users/Ziyad/Downloads/omnidracula.png").convert('RGB')).unsqueeze(0)


model = models.resnet50(pretrained=True)
model = nn.Sequential(*list(model.children())[:-1]) # remove the final layer because we just want the features extracted from previous layers
model.eval()

with torch.no_grad():
    embedding1 = model(originalImage)  
    embedding2 = model(copycatImage)  

print(embedding1)
embedding1 = embedding1.view(embedding1.size(0), -1)
embedding2 = embedding2.view(embedding2.size(0), -1)
print(embedding1)
cosine = nn.CosineSimilarity(dim=1, eps=1e-6)
similarity = cosine(embedding1, embedding2) 

similarity_score = similarity.item()
print(f"Cosine Similarity between the two icons: {similarity_score:.4f}")