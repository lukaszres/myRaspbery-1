from gpiozero import Button
from time import sleep

button17 = Button(17, pull_up=True)
button27 = Button(27, pull_up=True)
button22 = Button(22, pull_up=True)

while True:
    message = "Puste wiaderko"
    if button17.is_pressed:
        message = "1/2 wiaderka"
        if button27.is_pressed:
            message = "3/4 wiaderka"
            if button22.is_pressed:
                message = "Pelne wiaderko"
    print(message)

    sleep(1)