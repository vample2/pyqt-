import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import uic
import images_rc


# 样式配置类
class Settings:
    TIME_ANIMATION = 250
    MENU_WIDTH = 200
    MENU_COLLAPSED_WIDTH = 80

    DEFAULT_STYLESHEET = """
    QPushButton {
        background-image: url(:/background/文档.png);  /* 设置背景图像 */
        background-position: left center;  /* 背景图像居中 */
        background-repeat: no-repeat;  /* 不重复背景图像 */
        border: none;  /* 去除按钮边框 */
        border-left: 22px solid transparent;
        background-color: rgb(37, 41, 48);  /* 设置背景色 */
        text-align: left;  /* 文字左对齐 */
        padding: 50px;

        color: rgb(113, 126, 149);  /* 设置文字颜色 */
    }
    QPushButton:hover {
        background-color: rgb(89, 47, 49);
    }
    QPushButton:pressed {
        background-color: rgb(189, 147, 249);
    }
    """

    MENU_SELECTED_STYLESHEET = """
    QPushButton {
        background-image: url(:/background/文档.png);
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 22px solid qlineargradient(
            spread:pad, 
            x1:0.034, y1:0, 
            x2:0.216, y2:0, 
            stop:0.499 rgba(255, 121, 198, 255), 
            stop:0.5 rgba(85, 170, 255, 0)
        );
        background-color: rgb(40, 44, 52);
        text-align: left;
        padding: 50px;
        color: rgb(113, 126, 149);
    }
    """


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 加载UI
        self.ui = uic.loadUi('./untitled.ui', self)

        # 信号连接
        self.ui.pushButton.clicked.connect(self.toggleMenu)
        self.ui.pushButton_2.clicked.connect(lambda: self.setPage(self.ui.page_2, self.ui.pushButton_2))
        self.ui.pushButton_3.clicked.connect(lambda: self.setPage(self.ui.page, self.ui.pushButton_3))
        self.ui.pushButton_4.clicked.connect(lambda: self.setPage(self.ui.page_4, self.ui.pushButton_4))

        self.ui.show()

    def setAllMenuButtonsStyle(self,except_widget: str = None):
        """重置所有菜单按钮为默认样式"""
        # for btn in self.menu_buttons:
        #     btn.setStyleSheet(Settings.DEFAULT_STYLESHEET)

        for w in self.ui.widget.findChildren(QPushButton):
            if w.objectName() != except_widget:
                w.setStyleSheet(Settings.DEFAULT_STYLESHEET)

    def setPage(self, page_widget, clicked_button: QPushButton):
        """切换页面并高亮选中按钮"""
        self.ui.stackedWidget.setCurrentWidget(page_widget)
        self.setAllMenuButtonsStyle()
        # 设置当前按钮为选中样式（在默认样式基础上追加）
        clicked_button.setStyleSheet(Settings.MENU_SELECTED_STYLESHEET)

    def toggleMenu(self):
        """展开或收起左侧菜单栏"""
        menu = self.ui.widget
        current_width = menu.width()
        target_width = (
            Settings.MENU_WIDTH
            if current_width == Settings.MENU_COLLAPSED_WIDTH
            else Settings.MENU_COLLAPSED_WIDTH
        )

        animation = QPropertyAnimation(menu, b"minimumWidth")
        animation.setDuration(Settings.TIME_ANIMATION)
        animation.setStartValue(current_width)
        animation.setEndValue(target_width)
        animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
        animation.start()
        self.animation = animation  # 保持引用防止动画被GC


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
