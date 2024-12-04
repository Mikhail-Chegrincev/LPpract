from tkinter import *
from tkinter import messagebox, Button
import requests
from requests.exceptions import Timeout, ConnectionError
import json


window = Tk()
window.title("Данные учётной записи GitHub")
window.geometry('400x250')

def get_info():
    try:
        response = requests.get(f"https://api.github.com/users/{entry.get()}", timeout = (2, 5))
    except Timeout:
        messagebox.showerror('Ошибка', 'Произошло превышение времени ожидания')
    except ConnectionError:
        messagebox.showerror('Ошибка', 'Произошла ошибка подключения')
    else:
        if response.status_code == 200:
            data = response.json()
            info = {
                'company': data['company'],
                'created_at': data['created_at'],
                'email':  data['email'],
                'id': data['id'],
                'name': data['name'],
                'url': data['url']
            }
            with open("pr12.json", "w") as f:
                f.write(json.dumps(info, indent = 4))
            messagebox.showinfo('Результат', 'Данные записаны успешно!')
        elif response.status_code == 404:
            messagebox.showerror('Ошибка', 'Данной учётной записи не существует')
        else:
            messagebox.showerror('Ошибка', 'Не получилось записать данные')

label = Label(window, text = "Введите имя учётной записи")
label.pack()
entry = Entry(window)
entry.pack()
entry.focus()
button = Button(window, text = "Записать данные", command = get_info)
button.pack()
window.mainloop()