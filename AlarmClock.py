from tkinter import *
from time import strftime, sleep
import threading
import os

window = Tk()

def main_window():
    # Création de notre fenêtre
    window.config(bg="ivory")

    # Titre de la fenêtre
    window.title("Alarm Clock")

    # Message de bienvenue
    welcome = Label(window, text="Bienvenue")
    welcome.config(font=("Bahnschrift", 30, "bold"), fg='light sea green', bg="ivory")
    welcome.grid(row=0, column=1)

    # Positionnement de la fenêtre sur le bureau
    # Dans ce cas, la fenêtre va s'adapter pour toujours s'afficher au centre du bureau
    w = 440
    h = 330

    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Temps
    time = Label(window, font=('Bahnschrift', 100, 'bold'), fg='light sea green', bg="ivory")
    time.grid(row=1, column=1)

    global Time
    def Time():
        time.config(text=strftime('%H:%M:%S'))
        time.after(30, Time)

    Time()

    # Alarm
    wake_up = Label(window, text="À quelle heure voulez-vous vous réveiller ?", bg="ivory")
    wake_up.config(font=('Bahnschrift', 15, 'bold'))
    wake_up.grid(row=3, column=1)

    # Heure
    global set_hour
    global set_minute
    set_hour = Spinbox(window, from_=0, to=23, width=5, bg="ivory", wrap=True)
    set_hour.grid(row=4, column=1)
    hour = Label(window, text="h", font=('Bahnschrift', 15, 'bold'), bg="ivory")
    hour.grid(row=4, column=1)

    # Minute
    set_minute = Spinbox(window, from_=0, to=59, width=7, bg="ivory", wrap=True)
    set_minute.grid(row=5, column=1)
    minute = Label(window, text="m", font=('Bahnschrift', 15, 'bold'), bg="ivory", wrap=True)
    minute.grid(row=5, column=1)

main_window()

# Bouton de programation de l'heure de réveille
def setting_alarm():
    get_hour = set_hour.get()  # Recupération de la partie heure
    get_minute = set_minute.get()  # Récupération de la partie minute
    if int(get_minute) < 10 and int(get_hour) < 10:
        message = Label(window, text="Votre alarme est prévu pour 0{0}h0{1}min".format(get_hour, get_minute),
                        font=('Bahnschrift', 15, 'bold'), fg='light sea green', bg="ivory")
        message.grid(row=7, column=1)
    elif int(get_minute) < 10:
        message = Label(window, text="Votre alarme est prévu pour {0}h0{1}min".format(get_hour, get_minute),
                        font=('Bahnschrift', 15, 'bold'), fg='light sea green', bg="ivory")
        message.grid(row=7, column=1)
    elif int(get_hour) < 10:
        message = Label(window, text="Votre alarme est prévu pour 0{0}h{1}min".format(get_hour, get_minute),
                        font=('Bahnschrift', 15, 'bold'), fg='light sea green', bg="ivory")
        message.grid(row=7, column=1)
    else:
        message = Label(window, text="Votre alarme est prévu pour {0}h{1}min".format(get_hour, get_minute),
                        font=('Bahnschrift', 15, 'bold'), fg='light sea green', bg="ivory")
        message.grid(row=7, column=1)
    print("h= {} ".format(get_hour) + "min= {} ".format(get_minute))
    def verification():
        while int(get_hour) != int(strftime('%H:%M')[:2]) or int(get_minute) != int(strftime('%H:%M')[3:]):
            continue
        os.system("afplay /Users/ayoubhs/Desktop/alarme.mp3")
    th1 = threading.Thread(target=main_window)
    th2 = threading.Thread(target=verification)
    th1.start()
    th2.start()

button_alarm = Button(window, text="Initialiser", font=('Bahnschrift', 13, 'bold'), bg="light sea green", relief="flat",
                      command=setting_alarm)
button_alarm.grid(row=6, column=1, pady=10)

# Commande qui maintient la fenêtre afficher jusqu'à sa fermeture
window.mainloop()
