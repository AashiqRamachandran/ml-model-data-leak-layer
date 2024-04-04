import requests
from check_data_leak import check_stream_for_leaks
from main import lambda_handler as core_credential_scanner_main

patterns = [
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email pattern
        r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b',  # Phone pattern
        r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'  # Simplified credit card pattern
    ]
def fetch_response_from_huggingface(
        huggingface_api_key,
        model="TensaZangetsu/condensed-bert-vulnerable",
        payload={"inputs": "The quick brown fox jumps over the lazy dog."}
):
    """
    Fetch a response from a specific Hugging Face model.

    :param model: The model ID on Hugging Face.
    :param payload: The inputs required by the model.
    :return: The model's response text.
    """
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    headers = {
        "Authorization": f"Bearer {huggingface_api_key}"}

    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    # Assuming the response contains a 'generated_text' field. Update according to actual response structure.
    return result[0].get('generated_text', '')


def main():
    # Fetch model response
    initial_text_for_model = input("Enter the text to be sent to the model: ")
    model = input("Enter the model name from huggingface (Eg - TensaZangetsu/condensed-bert-vulnerable): ")
    huggingface_api_key = input("Enter the huggingface api key: ")
    model_response = fetch_response_from_huggingface(
        huggingface_api_key,
        model,
        {"inputs": initial_text_for_model}
    )
    print("Model response:", model_response)
    print("Scanning with ML model...")

    # Check the response for data leaks
    leaks = core_credential_scanner_main(
        model_response
    )

    # Check the response for data leaks using regex patterns
    print("Scanning with regex patterns... Regex pattern count: ", len(patterns))
    regex_matches = check_stream_for_leaks(
        str(check_stream_for_leaks),patterns
    )

    if leaks:
        print("Potential data leakage detected in Hugging Face API response powered by ML!")
        for pattern, matches in leaks.items():
            print(f"Pattern: {pattern}\nMatches found: {matches}\n")
    else:
        print("No data leakage detected in Hugging Face API response via ML.")

    if regex_matches:
        print("Potential data leakage detected in Hugging Face API response powered by rules!")
        for pattern, matches in regex_matches.items():
            print(f"Pattern: {pattern}\nMatches found: {matches}\n")
    else:
        print("No data leakage detected in Hugging Face API response via rules.")


if __name__ == "__main__":
    main()
