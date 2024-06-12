import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

#for m in genai.list_models():
 #   print(m)
img=PIL.Image.open('car.jpg')
#print(img.show())
model=genai.GenerativeModel('gemini-pro-vision')
response=model.generate_content(['generate description with only 50 words and give as points',img])
print(response.text)
