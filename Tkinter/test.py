import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class TkinterDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Демонстрация Tkinter виджетов")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Настройка стилей
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.create_widgets()
    
    def create_widgets(self):
        # Создаем основную структуру
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Панель вкладок
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Вкладка "Основные виджеты"
        self.basic_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.basic_tab, text="Основные")
        self.create_basic_widgets()
        
        # Вкладка "Продвинутые виджеты"
        self.advanced_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.advanced_tab, text="Продвинутые")
        self.create_advanced_widgets()
        
        # Вкладка "Действия"
        self.actions_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.actions_tab, text="Действия")
        self.create_actions_widgets()
    
    def create_basic_widgets(self):
        """Создание основных виджетов"""
        frame = ttk.LabelFrame(self.basic_tab, text="Базовые элементы", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Метка и поле ввода
        ttk.Label(frame, text="Имя пользователя:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.username_entry = ttk.Entry(frame)
        self.username_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Пароль
        ttk.Label(frame, text="Пароль:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Чекбоксы
        self.remember_var = tk.BooleanVar()
        ttk.Checkbutton(frame, text="Запомнить меня", variable=self.remember_var).grid(
            row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Радиокнопки
        ttk.Label(frame, text="Выберите вариант:").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.radio_var = tk.StringVar(value="option1")
        ttk.Radiobutton(frame, text="Вариант 1", value="option1", variable=self.radio_var).grid(
            row=4, column=0, sticky=tk.W)
        ttk.Radiobutton(frame, text="Вариант 2", value="option2", variable=self.radio_var).grid(
            row=4, column=1, sticky=tk.W)
        
        # Выпадающий список
        ttk.Label(frame, text="Выберите город:").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.city_combo = ttk.Combobox(frame, values=["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"])
        self.city_combo.grid(row=5, column=1, sticky=tk.EW, padx=5, pady=2)
        self.city_combo.current(0)
        
        # Шкала (Slider)
        ttk.Label(frame, text="Уровень:").grid(row=6, column=0, sticky=tk.W, pady=2)
        self.scale = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.grid(row=6, column=1, sticky=tk.EW, padx=5, pady=2)
        
        # Настройка веса колонок для правильного растягивания
        frame.columnconfigure(1, weight=1)
    
    def create_advanced_widgets(self):
        """Создание продвинутых виджетов"""
        frame = ttk.LabelFrame(self.advanced_tab, text="Продвинутые элементы", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Дерево (Treeview)
        self.tree = ttk.Treeview(frame, columns=("name", "age", "city"), show="headings")
        self.tree.heading("name", text="Имя")
        self.tree.heading("age", text="Возраст")
        self.tree.heading("city", text="Город")
        
        # Добавляем данные
        self.tree.insert("", tk.END, values=("Иван Иванов", 25, "Москва"))
        self.tree.insert("", tk.END, values=("Петр Петров", 30, "Санкт-Петербург"))
        self.tree.insert("", tk.END, values=("Анна Сидорова", 22, "Новосибирск"))
        
        self.tree.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=5)
        
        # Прогресс бар
        self.progress = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=200, mode="determinate")
        self.progress.grid(row=1, column=0, columnspan=2, sticky=tk.EW, pady=5)
        
        # Панель вкладок внутри вкладки
        sub_notebook = ttk.Notebook(frame)
        sub_notebook.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, pady=5)
        
        tab1 = ttk.Frame(sub_notebook)
        tab2 = ttk.Frame(sub_notebook)
        
        sub_notebook.add(tab1, text="Вкладка 1")
        sub_notebook.add(tab2, text="Вкладка 2")
        
        ttk.Label(tab1, text="Это содержимое первой вкладки").pack(pady=20)
        ttk.Label(tab2, text="Это содержимое второй вкладки").pack(pady=20)
        
        # Настройка веса для правильного растягивания
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
    
    def create_actions_widgets(self):
        """Создание виджетов для выполнения действий"""
        frame = ttk.LabelFrame(self.actions_tab, text="Действия", padding="10")
        frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Кнопки
        ttk.Button(frame, text="Показать сообщение", command=self.show_message).grid(
            row=0, column=0, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Button(frame, text="Запустить прогресс", command=self.start_progress).grid(
            row=0, column=1, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Button(frame, text="Открыть файл", command=self.open_file).grid(
            row=1, column=0, sticky=tk.EW, padx=5, pady=5)
        
        ttk.Button(frame, text="Сохранить файл", command=self.save_file).grid(
            row=1, column=1, sticky=tk.EW, padx=5, pady=5)
        
        # Текстовое поле с прокруткой
        self.text = tk.Text(frame, wrap=tk.WORD, height=10)
        self.scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        
        self.text.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW, pady=5)
        self.scroll.grid(row=2, column=2, sticky=tk.NS, pady=5)
        
        # Настройка веса для правильного растягивания
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(2, weight=1)
    
    def show_message(self):
        """Показать диалоговое окно с информацией"""
        username = self.username_entry.get()
        city = self.city_combo.get()
        level = self.scale.get()
        
        message = f"Имя: {username}\nГород: {city}\nУровень: {level:.0f}"
        messagebox.showinfo("Информация", message)
    
    def start_progress(self):
        """Запустить анимацию прогресс-бара"""
        self.progress["value"] = 0
        self.root.after(100, self.update_progress)
    
    def update_progress(self):
        """Обновить прогресс-бар"""
        if self.progress["value"] < 100:
            self.progress["value"] += 5
            self.root.after(100, self.update_progress)
    
    def open_file(self):
        """Открыть диалог выбора файла"""
        file_path = filedialog.askopenfilename(
            title="Открыть файл",
            filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text.delete(1.0, tk.END)
                    self.text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{str(e)}")
    
    def save_file(self):
        """Открыть диалог сохранения файла"""
        file_path = filedialog.asksaveasfilename(
            title="Сохранить файл",
            defaultextension=".txt",
            filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(self.text.get(1.0, tk.END))
                messagebox.showinfo("Успех", "Файл успешно сохранен")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterDemoApp(root)
    root.mainloop()