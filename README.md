social-environment
===

## Build

#### Status
![Build Status](http://build.social-environment.com/jenkins/buildStatus/icon?job=social-environment)

#### Code Coverage
![Code Coverage](http://build.social-environment.com/jenkins/job/social-environment/cobertura/graph)

## About This Project

Social-Environment is an application that allows visitors to check their local environmental score and share it with friends.  Given a location, visitors will see a local air quality score based on EPA <a href="http://www3.epa.gov/airdata/ad_basic.html">air quality data</a> and can drill down to see individual contributing factors to the local air quality score.

For a given location, Social-Environment displays an Air Quality Score which uses EPA's Air Quality Index to rate air quality related to known pollutants that were measured in that area within the past year.


##Design Approach
**<a href="http://www.excella.com">Excella Consulting</a>** put a small team together and followed an agile development methodology to build **Social-Environment** in an iterative, incremental manner. The cross-functional team, comprised of analysts and developers, began with a brainstorming session and defined an initial Minimum Viable Product (MVP). Not being co-located, and working on the project during off-hours, the team used Slack to communicate and held conference calls every three days to ensure proper coordination.

The self-organized team not only fulfilled their individual roles in the design and development process, but also helped where needed to deliver a quality product. Utilizing **[GitHub issues](https://github.com/excellaco/social-environment/issues)**, the team created and groomed a Kanban backlog, discussed design decisions, and tracked bugs.


##Initial Concept
The team met to brainstorm initial concepts after having reviewed available EPA datasets for consumption.  We landed on Air Quality and Toxic Release Inventory data, as we thought this data might provide an opportunity for an interesting visualization.

We defined a <a href="https://github.com/excellaco/social-environment/wiki/User-Persona">user persona</a> for our prototypical user and developed it with this persona in mind.

We developed some <a href="https://github.com/excellaco/social-environment/issues/3">napkin sketches</a> to visualize our concept.  Later we worked with our graphics designer to produce some custom art for the project.

We decided to use Kanban and developed a backlog of tasks that defined the Minimum Viable Product we wanted to build for our submission.  This can be found by viewing the <a href="https://github.com/excellaco/social-environment/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Minimum+Viable+Product%22">Minimum Viable Product milestone</a> in our Github repository.  We defined additional issues and recorded enhancement requests and bugs as <a href="https://github.com/excellaco/social-environment/issues">Issues</a>.

We agreed on a meeting cadence given everyone's holiday and work schedules, and decided to use Slack for daily communication.

In the first three days we established a github repository for our code and issues.  We decided to use a Continuous Integration server to provide automated testing and deployment.  We developed an automated mechanism to download raw data files and load the pertinent data into a relational database, and a simple mechanism to display those data points on a map.  And we analyzed the data sets and data dictionaries made available by EPA to better understand the data and its usage to determine how we could use them in our visualization.

##Data
The team chose the EPA Air Quality data as the source for the Social-Environment app.  The application contains code to download the EPA data from an EPA FTP site (in Excel format) and imports the data into a Postgres database for processing by the API.  Among other fields, the dataset contains latitude, longitude, pollutant, various quantity measurements, and a year for every air quality measurement recorded.  We ran these raw data through an <a href="https://github.com/excellaco/social-environment/wiki/Air-Quality-Calculation">algorithm</a>, leveraging the EPA Air Quality Index, to generate an easy-to-understand air quality score.  This score can be applied to a person's location by taking into account the air quality scores of all pollution measurements in a 2 mile radius for the given year.


##API Methods
The design began with creating an API to access the air quality data.  The challenge was to create a function that, given a latitude and longitude, would return a series of datapoints within an arbitrary radius of that latitude and longitude.  <a href="http://www.excella.com">Excella</a> used a haversine function to do so.  Then, each datapoint is evaluated to determine an air quality score.  The API is designed to provide consumers both the relative air quality score for a region, given a location and year; and to provide the discrete pollutant occurrences for the same location and year.


#### map_score
GET `/api/v1/map_score/`

The map_score service takes as optional parameters a latitude, longitude, and year and returns the air quality score of the area bounded by a 2 mile radius around the specified lat/lon.  The score is determined by choosing the highest (most hazardous) score for any compound in the radius for the specified year.

Example: `http://social-environment.com/api/v1/map_score/?latitude=38.06&longitude=-77.09&year=2013`

#### airquality
GET `/api/v1/airquality`

The airquality service takes as parameters a latitude, longitude, and year and returns a collection of air quality data points within an area bounded by a 2 mile radius around the specified latitude and longitude.

Example: `http://social-environment.com/api/v1/airquality/?latitude=38.06&longitude=-77.09&year=2013`


##Tech Stack

#### Web App - Front End

Our public facing web site is built in JavaScript, jQuery, HTML and third party JavaScript libraries. We used Bootstrap for our UI components, d3.js to create visualizations, and jQuery to make RESTful API calls to access the dataset.

#### Web App - Back End

The backend provides internal services not exposed to the public, as well as an API for the front end to access the data.  The backend runs on Python 2.7 with Django 1.8.7 and Wagtail as a Content Management System.

Utilizing Wagtail as a CMS will allow the expansion of the site as well as easy administration of new content outside the scope of the initial release. Wagtail also includes a built-in RESTful service (Django REST Framework) to expose the data model.  While the RESTful API is currently utilized by the front end application, it is also available for potential future web applications to interact with the data with no changes required to the back end.

The site also includes a basic administration console that allows our staff and super users to create new users, groups, permissions, delete, edit and create new air quality data points.

#### Data

The backend service stores data in a SQL database and limits its interface through the Django Object Relationship Model (ORM). The use of the ORM prevents most SQL injection attacks and other vulnerabilities associated with manual SQL manipulation.  The ORM also handles the forward and backward migrations of the database, greatly reducing the risk of data model changes.

Django ORM is agnostic to the specific backend database software. This affords us the ability to not be locked into any single database. The production server uses a PostgreSQL database.  While testing locally, the developers often used a SQLite database that sacrifices performance for a simpler setup.

#### Infrastructure

The resources for the example deployed version of social-environment are all managed in AWS. The build server is a Ubuntu EC2 instance running Jenkins polling our source control management at github. The production application server is an AWS Linux instance running the web application behind Apache, as well as the PostgreSQL database service. Both of these EC2 instances are on a secluded Virtual Private Cloud with a configured Internet Gateway to allow access to the internet. A Security Group is configured to permit access only through approved ports and protocols.


## Getting Started 

#### Prerequisites
 * git
 * python 2.7
 * pip
 * virtualenv
 * libjpeg-dev
   * Redhat: `yum install libjpeg-devel`
   * Debian: `apt-get install libjpeg-dev`
   * Mac with homebrew: `brew install libjpeg`
 * PostgreSQL server (optional for dev environment)

#### Setting up a Dev Environment

The following steps will set up social-environment on a Unix-based operating system.

```shell
git clone https://github.com/excellaco/social-environment
cd social-environment

# If setting up a dev environment and you want to use sqlite instead of postgres, comment out the psycopg2 line
# in requirements.txt before continuing.

# Install the python dependencies
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Create a secret key used to secure the webapp
export SECRET_KEY="1"

# Load the data model, this will take several minutes
./manage.py migrate

# Start the webserver
./manage.py runserver
```

At this point you can access the site at http://localhost:8000/. If running inside a virtual machine, you'll want to run `./manage.py runserver 0.0.0.0:8000` so that the server accepts external traffic.


####Testing
To execute the tests, run the server (if it's not already running)

    $ python manage.py runserver

Then in a separate terminal window, execute the tests

	$ nosetests
    
####Code Coverage
To generate a code coverage report, use the jenkins command. It will also run your tests. 

```shell
./manage.py jenkins --enable-coverage
ls reports
```


## Deployment

#### Continuous Integration

<a href="http://www.excella.com">Excella</a> uses Jenkins as a Continuous Integration Server and established a delivery pipeline to build, and test the software.  This action is performed automatically every time new code is pushed to the git repository.
* The Jenkins <a href="http://build.social-environment.com/jenkins/job/social-environment"/>build history</a> is available to the public.
* Jenkins is configured to use Cobertura, a static code analysis tool, to report unit test coverage and other analysis.  Test results are available <a href="http://build.social-environment.com/jenkins/job/social-environment/75/cobertura/ ">here</a>.
* Test results and code coverage are also automatically updated at the top of this README.

#### Continuous Delivery

If the tests pass, Jenkins will automatically deploy the updates to our app server.  This is executed using a secure SSH connection and deployment does not require root access to the app server.
