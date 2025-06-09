import re

# List of common spam keywords
spam_keywords = ['congratulations', 'winner', 'free', 'prize', 'claim', 'urgent', 'click here']

# List of fake or suspicious domains
suspicious_domains = ['bit.ly', 'tinyurl.com', 'freemoney.com', 'winbig.net']

def is_phishing(email_text):
    lower_text = email_text.lower()

    # Check for spam keywords
    keyword_matches = [word for word in spam_keywords if word in lower_text]

    # Check for suspicious domains
    domain_matches = [domain for domain in suspicious_domains if domain in lower_text]

    # Check for links
    links = re.findall(r'http[s]?://\S+', email_text)

    # Evaluation
    if keyword_matches or domain_matches or links:
        print("⚠️ Suspicious Email Detected!")
        if keyword_matches:
            print(f"• Spammy words found: {', '.join(keyword_matches)}")
        if domain_matches:
            print(f"• Suspicious domains: {', '.join(domain_matches)}")
        if links:
            print(f"• Links found: {', '.join(links)}")
    else:
        print("✅ Email seems safe.")

# Test
if __name__ == "__main__":
    sample_email = input("Paste your email content:\n")
    is_phishing(sample_email)
