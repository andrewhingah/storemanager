[![Coverage Status](https://coveralls.io/repos/github/andrewhingah/storemanager/badge.svg?branch=ch-host-on-heroku-api-%23161360493)](https://coveralls.io/github/andrewhingah/storemanager?branch=ch-host-on-heroku-api-%23161360493)
[![Build Status](https://travis-ci.com/andrewhingah/storemanager.svg?branch=ch-fix-error-in-badges-%23161313720)](https://travis-ci.com/andrewhingah/storemanager)
[![Maintainability](https://api.codeclimate.com/v1/badges/521089bff51ec7ab1d6d/maintainability)](https://codeclimate.com/github/andrewhingah/storemanager/maintainability)
# storemanager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store
#Features
Store attendant can search and add products to buyer’s cart.
Store attendant can see his/her sale records but can’t modify them.
App should show available products, quantity and price.
Store owner can see sales and can filter by attendants.
Store owner can add, modify and delete products.
Store owner can give admin rights to a store attendant.
Products should have categories.
Store attendants should be able to add products to specific categories.
#Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose
#Prerequisites
You need to have the following installed.
Git
Postman
Python 3.6
Pip
#Installing
Clone the repository git clone https://github.com/andrewhingah/storemanager.git
Change directory cd storemanager
Checkout to feature branch `git checkout ch-host-on-heroku-api-#161360493`
To test API locally, set up a virtual environment in the base project folder `virtualenv venv`
Activate the virtual environment `source venv/bin/activate`
Install dependecies pip install -r requirements.txt
Run tests pytest or nosetests --exe --with-coverage --cover-package=api
Test the endpoints on postman
#Built With
Python 3.6
Flask
Flask_Restful
#Contributing
- Fork it from https://github.com/andrewhingah/storemanager.git/fork
- Create your feature branch git branch somefeature git checkout somefeature
- Commit your changes git commit "Add some feature"
- Push to the branch git push origin somefeature
- Create a new pull request
#Author
Andrew Hinga
