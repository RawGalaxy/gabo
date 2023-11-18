import tkinter as tk
from tkinter import ttk

# Main application window
root = tk.Tk()
root.title("GABO")
root.geometry("640x480")  # Set the window size to 640x480
root.resizable(height= False, width= False)
root.configure(bg='beige')

# Function placeholders for button commands)
def analyze_screen():
  analyze_button.config(bg='#007D78')
  log_message("Analyze screen clicked.")

def optimize_now():
  optimize_button.config(bg='#10A900')
  log_message("OPTIMIZE NOW clicked.")

def revert_settings():
  optimize_button.config(bg='#3aeb34')
  analyze_button.config(bg='#2FD6D0')
  log_message("Revert Settings clicked.")

def log_message(message):
  log.config(state=tk.NORMAL)
  log.insert(tk.END, message + "\n")
  log.config(state=tk.DISABLED)

# Top frame for buttons
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X, pady=20)

# Buttons with a uniform size
button_size = 15  # You can adjust this size for your buttons
analyze_button = tk.Button(top_frame, text="Analyze Screen", command=analyze_screen, height=button_size, width=button_size, bg='#2FD6D0', cursor="hand2")
optimize_button = tk.Button(top_frame, text="OPTIMIZE NOW", command=optimize_now, height=button_size, width=button_size, bg='#3aeb34', cursor="hand2")
revert_button = tk.Button(top_frame, text="Revert Settings", command=revert_settings, height=button_size, width=button_size, bg='#FE383D', cursor="hand2")

analyze_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
optimize_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
revert_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# Bottom frame for log panel
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Scrollbar for the log panel
scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Log panel
log = tk.Text(bottom_frame, height=20, state=tk.DISABLED, yscrollcommand=scrollbar.set)
log.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

# Configure the scrollbar
scrollbar.config(command=log.yview)

# Start the application
root.mainloop()
