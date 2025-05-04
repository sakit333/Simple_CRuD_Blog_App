import psycopg2

# PostgreSQL connection
conn = psycopg2.connect(
    dbname='mydb',      # replace with your database name
    user='postgresql',      # replace with your username
    password='postgresql',  # replace with your password
    host='db',     # or your Docker/Postgres container name
    port='5432'
)
c = conn.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS blogtable (
            author TEXT,
            title TEXT PRIMARY KEY,
            article TEXT,
            postdate DATE
        );
    ''')
    conn.commit()

def add_data(author, title, article, postdate):
    c.execute('''
        INSERT INTO blogtable (author, title, article, postdate)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (title) DO NOTHING;
    ''', (author, title, article, postdate))
    conn.commit()

def view_all_notes():
    c.execute('SELECT * FROM blogtable')
    data = c.fetchall()
    return data

def view_all_titles():
    c.execute('SELECT DISTINCT title FROM blogtable')
    data = c.fetchall()
    return data

def get_single_blog(title):
    c.execute('SELECT * FROM blogtable WHERE title = %s', (title,))
    data = c.fetchall()
    return data

def get_blog_by_title(title):
    c.execute('SELECT * FROM blogtable WHERE title = %s', (title,))
    data = c.fetchall()
    return data

def get_blog_by_author(author):
    c.execute('SELECT * FROM blogtable WHERE author = %s', (author,))
    data = c.fetchall()
    return data

def get_blog_by_msg(article):
    search_term = f"%{article}%"
    c.execute('SELECT * FROM blogtable WHERE article ILIKE %s', (search_term,))
    data = c.fetchall()
    return data

def edit_blog_author(author, new_author):
    c.execute('UPDATE blogtable SET author = %s WHERE author = %s', (new_author, author))
    conn.commit()

def edit_blog_title(title, new_title):
    c.execute('UPDATE blogtable SET title = %s WHERE title = %s', (new_title, title))
    conn.commit()

def edit_blog_article(title, new_article):
    c.execute('UPDATE blogtable SET article = %s WHERE title = %s', (new_article, title))
    conn.commit()

def delete_data(title):
    c.execute('DELETE FROM blogtable WHERE title = %s', (title,))
    conn.commit()
