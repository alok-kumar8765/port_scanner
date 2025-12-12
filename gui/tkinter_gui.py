import tkinter as tk
from main import start_scan

def run_gui():
    root = tk.Tk()
    root.title("Network Scanner")

    tk.Label(root, text="Target Host:").pack()
    entry = tk.Entry(root)
    entry.pack()

    def on_scan():
        host = entry.get()
        start_scan(host)

    tk.Button(root, text="Scan", command=on_scan).pack()

    root.mainloop()
