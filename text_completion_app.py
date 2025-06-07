import openai
# this is a simple chat interface for OpenAI's GPT-3.5 model, which allows me to experiment with the model and see how it responds to different prompts.


# Replace with your actual OpenAI API key
OPENAI_API_KEY = "Key-Removed-For-Security"

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for an extern student looking to try you out."}, # provide a system message to set the context   
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# this is a main function to run the chat interface, where the user can input text and get responses from ChatGPT while
# the program is running in a loop until the user types 'exit', and while we still have the OpenAI API key set up with sufficient tokens.
def main():
    openai.api_key = OPENAI_API_KEY
    print("ChatGPT 3.5 Interface. Type 'exit' to quit.")

    # while the user can input text, we will keep the program running
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = chat_with_gpt(user_input)
        print("ChatGPT:", reply)

if __name__ == "__main__":
    main()