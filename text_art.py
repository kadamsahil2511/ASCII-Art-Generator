import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyfiglet
from PIL import Image, ImageDraw, ImageFont

class TextArtGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text to ASCII Art Generator")
        self.window.geometry("1200x800")
        
        # Configure window
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        self.current_ascii_art = ""
        self.available_fonts = pyfiglet.FigletFont.getFonts()
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.window)
        main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input")
        input_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        input_frame.grid_columnconfigure(1, weight=1)
        
        # Text input
        ttk.Label(input_frame, text="Enter Text:").grid(row=0, column=0, padx=5, pady=5)
        self.text_input = ttk.Entry(input_frame)
        self.text_input.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.text_input.bind('<KeyRelease>', lambda e: self.generate_preview())
        
        # Font selection
        ttk.Label(input_frame, text="Font Style:").grid(row=1, column=0, padx=5, pady=5)
        self.font_style = ttk.Combobox(input_frame, values=self.available_fonts)
        self.font_style.set("standard")
        self.font_style.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.font_style.bind('<<ComboboxSelected>>', lambda e: self.generate_preview())
        
        # Preview section
        preview_frame = ttk.LabelFrame(main_frame, text="Preview")
        preview_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=1)
        
        # ASCII preview
        self.ascii_preview = tk.Text(
            preview_frame,
            wrap=tk.NONE,
            bg='white',
            fg='black',
            font=('Courier', 10)
        )
        self.ascii_preview.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Scrollbars
        y_scrollbar = ttk.Scrollbar(preview_frame, orient='vertical',
                                  command=self.ascii_preview.yview)
        y_scrollbar.grid(row=0, column=1, sticky='ns')
        
        x_scrollbar = ttk.Scrollbar(preview_frame, orient='horizontal',
                                  command=self.ascii_preview.xview)
        x_scrollbar.grid(row=1, column=0, sticky='ew')
        
        self.ascii_preview.configure(yscrollcommand=y_scrollbar.set,
                                   xscrollcommand=x_scrollbar.set)
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(control_frame, text="Save as PNG",
                  command=lambda: self.save_ascii('png')).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Save as TXT",
                  command=lambda: self.save_ascii('txt')).pack(side=tk.LEFT, padx=5)
    
    def generate_preview(self):
        text = self.text_input.get().strip()
        if text:
            try:
                f = pyfiglet.Figlet(font=self.font_style.get())
                self.current_ascii_art = f.renderText(text)
                self.ascii_preview.delete(1.0, tk.END)
                self.ascii_preview.insert(1.0, self.current_ascii_art)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate ASCII art: {str(e)}")
    
    def save_ascii_to_png(self, ascii_art, output_path):
        # Calculate dimensions
        lines = ascii_art.split("\n")
        line_count = len(lines)
        max_line_length = max(len(line) for line in lines)
        
        # Font configuration
        font_size = 15
        char_width = font_size * 0.6
        char_height = font_size * 1.2
        padding = 40
        
        # Calculate image dimensions
        width = int(max_line_length * char_width) + padding * 2
        height = int(line_count * char_height) + padding * 2
        
        # Create image
        img = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(img)
        
        # Try to load font
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Courier.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        # Draw ASCII art
        y = padding
        for line in lines:
            if line.strip():
                draw.text((padding, y), line, font=font, fill="black")
            y += char_height
        
        # Save image
        img.save(output_path, quality=95, dpi=(300, 300))
    
    def save_ascii(self, format_type):
        if not self.current_ascii_art:
            messagebox.showwarning("Warning", "No ASCII art to save!")
            return
        
        if format_type == 'png':
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if file_path:
                try:
                    self.save_ascii_to_png(self.current_ascii_art, file_path)
                    messagebox.showinfo("Success", "ASCII art saved as PNG!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save PNG: {str(e)}")
        
        else:  # txt format
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")]
            )
            if file_path:
                try:
                    with open(file_path, 'w') as f:
                        f.write(self.current_ascii_art)
                    messagebox.showinfo("Success", "ASCII art saved as text!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save text: {str(e)}")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TextArtGenerator()
    app.run()
