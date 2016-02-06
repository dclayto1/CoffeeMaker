import RPi.GPIO as GPIO
import signal
import sys

#'Globals'
PIN = 5 #pin number, not "GPIO5", it's actually "GPIO3" but "Pin No.5"
off = "OFF"
on = "ON"
status = ""


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def coffee():

    if request.method == "POST":
        toggle() #calls toggle function below

    return render_template("coffeemaker.html", status=status)





##################################
# Functions for webserver to use #
##################################


#Making sure that the coffee pot is turned off if
# server process ends
def endProcess(signum, frame):
    status = off
    GPIO.output(PIN, False)
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, endProcess)


def toggle():
    if(status == off):
        status = on
        GPIO.output(PIN, False)
    else:
        status = off
        GPIO.output(PIN, True)



#Runs the Flask application
if __name__ == "__main__":
    status = off
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

    app.run(host='0.0.0.0')
