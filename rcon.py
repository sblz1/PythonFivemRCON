#!"C:\Users\bla\AppData\Local\Programs\Python\Python312\python.exe"
# to be executed in a cgi-bin fashion
# e.g http://127.0.0.1/cgi-bin/rcon.py?resmon true
# e.g http://127.0.0.1/cgi-bin/rcon.py?resmon false
# code is dirty but works
# adapted from https://github.com/EggRP/fxcommands for python and cgi-bin support - thanks

from ast import Try
import socket
import sys

lecommand = sys.argv[0:]
lecommand = lecommand[1:]

def print_header():
    print ("""Content-type: text/html\n
    <!DOCTYPE html>
    <html>
    <body>""")

def print_close():
    print ("""</body>
    </html>""")

def execute(command):
    HOST = "localhost"
    PORT = 29200  # devcon port (29200)
    command = ''.join(command)
    b_command = command[0:].encode("utf-8").hex()
    b_nog = "00d20000"
    b_header = "CMND".encode("utf-8").hex()
    b_padding = "0000"
    b_length = repr((len(command) + 12 + 1)).encode("utf-8").hex()
    b_terminator = "00"
    print_header()
    print ("Executing:  " + (command)+"<br><br>")
    print ("ncommand    "+(b_command)+"<br>")
    print ("nog         "+(b_nog)+"<br>")
    print ("header      "+(b_header)+"<br>")
    print ("padding     "+(b_padding)+"<br>")
    print ("length      "+(b_length)+"<br>")
    print ("terminator  "+(b_terminator)+"<br>")

    totalstring = (str(b_header) + str(b_nog) + str(b_length) + str(b_padding) + str(b_command) + str(b_terminator))
    print (totalstring)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        s.send(bytes.fromhex(totalstring))
    except:
        print("Cannot connect to host. Is FiveM running?")
    print_close()


execute(lecommand)
