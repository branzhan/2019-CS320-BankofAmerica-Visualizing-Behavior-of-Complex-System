# A second version of the bankapp

The first folder \flask is a basic copy of the original flask tutorial.

In this version \flask1, I'm getting more creative.  I'm importing the work of the students.

## to run the application

For Linux and Mac:

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

For Windows cmd, use set instead of export:
```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

For Windows PowerShell, use $env: instead of export:
```
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```

## to run the test harness

```
> pip install -e .
> pytest
> coverage run -m pytest
```
## To view a menu highlighting features in this app

[http://localhost:5000/](http://localhost:5000/)

## To view the original team HTML files from the test, visit:

[http://localhost:5000/originals/dashboard.html](http://localhost:5000/originals/dashboard.html)

## To view D3 example using titanic data

[http://localhost:5000/titanic/](http://localhost:5000/titanic/)

# References

This application represents a "full stack" of web and data base services.  The following references were used as the
package was cobbled together.

[flask and a data base](https://flask.palletsprojects.com/en/1.1.x/tutorial/)  - this reference presents the
basic Flask tutorial, walking the reader through the creation of a blog application.  The application includes
a number of best practices including creating an installable application, full data base read/writes, and testing.

[flask routing](https://hackersandslackers.com/flask-routes/) - this reference offers fun examples of how to 
accomplishing different routing feats using flask.  A *route* is a mapping between a URL displayed in a browser
and a file or other asset located in the working folder of the application.

[flask and D3](http://www.mydatastack.com/flaskd3part1) - this link offers some nice examples using real data, panda, numpy
and D3.  The link is a little slow but the code is good.  I used this site to add the /titanic/ D3 graphics

[flask and D3](https://towardsdatascience.com/combining-python-and-d3-js-to-create-dynamic-visualization-applications-73c87a494396) = this link is more complicated
than the version above, but it offers nice images that demonstrate the flow of information from the back end to the front end via a flask rest-full-api.

# To dos

Below is a check list of things that I beleive should be completed.  The focus on completing out the full stack.

- [ ] Replace each of the original visuals with appropriate D3 scripts.
- [ ] Push bank data into sqlite data base.  Factor the data a base to associate a time stamp with all records, like a log file.
- [ ] Develop front-end that permits viewing of database tabular style.  Add filters at the time to select different links by name, time, connection, etc.
- [ ] Add mechanic that shows links from data base that have changed recently.  Simple SQL query would produce record set.
- [ ] Use these *changed* links to update/freshen the D3 graphics


  