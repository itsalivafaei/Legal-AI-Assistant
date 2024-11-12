import gradio as gr

def pain_ui(process_input):
    # Build the Gradio Interface
    inputs = [
        gr.Textbox(lines=2, label="Type your question here..."),
        gr.Audio(sources=["microphone", "upload"], type="filepath", label="Audio Input")
    ]

    outputs = [
        gr.Textbox(label="Chatbot Response"),
        gr.Audio(label="Assistant's Response", type="filepath")
    ]

    interface = gr.Interface(
        fn=process_input,
        inputs=inputs,
        outputs=outputs,
        title="Domain-Specific Q&A Chatbot",
        description="Ask questions related to legal issues."
    )

    interface.launch(debug=True)