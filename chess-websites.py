from tkinter import *
import webview
import requests
from requests_html import HTMLSession

session = HTMLSession()

def open_chess_website():
    login_url = "https://chess.com/login"
    username = "SteamWo1f"
    password = "passwrd"
    data = {"username": username, "password": password}
    r = session.post(login_url, data=data)

    webview.create_window('Chess.com', 'https://chess.com', height=1000, width=1800)
    webview.start()

def open_chess_website2():
    login_url = "https://lichess.org/login"
    username = "your_username"
    password = "your_password"
    data = {"username": username, "password": password}
    r = session.post(login_url, data=data)

    webview.create_window('Puzzles', 'https://lichess.org/training', height=1000, width=1800)
    webview.start()

def open_chess_website3():
    login_url = "https://lichess.org/login"
    username = "your_username"
    password = "your_password"
    data = {"username": username, "password": password}
    r = session.post(login_url, data=data)

    webview.create_window('Analysis', 'https://lichess.org/analysis', height=1000, width=1800)
    webview.start()

# Create a new tkinter window
root = Tk()
root.geometry("300x200")
root.configure(background='#2e2e2e')


# Create a button widget
chess_button = Button(root, text="♔ Chess ♔", command=open_chess_website, bg='#7289DA', fg='white', font=('Sans-Serif', 16))
chess_button.pack(pady=10)

chess_button2 = Button(root, text="♕ Puzzles ♕", command=open_chess_website2, bg='#7289DA', fg='white', font=('Sans-Serif', 16))
chess_button2.pack(pady=10)

chess_button3 = Button(root, text="♗ Analysis ♗", command=open_chess_website3, bg='#7289DA', fg='white', font=('Sans-Serif', 16))
chess_button3.pack(pady=10)

root.title("Chess Websites")

# Start the tkinter event loop
root.mainloop()
