import gradio as gr

conversation_history = []

def process_text(input_text):
    global conversation_history
    conversation_history.append({"role": "user", "content": input_text})
    
    # Simulate an AI response (replace this with actual AI integration later)
    assistant_response = f"This is a simulated response to: {input_text}"
    conversation_history.append({"role": "assistant", "content": assistant_response})
    
    return gr.update(value=format_conversation(conversation_history))

def clear_conversation():
    global conversation_history
    conversation_history = []
    return ""

def format_conversation(history):
    formatted = ""
    for message in history:
        if message["role"] == "user":
            formatted += f"{message['content']}\n\n"
        else:
            formatted += f"    {message['content']}\n\n"
    return formatted.strip()

# Define the Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# Deep-Learning Plugins")
    gr.Markdown("Enter your message and click submit to get a response. Click clear to start a new conversation.")
    
    chat_interface = gr.Textbox(label="Chat", lines=10, interactive=False)
    input_text = gr.Textbox(label="Your Message")
    
    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")
    
    submit_btn.click(fn=process_text, inputs=input_text, outputs=chat_interface)
    clear_btn.click(fn=clear_conversation, outputs=chat_interface)

# Launch the interface
iface.launch()
