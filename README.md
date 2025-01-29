## Prerequisites
1. Registered account on Hugging Face and created your own API key.
![Screenshot 2025-01-29 185630](https://github.com/user-attachments/assets/0823e2da-31e7-4fa1-9629-db1ebd632fc3)
2. Streamlit.io for deployment
3. Python > 3.7 installed on your system.
4. Required Python libraries:
   - requests
   - streamlit
   - python-dotenv
   - huggingface-hub

## Steps
1. Obtain API Key from Hugging Face
- Sign up or log in to your account on [Hugging Face](https://huggingface.co/).
- Navigate to the API Token section in your account settings and generate a new token.
- Copy the token for future reference.

2. Set Up Environment
Create a __.env__ file in your project directory and add your API key:
```python
api_key=YOUR_API_KEY_HERE
```
Replace YOUR_API_KEY_HERE with the actual key.

3. Install Dependencies
```python
pip install requests streamlit python-dotenv
```

4. Run the Streamlit App
To run the app, open a terminal, navigate to your project directory, and execute:
```python
streamlit run your_script.py
```

[Video demo](https://drive.google.com/file/d/1DxHd8e8eQGNn-N7UArtCqcS4GwPmTU7n/view?usp=sharing)
