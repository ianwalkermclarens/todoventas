import re
from PyQt6.QtGui import QValidator


class input_datasNumbers(QValidator):
    def validate(self,string,index):
        pattern = re.compile("[0-9]+")
        if string=="":
            return QValidator.State.Acceptable, string, index
        if pattern.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index





class input_datasMails(QValidator):
    def validate(self,string,index):
        pattern = re.compile(r'^([\w\!\#$\%\&\'\*\+\-\/\=\?\^\`{\|\}\~]+\.)*[\w\!\#$\%\&\'\*\+\-\/\=\?\^\`{\|\}\~]+@((((([a-z0-9]{1}[a-z0-9\-]{0,62}[a-z0-9]{1})|[a-z])\.)+[a-z]{2,6})|(\d{1,3}\.){3}\d{1,3}(\:\d{1,5})?)$', re.VERBOSE | re.IGNORECASE)
        if string=="":
            return QValidator.State.Acceptable, string, index
            
        if pattern.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index


class input_datasPassword(QValidator):
    def validate(self,string,index):
        pattern = re.compile("[a-zA-Z0-9_]+")
        if string=="":
            return QValidator.State.Acceptable, string, index
        if pattern.fullmatch(string):
            return QValidator.State.Acceptable, string, index
        else:
            return QValidator.State.Invalid, string, index
