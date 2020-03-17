import sqlite3

connection = sqlite3.connect('data.db')
cursor= connection.cursor()

create_table = "Create TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
cursor.execute(create_table)

#create_table = "Create TABLE IF NOT EXISTS items(name text, price real)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
#cursor.execute(create_table)

#create_table = "Create TABLE IF NOT EXISTS geometry_columns(id INTEGER PRIMARY KEY, name text, score FLOAT, latitude FLOAT, longitude FLOAT)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
#cursor.execute(create_table)

create_table = "Create TABLE IF NOT EXISTS geometry_columns(id INTEGER PRIMARY KEY, idm text,date text, name text, telephone int, email text, categorie text, toelichting text, XCoordinaat FLOAT, YCoordinaat FLOAT)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
cursor.execute(create_table)


'''create_table = "Create TABLE IF NOT EXISTS spatial_ref_sys(srid INTEGER, auth_name TEXT, auth_srid TEXT, srtext TEXT)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
cursor.execute(create_table)

create_table = "Create TABLE IF NOT EXISTS sql(ogc_fid INTEGER, GEOMETRY BLOB, fid BIGINT, score FLOAT)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
cursor.execute(create_table)'''

#create_table = "Create TABLE IF NOT EXISTS sqlite_sequence(name name, seq seq)" #Auto incrementing ID (id INTEGER PRIMARY KEY)
#cursor.execute(create_table)

#cursor.execute("INSERT INTO items VALUES ('test', 10.99)")
connection.commit()
connection.close()