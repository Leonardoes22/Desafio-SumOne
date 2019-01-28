# Book Organizer for Python 3.6.0

# Requirements
This program uses the CSV and OPERATOR libraries, which are usually included in standard Python installations. If they are not installed please use a packge manager such as Pip to get them into your machine.

This program will return an organized book collection in the form of a csv file called "Organized Collection.csv".
For this program to work there should be 2 csv files in the same folder: 

-"collection.csv" which will hold the the book collection to be organized and has the following format. Each line represents a different book and has the form of "title,author,year" where year is the edition year of the book.

-"config.csv" which will provide the Organizer a the set of rules on how to sort the books. for each different atribute to be sorted there should be a line with the atribute name and the order "asc"(ascendent) and "desc"(descendent) as "author,desc".

It is important to remember that the priority of the lines are ascendent, so the atribute in the last line will have the greatest priority.

#Exemple

collection.csv
|1 Java How To Program,Deitel & Deitel,2007                           |
|2 Internet & World Wide Web: How to Program,Deitel & Deitel,2007     |
|3 Head First Design Patterns,Elisabeth Freeman,2004                  |
|4 Patterns of Enterprise Application Architecture,Martin Fowler,2002 |

config.csv
|1 title,desc  |  |
|2 author,desc |  | Priority
|3 year,asc    |  V

This will result in 

organized collection.csv
|1 Patterns of Enterprise Application Architecture,Martin Fowler,2002 |
|2 Head First Design Patterns,Elisabeth Freeman,2004                  |
|3 Java How To Program,Deitel & Deitel,2007                           |
|4 Internet & World Wide Web: How to Program,Deitel & Deitel,2007     |
