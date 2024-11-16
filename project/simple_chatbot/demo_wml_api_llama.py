import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key = os.getenv("api_key")
client = InferenceClient(api_key=api_key)


def answer_questions():
    st.title('🌠 Test Hugging Face QA Model')

    user_question = st.text_input('Ask a question, for example: What is IBM?')

    if user_question:
        messages = [
            {
                "role": "user",
                "content": user_question
            }
        ]

        output = generate_text(messages)

        if "error" in output:
            st.error(f"Error: {output['error']}")
        else:
            answer = output
            st.markdown(f"**Answer to your question:** {answer}")




def generate_text(messages):
    stream = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True
    )

    response_text = ""
    for chunk in stream:
        response_text += chunk.choices[0].delta.content
    return response_text


answer_questions()
