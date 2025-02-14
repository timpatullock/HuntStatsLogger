import sys
import ctypes
import platform
from resources import *

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFontDatabase, QIcon
from PyQt6.QtCore import Qt
from resources import *
from style.process import process_style

from MainWindow.MainWindow import MainWindow

class App(QApplication):
    def __init__(self, argv=None):
        super().__init__(argv)

if __name__ == '__main__':
    log('launching app')
    # fixing scaling issue for multiple monitors/multiple DPI:
    if platform.system() == "Windows" and int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    

    app = App(sys.argv)
    stylesheet_f = resource_path('./assets/style/style.qss')
    style_vars_f = resource_path('./assets/style/variables.txt')
    style_vars = {}
    with open(style_vars_f,'r') as f:
        for line in f.readlines():
            key_value = line.strip().replace(' ','').split("=")
            if len(key_value) > 1:
                style_vars[key_value[0]] = key_value[1]

    stylesheet = process_style(stylesheet_f,style_vars)
    #stylesheet = open(resource_path('./assets/MaterialDark.qss'), 'r').read()
    app.setStyleSheet(stylesheet)

    QFontDatabase.addApplicationFont(resource_path(
        './assets/fonts/LibreBaskerville/LibreBaskerville-Regular.ttf'))
    QFontDatabase.addApplicationFont(
        resource_path('./assets/fonts/Ubuntu/Ubuntu-R.ttf'))
    QFontDatabase.addApplicationFont(
        resource_path('./assets/fonts/Roboto/Roboto/static/RobotoSerif-Regular.ttf'))

    app.setQuitOnLastWindowClosed(False)

    window = MainWindow()
    window.setBaseSize(1024, 768)
    window.show()

    app.setWindowIcon(QIcon(resource_path('assets/icons/hsl.ico')))
    if settings.value("xml_path", "") == "":
        window.mainframe.settingsWindow.show()

    app.exec()