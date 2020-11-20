DATA 612: Assignment 5

This folder works with the dataset provided by the author of the "Easy And Fun With BeautifulSoup". The data are extracted from the Yahoo Finance website and include 90 days of data from November 21, 2019 until April 28, 2020.

I first show the current data types of the data set. Most of the columns are categorized as string. I then convert the company_name to categorical. I want to convert some of the other columns to float or int but run into a problem when trying to split and strip either a comma and a plus sign or a comma and a negative sign. I will continue to work on this because I feel it will be needed to completely clean and tidy the data before visualization. I also drop columns that I are not needed once they have been split. I convert one of the int column to a string.
