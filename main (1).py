import cv2
import matplotlib.pyplot as plt

# 1. Read image
image = cv2.imread('image.png')

# Check whether image is loaded
if image is None:
    print("Image not found!")
    exit()

# 2. Display image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')
plt.show()

# 3. Print image dimensions
print("Image dimensions:", image.shape)

# 4. Print pixel value at (100,100)
print("Pixel value at (100,100):", image[100, 100])

# 5. Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 6. Print grayscale image dimensions
print("Grayscale dimensions:", gray.shape)

# 7. Display grayscale image
plt.imshow(gray, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')
plt.show()

# 8. Resize image to 300 x 300
resized = cv2.resize(image, (300, 300))

plt.imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
plt.title('Resized Image (300 x 300)')
plt.axis('off')
plt.show()

# 9. Crop a portion of the image
cropped = image[50:250, 50:250]

plt.imshow(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
plt.title('Cropped Image')
plt.axis('off')
plt.show()

# 10. Save grayscale image
cv2.imwrite('gray_output.jpg', gray)

print("Grayscale image saved successfully!")