# Creating a Chatbot using OpenAI API 
####
## Task Description:-
#### 
Write Python or Node.js code that uses the OpenAI API to take input from the user and display the response.
#### 
### Programming Language Used:
#### 
Python
#### 
### Duration:
#### 
1 Day
#### 
## Building the Code, Step by Step:-
#### 
### 1- Import the OpenAI Library:
#### 
```
from openai import OpenAI
```
#### 
This line imports the 'OpenAI' class from the 'openai' library, which is used to interact with the OpenAI API.
#### 
### 2- Initialize the OpenAI Client:
####
```
openai = OpenAI(
    api_key='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'
)
```
####
- The 'api_key' parameter is used to authenticate your requests to the OpenAI API, allowing you to access the model's capabilities.
####
### 3- Initialize the Conversation:
#### 
```
conversation = []
```
#### 
This line initializes an empty list called 'conversation', which will store the messages exchanged between the user and the chatbot during the conversation.
#### 
### 4- Define the Function to Get GPT Responses:
#### 
```
def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    conversation.append(message)

    response = openai.chat.completions.create(
        messages = conversation,
        model = "gpt-3.5-turbo"
    )

    conversation.append(response.choices[0].message)

    return response.choices[0].message.content
```
#### 
- Function Definition ('def get_gpt_response(user_input):'): This function takes 'user_input' as a parameter, which is the text that the user enters during the conversation.  
- Creating the User Message ('message = { ... }'): A dictionary 'message' is created, where:    
'"role": "user"' specifies that this message is from the user.     
'"content": user_input' stores the actual text input from the user.       
- Appending the Message to Conversation ('conversation.append(message)'): The user’s message is added to the 'conversation' list, preserving the sequence of the dialogue.  
- Making the API Call ('response = openai.chat.completions.create(...)'):   
The 'create' method is called on 'openai.chat.completions' to generate a response from the OpenAI model.   
'messages=conversation' sends the entire conversation history (including the current user input) to the model so it can generate a context-aware response.   
'model="gpt-3.5-turbo"' specifies which version of the GPT model to use for generating the response.      
- Appending the Model’s Response to Conversation: The model's response, which is the first choice ('choices[0].message'), is added to the 'conversation' list.  
- Returning the Model’s Response ('return response.choices[0].message.content'): The content of the model’s response is returned so it can be printed or further processed.  
####
### 5- Defining the Chat Function:
#### 
```
def chat():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye! I hope You learned a lot from me today! Have a nice day.")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")
```
#### 
- Function Definition ('def chat():'): This function initiates a continuous chat loop where the user can input text and receive responses.
- Input Loop ('while True:'): A loop that runs indefinitely until the user decides to exit the chat.
- User Input ('user_input = input("You: ")'): The user is prompted to input text, which is stored in the variable 'user_input'.
- Exit Condition ('if user_input == 'exit':'): If the user types '"exit"', the chatbot responds with a goodbye message, and the loop breaks, ending the chat session.
- Get and Print Response ('response = get_gpt_response(user_input)'): The user's input is passed to 'get_gpt_response', and the returned response is printed to the console.
#### 
### 6- Running the Chat Function:
#### 
```
if __name__ == "__main__":
    chat()
```
####
- This block ensures that the 'chat' function runs when the script is executed directly (not when imported as a module in another script).
#### 
## References:
#### 
[Python Chatbot Tutorial | Using OpenAI API to Create a Smart Chatbot](https://youtu.be/w55C8cLWz74?si=S5BuYAL5wTckqU9r)
#### 
## Illustrations:-
#### 
![‏‏لقطة الشاشة (2405)](https://github.com/user-attachments/assets/12c8ae3a-d6c6-40ca-a419-582062f000bf)
#### 
![‏‏لقطة الشاشة (2400)](https://github.com/user-attachments/assets/82d247e9-f358-4426-bb88-38039d2507fd)
####
