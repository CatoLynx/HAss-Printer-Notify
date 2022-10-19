import json
import serial
import textwrap
import time
from flask import Flask, request, Response


app = Flask(__name__)


def print_message(text):
    printer = serial.Serial("/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2.1:1.0-port0", baudrate=19200)
    message = time.strftime("%d.%m.%Y %H:%M:%S")
    message += "\n"
    message += "\n".join(textwrap.wrap(text, width=24))
    message += "\n" * 4
    printer.write(message.encode("cp437"))
    printer.close()


@app.route("/notify.json", methods=["GET", 'POST'])
def root():
    if 'message' in request.args:
        print_message(request.args.get('message'))
    return Response(json.dumps({"test": True}), mimetype='application/json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2342)
