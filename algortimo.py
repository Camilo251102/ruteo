
from scipy.spatial.distance import cdist
import pandas as pd
import datetime
from pulp import *
import requests
import folium
from folium.plugins import MarkerCluster
from folium import Marker
from folium import IFrame
from unidecode import unidecode
import math
from math import e
import numpy as np
import matplotlib.pyplot as plt
import duckdb
con = duckdb.connect(database=':memory:')
from IPython.display import display, Markdown, Latex, HTML

from pykml.factory import KML_ElementMaker as KML
from pykml.factory import ATOM_ElementMaker as ATOM
from pykml.factory import GX_ElementMaker as GX
from lxml import etree
from IPython.display import display, HTML

from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)


from urllib import request
from urllib import parse
import json
