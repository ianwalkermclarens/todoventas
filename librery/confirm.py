from PyQt6.QtWidgets import QMessageBox

class confirms():
    def __init__(self,messages):
        dlg = QMessageBox()
        dlg.setWindowTitle("Todoventas - Error")
        dlg.setText(messages)
        buttons = (QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes)
        dlg.setStandardButtons(buttons)
        dlg.setIcon(QMessageBox.Icon.Warning)
        ret = dlg.exec()
        if ret==QMessageBox.StandardButton.Yes:
            self.resultado = 1
        else:
            self.resultado = 0

    def getResult(self):
        return self.resultado
        
        
