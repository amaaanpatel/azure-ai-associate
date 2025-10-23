import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from openai import AzureOpenAI


def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Load environment variables from .env file
        load_dotenv()
        project_endpoint = os.getenv("AZURE_PROJECT_ENDPOINT")
        model_deployment = os.getenv("AZURE_MODEL_DEPLOYMENT")

        # Initialize the project client
        project_client = AIProjectClient(
            credential=DefaultAzureCredential(
                exclude_environment_credential=True,
                exclude_managed_identity_credential=True
            ),
            endpoint=project_endpoint,
        )
        # Get a chat client
        openai_client = project_client.get_openai_client(api_version="2024-10-21")


        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]

        while True:
            input_text = input("Enter your question (or type 'exit' to quit): ")
            if input_text.lower() == 'exit':
                print("Exiting the chat. Goodbye!")
                break   
            if len(input_text) == 0:
                print("Please enter a valid question.")
                continue

            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = openai_client.chat.completions.create(
                model=model_deployment,
                messages=prompt
            )
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your environment variables and ensure the Azure AI Project is set up correctly.")


if __name__ == "__main__":
    main()