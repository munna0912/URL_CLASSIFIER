import re
import pandas as pd
from urllib.parse import urlparse

# Typically, cyber attackers replace the domain name in a URL with an IP address to conceal the website's identity. This feature is designed to verify whether the URL includes an IP address or not.
def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

# check whether link is in proper formatting or not
def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        return 1
    else:
        return 0

# Phishing or malware websites often incorporate multiple sub-domains into their URLs, with each sub-domain separated by a dot (.). URLs containing more than three dots (.) are more likely to be malicious sites.
def count_dot(url):
    count_dot = url.count('.')
    return count_dot

# In general, most safe websites contain only one "www" in their URLs. This feature can aid in identifying malicious websites by detecting URLs that either lack "www" or contain more than one instance of it.
def count_www(url):
    url.count('www')
    return url.count('www')

# The occurrence of the "@" symbol in a URL causes everything preceding it to be disregarded.
def count_atrate(url): 
    return url.count('@')

# Websites that contain multiple directories within their URLs are typically considered suspicious.
def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

# Examining the frequency of the " //" sequence within a URL can aid in identifying malicious URLs with multiple embedded domains.
def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count('//')

# Malicious URLs often avoid using HTTPS protocols as they typically require user credentials and provide a layer of security for online transactions. Therefore, the presence or absence of HTTPS protocol in a URL can be a crucial indicator in determining its safety.
def count_https(url):
    return url.count('https')

# Typically, phishing or malicious websites contain multiple instances of HTTP in their URL, whereas safe websites only have one.
def count_http(url):
    return url.count('http')

# As URLs cannot contain spaces, they are often replaced with symbols (%), which is known as URL encoding. Safe websites tend to have fewer spaces in their URLs, while malicious sites often have more, resulting in a higher number of % symbols.
def count_per(url):
    return url.count('%')

# A symbol (?) in a URL indicates the presence of a query string, which contains data to be sent to the server. If a URL contains multiple instances of the symbol (?), it can be a sign of a suspicious URL.
def count_ques(url):
    return url.count('?')

# To make a URL appear genuine, phishers and cybercriminals often add dashes (-) to the prefix or suffix of a brand name. For instance, they may create a URL like www.flipkart-india.com.
def count_hyphen(url):
    return url.count('-')

# The presence of an equal sign (=) in a URL implies that variable values are being passed from one form page to another. This is considered risky since anyone can modify the values and alter the page.
def count_equal(url):
    return url.count('=')

#Length of URL
def url_length(url):
    return len(str(url))

#Hostname Length
def hostname_length(url):
    return len(urlparse(url).netloc)

def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

#First Directory Length
def fd_length(url):
    urlpath= urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

def create_features(df):
    df['use_of_ip'] = df['url'].apply(lambda i: having_ip_address(i))
    df['abnormal_url'] = df['url'].apply(lambda i: abnormal_url(i))
    df['count.'] = df['url'].apply(lambda i: count_dot(i))
    df['count-www'] = df['url'].apply(lambda i: count_www(i))
    df['count@'] = df['url'].apply(lambda i: count_atrate(i))
    df['count_dir'] = df['url'].apply(lambda i: no_of_dir(i))
    df['count_embed_domian'] = df['url'].apply(lambda i: no_of_embed(i))
    df['count-https'] = df['url'].apply(lambda i : count_https(i))
    df['count-http'] = df['url'].apply(lambda i : count_http(i))
    df['count%'] = df['url'].apply(lambda i : count_per(i))
    df['count?'] = df['url'].apply(lambda i: count_ques(i))
    df['count-'] = df['url'].apply(lambda i: count_hyphen(i))
    df['count='] = df['url'].apply(lambda i: count_equal(i))
    df['url_length'] = df['url'].apply(lambda i: url_length(i))
    df['hostname_length'] = df['url'].apply(lambda i: hostname_length(i))
    df['count-digits']= df['url'].apply(lambda i: digit_count(i))
    df['count-letters']= df['url'].apply(lambda i: letter_count(i))
    df['fd_length'] = df['url'].apply(lambda i: fd_length(i))
    return df