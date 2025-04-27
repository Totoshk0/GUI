import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                            QHBoxLayout, QLabel, QPushButton, QLineEdit,
                            QComboBox, QCheckBox, QRadioButton, QSlider,
                            QProgressBar, QSpinBox, QDoubleSpinBox, QTextEdit,
                            QListWidget, QTabWidget, QMessageBox, QInputDialog)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt6 Widgets Demo")
        self.setGeometry(100, 100, 800, 600)
        
        # Центральный виджет и основной layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Создаем вкладки для разных групп виджетов
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Вкладка с базовыми виджетами
        self.create_basic_widgets_tab()
        # Вкладка с виджетами ввода
        self.create_input_widgets_tab()
        # Вкладка с индикаторами
        self.create_indicator_widgets_tab()
        # Вкладка с контейнерами
        self.create_container_widgets_tab()
        
        # Статус бар
        self.statusBar().showMessage("Готово")
    
    def create_basic_widgets_tab(self):
        """Создаем вкладку с базовыми виджетами"""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Метка с изображением
        label = QLabel("Демонстрация PyQt6 Widgets")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = label.font()
        font.setPointSize(16)
        label.setFont(font)
        layout.addWidget(label)
        
        # Изображение
        image_label = QLabel()
        pixmap = QPixmap(":images/python-logo.png")  # Используем встроенный ресурс
        if not pixmap.isNull():
            image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)
        
        # Кнопки
        btn_layout = QHBoxLayout()
        
        btn1 = QPushButton("Обычная кнопка")
        btn1.clicked.connect(self.on_button_click)
        btn_layout.addWidget(btn1)
        
        btn2 = QPushButton(QIcon(":images/python-logo.png"), "Кнопка с иконкой")
        btn2.clicked.connect(self.on_button_click)
        btn_layout.addWidget(btn2)
        
        btn3 = QPushButton("Отключенная кнопка")
        btn3.setEnabled(False)
        btn_layout.addWidget(btn3)
        
        layout.addLayout(btn_layout)
        
        # Горизонтальная линия
        layout.addWidget(QLabel("<hr>"), 1)
        
        # Текстовое поле
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Введите текст здесь...")
        self.line_edit.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.line_edit)
        
        self.tabs.addTab(tab, "Базовые виджеты")
    
    def create_input_widgets_tab(self):
        """Создаем вкладку с виджетами ввода"""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Комбобокс (выпадающий список)
        combo_label = QLabel("Выберите вариант:")
        layout.addWidget(combo_label)
        
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Вариант 1", "Вариант 2", "Вариант 3", "Вариант 4"])
        self.combo_box.currentIndexChanged.connect(self.on_combo_changed)
        layout.addWidget(self.combo_box)
        
        # Чекбоксы
        check_label = QLabel("Выберите опции:")
        layout.addWidget(check_label)
        
        self.check1 = QCheckBox("Опция 1")
        self.check1.stateChanged.connect(self.on_check_changed)
        layout.addWidget(self.check1)
        
        self.check2 = QCheckBox("Опция 2")
        self.check2.stateChanged.connect(self.on_check_changed)
        layout.addWidget(self.check2)
        
        # Радио кнопки
        radio_label = QLabel("Выберите один вариант:")
        layout.addWidget(radio_label)
        
        self.radio1 = QRadioButton("Вариант A")
        self.radio1.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.radio1)
        
        self.radio2 = QRadioButton("Вариант B")
        self.radio2.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.radio2)
        
        self.radio3 = QRadioButton("Вариант C")
        self.radio3.toggled.connect(self.on_radio_toggled)
        layout.addWidget(self.radio3)
        
        # Слайдер
        slider_label = QLabel("Регулировка значения:")
        layout.addWidget(slider_label)
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.on_slider_changed)
        layout.addWidget(self.slider)
        
        # Спинбоксы
        spin_layout = QHBoxLayout()
        
        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 100)
        self.spin_box.setValue(25)
        self.spin_box.valueChanged.connect(self.on_spin_changed)
        spin_layout.addWidget(self.spin_box)
        
        self.double_spin = QDoubleSpinBox()
        self.double_spin.setRange(0, 10)
        self.double_spin.setSingleStep(0.1)
        self.double_spin.setValue(2.5)
        self.double_spin.valueChanged.connect(self.on_double_spin_changed)
        spin_layout.addWidget(self.double_spin)
        
        layout.addLayout(spin_layout)
        
        self.tabs.addTab(tab, "Виджеты ввода")
    
    def create_indicator_widgets_tab(self):
        """Создаем вкладку с индикаторами"""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Прогресс бар
        progress_label = QLabel("Прогресс бар:")
        layout.addWidget(progress_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        # Кнопка для запуска прогресса
        self.progress_btn = QPushButton("Запустить прогресс")
        self.progress_btn.clicked.connect(self.start_progress)
        layout.addWidget(self.progress_btn)
        
        # Таймер для прогресс бара
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        
        # Метка для отображения значений
        self.value_label = QLabel("Значения будут отображаться здесь")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.value_label)
        
        self.tabs.addTab(tab, "Индикаторы")
    
    def create_container_widgets_tab(self):
        """Создаем вкладку с контейнерными виджетами"""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)
        
        # Текстовый редактор
        text_edit_label = QLabel("Текстовый редактор:")
        layout.addWidget(text_edit_label)
        
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Введите текст здесь...")
        layout.addWidget(self.text_edit)
        
        # Кнопки для работы с текстом
        text_btn_layout = QHBoxLayout()
        
        clear_btn = QPushButton("Очистить")
        clear_btn.clicked.connect(self.text_edit.clear)
        text_btn_layout.addWidget(clear_btn)
        
        get_text_btn = QPushButton("Показать текст")
        get_text_btn.clicked.connect(self.show_text)
        text_btn_layout.addWidget(get_text_btn)
        
        layout.addLayout(text_btn_layout)
        
        # Список
        list_label = QLabel("Список элементов:")
        layout.addWidget(list_label)
        
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Элемент 1", "Элемент 2", "Элемент 3"])
        self.list_widget.itemClicked.connect(self.on_list_item_clicked)
        layout.addWidget(self.list_widget)
        
        # Кнопки для работы со списком
        list_btn_layout = QHBoxLayout()
        
        add_item_btn = QPushButton("Добавить")
        add_item_btn.clicked.connect(self.add_list_item)
        list_btn_layout.addWidget(add_item_btn)
        
        remove_item_btn = QPushButton("Удалить")
        remove_item_btn.clicked.connect(self.remove_list_item)
        list_btn_layout.addWidget(remove_item_btn)
        
        layout.addLayout(list_btn_layout)
        
        self.tabs.addTab(tab, "Контейнеры")
    
    # Методы обработки событий
    def on_button_click(self):
        sender = self.sender()
        QMessageBox.information(self, "Кнопка нажата", f"Нажата кнопка: {sender.text()}")
    
    def on_text_changed(self, text):
        self.statusBar().showMessage(f"Текст изменен: {text}", 2000)
    
    def on_combo_changed(self, index):
        self.value_label.setText(f"Выбран комбобокс: {self.combo_box.currentText()} (индекс {index})")
    
    def on_check_changed(self, state):
        sender = self.sender()
        checked = "включена" if state else "отключена"
        self.value_label.setText(f"Опция {sender.text()} {checked}")
    
    def on_radio_toggled(self, checked):
        if checked:
            sender = self.sender()
            self.value_label.setText(f"Выбран радио-вариант: {sender.text()}")
    
    def on_slider_changed(self, value):
        self.value_label.setText(f"Значение слайдера: {value}")
    
    def on_spin_changed(self, value):
        self.value_label.setText(f"Значение спинбокса: {value}")
    
    def on_double_spin_changed(self, value):
        self.value_label.setText(f"Значение double спинбокса: {value:.2f}")
    
    def start_progress(self):
        if not self.progress_timer.isActive():
            self.progress_value = 0
            self.progress_bar.setValue(0)
            self.progress_timer.start(100)
            self.progress_btn.setText("Остановить прогресс")
        else:
            self.progress_timer.stop()
            self.progress_btn.setText("Запустить прогресс")
    
    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)
        
        if self.progress_value >= 100:
            self.progress_timer.stop()
            self.progress_btn.setText("Запустить прогресс")
            QMessageBox.information(self, "Готово", "Прогресс завершен!")
    
    def show_text(self):
        text = self.text_edit.toPlainText()
        if text:
            QMessageBox.information(self, "Текст", text)
        else:
            QMessageBox.warning(self, "Ошибка", "Текст не введен!")
    
    def on_list_item_clicked(self, item):
        self.value_label.setText(f"Выбран элемент списка: {item.text()}")
    
    def add_list_item(self):
        text, ok = QInputDialog.getText(self, "Добавить элемент", "Введите текст элемента:")
        if ok and text:
            self.list_widget.addItem(text)
    
    def remove_list_item(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            self.list_widget.takeItem(self.list_widget.row(current_item))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Устанавливаем стиль для приложения
    app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())