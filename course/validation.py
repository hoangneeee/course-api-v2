import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

'''Handle Validate Gmail'''
def validate_gmail(gmail):

    if re.fullmatch(regex, gmail):
        return True
    else:
        return False
