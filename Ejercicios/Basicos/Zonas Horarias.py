#Zonas Horarias

from datetime import datetime
from pytz import timezone
import pytz

#print(pytz.all_timezones) Ver todas las zonas horarias (Ej. Europe/Madrid)


print ("Asia/Tokyo:", datetime.now(pytz.timezone('Asia/Tokyo')))
print ("Europe/Madrid:", datetime.now(pytz.timezone('Europe/Madrid')))