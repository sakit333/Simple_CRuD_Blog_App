# import sqlite3
# import pandas as pd

# conn = sqlite3.connect('data.db')
# df = pd.read_sql_query('SELECT * FROM blogtable;', conn)
# df.to_csv('blogtable.csv', index=False)


import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('data.db')

# Open a file to write the dump
with open('dump.sql', 'w', encoding='utf-8') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

conn.close()

print("Database dump saved to dump.sql")
