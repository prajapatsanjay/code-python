
# ## Interactive chat session with Gemini-2.5-flash model ##

from google import genai
#from google.genai import types
import os # Import os to check env variables

# The client automatically uses the API key from your environment variable
client = genai.Client()

# Create a chat session using the client
chat = client.chats.create(
    model='gemini-2.5-flash',  # Specify the chat model
    history=[]

)
print("chat session started. type 'quit' or 'exit' to end the session.")
while True:
    user_input = input("You: ")
    
    # Check for exit conditions
    if user_input.lower() in ["quit", "exit"]:
        print("Chat session ended.")
        break # Exit the while loop

    # Send message and get response
    response = chat.send_message(user_input)
    
    print(f"AI: {response.text}")





## image understanding with gemini-2.5-flash ##


from google import genai
from google.genai import types


client = genai.Client()
Uploaded_file = client.files.upload(file="cat.jpg")

# Create a chat session using the client
resopnse = client.models.generate_content(
    model='gemini-2.5-flash',  # Specify the chat model"
    contents=["what do you see in this image?", Uploaded_file],
    # config=types.GenerationConfig(
    #     Syntem_instructions="you are a rude teacher",
    #     max_output_tokens=1024,

)
print(resopnse.text)









