from logging import exception
import traceback

def boxprint(symbol, height, width):
    try:
        if len(symbol) != 1:
            raise exception('"symbol" needs to be a string of length 1')
        if height <= 2 or width <= 2:
            raise exception('"height" and "width" need to be greater than 2')
        
        print(symbol * width)
        
        for i in range(height - 2):
            print(symbol + ' ' * (width - 2) + symbol)
        
        print(symbol * width)
    except:
        errorFile = open('errorlog.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print(traceback.format_exc())


boxprint('$', 9, 12)

market = {'ns': 'green', 'ew': 'red'}
# ns indicating traffic from north to south, ew indicating east to west
def switchlights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # as atleast one traffic light must remain red, assert raises AssertionError if the condition is false
    assert 'red' in intersection.keys(), 'Neither light is red! Accidents will occur! ' + str(intersection)

switchlights(market)
