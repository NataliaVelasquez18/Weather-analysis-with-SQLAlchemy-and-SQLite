# surfs_up

Overview of the statistical analysis:

The purpose of the analysis is well defined. (3 pt)
Results:

There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)
Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)

Investing in Waves and Ice Cream


# Weather Analysis with SQLAlchemy and SQLite

Advanced Data Storage and Retrieval using SQLAlchemy to connect to and query a SQLite database. Then, use statistics like minimum, maximum, and average to analyze data.

## Getting Started

These instructions will get your SQLite database up and running on your local machine.


### Prerequisites

Before the installations there are some important concepts you need to know:  

**SQLite**, a version of SQL that lives in the computer or phone and provides a quick way to setup a database engine without requiring a server. SQLite's main purpose is to supporting quick testing and easy prototyping. When prototyping, it is not ideal to set up a SQL database server just to test something out. You can compare SQLite databases to a CSV or Excel file: each SQLite database can have one or more tables with columns and rows, and it is stored as a file on your computer. The key difference between SQLite databases and a CSV or Excel file is that you can write queries for it.

**When to use SQLite and PostgreSQL?**

**SQLite** is highly useful for: Standalone apps, small apps that don’t require expansion, apps need to read or write files to disk directly, the internet of things devices, developing and even testing.

**PostgreSQL** is recommended when: Data integrity and reliability is highly concerned, custom Procedures which is extensible to run the complex task, complexity with ease. PostgreSQL gives you the functionality to maintain such a complex database smoothly without limitations.

**SQLAlchemy** is a library that facilitates the communication between Python programs and databases. Most of the times, this library is used as an Object Relational Mapper (ORM) tool that translates Python classes to tables on relational databases and automatically converts function calls to SQL statements.


### Installing

**First**, visit the [DB Browser for SQLite](https://sqlitebrowser.org/) site and download the last released version for your operating system.  **DB Browser for SQLite**, is a high quality, visual, open source tool to create, design, and edit database files compatible with SQLite.  It is for users and developers who want to create, search, and edit databases. DB4S uses a familiar spreadsheet-like interface, and complicated SQL commands do not have to be learned.

**Second**, download [Anaconda](https://docs.anaconda.com/anaconda/install/) for your operating system.  From your Anaconda Navigator you can launch Visual Studio Code and Jupyter Notebook.


### Download files

Download the folders and files contained in this repository on your local machine except for the png_images folder


---


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
