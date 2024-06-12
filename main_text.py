import google.generativeai as genai
import pathlib
import textwrap
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#for m in genai.list_models():
 #   print(m)

model=genai.GenerativeModel('gemini-pro')

response=model.generate_content('what is the ML')
print(response.text)