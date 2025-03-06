# 🎨 ASCII Art Converter

A versatile Python application that converts both images and text into ASCII art with a modern, user-friendly interface.

## 📌 Description

ASCII Art Converter is a desktop application that offers dual functionality:
1. Convert images into ASCII art
2. Transform text into stylized ASCII art using various fonts

The application provides real-time preview, multiple save options, and an intuitive user interface.

## 🔥 Unique Features

- **Dual Conversion Modes**
  - Image to ASCII conversion
  - Text to ASCII art with multiple font styles
- **Real-time Preview**
  - Instant preview as you type text
  - Live font style changes
- **Save Options**
  - Save as PNG with high quality
  - Export as TXT file
- **User-Friendly Interface**
  - Clean, modern UI
  - Easy navigation between modes
  - Scrollable preview area
  - Responsive layout

## 🛠 Technologies Used

- **Python 3.x**
- **Libraries:**
  - `tkinter` - GUI framework
  - `Pillow` - Image processing
  - `pyfiglet` - ASCII text art generation
  - `opencv-python-headless` - Image processing
  - `numpy` - Numerical operations

## 🎨 Screenshots

[Add screenshots here showing:
1. Main menu
2. Image converter interface
3. Text converter interface
4. Sample outputs]

## 🚀 How to Run

1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application:**
   ```bash
   python ascii_viewer.py
   ```

3. **Using the App:**
   - Choose between "Convert Image" or "Convert Text"
   - For Images:
     1. Click "Load Image"
     2. Select an image file
     3. View the ASCII preview
     4. Save as PNG or TXT
   - For Text:
     1. Enter text in the input field
     2. Select a font style
     3. View real-time preview
     4. Save in desired format

## 🤖 Extra Features

1. **High-Quality PNG Export**
   - Custom font rendering
   - High DPI support
   - Quality preservation

2. **Font Customization**
   - Multiple pyfiglet fonts
   - Real-time font preview
   - Sorted font list for easy selection

3. **Error Handling**
   - Graceful error messages
   - File type validation
   - Empty input handling

4. **UI Enhancements**
   - Responsive window sizing
   - Scrollbars for large outputs
   - Clear navigation with back button
   - Consistent styling throughout

## 📝 Notes

- Supported image formats: PNG, JPG, JPEG, GIF, BMP
- Text art supports all pyfiglet fonts
- Recommended for desktop use with minimum resolution of 1200x800

## 🤝 Contributing

Feel free to fork, improve, and create pull requests. For major changes, please open an issue first.
