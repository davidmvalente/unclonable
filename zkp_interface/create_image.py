from PIL import Image

# Create a new blank image with red pixels (RGBA format)
image = Image.new("RGBA", (16, 16), (255, 0, 0, 255))

# Save the image as a PNG file without compression
image.save("red_pixel.png", "PNG", compress_level=0)

print("Red pixel PNG file created as 'red_pixel.png' without compression.")
