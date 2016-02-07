from datetime import datetime

def checkTime(hour):
    now = datetime.now().time()
    if now.hour == hour:
        return True
    return False