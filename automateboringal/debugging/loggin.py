import logging

# While print() for debugging is useful, it is a pain to remove all the debugging print statements afterwards

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# The following command writes off the logs to a text file
#    logging.basicConfig(filename='MyErrorLog.txt', level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.CRITICAL)          # can be used to turn off the logs

logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % n)
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    
    logging.debug('Return value is, %s' % (total))
    return total

print(factorial(5))

logging.debug('End of Program')