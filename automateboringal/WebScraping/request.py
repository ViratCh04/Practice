import requests

# This module allows us to download webpages in text format
req = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(req.status_code)          # A status code of 200 means everything went a-okay, while 404 means file not found
print(req.text[:50])            # Prints the text of file

req.raise_for_status()          # Raises exception if file request didnt succeed
# This above function only helps if not being able to download the file is a huge deal breaker for you
# You can also just encase the function in a try and except block if you do not want any program crashes

# Writing the downloaded request to a local file
book = open('RomeoAndJuliet.txt', 'wb')
# 'wb' stands for write-binary mode, as plain text will remove the unicode encoding, which we do not want to happen
for chunk in req.iter_content(50000):           # Specify how many bytes you want in each chunk
    book.write(chunk)

book.close()