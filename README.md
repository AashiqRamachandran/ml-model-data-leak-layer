# Layer For Detecting LLM Inference PII Leakage
## Introduction

This project introduces a robust layer designed to be placed in front of your machine learning (ML) model inference endpoints. Its primary function is to scan for potential leaks of Personally Identifiable Information (PII) as the model generates content. This is particularly crucial for projects utilizing Large Language Models (LLMs), which, due to their extensive training data, might inadvertently generate sensitive information.

## What are LLMs?
Large Language Models (LLMs) like GPT (Generative Pre-trained Transformer) and BERT (Bidirectional Encoder Representations from Transformers) are advanced AI models capable of understanding and generating human-like text. They are trained on vast datasets from the internet, enabling them to perform a wide range of language tasks, from translation and summarization to question-answering and content generation.

## What Does Leaking Data Mean in the Context of LLMs?
Data leakage in the context of LLMs refers to the models generating output that includes sensitive or personal information. This can happen when the models, trained on large datasets containing real-world information, reproduce patterns or data points that should be confidential. Such leaks can pose significant privacy risks, especially when the models are used in applications that handle user data.

## How This Project Works
The project employs a two-pronged approach to detect potential data leaks:

1. ML Model Scanning: It uses a core credential scanner (core_credential_scanner_main) that leverages machine learning techniques to analyze the text generated by LLMs for potential PII leaks.

2. Regex Pattern Matching: Alongside ML-based scanning, the project uses regular expressions (regex) to identify common patterns of sensitive information like email addresses, phone numbers, and credit card numbers in the generated text.

The process begins with fetching a response from a specified Hugging Face model using the fetch_response_from_huggingface function. The response is then scanned for data leaks using both the ML model and regex patterns. The system flags any detected leaks, providing a comprehensive layer of protection against inadvertent data exposure.

## Installation Guide
To set up this project, follow these steps:

1. Clone the Repository: First, clone the repository to your local machine using Git:
```
git clone https://github.com/AashiqRamachandran/ml-model-data-leak-layer.git
```
2. Install Dependencies: Navigate to the project directory and install the required Python packages:
```
cd ml-model-data-leak-layer
pip install -r requirements.txt
```
3. Set Up Environment Variables: For the Hugging Face API key, it's recommended to use an environment variable for security reasons. You can set this up in your shell or use a .env file with a library like python-dotenv.

## Usage Examples
Here are some examples of how to use this project:

- Scanning Text for Data Leaks:
After setting up the project, you can run the entrypoint.py script to scan text generated by a Hugging Face model. You'll be prompted to enter the text, the model name, and your Hugging Face API key.

- Integrating with Other LLMs:
While the provided example uses a Hugging Face model, you can modify the fetch_response_from_huggingface function to work with other LLMs. Adjust the API endpoint and request format according to the documentation of the LLM you're using.
Security Practices
When dealing with sensitive data, especially PII, it's crucial to follow best security practices:

- Use Environment Variables: Store sensitive information like API keys in environment variables instead of hardcoding them into your scripts.

- Regularly Update Dependencies: Keep all dependencies up to date to avoid security vulnerabilities.

- Limit Access: If you're deploying this project, ensure that access is limited to authorized users only, using authentication and authorization mechanisms.

- Review Regular Expressions: Regularly review and update the regex patterns to cover new forms of PII that might be leaked.

## FAQs

Q: Can this project guarantee the detection of all data leaks?
A: While this project significantly enhances the detection of potential data leaks, no system can guarantee 100% detection due to the complexity and evolving nature of language and data.

Q: Is it possible to use this project with any LLM?
A: Yes, with some modifications to the API calls, you can adapt this project to work with various LLMs. The core functionality of scanning for data leaks remains applicable across different models.

Q: How can I contribute if I'm not a programmer?
A: Contributions aren't limited to code. You can help by improving documentation, reporting bugs, suggesting features, or even spreading the word about the project.

Q: What should I do if I find a bug?
A: If you encounter a bug, please open an issue on the project's GitHub repository with a detailed description of the bug and, if possible, steps to reproduce it.

This project aims to foster a safer environment for using LLMs by providing tools to detect and mitigate unintended data leaks. Your feedback, contributions, and questions are invaluable to achieving this goal.

## References & Credits
- Hugging Face Models: Hugging Face Model Hub
- Regular Expressions (Regex): Regex101
- Credsweeper
- OctoPII

## Contributing
Contributions to this project are welcome! Whether you're looking to fix bugs, enhance the functionality, or improve the documentation, your input is valuable. Here's how you can contribute:

1. Fork the Repository: Start by forking the project repository to your GitHub account.

2. Create a New Branch: Make your changes in a new git branch based on the main branch.

3. Submit a Pull Request: Once you've made your changes, submit a pull request for review.

4. Code Review: Your pull request will be reviewed, and suggestions for improvements may be given.

5. Merge: After approval, your changes will be merged into the main project.

For more detailed instructions, please refer to the project's CONTRIBUTING.md file.
