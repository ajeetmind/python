import psycopg2

# can also use a standard URL format for the connection string:
#   psycopg2.connect('postgres://username:password@host:port/database')
with psycopg2.connect('postgresql://doadmin:d7o7kx6q4vp3r6q9@private-finqle-db-postgresql-ams3-staging-do-user-5272736-0.db.ondigitalocean.com:25060/defaultdb?sslmode=require')as connection:
    connection.autocommit = True

    with connection.cursor() as cursor:
    # list all tables in this database
     cursor.execute('select table_schema, table_name from information_schema.tables')
     results = cursor.fetchall()
    print(results)
