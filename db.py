import sqlite3
con = sqlite3.connect("connect.db")
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE posts
               (id integer PRIMARY KEY, 
               name text NOT NULL, 
               age integer NOT NULL,
               contact text NOT NULL, 
               title text NOT NULL, 
               description text NOT NULL)''')

cur.execute('''CREATE TABLE replies
               (id integer PRIMARY KEY, 
               postid integer NOT NULL,
               name text NOT NULL, 
               age integer NOT NULL,
               contact text NOT NULL, 
               title text NOT NULL, 
               description text NOT NULL)''')

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()