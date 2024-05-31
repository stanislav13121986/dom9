import requests
import tkinter as tk

# Окно приложения
window = tk.Tk()
window.title("Конвертер валют")

# Поле для ввода валюты
label_currency = tk.Label(text="Введите валюту (например, USD):")
label_currency.pack()
entry_currency = tk.Entry()
entry_currency.pack()

# Функция для получения курса валюты
def get_currency_rate():
    currency = entry_currency.get()
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()
    rate = data["Valute"][currency]["Value"]
    return rate

# Функция для отображения курса валюты
def show_currency_rate():
    rate = get_currency_rate()
    label_result = tk.Label(text=f"{entry_currency.get()}: {rate}")
    label_result.pack()

# Кнопка для запуска процесса
button = tk.Button(text="Получить курс", command=show_currency_rate)
button.pack()

window.mainloop()