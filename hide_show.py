import tkinter as tk

def hide_window():
    root.withdraw()  # Скрыть окно

def show_window():
    root.deiconify()  # Показать окно

root = tk.Tk()
root.title("Пример с withdraw()")

# Кнопка для скрытия окна
hide_button = tk.Button(root, text="Скрыть окно", command=hide_window)
hide_button.pack(pady=20)

# Кнопка для восстановления окна
show_button = tk.Button(root, text="Показать окно", command=show_window)
show_button.pack(pady=20)

root.geometry("300x200")
root.mainloop()
