import signal
import threading
from application import Application

# This overly complicated start provides a basic way to run a background thread
app = Application()

def start_app():
    app.start()

def handle_exit(signal, frame):
    app.close()
    raise SystemExit

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

thread = threading.Thread(target=start_app)
thread.start()

print('Use Ctrl-C to stop')
while True:
    signal.pause()