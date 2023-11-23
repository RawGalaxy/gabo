import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GABO")
root.geometry("700x480") 
style = ttk.Style(root)
style.theme_use("default")

def analisis():
    log_message("Tombol Analyze screen di-klik.")

def optimisasi():
    log_message("Tombol Optimize di-klik.")

def balikan_settings():
    log_message("Tombol Revert Settings di-klik.")

def log_message(message):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)
    log_text.config(state=tk.DISABLED)

l1 = tk.Label(root, text="GPU AI-Based Optimizer", font=('Times', 20))
l1.pack(side=tk.TOP)

top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, fill=tk.X, pady=20)

button_size = 15  
analyze_button = tk.Button(top_frame, text="Analyze Screen", command=analisis, height=button_size, width=button_size, bg="#FFEBD8", activebackground="#efd9c1")
optimize_button = tk.Button(top_frame, text="Optimize", command=optimisasi, height=button_size, width=button_size, bg="#FFEBD8", activebackground="#efd9c1")
revert_button = tk.Button(top_frame, text="Revert Settings", command=balikan_settings, height=button_size, width=button_size, bg="#FFEBD8", activebackground="#efd9c1")
exit_button = tk.Button(top_frame, text="Exit", command=root.destroy, height=button_size, width=button_size, bg="#FFEBD8", activebackground="#efd9c1")

analyze_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
optimize_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
revert_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
exit_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_text = tk.Text(bottom_frame, height=20, state=tk.DISABLED, yscrollcommand=scrollbar.set)
log_text.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

scrollbar.config(command=log_text.yview)

root.mainloop()

'''
Pseudocode

import win32gui

Close/minimize all applications (python left clicks bottom right)
Opens all the required applications
            >Python clicks search bar at the left bottom, searches the GPU app (MSI Afterburner) and benchmark
            >Python moves the apps to their desired location (based on the videographic) 
Start the algorithm
            >Python clicks/modifies clockspeed/voltage
            >Wait for 5 minutes (testing the result of modifying clockspeed/voltage)
            >Python takes a screenshot of the screen and analyze the benchmark and the graphs
            >It saves the results and proceeds
            >If the system crashes, Python uses the previous result and change another value (If increasing the clockspeed makes the system crash, adjust the voltage instead and vice versa)
            >Python gathers all the required information then gives result on what the most optimal clockspeed and voltage
Output the results
'''