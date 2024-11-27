from flask import Flask, render_template_string
from threading import Thread
import logging

class InboxServer(Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.app = Flask("NBPS Custom Inbox")
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        @self.app.route("/")
        def index():
            return render_template_string(open("NBPS/Inbox/Files/index.html").read())

    def run(self):
        self.app.run(host="0.0.0.0", port=self.port, debug=False)