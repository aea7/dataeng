# A PySpark groupby
# You've seen how to use the dask framework and its DataFrame abstraction to do some calculations.
# However, as you've seen in the video, in the big data world Spark is probably a more popular choice for data processing.

# In this exercise, you'll use the PySpark package to handle a Spark DataFrame.
# The data is the same as in previous exercises: participants of Olympic events between 1896 and 2016.

# The Spark Dataframe, athlete_events_spark is available in your workspace.

# The methods you're going to use in this exercise are:

# .printSchema(): helps print the schema of a Spark DataFrame.
# .groupBy(): grouping statement for an aggregation.
# .mean(): take the mean over each group.
# .show(): show the results.

# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Read from db and put it into spark dataframe
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila", "customer", {"user":"repl","password":"password"})

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())

# In this exercise, you're going to run a PySpark file using spark-submit.
# This tool can help you submit your application to a spark cluster.

# For the sake of this exercise, you're going to work with a local Spark instance running on 4 threads.

# You can use spark-submit as follows:

# spark-submit --master local[4] /home/repl/spark-script.py