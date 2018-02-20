import datetime

now = datetime.datetime.today()
position = now.weekday() #thesi imeras
year = now.year #twrini xronia
month = now.month #twrinos minas
day = now.day # twrini imera
counter = 0

for i in range(11):
    imerominia = datetime.date(year,month,day)
    if imerominia.weekday() == position:
        counter = counter + 1
    year = year + 1

print (counter, "Μερες είναι" , day,"ες" , "του", month, "ου μηνα" , )
