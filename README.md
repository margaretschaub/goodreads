This program scrapes a user’s Goodreads shelf and exports the data as a CSV file. Goodreads is a social-media, book-logging platform. I wrote this scraper to be used as a part of a bigger project, hopefully analyzing a user’s reading tendencies.

This program utilizes the Beautiful Soup Python library to parse HTML from goodreads.com. The Goodreads data resulted is the "read" shelf data for a particular user, including the following information for each book read: title, author, ISBN, number of pages, average rating, number of ratings, publication date, and date read. Any Goodreads user's data can be scraped with the user’s id number. This id number is found in the URL for the user’s profile. For example:
https://www.goodreads.com/user/show/145198074-maci. This user's id is 145198074.

To successfully run this program, you must input two variables: user-id and output file name for the final CSV. 
Insert user-id on line 102 and output file name on line 103.

The first element of this program generates links for each page of the user’s ‘read’ shelf. The number of links generated depends on the number of books read, which can vary from user to user. Luckily, the HTML contains a statement expressing how many books are shown per link as a fraction of the total the user has read. For example, "30 of 62 total books shown." Using regular expressions, this phrase can be distilled to the digits to calculate how many pages the user’s read shelf spans. For example, if 30 of 62 books are shown on the first page, the user's "read" shelf spans three pages, and three links must be generated to scrape the entirity of the user's library.

The next element uses the links generated and Beautiful Soup to scrape data for each book the user has read. The data is converted into a data frame using PANDAS and exported as a CSV. 

Some elements to be improved upon:

I would like to have this scraper grab the user’s rating for each book as well. Currently, this is published on Goodreads graphically with stars. 

Some books do not have an ISBN in the HTML within the ‘read shelf’ link. I plan to investigate how to fix this issue and improve the results generated to prevent null values. This solution would involve generating and following the link specific to the particular book that is missing the ISBN or other information.

Lastly, I envision this code can be expanded to scrape many shelves in a user's Goodreads library. The Goodreads platform includes other shelves like “Want to Read” and even user-created shelves. I would like to expand this program to scrape these other shelves, or perhaps have a variable where the shelf name can be specified.  