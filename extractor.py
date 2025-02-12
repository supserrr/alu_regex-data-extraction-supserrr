import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

def extract_urls(text):
    url_pattern = r'https?://[^\s]+'
    return re.findall(url_pattern, text)

def extract_phone_numbers(text):
    phone_pattern = r'\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(phone_pattern, text)

def extract_credit_card_numbers(text):
    credit_card_pattern = r'\b(?:\d{4}[\s-]){3}\d{4}\b'
    return re.findall(credit_card_pattern, text)

def extract_times(text):
    time_pattern = r'\b(?:\d{1,2}:\d{2}(?:\s?[APap][Mm])?|\d{2}:\d{2})\b'
    return re.findall(time_pattern, text)

def extract_html_tags(text):
    html_tag_pattern = r'<[^>]+>'
    return re.findall(html_tag_pattern, text)

def extract_hashtags(text):
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

def extract_currency_amounts(text):
    currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(currency_pattern, text)

if __name__ == "__main__":
    with open('data/sample_data.txt', 'r') as file:
        sample_text = file.read()

    print("Extracted Emails:", extract_emails(sample_text))
    print("Extracted URLs:", extract_urls(sample_text))
    print("Extracted Phone Numbers:", extract_phone_numbers(sample_text))
    print("Extracted Credit Card Numbers:", extract_credit_card_numbers(sample_text))
    print("Extracted Times:", extract_times(sample_text))
    print("Extracted HTML Tags:", extract_html_tags(sample_text))
    print("Extracted Hashtags:", extract_hashtags(sample_text))
    print("Extracted Currency Amounts:", extract_currency_amounts(sample_text))