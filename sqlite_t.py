import sqlite3

conn = sqlite3.connect('t.db')

# conn.execute('''CREATE TABLE student(
# user1 varchar(255),
# user2 varchar(255),
# day date
# );''')

conn.execute('''INSERT INTO student VALUES ('man','mu','saturday')''')

conn.commit()
conn.close()
