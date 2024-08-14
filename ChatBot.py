from openai import OpenAI

openai = OpenAI(
    api_key='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'
)

conversation = []

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

def chat():
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            print("Chatbot: Goodbye! I hope You learned a lot from me today! Have a nice day.")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
