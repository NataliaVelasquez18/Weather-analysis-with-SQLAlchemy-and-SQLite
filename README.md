# Weather Analysis with SQLAlchemy and SQLite

Advanced Data Storage and Retrieval using SQLAlchemy to connect to and query a SQLite database. Then, use statistics like minimum, maximum, and average to analyze data.


## Business Problem

When opening a new venture and delivering profitability to investors depending on the type of buisness, several external conditions, such as weather, need to be taking in account before presenting the proposal.  In this project, we will be analyzing historical weather data.  The success of the project will depend mainly on **having warm weather and zero precipitation**. The purpose of this work, is to enable investors with the necessary information in order to make a well informed decision on wheather or not they should invest in the business.

Note: In this project in order to store our data, we will be using **SQLite** over **PostgreSQL** because according to our business case, SQLite is useful for testing and small apps that do not requiere expansion.  On the other hand, PostgreSQL is recommended when data integrity and reliability is highly concerned and to maintain complex databases without limitations.


## Getting Started

These instructions will get your SQLite database up and running on your local machine.


### Prerequisites

Before the installations there are some important concepts you need to know:  

**SQLite**, a version of SQL that lives in the computer or phone and provides a quick way to setup a database engine without requiring a server. SQLite's main purpose is to supporting quick testing and easy prototyping. 


**SQLAlchemy** is a library that facilitates the communication between Python programs and databases. Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.


### Installing

**First**, visit the [DB Browser for SQLite](https://sqlitebrowser.org/) site and download the last released version for your operating system.  **DB Browser for SQLite**, is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite.  It is for users and developers who want to create, search, and edit databases. DB4S uses a familiar spreadsheet-like interface, and complicated SQL commands do not have to be learned.

**Second**, download [Anaconda](https://docs.anaconda.com/anaconda/install/) for your operating system.  From your Anaconda Navigator you can launch Visual Studio Code and Jupyter Notebook.


### Download files

Download the folders and files contained in this repository on your local machine except for the png_images folder


---

### Analysis


1. **Precipitation in the last 365 days**: 

In this graph we have along the x-axis are the dates from the last 365 days from our dataset, and the y-axis is the total amount of precipitation for each day. We can observe that some months have higher amounts of precipitation than others.



<div style="text-align:center"><img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/precipitation_last_year.png" width="790" height="350" /></div>



2. **Temperature in the last 365 days**:


Drilling down into the last year's data and only analyzing the meteorological station with the largest number of observations, we can infer that a vast majority of the observations were over 67 degrees. If you count up the bins to the right of 67 degrees, you will get about 325 days where it was over 67 degrees when the temperature was observed.


<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/histogram.png" width="790" height="350" />



4. **Analysis on Temperature for the month of June from 2010 - 2017 including all the meteorological stations**:


* There are 1,700 observations of temperature of June days.
* As we can observe from the image and the stats below, 75% of our observations sit above the 73 deegrees. 
* The minimun temperature observed for a summer month such as June is 64 degrees.
* Being the mean and median almost identical mean that....
* A standard deviation of xxxx mean that...


<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/june_hist.png" width="790" height="350" />



<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/june_statistics.png" width="180" height="350" />



5. **Analysis on Temperature for the month of December from 2010 - 2016 including all the meteorological stations**:


* There are 1,5170 observations of temperature of December days.
* As we can observe from the image and the stats below, 75% of our observations sit above the 69 deegrees Farenheit. 
* The minimun temperature observed for a winter month such as December is 56 degrees.  
* Less than 10 observations sit below the 60 degrees.
* Being the mean and median almost identical mean that....
* A standard deviation of xxxx mean that...



<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/dec_hist.png" width="790" height="350" />



<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/dec_statistics.png" width="180" height="350" />


6. **Analysis on Precipitation from 2010 - 2017 including all the meteorological stations**:

* Null values (7%) on precipitation were removed from the dataset.

* We can observe that the vast majority of our data sits where there is zero precipitation.  Meaning, the rain was almos unexistent from 2010 to 2017.

<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/precip_hist.png" width="790" height="350" />



<img src="https://github.com/NataliaVelasquez18/Weather-analysis-with-SQLAlchemy-and-SQLite/blob/main/png_images/precip_statistics.png" width="180" height="350" />


---


### Recommendations

* 

---

## Acknowledgments

* Berkeley University Department of Data Science provided the training materials to develop this project.

---

## Author

* Contact: Natalia Velasquez
* Email: nativelasquez@gmail.com
* Twitter: @NatiVelasquez18

