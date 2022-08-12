import webbrowser, sys, pyperclip

sys.argv        # ['mapit.py', '790', 'Valencia', 'St.']

if len(sys.argv) > 1:
    # ['mapit.py', '790', 'Valencia', 'St.'] --> '790 Valencia St.'
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('www.google.com/maps/place/' + address)

# See Lecture 22 for launching the program from Run with batch file