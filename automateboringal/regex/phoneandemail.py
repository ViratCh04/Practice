import re, pyperclip

# Make regex for phone numbers
phoneregex = re.compile(r'''(
                        # 419-408-8041, (930) 305-6871, 849-3801 ext. 39380, 180-1902 ext 124
                        (\d{3} | \(\d{3}\))?       # area code w or w\o parentheses
                        (\s | -)?                        # first seperator
                        \d{3}                          # first three digits
                        -                              # second seperator
                        \d{4}                          # last four digits
                        ((ext(.)?\s | x\s)                 # extension word part (optional) 
                        \d{2,5})?                      # extension number part (optional) make it a grp if output buggy
                        )''', re.VERBOSE)

# Make regex for emails
emailregex = re.compile(r'''(
                        # some.+_thing@(\w+)(\d{2,5})?.com
                        [a-zA-Z0-9_+.]+           # name part
                        @                         # @ symbol
                        [a-zA-Z0-9_+.]+           # domain name part
                        )''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/s and phone number/s from this text
extractedPhone = phoneregex.findall(text)
extractedEmail = emailregex.findall(text)

# As there are many groups in the re object for phone numbers, we will create another list and store the 
# 0th group inside of it(as it contains the entire matching string, being the first group encasing the regex)
allphonenumbers = []

for phonenumber in extractedPhone:
    allphonenumbers.append(phonenumber[0])

# Copy the extracted emails and phones to clipboard
results = '\n'.join(allphonenumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)