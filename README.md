# openai API Chatbot
####
## Task Description:-
#### 
Write Python or Node.js code that uses the OpenAI API to take input from the user and display the response.
#### 
## Step-By-Step:-
1- Importing the OpenAI Library:
```
from openai import OpenAI
```
#### 
This line imports the OpenAI class from the openai library, which is used to interact with the OpenAI API.
#### 
2- Initializing the OpenAI Client:
```
openai = OpenAI(
    api_key='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'
)
```
####
- Here, an instance of the OpenAI class is created and assigned to the variable openai.
- The api_key parameter is used to authenticate your requests to the OpenAI API, allowing you to access the model's capabilities.
####
3-  Initializing the Conversation:
```
conversation = []
```
#### 
This line initializes an empty list called conversation, which will store the messages exchanged between the user and the chatbot during the conversation.
#### 
4- Defining the Function to Get GPT Responses:
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
- Function Definition (def get_gpt_response(user_input):)
- Creating the User Message (message = { ... })
- Appending the Message to Conversation (conversation.append(message))
- Making the API Call (response = openai.chat.completions.create(...))
- Appending the Model’s Response to Conversation
- Returning the Model’s Response (return response.choices[0].message.content)
####
5- 
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
- Function Definition (def chat():)
- Input Loop (while True:)
- User Input (user_input = input("You: "))
- Exit Condition (if user_input == 'exit':)
- Get and Print Response (response = get_gpt_response(user_input))
#### 
6- Running the Chat Function:
```
if __name__ == "__main__":
    chat()
```
####
- This block ensures that the chat function runs when the script is executed directly (not when imported as a module in another script).
#### 
## References:
#### 
[Python Chatbot Tutorial | Using OpenAI API to Create a Smart Chatbot](https://youtu.be/w55C8cLWz74?si=S5BuYAL5wTckqU9r)
#### 
