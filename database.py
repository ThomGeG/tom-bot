import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password"
)

db_cursor = mydb.cursor()
CHANGELOG_DIR = "database_scripts"
changelogs = [os.path.join(CHANGELOG_DIR, fname) for fname in os.listdir(CHANGELOG_DIR)]

for changelog in changelogs:
    db_cursor.execute(open(changelog, 'r').read())
