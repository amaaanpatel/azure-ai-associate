from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def authenticate_client():
    key = "1788mIQ4Uf1P14BBJPefguhvXzxNxxEd3XgQoH2zuhDLlDxV4Dq3JQQJ99BJACYeBjFXJ3w3AAAaACOGpR6h"
    endpoint = "https://amaanailanguage.cognitiveservices.azure.com/"
    return TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )


def sentiment_analysis(client):
    # Prompt the user to enter text for analysis
    try:
        user_input = input("Enter text for sentiment analysis: ")
        # Analyze the sentiment of the input text
        response = client.analyze_sentiment(documents=[user_input])[0]
        print("Sentiment Analysis Result:")
        print("Overall Sentiment:", response.sentiment)
        print(
            "Scores: positive={0:.2f}; "
            "neutral={1:.2f}; "
            "negative={2:.2f}".format(
                response.confidence_scores.positive,
                response.confidence_scores.neutral,
                response.confidence_scores.negative,
            ))
    except Exception as e:
        print(f"An error occurred: {e}")
        return


def main():
    client = authenticate_client()
    sentiment_analysis(client)

if __name__ == "__main__":
    main()
# End of file: azure_engineer/analysis.py