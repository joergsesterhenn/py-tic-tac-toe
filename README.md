# py-tic-tac-toe 
![Python application](https://github.com/joergsesterhenn/py-tic-tac-toe/workflows/Python%20application/badge.svg)

A tic-tac-toe game written in python with different user interfaces all using the same datamodel.

Currently, the following user interfaces are implemented: 
* commandline ASCII (pure python)
* standalone window (kivy framework) 
* web app (flask framework)

## update dependencies

* poetry update

## build

* poetry build

## run tests

* poetry run pytest --cov=tictactoe tests/

## run the applications

* poetry run ascii
* poetry run kivy
* poetry run flask


