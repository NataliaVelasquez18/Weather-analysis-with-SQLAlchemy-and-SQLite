# surfs_up

Overview of the statistical analysis:

The purpose of the analysis is well defined. (3 pt)
Results:

There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)
Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)

Investing in Waves and Ice Cream


# Weather Analysis with SQLAlchemy and SQLite

Advanced Data Storage and Retrieval using SQLAlchemy to connect to and query a SQLite database. Then, using statistics like minimum, maximum, and average to analyze data.

## Getting Started

These instructions will get your PostgreSQL database up and running on your local machine.


### Prerequisites

Before the installations there are some important concepts you need to know:  

**SQLite**, a version of SQL that lives in the computer or phone and provides a quick way to setup a database engine without requiring a server. SQLite's main purpose is to supporting quick testing and easy prototyping. When prototyping, it is not ideal to set up a SQL database server just to test something out.  All SQLite databases are flat files, which means that they don't have relationships that connect the data to anything else. As a result, flat files can be stored locally.You can compare SQLite databases to a CSV or Excel file: each SQLite database can have one or more tables with columns and rows, and it is stored as a file on your computer. The key difference between SQLite databases and a CSV or Excel file is that you can write queries for it.




### Installing

**First**, visit the **PostgresSQL** [download website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) - The web framework used to initiate your download. Be sure to choose the correct download option for your operating system. Both Postgres and pgAdmin are downloaded together as a package. Be sure to Not select the latest Postgres version, we're installing a previous version to the latest because it is a more stable release.  During installation, you'll need to create a password. Be sure to record it, as you'll use it to access your SQL database.  

An InstallBuilder window will show the components selected for installation. Be sure to uncheck Stack Builder's box. Stack Builder is used to install Postgres add-ons, but we won't need it for our project.

<img src="https://github.com/NataliaVelasquez18/Employee-database/blob/main/png_images/uncheck_stack_builder.png" width="350" height="250" />


To confirm your installation, start pgAdmin (a new browser window will launch) and double-click to connect to the default server and enter your password.


<img src="https://github.com/NataliaVelasquez18/Employee-database/blob/main/png_images/confirm_pgadmin_installation.png" width="390" height="250" />



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
