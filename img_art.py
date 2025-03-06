from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Function to convert image to ASCII
def image_to_ascii(image_path, new_width=100):
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    img = img.resize((new_width, new_height))
    img = img.convert("L")  # Convert to grayscale
    pixels = np.array(img)
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    
    ascii_image = ""
    for row in pixels:
        for pixel in row:
            ascii_image += ascii_chars[pixel // 25]  # Mapping grayscale to ASCII
        ascii_image += "\n"
    
    return ascii_image

def save_ascii_to_png(ascii_art, output_path, is_dark_mode=True):
    # Calculate dimensions
    lines = ascii_art.split("\n")
    line_count = len(lines)
    max_line_length = max(len(line) for line in lines)
    
    # Font configuration
    font_size = 15  # Base font size
    char_width = font_size * 0.6  # Monospace character width
    char_height = font_size * 0.9  # Line height with spacing
    
    # Calculate image dimensions with padding
    padding = 40
    width = int(max_line_length * char_width) + padding * 2
    height = int(line_count * char_height) + padding * 2
    
    # Set colors based on mode
    if is_dark_mode:
        bg_color = (0, 0, 0)  # Black background
        text_color = (0, 255, 0)  # Green text
    else:
        bg_color = (255, 255, 255)  # White background
        text_color = (102, 102, 102)  # Gray text
    
    # Create image with calculated dimensions
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load monospace font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Courier.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("/Library/Fonts/Courier New.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    # Draw the ASCII art
    y = padding  # Start from top padding
    for line in lines:
        if line.strip():  # Only draw non-empty lines
            draw.text((padding, y), line, font=font, fill=text_color)
        y += char_height
    
    # Save the image with high quality
    img.save(output_path, quality=95, dpi=(300, 300))

# Example usage
if __name__ == "__main__":
    image_path = "cat.jpg"  # Input image path
    output_path = "ascii_art.png"  # Output path for the PNG
    
    # Convert image to ASCII
    ascii_art = image_to_ascii(image_path)
    
    # Save as PNG with dark mode
    save_ascii_to_png(ascii_art, output_path, is_dark_mode=False)