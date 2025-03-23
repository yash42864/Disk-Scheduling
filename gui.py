# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from traditional_algorithms import fcfs, sstf, scan
from ai_scheduler import AI_DiskScheduler
from utils import plot_results

# Function to execute selected scheduling algorithm
def run_algorithm():
    try:
        requests = list(map(int, entry_requests.get().split(',')))
        head = int(entry_head.get())
        algorithm = combo_algorithm.get()

        if algorithm == "FCFS":
            seek_sequence, total_seek = fcfs(requests, head)
        elif algorithm == "SSTF":
            seek_sequence, total_seek = sstf(requests, head)
        elif algorithm == "SCAN":
            seek_sequence, total_seek = scan(requests, head)
        elif algorithm == "AI-Based":
            ai_scheduler = AI_DiskScheduler()
            ai_scheduler.train(requests)
            seek_sequence, total_seek = ai_scheduler.schedule(requests, head)
        else:
            messagebox.showerror("Error", "Invalid Algorithm Selected")
            return

        # Display results
        label_result.config(text=f"Total Seek Time: {total_seek}")
        plot_results(seek_sequence, algorithm, frame_graph)

    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers separated by commas.")

# GUI Setup
root = tk.Tk()
root.title("AI-Based Disk Scheduling Simulator")
root.geometry("600x500")

frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(pady=20)

tk.Label(frame_input, text="Disk Requests (comma-separated):").grid(row=0, column=0)
entry_requests = tk.Entry(frame_input, width=30)
entry_requests.grid(row=0, column=1)

tk.Label(frame_input, text="Initial Head Position:").grid(row=1, column=0)
entry_head = tk.Entry(frame_input, width=10)
entry_head.grid(row=1, column=1)

tk.Label(frame_input, text="Algorithm:").grid(row=2, column=0)
combo_algorithm = ttk.Combobox(frame_input, values=["FCFS", "SSTF", "SCAN", "AI-Based"])
combo_algorithm.grid(row=2, column=1)
combo_algorithm.set("FCFS")

btn_run = tk.Button(root, text="Run Algorithm", command=run_algorithm)
btn_run.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack()

frame_graph = tk.Frame(root)
frame_graph.pack()

root.mainloop()
