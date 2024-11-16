import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {api_key}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def answer_question():
    st.title('🌠 Test Hugging Face QA Model')

    quest = st.text_input(' Ask something.')

    if quest:
        payload = {
            "inputs": quest
        }

        output = query(payload)
        if "error" in output:
            st.error(f"Error: {output['error']}")
        else:
            if isinstance(output, list) and len(output) > 0:
                first_item = output[0]
                if isinstance(first_item, dict) and 'generated_text' in first_item:
                    answer = first_item['generated_text']
                else:
                    answer = 'No answer found in the expected format.'
            else:
                answer = 'No output received from the model.'

            st.markdown(f"**Answer to your question:** {answer}")


if __name__ == "__main__":
    answer_question()
