from tools import Event
#from openpyxl import Workbook

event1 = Event("D665", "12:12:14", "PWR MODULE")
print(event1.eventActualCousingPart)
print(event1.eventTime)
print(event1.eventWorkOrder)
