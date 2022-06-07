import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('this message should go to the log file')
logging.info('So should this')
logging.warning('And this , too')
logging.error('And non-ASCII stuff, too, like resend and mallfjdj')


# # Logging from multiple modules¶
import logging
import mylib
def main():
    logging.basicConfig(filename='myapp.log',level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()


# # Logging variable data¶
import logging
logging.basicConfig(filename='myapp.log',level=logging.INFO)
logging.warning('%s before you %s','Look','leap!')


# # Changing the format of displayed messages¶
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')

# # Displaying the date/time in messages
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')


import logging 
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')