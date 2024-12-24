import keyboard
import mouse
from time import sleep
from threading import Thread
import tkinter as tk

# Глобальные переменные
running = False
activate_button = "+"
time_sleep = 0.005

# Функция для изменения клавиши активации
def set_activate_button():
    global activate_button
    activate_button = activate_button_var.get()

# Функция для изменения задержки
def set_time_sleep():
    global time_sleep
    try:
        time_sleep = float(time_sleep_var.get())
    except ValueError:
        time_sleep = 0.01  # Устанавливаем значение по умолчанию при ошибке

# Функция для обработки клавиш
def on_key_press(event):
    global running
    if event.name == activate_button:
        running = not running
        update_status_label()

keyboard.on_press(on_key_press)

# Кликер
def clicker():
    while True:
        if running:
            sleep(time_sleep)
            mouse.double_click(button="left")

# Функция для обновления метки состояния
def update_status_label():
    if running:
        status_label.config(text="АКТИВИРОВАНО", fg="green")
    else:
        status_label.config(text="НЕ активно", fg="red")

# Интерфейс
def create_interface():
    root = tk.Tk()
    root.title("Автокликер by Юрыч")
    root.geometry("300x400")

    # Переменные для интерфейса
    global activate_button_var, time_sleep_var, status_label
    activate_button_var = tk.StringVar(value=activate_button)
    time_sleep_var = tk.DoubleVar(value=time_sleep)

    # Надпись приветствия
    tk.Label(root, text="Автокликер by Юрыч", font=("Arial", 14)).pack(pady=10)

    # Поле для изменения клавиши активации
    tk.Label(root, text="Bind:").pack()
    tk.Entry(root, textvariable=activate_button_var).pack()
    tk.Button(root, text="Set Bind", command=set_activate_button).pack(pady=5)

    # Поле для изменения задержки
    tk.Label(root, text="Delay:").pack()
    tk.Entry(root, textvariable=time_sleep_var).pack()
    tk.Button(root, text="Set Delay", command=set_time_sleep).pack(pady=5)

    # Поле - статус активации программы
    status_label = tk.Label(root, text="НЕ активно", fg="red", font=("Arial", 12))
    status_label.pack(pady=10)

    # Запуск окна
    root.mainloop()

if __name__ == '__main__':
    # Запуск кликера в отдельном потоке
    Thread(target=clicker, daemon=True).start()

    # Создание интерфейса
    create_interface()

