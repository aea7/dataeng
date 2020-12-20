# A PostgreSQL database is set up in your local environment, which contains this database schema.
# It's been filled with some example data. You can use pandas to query the database using the read_sql() function.
# You'll have to pass it a database engine, which has been defined for you and is called db_engine.

# The pandas package imported as pd will store the query result into a DataFrame object, so you can use
# any DataFrame functionality on it after fetching the results from the database.
# Complete the SELECT statement
import pandas as pd

data = pd.read_sql("""
SELECT first_name, last_name FROM "Customer"
ORDER BY last_name, first_name
""", db_engine)

# Show the first 3 rows of the DataFrame
print(data.head(3))

# Show the info of the DataFrame
print(data.info())

# JOIN:

data = pd.read_sql("""
SELECT * FROM "Customer"
INNER JOIN "Order"
ON "Order"."customer_id"="Customer"."id"
""", db_engine)

# Show the id column of data
print(data.id)