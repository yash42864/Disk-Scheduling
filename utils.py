# utils.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_results(seek_sequence, algorithm, frame):
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(seek_sequence, range(len(seek_sequence)), marker='o', linestyle='-', color='b')
    ax.set_xlabel("Cylinder Number")
    ax.set_ylabel("Order of Access")
    ax.set_title(f"{algorithm} Disk Scheduling")
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
