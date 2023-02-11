
from win32gui import GetWindowText, GetForegroundWindow
while True:
    print(GetWindowText(GetForegroundWindow()))
