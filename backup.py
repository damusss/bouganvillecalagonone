import shutil
import datetime
import os

now = datetime.datetime.now()
os.system("py manage.py dumpdata > db.json")
shutil.copyfile(
    "db.sqlite3",
    rf"D:\BACKUP\General_Backup\SiteDB\db{now.day}-{now.month}-{now.year}-{now.hour}-{now.minute}.sqlite3",
)
shutil.copyfile(
    "db.json",
    rf"D:\BACKUP\General_Backup\SiteDB\db{now.day}-{now.month}-{now.year}-{now.hour}-{now.minute}.json",
)
print("Backup Created")
