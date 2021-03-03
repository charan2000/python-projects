import time
import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
percentage = round(battery.percent)

while(battery.percent!=95):
    Notification(title="Battery Information",
                 description="The Battery Percentage is: "+str(percentage)+"\nPlease disconnect to your charger :)",
                 duration=5).send()
    time.sleep(60)
