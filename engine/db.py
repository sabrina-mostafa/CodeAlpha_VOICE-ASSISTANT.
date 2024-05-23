import csv
import sqlite3

con = sqlite3.connect("sabreen.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'code blocks', 'C:\\Program Files\\CodeBlocks\\codeblocks.exe')"
# #query = "DELETE FROM sys_command WHERE id=2".format(id)    # To delete a row
# cursor.execute(query)
# con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "DELETE FROM web_command WHERE id=10".format(id)      # To delete a row
query = "INSERT INTO web_command VALUES (null,'chat gpt', 'https://chat.openai.com/')"
cursor.execute(query)
con.commit()