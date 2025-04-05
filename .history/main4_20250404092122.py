import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QAction, QPalette, QBrush, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer


class FirstWindow(QMainWindow):
    def __init__(self, switch_callback):
        super().__init__()

        self.setWindowTitle("Биринчи ойна")
        self.resize(500, 300)

        menubar = self.menuBar()
        self.create_menus(menubar, switch_callback)

        # Layout for the buttons
        layout = QVBoxLayout()

        # Label
        label = QLabel("Бу биринчи ойна")
        layout.addWidget(label)

        # Button 1
        self.button1 = QPushButton("Бirinchi tugma", self)
        self.button1.clicked.connect(self.on_button1_click)
        layout.addWidget(self.button1)

        # Button 2
        self.button2 = QPushButton("Ikkinchi tugma", self)
        self.button2.clicked.connect(self.on_button2_click)
        layout.addWidget(self.button2)

        # Set layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def paintEvent(self, event):
        # QWidgetning paintEvent metodida SVG rasmni chizish
        if self.renderer:
            painter = QPainter(self)
            self.renderer.render(painter)
            painter.end()

    def create_menus(self, menubar, switch_callback):
        home_menu = menubar.addMenu("🏠 Бош саҳифа")
        info_menu = menubar.addMenu("📂 Маълумотлар")
        settings_menu = menubar.addMenu("⚙️ Созламалари")
        help_menu = menubar.addMenu("❓ Ёрдам")

        switch_action = QAction("Иккинчи ойнани очиш", self)
        switch_action.triggered.connect(
            lambda: switch_callback(1))  # Ikkinchi oynaga o'tish
        home_menu.addAction(switch_action)

        info_menu.addAction(QAction("Файл маълумотлари", self))
        settings_menu.addAction(QAction("Дастур созламалари", self))
        help_menu.addAction(
            QAction("Ёрдамни кўриш", self, triggered=self.show_help))

    def show_help(self):
        QMessageBox.information(self, "Ёрдам", "Бу биринчи ойна ёрдами.")

    def on_button1_click(self):
        QMessageBox.information(
            self, "Тугма 1", "Сиз биринчи тугмани босдингиз!")

    def on_button2_click(self):
        QMessageBox.information(
            self, "Тугма 2", "Сиз иккинчи тугмани босдингиз!")


class SecondWindow(QMainWindow):
    def __init__(self, switch_callback):
        super().__init__()

        self.setWindowTitle("Иккинчи ойна")
        self.resize(500, 300)

        menubar = self.menuBar()
        self.create_menus(menubar, switch_callback)

        layout = QVBoxLayout()
        label = QLabel("Бу иккинчи ойна")
        widget = QWidget()
        layout.addWidget(label)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def create_menus(self, menubar, switch_callback):
        home_menu = menubar.addMenu("🏠 Бош саҳифа")
        info_menu = menubar.addMenu("📂 Маълумотлар")
        settings_menu = menubar.addMenu("⚙️ Созламалари")
        help_menu = menubar.addMenu("❓ Ёрдам")

        switch_action = QAction("Биринчи ойнани очиш", self)
        switch_action.triggered.connect(
            lambda: switch_callback(0))  # Birinchi oynaga o'tish
        home_menu.addAction(switch_action)

        info_menu.addAction(QAction("Фойдаланувчи маълумотлари", self))
        settings_menu.addAction(QAction("Тизим созламалари", self))
        help_menu.addAction(
            QAction("Ёрдамни кўриш", self, triggered=self.show_help))

    def show_help(self):
        QMessageBox.information(self, "Ёрдам", "Бу иккинчи ойна ёрдами.")


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.first_window = FirstWindow(self.switch_window)
        self.second_window = SecondWindow(self.switch_window)

    def switch_window(self, window_num):
        if window_num == 0:
            self.second_window.hide()
            self.first_window.show()
        elif window_num == 1:
            self.first_window.hide()
            self.second_window.show()

    def run(self):
        self.first_window.show()
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = MainApp()
    app.run()
