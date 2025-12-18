import re
from urllib.parse import urlparse

def extract_urls(text):
    return re.findall(r'https?://\S+|www\.\S+', text)

def is_suspicious_url(url):
    if len(url) > 75:
        return True
    if "@" in url or "-" in url:
        return True
    if urlparse(url).scheme != "https":
        return True
    return False
