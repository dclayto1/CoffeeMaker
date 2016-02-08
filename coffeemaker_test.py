#import RPi.GPIO as GPIO
import signal
import sys

#'Globals'
PIN = 5 #pin number, not "GPIO5", it's actually "GPIO3" but "Pin No.5"
off = "OFF"
on = "ON"
status = ""


from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def coffee():

    if request.method == "POST":
        toggleFunc() #calls toggle function below
        #return redirect(url_for("coffee"))

    return render_template("coffeemaker_test.html", status=status)



##################################
# Functions for webserver to use #
##################################


#Making sure that the coffee pot is turned off if
# server process ends
def endProcess(signum, frame):
    global status 
    status = off
    #GPIO.output(PIN, False)
    #GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, endProcess)


def toggleFunc():
    global status
    if(status == off):
        status = on
        #GPIO.output(PIN, False)
    else:
        status = off
        #GPIO.output(PIN, True)



#Runs the Flask application
if __name__ == "__main__":
    status = off
    #GPIO.cleanup()
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(PIN, GPIO.OUT)
    #GPIO.output(PIN, True)

    app.run(host='0.0.0.0', debug=True)
