import re

# List of common spam keywords
spam_keywords = ['congratulations', 'winner', 'free', 'prize', 'claim', 'urgent', 'click here']

# List of suspicious domains
suspicious_domains = ['bit.ly', 'tinyurl.com', 'freemoney.com', 'winbig.net']

def is_phishing(email_text):
    lower_text = email_text.lower()

    # Check for spam keywords
    keyword_matches = [word for word in spam_keywords if word in lower_text]

    # Check for suspicious domains
    domain_matches = [domain for domain in suspicious_domains if domain in lower_text]

    # Find all links
    links = re.findall(r'http[s]?://\S+', email_text)

    print("\n" + "="*50)
    print("🛡️  EMAIL PHISHING DETECTOR REPORT  🛡️")
    print("="*50 + "\n")

    print("📧 Email Preview:")
    print(f"\"{email_text.strip()}\"\n")

    if keyword_matches or domain_matches or links:
        total_issues = len(keyword_matches) + len(domain_matches) + len(links)
        print(f"🚨 ALERT: Potential phishing indicators detected! ({total_issues} found)\n")

        if keyword_matches:
            print("🔍 Spammy Keywords Found:")
            for kw in keyword_matches:
                print(f"  • {kw}")

        if domain_matches:
            print("\n🌐 Suspicious Domains Found:")
            for dm in domain_matches:
                print(f"  • {dm}")

        if links:
            print("\n🔗 Suspicious Links Found:")
            for link in links:
                print(f"  • {link}")

        print("\n⚠️ Advice:")
        print("  • Avoid clicking suspicious links.")
        print("  • Do not share personal or financial info.")
        print("  • Verify sender's email address.")
        print("  • When in doubt, delete the email.")
        print("\n🔔 Stay safe online! Always verify before you trust.")
    else:
        print("✅ No phishing indicators detected! This email looks safe. 🎉")

    print("\n" + "="*50 + "\n")

# Run the script
if __name__ == "__main__":
    email_content = input("Paste your email content:\n")
    is_phishing(email_content)
