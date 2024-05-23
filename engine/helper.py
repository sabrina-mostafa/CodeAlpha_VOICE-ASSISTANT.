import re


def extract_yt_term(command):
    # Define a regular expression pattern to capture the YT video name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # if a match is found, return the extracted video name; otherwise return none
    return match.group(1) if match else None