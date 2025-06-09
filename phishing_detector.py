import re

# Spam keywords and suspicious domains
spam_keywords = ['congratulations', 'winner', 'free', 'prize', 'claim', 'urgent', 'click here']
suspicious_domains = ['bit.ly', 'tinyurl.com', 'freemoney.com', 'winbig.net']

def is_phishing(email_text):
    lower_text = email_text.lower()

    # Detect spam keywords and domains
    keyword_matches = [word for word in spam_keywords if word in lower_text]
    domain_matches = [domain for domain in suspicious_domains if domain in lower_text]
    links = re.findall(r'http[s]?://\S+', email_text)

    print("\n" + "="*50)
    print("🛡️  EMAIL PHISHING DETECTOR REPORT  🛡️")
    print("="*50)
    print(f"\n📧 Email Preview:\n\"{email_text[:120]}{'...' if len(email_text) > 120 else ''}\"\n")
    
    # Summary counters
    total_flags = len(keyword_matches) + len(domain_matches) + len(links)

    if total_flags == 0:
        print("✅ No phishing indicators detected! This email looks safe. 🎉\n")
        print("🔒 Keep being cautious, but no immediate red flags found.")
    else:
        print(f"🚨 ALERT: Potential phishing indicators detected! ({total_flags} found)\n")

        if keyword_matches:
            print("🔍 Spammy Keywords Found:")
            for kw in keyword_matches:
                print(f"  • {kw}")

        if domain_matches:
            print("\n🌐 Suspicious Domains Found:")
            for domain in domain_matches:
                print(f"  • {domain}")

        if links:
            print("\n🔗 Suspicious Links Found:")
            for link in links:
                print(f"  • {link}")

        print("\n⚠️ Advice:")
        print("  • Avoid clicking on suspicious links.")
        print("  • Do not share personal or financial info.")
        print("  • Verify sender's email address.")
        print("  • When in doubt, delete the email.\n")

        print("🔔 Stay safe online! Always verify before you trust.\n")

    print("="*50 + "\n")

if __name__ == "__main__":
    sample_email = """Congratulations! You've won a free prize. Click here: http://bit.ly/winbig"""
    is_phishing(sample_email)
