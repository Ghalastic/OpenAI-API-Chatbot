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
