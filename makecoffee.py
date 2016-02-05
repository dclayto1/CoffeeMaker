import RPi.GPIO as GPIO
import signal
import sys

PIN = 5 #pin number, not "GPIO5", its actually "GPIO3" but "Pin No. 5"
off = "OFF"
on = "ON"
status = ""

#cleanup function. Called on user enter -1, or program is interrupted
def cleanup():
    print
    print "!!!"

    print "Program cleaning up. Turning off coffee maker..."
    print

    status = off
    GPIO.output(PIN, False) #make sure the coffee maker is off
    GPIO.cleanup()
    print "Current status for the coffee maker: " + status
    print
    
    print "########################################"
    print "# Thank you for using the Coffee Maker #"
    print "########################################"
    print

    #finally, exit the program
    sys.exit(0)

#function for the signal interuption to call which calls the cleanup
def processKill(signum, frame):
    cleanup()


def main():
    status = off
    
    GPIO.cleanup() #throws a warning/error if none are setup, but better to be sure
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)

    while True:
        print "Current status for coffee maker: " + status
        user_in = raw_input("Press enter to toggle the status of the coffee maker\nType -1 to end the program and turn off the coffee maker\nEnter: ")

        if(user_in == "-1"):
            processKill(0,0)

        if(status == off):
            status = on
            GPIO.output(PIN, False)
        else:
            status = off
            GPIO.output(PIN, True)

        print "--------------"
        print
    


signal.signal(signal.SIGINT, processKill)
main()
