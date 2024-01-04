import tkinter as tk
from tkinter import ttk
from scipy.optimize import minimize
import numpy as np
import time

def objective(x, d1, d2, d3, d4):
    p1, p2 = x
    g = [1 / (10 ** (10 * np.log10(24 * np.pi * d))) for d in (d1, d2, d3, d4)]
    sinr1 = (p1 * g[0]) / (p2 * g[2] + 10 ** (-11.8))
    sinr2 = (p2 * g[1]) / (p1 * g[3] + 10 ** (-11.8))
    return -(sinr1 + sinr2)  # to maximize, minimize the negative

def optimize_sinr():
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Starting optimization...\n")
    result_text.update_idletasks()

    d_values = [float(entry.get()) for entry in entries[:-1]]
    if len(d_values) != 4:
        result_text.insert(tk.END, "Error: Please provide exactly four values for d1, d2, d3, and d4\n")
        return
    d1, d2, d3, d4 = d_values

    num_guesses = int(entries[-1].get())

    bounds = [(0, 1), (0, 1)]
    np.random.seed(0)

    start_time = time.time()  
    max_sinr_sum = -np.inf
    best_p1, best_p2 = None, None

    progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=100, mode='determinate', style='green.Horizontal.TProgressbar')
    progress_bar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    for count, _ in enumerate(range(num_guesses), 1):
        x0 = np.random.uniform(0, 1, size=2)  
        result = minimize(lambda x: objective(x, d1, d2, d3, d4), x0=x0, bounds=bounds, method='SLSQP')

        if result.success:
            p1, p2 = result.x
            g = [1 / (10 ** (10 * np.log10(24 * np.pi * d))) for d in (d1, d2, d3, d4)]
            sinr1 = (p1 * g[0]) / (p2 * g[2] + 10 ** (-11.8))
            sinr2 = (p2 * g[1]) / (p1 * g[3] + 10 ** (-11.8))
            sinr_sum = sinr1 + sinr2
            if sinr_sum > max_sinr_sum:
                max_sinr_sum = sinr_sum
                best_p1, best_p2 = p1, p2

        progress_bar['value'] = count * 100 / num_guesses
        root.update_idletasks()

    end_time = time.time()  
    display_results(max_sinr_sum, best_p1, best_p2, end_time - start_time)
    progress_bar.grid_forget()

def display_results(max_sinr_sum, best_p1, best_p2, time_elapsed):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Results:\n\n")
    result_text.insert(tk.END, f"Max SINR Sum: {max_sinr_sum}\n")
    result_text.insert(tk.END, f"Best p1: {best_p1}\n")
    result_text.insert(tk.END, f"Best p2: {best_p2}\n")
    result_text.insert(tk.END, f"Time Elapsed: {time_elapsed} seconds\n")

def display_copyright():
    copyright_text = (
        "© 2023 Aayam Raj Shakya.\n\n"
        "github.com/aayamrajshakya/SINR_optimization"
    )
    copyright_label = tk.Label(root, text=copyright_text, fg = "blue")
    copyright_label.grid(row=2, column=1, padx=10, pady=10)

root = tk.Tk()
root.title("SINR Optimization")
root.attributes('-zoomed', True)

inputs_frame = tk.Frame(root)
inputs_frame.grid(row=0, column=0, padx=10, pady=10)

labels = ["d1:", "d2:", "d3:", "d4:", "Iterations:"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(inputs_frame, text=label_text)
    label.grid(row=i, column=0)

    entry = tk.Entry(inputs_frame)
    entry.grid(row=i, column=1)
    entries.append(entry)

style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

optimize_button = tk.Button(root, text="Optimize SINR", command=optimize_sinr)
optimize_button.grid(row=1, column=0, padx=10, pady=10)

result_text = tk.Text(root, height=15, width=50)
result_text.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

display_copyright()

root.mainloop()
