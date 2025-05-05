from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
    QFrame, QStackedWidget, QComboBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from src.windows.all_models_page import AllModelsPage
from src.windows.mens_page import MensPage
from src.windows.womens_page import WomensPage
from src.utils.product_data import get_product_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Магазин обуви")
        self.setGeometry(100, 100, 1200, 800)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Верхняя панель (иконка, категории, поиск, корзина, кабинет)
        top_bar = QHBoxLayout()

        icon = QLabel("🏡")  # Заглушка для иконки
        top_bar.addWidget(icon)

        vertical_line1 = QFrame()
        vertical_line1.setFrameShape(QFrame.VLine)
        vertical_line1.setFrameShadow(QFrame.Sunken)
        top_bar.addWidget(vertical_line1)

        for category in ["Все модели", "Мужчинам", "Женщинам"]:
            btn = QPushButton(category)
            btn.clicked.connect(lambda checked, text=category: self.on_nav_button_clicked(text))
            top_bar.addWidget(btn)

        top_bar.addSpacing(20)

        search_icon = QPushButton("🔍")  # Иконка поиска
        search_icon.clicked.connect(self.on_search_clicked)  # Заглушка
        top_bar.addWidget(search_icon)

        vertical_line2 = QFrame()
        vertical_line2.setFrameShape(QFrame.VLine)
        vertical_line2.setFrameShadow(QFrame.Sunken)
        top_bar.addWidget(vertical_line2)

        cart_icon = QPushButton("🛒")
        top_bar.addWidget(cart_icon)

        user_icon = QPushButton("👤")
        top_bar.addWidget(user_icon)

        top_bar.addStretch()
        main_layout.addLayout(top_bar)

        # Горизонтальная линия
        top_line = QFrame()
        top_line.setFrameShape(QFrame.HLine)
        top_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(top_line)

        # Заголовки "Каталог / ..." и "Мужская обувь"
        self.catalog_path_label = QLabel()
        self.catalog_path_label.setStyleSheet("font-size: 14px; color: gray;")

        self.category_title_label = QLabel()
        self.category_title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        main_layout.addWidget(self.catalog_path_label)
        main_layout.addWidget(self.category_title_label)

        # Ещё одна горизонтальная линия
        mid_line = QFrame()
        mid_line.setFrameShape(QFrame.HLine)
        mid_line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(mid_line)

        # Кол-во товаров + фильтры
        filter_bar = QHBoxLayout()

        self.product_count_label = QLabel("Найдено товаров: ...")
        filter_bar.addWidget(self.product_count_label)

        vline = QFrame()
        vline.setFrameShape(QFrame.VLine)
        vline.setFrameShadow(QFrame.Sunken)
        filter_bar.addWidget(vline)

        filter_icon = QLabel("🧰 Фильтры")
        filter_bar.addWidget(filter_icon)

        vline2 = QFrame()
        vline2.setFrameShape(QFrame.VLine)
        vline2.setFrameShadow(QFrame.Sunken)
        filter_bar.addWidget(vline2)

        self.sort_combobox = QComboBox()
        self.sort_combobox.addItems(["По возрастанию цены", "По убыванию цены"])
        self.sort_combobox.currentIndexChanged.connect(self.on_filter_changed)
        filter_bar.addWidget(self.sort_combobox)

        filter_bar.addStretch()
        main_layout.addLayout(filter_bar)

        # Страницы товаров
        self.page_stack = QStackedWidget()
        self.pages = {
            "Все модели": AllModelsPage(),
            "Мужчинам": MensPage(),
            "Женщинам": WomensPage()
        }
        for page in self.pages.values():
            self.page_stack.addWidget(page)

        main_layout.addWidget(self.page_stack)

        self.current_page_title = "Все модели"
        self.set_page("Все модели")

    def set_page(self, title):
        self.current_page_title = title
        self.catalog_path_label.setText(f"Каталог / {self.get_visible_category_title(title)}")
        self.category_title_label.setText(self.get_visible_category_title(title))
        self.update_product_count(title)

        page = self.pages[title]
        self.page_stack.setCurrentWidget(page)
        self.apply_sorting()

    def on_nav_button_clicked(self, title):
        self.set_page(title)

    def on_filter_changed(self):
        self.apply_sorting()

    def apply_sorting(self):
        current_page = self.pages[self.current_page_title]
        if hasattr(current_page, "filter_combobox"):
            # Если у страницы есть своя комбобокс, синхронизируем с основной
            current_page.filter_combobox.setCurrentIndex(self.sort_combobox.currentIndex())
        elif hasattr(current_page, "update_product_display"):
            # Если страница может обновить отображение
            current_page.filter_combobox.setCurrentIndex(self.sort_combobox.currentIndex())
            current_page.update_product_display()

    def update_product_count(self, title):
        products = get_product_data(title)
        self.product_count_label.setText(f"Найдено товаров: {len(products)}")

    def get_visible_category_title(self, internal_title):
        if internal_title == "Мужчинам":
            return "Мужская обувь"
        elif internal_title == "Женщинам":
            return "Женская обувь"
        return internal_title

    def on_search_clicked(self):
        print("🔍 Заглушка: поиск пока не реализован.")
