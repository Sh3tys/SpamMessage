#Bibliotheque
import pyautogui as auto
import time

#Function
def spam():
    choice = str(input("What message for spam ?: "))
    while True:
        auto.write(choice)
        auto.press('enter')
        time.sleep(1)

#Progs principal

if __name__ == "__main__":
    spam()

#END