import albumentations as A
import cv2

transform = A.Compose([
    A.RandomCrop(width=190, height=190),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])

image = cv2.imread("NewYork.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


transformed = transform(image=image)
transformed_image = transformed["image"]
