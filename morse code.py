import sys
from gpiozero import LED
from time import sleep
code = {'A' : '.-',"B" : "-...","C" : "-.-.","D" : "-..","E" : ".",
        "F" : "..-.","G" : "--.","H" : "....","I" : "..","J" : ".---",
        "K" : "-.-","L" : ".-..","M" : "--","N" : "-.","O" : "---","P" : ".--.",
        "Q" : "--.-","R" : ".-.","S" : "...","T" : "-","U" : "..-","V" : "...-",
        "W" : ".--","X" : "-..-","Y" : "-.--","Z" : "--..","1" : ".----",
        "2" : "..---","3" : "...--","4" : "....-","5" : ".....","6" : "-....",
        "7": "--...","8" : "---..","9" : "----.","0" : "-----", " " : " "}

led = LED(4)

def long_light():
    led.on()
    sleep(1)
    led.off()
    sleep(0.1)

def short_light():
    led.on()
    sleep(0.2)
    led.off()
    sleep(0.1)

def main():
    print()
    msg = input('message:')
    
    for char in msg:
        sys.stdout.write(code[char.upper()])
        sys.stdout.write(' ')
        
        for i in range(len(code[char.upper()])):
            #print(i)
            symbol = code[char.upper()][i]
            if symbol == '.':
                short_light()
            elif symbol == '-':
                long_light()
            else:
                sleep(1)
           
while True:
    main()





