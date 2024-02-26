from PyQt6.QtWidgets import QMessageBox

class alerts():
    def __init__(self,messages):
        dlg = QMessageBox()
        dlg.setWindowTitle("Banco W - Error")
        dlg.setText(messages)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes)
        dlg.setIcon(QMessageBox.Icon.Critical)
        button = dlg.exec()
