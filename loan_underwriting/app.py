import os
import gradio as gr
from typing import List, Dict, Optional
from dotenv import load_dotenv

from loan_underwriting.week1.factory import Week1Mode, create_chat_implementation

# Load environment variables
load_dotenv()

def create_demo(mode_str: str = "part1"):
    """Create and return a Gradio demo with chat and file upload."""
    
    # Map string to mode enum
    mode_map = {
        "part1": Week1Mode.PART1_QUERY_UNDERSTANDING,
        "part2": Week1Mode.PART2_BASIC_TOOLS,
        "part3": Week1Mode.PART3_MEMORY
    }

    if mode_str not in mode_map:
        raise ValueError(f"Unknown mode: {mode_str}. Choose from: {list(mode_map.keys())}")
    
    mode = mode_map[mode_str]

    # Initialize chat implementation
    chat_interface = create_chat_implementation(mode)
    chat_interface.initialize()

    # Helper: process uploaded files
    def process_files(files: List) -> str:
        file_contents = []
        for file in files or []:
            try:
                if file.name.lower().endswith(".txt"):
                    content = file.read().decode("utf-8")
                    file_contents.append(f"File: {file.name}\nContent:\n{content}")
                else:
                    file_contents.append(f"File: {file.name} (content extraction not implemented)")
            except Exception as e:
                file_contents.append(f"Error reading {file.name}: {str(e)}")
        return "\n\n".join(file_contents)

    # Actual response logic
    def respond(message: str, history: List[Dict[str, str]], files: Optional[List] = None) -> str:
        tuple_history = []
        i = 0
        while i < len(history):
            user_msg = history[i]["content"] if history[i]["role"] == "user" else ""
            assistant_msg = ""
            if i + 1 < len(history) and history[i+1]["role"] == "assistant":
                assistant_msg = history[i+1]["content"]
                i += 2
            else:
                i += 1
            if user_msg:
                tuple_history.append((user_msg, assistant_msg))
        
        if files:
            file_context = process_files(files)
            if file_context:
                message = f"Document Context:\n{file_context}\n\nUser Question: {message}"
        
        return chat_interface.process_message(message, tuple_history)

    # UI titles
    titles = {
        "part1": "Loan Underwriting Agent - Query Understanding",
        "part2": "Loan Underwriting Agent - Basic Tools",
        "part3": "Loan Underwriting Agent - Memory"
    }

    descriptions = {
        "part1": "Your intelligent loan underwriting assistant that can understand different types of questions and format responses accordingly. Upload loan documents to provide context.",
        "part2": "Your intelligent loan underwriting assistant that can answer questions, perform calculations, and format responses. Upload loan documents to provide context.",
        "part3": "Your intelligent loan underwriting assistant that can answer questions, perform calculations, and maintain conversation context. Upload loan documents to provide context."
    }

    # Build UI using Blocks
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(f"# {titles[mode_str]}")
        gr.Markdown(descriptions[mode_str])

        file_upload = gr.File(
            label="Upload loan documents",
            file_count="multiple",
            file_types=[
                "text/plain",
                "application/pdf",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "application/msword"
            ],
            height=160
        )

        chat = gr.ChatInterface(
            fn=None,  # We'll override below
            type="messages",
            examples=[
                ["What is the debt-to-income ratio for this loan application?"],
                ["Compare the applicant's income vs expenses"],
                ["Calculate the monthly mortgage payment for a $300,000 loan at 4.5% interest"],
                ["What are the key risk factors in this application?"]
            ],
            title=titles[mode_str],
            description=descriptions[mode_str]
        )

        # Wrap the chat function to inject uploaded files
        def wrapped_respond(message, history):
            files = file_upload.value
            return respond(message, history, files)

        chat.fn = wrapped_respond

    return demo
