from PIL import Image

# Create a new blank image with a red pixel (1x1 pixel, RGBA format)
image = Image.new("RGBA", (1, 1), (255, 0, 0, 255))

# Save the image as a PNG file without compression
image.save("red_pixel.png", "PNG", compress_level=0)

print("Red pixel PNG file created as 'red_pixel.png' without compression.")
