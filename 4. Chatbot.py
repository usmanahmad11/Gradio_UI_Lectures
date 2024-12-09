import gradio as gr

def chatbot_response(message):
    return f"Bot: You said '{message}'. How can I help you further?"

# Create the interface
interface = gr.Interface(fn=chatbot_response, inputs="text", outputs="text")

# Launch the interface
interface.launch()
