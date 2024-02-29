from PyQt6.QtGui import QFontDatabase
import os


class file_sources():
        def __init__(self):
            ROOT_DIR = os.path.dirname(__file__)
            dirname_ttf = os.path.join(ROOT_DIR,"sources","Idealist_Sans_Light.ttf")
            dirname_img = os.path.join(ROOT_DIR,"sources")
            id = QFontDatabase.addApplicationFont(dirname_ttf)
            if id < 0: print("Error")
            self.families = QFontDatabase.applicationFontFamilies(id)
            self.dirname_img = dirname_img