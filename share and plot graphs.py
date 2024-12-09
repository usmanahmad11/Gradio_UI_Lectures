import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def plot_sine(frequency):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(frequency * x)
    plt.figure()
    plt.plot(x, y)
    return plt

# Create the interface
interface = gr.Interface(fn=plot_sine, inputs=gr.Slider(1, 10, step=1, label="Frequency"), outputs="plot")

# Launch the interface
interface.launch()
