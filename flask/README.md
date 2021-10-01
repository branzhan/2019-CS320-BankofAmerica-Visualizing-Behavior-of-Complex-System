# Run The Application

I developed the application on Windows 10 box with Powershell.  Here are a few commands:

For Windows cmd, use set instead of export:

> set FLASK_APP=bankapp
> set FLASK_ENV=development
> flask run

For Windows PowerShell, use $env: instead of export:

> $env:FLASK_APP = "bankapp"
> $env:FLASK_ENV = "development"
> flask run

Then open a browser to:  

  http://localhost:5000
  

# test the application

As part of the Flask tutorial this application implements pytest and coverage:

> pytest

> coverage run -m pytest
