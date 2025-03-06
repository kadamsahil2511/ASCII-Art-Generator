import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import img_art
from text_art import TextArtGenerator
import os
import pyfiglet

class UnifiedASCIIConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ASCII Art Converter")
        self.window.geometry("400x200")  # Start with small window for choice
        
        # Configure window
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        self.setup_choice_ui()
        
    def setup_choice_ui(self):
        # Main choice container
        choice_frame = ttk.Frame(self.window, padding="20")
        choice_frame.grid(row=0, column=0, sticky="nsew")
        
        # Welcome label
        ttk.Label(
            choice_frame, 
            text="Welcome to ASCII Art Converter",
            font=('Helvetica', 16)
        ).pack(pady=20)
        
        # Choice buttons
        button_frame = ttk.Frame(choice_frame)
        button_frame.pack(expand=True)
        
        ttk.Button(
            button_frame,
            text="Convert Image",
            command=self.show_image_converter,
            width=20
        ).pack(pady=5)
        
        ttk.Button(
            button_frame,
            text="Convert Text",
            command=self.show_text_converter,
            width=20
        ).pack(pady=5)
        
        # Back button (hidden initially)
        self.back_button = ttk.Button(
            self.window,
            text="← Back to Menu",
            command=self.show_choice_ui
        )
    
    def show_image_converter(self):
        # Hide choice UI
        for widget in self.window.winfo_children():
            widget.grid_remove()
        
        # Resize window to be bigger
        self.window.geometry("1200x800")  # Changed from 800x600
        
        # Show back button
        self.back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        # Create image converter frame
        self.image_frame = ttk.Frame(self.window)
        self.image_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Setup image converter UI
        self.setup_image_ui(self.image_frame)
    
    def show_text_converter(self):
        # Hide choice UI
        for widget in self.window.winfo_children():
            widget.grid_remove()
        
        # Resize window
        self.window.geometry("1200x800")
        
        # Show back button
        self.back_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        # Create text converter frame
        self.text_frame = ttk.Frame(self.window)
        self.text_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Setup text converter UI
        self.setup_text_ui(self.text_frame)
    
    def show_choice_ui(self):
        # Reset window size
        self.window.geometry("400x200")
        
        # Hide all current widgets
        for widget in self.window.winfo_children():
            widget.grid_remove()
        
        # Show choice UI
        self.setup_choice_ui()
    
    def setup_image_ui(self, parent):
        # Main container
        main_frame = ttk.Frame(parent)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Top control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        control_frame.grid_columnconfigure(1, weight=1)
        
        ttk.Button(
            control_frame, 
            text="Load Image",
            command=self.load_image,
            width=20  # Make button wider
        ).grid(row=0, column=0, padx=5)
        
        self.file_label = ttk.Label(control_frame, text="No image selected")
        self.file_label.grid(row=0, column=1, padx=5)
        
        # ASCII preview panel
        preview_frame = ttk.LabelFrame(main_frame, text="ASCII Preview")
        preview_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=1)
        
        # Bigger ASCII preview with larger font
        self.ascii_preview = tk.Text(
            preview_frame, 
            wrap=tk.NONE, 
            bg='white', 
            fg='black',
            font=('Courier', 12),  # Increased font size
            width=100,  # Set initial width
            height=40   # Set initial height
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
        
        # Bottom control panel with bigger buttons
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(
            bottom_frame, 
            text="Save as PNG",
            command=lambda: self.save_ascii('png'),
            width=20  # Make button wider
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame, 
            text="Save as TXT",
            command=lambda: self.save_ascii('txt'),
            width=20  # Make button wider
        ).pack(side=tk.LEFT, padx=5)
    
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if not file_path:
            return
            
        try:
            # Update file label
            self.file_label.config(text=f"File: {os.path.basename(file_path)}")
            
            # Convert to ASCII
            self.current_ascii_art = img_art.image_to_ascii(file_path)
            self.ascii_preview.delete(1.0, tk.END)
            self.ascii_preview.insert(1.0, self.current_ascii_art)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def save_ascii(self, format_type):
        if not hasattr(self, 'current_ascii_art') or not self.current_ascii_art:
            messagebox.showwarning("Warning", "No ASCII art to save!")
            return
        
        if format_type == 'png':
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if file_path:
                try:
                    img_art.save_ascii_to_png(self.current_ascii_art, file_path)
                    messagebox.showinfo("Success", "ASCII art saved as PNG!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save PNG: {str(e)}")
        else:
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
    
    def setup_text_ui(self, parent):
        # Main container
        main_frame = ttk.Frame(parent)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        
        # Top control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        control_frame.grid_columnconfigure(1, weight=1)
        
        # Text input
        ttk.Label(control_frame, text="Enter Text:").grid(row=0, column=0, padx=5)
        self.text_input = ttk.Entry(control_frame, width=50)
        self.text_input.grid(row=0, column=1, sticky="ew", padx=5)
        self.text_input.bind('<KeyRelease>', lambda e: self.generate_text_preview())
        
        # Font selection
        ttk.Label(control_frame, text="Font Style:").grid(row=1, column=0, padx=5, pady=5)
        self.font_style = ttk.Combobox(
            control_frame, 
            values=sorted(pyfiglet.FigletFont.getFonts()), 
            width=47
        )
        self.font_style.set("standard")
        self.font_style.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.font_style.bind('<<ComboboxSelected>>', lambda e: self.generate_text_preview())
        
        # ASCII preview panel
        preview_frame = ttk.LabelFrame(main_frame, text="ASCII Preview")
        preview_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        preview_frame.grid_columnconfigure(0, weight=1)
        preview_frame.grid_rowconfigure(0, weight=1)
        
        # ASCII preview
        self.text_preview = tk.Text(
            preview_frame, 
            wrap=tk.NONE, 
            bg='white', 
            fg='black',
            font=('Courier', 12),
            width=100,
            height=40
        )
        self.text_preview.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Scrollbars
        y_scrollbar = ttk.Scrollbar(preview_frame, orient='vertical',
                                  command=self.text_preview.yview)
        y_scrollbar.grid(row=0, column=1, sticky='ns')
        
        x_scrollbar = ttk.Scrollbar(preview_frame, orient='horizontal',
                                  command=self.text_preview.xview)
        x_scrollbar.grid(row=1, column=0, sticky='ew')
        
        self.text_preview.configure(yscrollcommand=y_scrollbar.set,
                                  xscrollcommand=x_scrollbar.set)
        
        # Bottom control panel
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.grid(row=2, column=0, pady=10)
        
        ttk.Button(
            bottom_frame, 
            text="Save as PNG",
            command=lambda: self.save_text_ascii('png'),
            width=20
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            bottom_frame, 
            text="Save as TXT",
            command=lambda: self.save_text_ascii('txt'),
            width=20
        ).pack(side=tk.LEFT, padx=5)

    def generate_text_preview(self):
        text = self.text_input.get().strip()
        if text:
            try:
                f = pyfiglet.Figlet(font=self.font_style.get())
                self.current_ascii_art = f.renderText(text)
                self.text_preview.delete(1.0, tk.END)
                self.text_preview.insert(1.0, self.current_ascii_art)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate ASCII art: {str(e)}")

    def save_text_ascii(self, format_type):
        if not hasattr(self, 'current_ascii_art') or not self.current_ascii_art:
            messagebox.showwarning("Warning", "No ASCII art to save!")
            return
        
        if format_type == 'png':
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if file_path:
                try:
                    # Use img_art.py's save function
                    img_art.save_ascii_to_png(self.current_ascii_art, file_path)
                    messagebox.showinfo("Success", "ASCII art saved as PNG!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save PNG: {str(e)}")
        else:
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
    app = UnifiedASCIIConverter()
    app.run() 