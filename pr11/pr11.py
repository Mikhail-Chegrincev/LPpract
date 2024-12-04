from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Combobox, Notebook, Frame, Checkbutton

window = Tk()
window.title("Чегринцев Михаил Сергеевич")
window.geometry('720x480')

tab_control = Notebook(window)
tab_control.pack(expand = 1, fill = 'both')
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab_control.add(tab1, text = 'Первая')
tab_control.add(tab2, text = 'Вторая')
tab_control.add(tab3, text = 'Третья')

vch1 = Entry(tab1, width = 10)
vch1.grid(column = 0, row = 0)
combo = Combobox(tab1, state = 'readonly')
combo['values'] = ('+','-','*','/')
combo.grid(column = 1, row = 0)
vch2 = Entry(tab1, width = 10)
vch2.grid(column = 2, row = 0)
def clicked():
    try:
        type = combo.get()
        if type == '+':
            ch1 = float(vch1.get())
            ch2 = float(vch2.get())
            lbl = Label(tab1, text = f'Ответ: {ch1 + ch2}')
            lbl.grid(column = 1, row = 1)
        elif type == '-':
            ch1 = float(vch1.get())
            ch2 = float(vch2.get())
            lbl = Label(tab1, text = f'Ответ: {ch1 - ch2}')
            lbl.grid(column = 1, row = 1)
        elif type == '*':
            ch1 = float(vch1.get())
            ch2 = float(vch2.get())
            lbl = Label(tab1, text = f'Ответ: {ch1 * ch2}')
            lbl.grid(column = 1, row = 1)
        else:
            ch1 = float(vch1.get())
            ch2 = float(vch2.get())
            if ch2 == 0:
                lbl = Label(tab1, text = 'Нельзя делить на 0')
                lbl.grid(column = 1, row = 1)
            else:
                lbl = Label(tab1, text = f'Ответ: {ch1 / ch2}')
                lbl.grid(column = 1, row = 1)
    except:
        messagebox.showerror('Ошибка', 'Не удалось посчитать')
btn = Button(tab1, text = "Посчитать", command = clicked)
btn.grid(column = 0, row = 1)

chk_state1 = BooleanVar()
chk_state1.set(False)
chk_state2 = BooleanVar()
chk_state2.set(False)
chk_state3 = BooleanVar()
chk_state3.set(False)
chk1 = Checkbutton(tab2, text = 'Первый', var = chk_state1)
chk2 = Checkbutton(tab2, text = 'Второй', var = chk_state2)
chk3 = Checkbutton(tab2, text = 'Третий', var = chk_state3)
def clicked():
    if chk_state1.get() == chk_state3.get() == chk_state3.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали все варианты')
    elif chk_state1.get() == chk_state2.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали первый и второй варианты')
    elif chk_state1.get() == chk_state3.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали первый и третий варианты')
    elif chk_state2.get() == chk_state3.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали второй и третий варианты')
    elif chk_state1.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали первый вариант')
    elif chk_state2.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали второй вариант')
    elif chk_state3.get() == True:
        messagebox.showinfo('Результат', 'Вы выбрали третий вариант')
    else:
        messagebox.showinfo('Результат', 'Вы не выбрали ни одного варианта')
btn = Button(tab2, text = "Выбрать", command = clicked)
chk1.grid(column = 0, row = 0)
chk2.grid(column = 1, row = 0)
chk3.grid(column = 2, row = 0)
btn.grid(column = 3, row = 0)

def open_file():
    filepath = filedialog.askopenfilename(filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, 'r') as file:
            text = file.read()
            text_area.delete(1.0, END)
            text_area.insert(END, text)
menu = Menu(window)
window.config(menu = menu)
file_menu = Menu(menu, tearoff = 0)
menu.add_cascade(label = "Файл", menu = file_menu)
file_menu.add_command(label = "Открыть", command = open_file)
text_area = Text(tab3, wrap = WORD, width = 80, height = 25)
text_area.grid(column = 0, row = 0)

window.mainloop()