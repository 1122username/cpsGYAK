__author__ = 'User'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO6, GPIO.IN)
GPIO.setup(GPIO13, GPIO.IN)

GPIO.setup(GPIO19, GPIO.OUT) //outputra állítás
GPIO.setup(GPIO26, GPIO.OUT) //outputra állítás
GPIO.output(GPIO19, 1) //output irás, 0 vagy 1.
GPIO.output(GPIO26, 1) //output irás, 0 vagy 1.
