import sys,os
from bs4 import BeautifulSoup
import requests
from flask import Flask
import pandas as pd
import numpy as np
import FinScraper.classmodule as classmodule
import click
from FinScraper.webapp import app
import argparse
my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-a', action='classmodule.Menu().run()')


##def r(run):
 #   classmodule.Menu().run()


if __name__ == '__main__':
    app.run(debug=True)








