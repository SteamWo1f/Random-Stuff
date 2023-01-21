from PIL import Image

def image_to_ascii(image_file):
    # Open the image file
    with Image.open(image_file) as img:
        # Convert the image to grayscale
        img = img.convert('L')
        # Resize the image
        img = img.resize((15, 15))
        # Define the ASCII characters to use
        chars = "!#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]""^_`abcdefghijklmnopqrstuvwxyz{|}~"
        # Get the pixel values
        pixels = img.getdata()
        # Define the new image
        new_image = []
        for pixel in pixels:
            # Get the ASCII character for each pixel
            char = chars[pixel // 25]
            new_image.append(char)
        # Print the new image
        print(''.join(new_image))
        # Save the output to a file
        with open("ascii_image.txt", "w") as f:
            f.write("\n".join("".join(new_image[i:i+80]) for i in range(0, len(new_image), 80)))


image_to_ascii("85211822.png")
