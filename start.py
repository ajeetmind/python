import psycopg2

# can also use a standard URL format for the connection string:
#   psycopg2.connect('postgres://username:password@host:port/database')
with psycopg2.connect('')as connection:
    connection.autocommit = True

    with connection.cursor() as cursor:
    # list all tables in this database
     cursor.execute('select table_schema, table_name from information_schema.tables')
     results = cursor.fetchall()
    print(results)
