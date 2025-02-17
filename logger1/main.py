import logging

# Configure logging to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("hacking attempt ...")
pwd = input('password?')
if pwd != "admin":
    logging.fatal(f"wrong password ... typed {pwd}")
try:
    number = int(input('enter number:'))
except Exception as e:
    logging.error(f"failed in enter number, error={e}")


