#!/usr/bin/env python3
"""
Modern GUI Calculator in Python
A fully functional calculator with a beautiful user interface
"""

import tkinter as tk
from tkinter import font
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        # Variables
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
        # Configure fonts
        self.display_font = font.Font(family="Arial", size=32, weight="bold")
        self.button_font = font.Font(family="Arial", size=18, weight="bold")
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
    def create_display(self):
        """Create the display screen"""
        display_frame = tk.Frame(self.root, bg="#1e1e1e", height=150)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.display = tk.Label(
            display_frame,
            text=self.current,
            font=self.display_font,
            bg="#1e1e1e",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20
        )
        self.display.pack(expand=True, fill="both")
        
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button configuration: (text, row, col, colspan, bg_color, command)
        buttons = [
            # Row 1
            ("C", 0, 0, 1, "#ff6b6b", self.clear_all),
            ("⌫", 0, 1, 1, "#ff6b6b", self.backspace),
            ("%", 0, 2, 1, "#4ecdc4", self.percentage),
            ("÷", 0, 3, 1, "#4ecdc4", lambda: self.operation("/")),
            
            # Row 2
            ("7", 1, 0, 1, "#2d3436", lambda: self.number_press(7)),
            ("8", 1, 1, 1, "#2d3436", lambda: self.number_press(8)),
            ("9", 1, 2, 1, "#2d3436", lambda: self.number_press(9)),
            ("×", 1, 3, 1, "#4ecdc4", lambda: self.operation("*")),
            
            # Row 3
            ("4", 2, 0, 1, "#2d3436", lambda: self.number_press(4)),
            ("5", 2, 1, 1, "#2d3436", lambda: self.number_press(5)),
            ("6", 2, 2, 1, "#2d3436", lambda: self.number_press(6)),
            ("-", 2, 3, 1, "#4ecdc4", lambda: self.operation("-")),
            
            # Row 4
            ("1", 3, 0, 1, "#2d3436", lambda: self.number_press(1)),
            ("2", 3, 1, 1, "#2d3436", lambda: self.number_press(2)),
            ("3", 3, 2, 1, "#2d3436", lambda: self.number_press(3)),
            ("+", 3, 3, 1, "#4ecdc4", lambda: self.operation("+")),
            
            # Row 5
            ("±", 4, 0, 1, "#636e72", self.negate),
            ("0", 4, 1, 1, "#2d3436", lambda: self.number_press(0)),
            (".", 4, 2, 1, "#636e72", self.dot),
            ("=", 4, 3, 1, "#00b894", self.calculate),
        ]
        
        # Configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # Create buttons
        for text, row, col, colspan, bg_color, command in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                font=self.button_font,
                bg=bg_color,
                fg="#ffffff",
                activebackground="#74b9ff",
                activeforeground="#ffffff",
                relief="flat",
                border=0,
                command=command,
                cursor="hand2"
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=5,
                pady=5
            )
            
            # Add hover effect
            def on_enter(e, btn=btn, original_bg=bg_color):
                btn.config(bg="#74b9ff")
            
            def on_leave(e, btn=btn, original_bg=bg_color):
                btn.config(bg=original_bg)
            
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
    
    def update_display(self):
        """Update the display with current value"""
        try:
            # Format display value
            if isinstance(self.current, float):
                if self.current.is_integer():
                    display_value = str(int(self.current))
                else:
                    display_value = str(self.current)
            else:
                display_value = str(self.current)
            
            # Limit display length
            if len(display_value) > 15:
                display_value = display_value[:15]
            
            self.display.config(text=display_value)
        except:
            self.display.config(text="Error")
    
    def number_press(self, num):
        """Handle number button press"""
        self.result = False
        first_num = self.current
        second_num = str(num)
        
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == '.':
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        
        self.update_display()
    
    def clear_all(self):
        """Clear all and reset calculator"""
        self.result = False
        self.current = "0"
        self.display_value = True
        self.check_sum = False
        self.total = 0
        self.update_display()
    
    def backspace(self):
        """Remove last character"""
        if len(str(self.current)) > 1:
            self.current = str(self.current)[:-1]
        else:
            self.current = "0"
        self.update_display()
    
    def dot(self):
        """Add decimal point"""
        self.result = False
        if self.input_value:
            self.current = "0."
            self.input_value = False
        elif "." not in str(self.current):
            self.current = str(self.current) + "."
        self.update_display()
    
    def negate(self):
        """Negate the current number"""
        self.result = False
        self.current = -float(self.current)
        self.update_display()
    
    def percentage(self):
        """Convert to percentage"""
        self.result = False
        self.current = float(self.current) / 100
        self.update_display()
    
    def operation(self, op):
        """Handle operation button press"""
        self.current = float(self.current)
        if self.check_sum:
            self.calculate()
        else:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = True
    
    def calculate(self):
        """Perform calculation"""
        self.result = True
        self.check_sum = False
        self.input_value = True
        
        try:
            if self.op == "+":
                self.total += float(self.current)
            elif self.op == "-":
                self.total -= float(self.current)
            elif self.op == "*":
                self.total *= float(self.current)
            elif self.op == "/":
                if float(self.current) == 0:
                    self.display.config(text="Error")
                    self.current = "0"
                    return
                self.total /= float(self.current)
            
            # Round to avoid floating point errors
            self.current = round(self.total, 10)
            
            # Remove trailing zeros
            if isinstance(self.current, float) and self.current.is_integer():
                self.current = int(self.current)
            
            self.update_display()
            
        except Exception as e:
            self.display.config(text="Error")
            self.current = "0"
        
        self.total = 0

def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
