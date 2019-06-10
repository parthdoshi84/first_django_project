# IMDB Clone
Developed for the course - Web Development at UCLA

My project is based on creating a IMDB Clone where users can see the ratings of different movies. It includes pages  showing a list of movies in the descending order of their ratings, individual movie, actor, director, producer pages, home page, login page and contact page.  

The following features have been implemented:

1) 4 Models - Actor, Director, Producer, Movie
2) Many to Many relationship exists between Actor and Movie while One to Many relationship exists between Director/Producer and Movie respectively.
2) ListView for Movies - Lists all the movies (name and ratings) in the descending order of their ratings
3) DetailView for each of the actor, director and producer. 
4) Generic base template which is inherited by all pages. Separate html templates for each of the pages. 
5) Bootstrap and css have been incorporated in all the templates
6) Contact us form and the corresponding template
7) Is navigable through hyperlinks
8) Login functionaliy for all users (superuser as well as normal users)
9) Only super user (admin) can upload data. Data can be uploaded in two ways: 
   a) Through the admin website. 
   b) By uploading a csv file which contains data. This features is implemented through a python script
10) The website is also implemented on heroko. The link is as follows:
http://demoparth.herokuapp.com/imdb/

