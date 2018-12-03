#!/usr/bin/env python
# coding: utf-8

# In[1]:


# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
from datetime import *
#from dateutil.parser import parse

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.lacity.org", None)

AppTolken= 'zEAtZDI2DaDpod2Z6HzzdwG0h'
SecretTolken='z-oNcKNakPE9a7pguEEjk37FGftEub8kzp9n'

client = Socrata('data.lacity.org',AppTolken)


# In[2]:


# Example authenticated client (needed for non-public datasets):

#,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("e7h6-4a3e", limit=6000)
                     
#where = "datetime BETWEEN '2013-01-19T23:50:32.000' AND '2014-12-14T23:50:32.000'")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
FileName='ParkingFile-{date:%Y:%m:%d:%H:%M:%S}.txt'.format( date=datetime.now())
results_df.to_csv(FileName,index = False)




