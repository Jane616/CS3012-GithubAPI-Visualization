# CS3012-GithubAPI-Visualization
files for TCD CS3012 coursework on accessing Github API and do visualization

# documents
Test.py is a simple python program using PyGithub library to perform repository search, where I learn how to use the PyGithub library.
result folder is the json files exported from querying database, and the svg graph generated by d3.
GithubVisualization is the django project in which data collection, store to database, export to json and display with d3 are implemented.

# goal
The goal of this project is to find out the programming language diversity in Google and Microsoft employees, and the difference between the two companies.

# overview
This project is done using Python and Javascript, d3.js, Pygithub and Django libraries are used. The project is setup with the django local web server and sqlite database. There are 3 applications in this project: collect, export and display. The collect application interrogate the github API for information about Google and Microsoft employees and the languages used in their repositories, then insert those information into sqlite database. The export application query the database, calculate required information and export 3 json files corrresponding to 3 graphs to the folder where manage.py is. The display application display the 2 parts of this visualization with 3 graphs in 3 webpages, using the json files exported in export application.

The db.sqlite3 in the project folder is already inserted with collected data from github. The 3 json files in project folder is the json files exported by the application.

# set up
download GithubVisualization folder.
install Pygithub, Django library using pip --install.
navigate terminal to where the manage.py is.
type in command: python manage.py runserver.
After the server is setup, open browser and type in url: 127.0.0.1:8000/ .
Then you will see the home page that navigate to the three applications.

# collect
Collect application will first ask for github username and password, if the inputs are valid credencials, then the data collection will begin. The collect application interrogate the github API for information about Google and Microsoft employees and the languages used in their repositories, then insert those information into sqlite database. THe progress of the collection process can be seen from the terminal, the whole process takes about 5-6 hours. After the process is completed then a message "done!" should appear, but it may not appear and give an error because browser has stopped waiting, but this does not mean data collection is not completed.

# export
Export application will give options to export json files for visualization part 1 or part 2. after clicking the link, the export shall begin and the progress can be seen from the terminal, a export done message will appear on the webpage when it is finished. This takes about a few minutes.

# display
Disploay application has 3 webpages, each correspond to a graph, visualization part 1 has 1 graph and part 2 has 2 graphs. The webpages will read from the exported json files and plot using d3. X and Y axis information is also written in the webpage.

# visualization
The visualization has 2 parts: part 1 is language-based analysis with 1 graph, and part 2 is user-based analysis with 2 graphs.

# visualization part 1
Part 1 is language-based analysis, the grpah shows the percentages of code written in interrogated users' repositories with different languages in microsoft and google.
This graph is the part1-graph.svg in result folder.
It can be seen from the graph that the languages google employees use the most are Javascript, html, css, Python, shell and java. For microsoft employees, they are Javascript, html, css, powershell, shell, c# and Python.

# visualization part 2
Part 2 is user-based analysis. Graph one shows how many programming langueges employees in the two companies are familliar with. Graph two shows the percentages of employees that are most good at a certain language.
The graphs are part2-graph1.svg and part2-graph2.svg in result folder.
It can be seen from graph 1 that most employees in both companies are familliar with 10-20 languages, but microsoft has more employees that know 20-30 languages while google has more employees that know 10-20 languages.
It can be seen from graph 2 that most google employees know Java, C++, Python, Javascript, Jupyter and HTML best. Microsot has a large percentage of employees who know C# best, other languages include Java, C++, Python, Javascript and Jupyter. 
