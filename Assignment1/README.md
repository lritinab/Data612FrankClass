DATA 612: Assignment 1

This folder loads and does a basic examine of the dataset provided by the author of the "Easy And Fun With BeautifulSoup". The data are extracted from the Yahoo Finance website and include 90 days of data from November 21, 2019 until April 28, 2020.

In the Jupiter notebook, I import the pandas and the dataset, showing the first 20 rows and the last 15 rows. I then show the column names as well as the column data types. The shape of the data shows that there are 67,905 rows and 19 columns. The column "beta (3Y Monthly)" has the only data type that is numeric and can be aggregated to show the mean. I group the "beta (3Y Monthly)" mean by date.