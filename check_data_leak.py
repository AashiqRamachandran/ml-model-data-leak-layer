import re


def check_stream_for_leaks(stream, patterns):
    """
    Checks a stream (text) against a list of regex patterns to identify potential data leakage.

    :param stream: The stream (string) to be checked.
    :param patterns: A list of regex patterns to check against the stream.
    :return: A dictionary with pattern as key and list of matches as values.
    """
    leaks_detected = {}
    for pattern in patterns:
        matches = re.findall(pattern, stream)
        if matches:
            leaks_detected[pattern] = matches
    return leaks_detected


def main():
    # Example patterns to detect email, phone numbers, and credit card numbers.
    # Note: These patterns are simplified and should be refined for production use.
    patterns = [
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email pattern
        r'\b(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\b',  # Phone pattern
        r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'  # Simplified credit card pattern
    ]

    # Example stream (Replace or extend this with your actual stream content)
    example_stream = """Contact me at example@example.com for details.
                        Also, my phone number is 123-456-7890. Don't share my credit
                        card number 1234-5678-9012-3456 with anyone."""

    leaks = check_stream_for_leaks(example_stream, patterns)

    if leaks:
        print("Potential data leakage detected!")
        for pattern, matches in leaks.items():
            print(f"Pattern: {pattern}\nMatches found: {matches}\n")
    else:
        print("No data leakage detected.")


if __name__ == '__main__':
    main()