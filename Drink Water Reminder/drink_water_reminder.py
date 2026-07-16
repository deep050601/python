import time
from plyer import notification

for i in range(5):
   time.sleep(10)
   notification.notify(
      title="drink water reminder",
      message="This is the notification body",
      app_name="My App",
      
      timeout=10,  
   )
