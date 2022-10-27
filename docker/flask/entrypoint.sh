#!/bin/sh
gunicorn 'tictactoe.flask.main:create_app()' -b 0.0.0.0:5000