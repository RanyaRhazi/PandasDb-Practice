#! /usr/bin/env python3

import pandas as pd
import scipy
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def sample():
    
    data_fn = "./speed-db.csv"
    df = pd.read_csv(data_fn)
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
    df = df.set_index('TIMESTAMP')
    
    start_date = ''; end_date = ''
    df.query("@start_date <= index <= @end_date", inplace=True)
    
    print (df.to_string())
    
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()

    del df

#####################
# Dataset description
#####################
# 'speed-db.csv' file have the speed test datasets from 2012-2016.
# Each row indicates a single speed test.
# Schema: TIMESTAMP,ID,DOWN_SPEED,UP_SPEED,LATITUDE,LONGITUDE.

# Some References:
# https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#
# https://sparkbyexamples.com/pandas/pandas-dataframe-query-examples/

# Do the following questions. Show your code and results. 
# NOTE: Your answer can be a combination of query-like and pandas-like.
# Do as you wish. You can change anywhere in this code template.

def question_1():
    
    #pass
    #How many datasets are available between (inclusive) 2013 and 2015?
    data_fn = "./speed-db.csv"
    db = pd.read_csv(data_fn)
    db['TIMESTAMP'] = pd.to_datetime(db['TIMESTAMP'])
    mask = (db["TIMESTAMP"] >= '2013-1-1') & (db["TIMESTAMP"] <= '2015-12-31')
    print("data sets between 2013 and 2015:")
    print(len(db.loc[mask]))
    
    

def question_2():
    
    #pass
    #How many datasets are available per ID of year 2013 to 2015?
    #e.g.) Year 2013 has ID1:61,297, ID2: 396,807, ID3: 301,784
    #e.g.) Year 2014 has ...
    data_fn = "./speed-db.csv"
    db = pd.read_csv(data_fn)
    db['TIMESTAMP'] = pd.to_datetime(db['TIMESTAMP'])
    mask = (db["TIMESTAMP"] >= '2013-1-1') & (db["TIMESTAMP"] <= '2015-12-31')
    d = db.loc[mask]
    print("Data sets 2013 to 2015 per ID:")
    print(d["ID"].value_counts())
    
    

def question_3():
    
    #pass
    #What are the average DOWN_SPEED and UP_SPEED of year 2012 to 2016?
    #e.g.) Year 2013 shows ...
    #e.g.) Year 2014 shows ...
    
    start = ['2012-1-1', '2013-1-1', '2014-1-1', '2015-1-1', '2016-1-1']
    end = ['2012-12-31', '2013-12-31', '2014-12-31', '2015-12-31', '2016-12-31']
 
    data_fn = "./speed-db.csv"
    db = pd.read_csv(data_fn)
    
    for i, j in zip(start, end):
        mask = (db["TIMESTAMP"] >= i) & (db["TIMESTAMP"] <= j)
        d = db.loc[mask]
        print("Average Downspeed and UpSpead from " + i)
        print(d["DOWN_SPEED"].mean())
        print(d["UP_SPEED"].mean())


    
    

def question_4():

    pass
    #What are the monthly average DOWN_SPEED and UP_SPEED of year 2015?
    #e.g.) Jan 2015 shows ...
    #e.g.) Feb 2015 shows ...
        
    data_fn = "./speed-db.csv"
    db = pd.read_csv(data_fn)
    db['TIMESTAMP'] = pd.to_datetime(db['TIMESTAMP'])
    mask = (db["TIMESTAMP"] >= '2015-1-1') & (db["TIMESTAMP"] <= '2015-12-31')
    d = db.loc[mask]
    
    f = (d.groupby([pd.Grouper(freq='m', key = 'TIMESTAMP')])['DOWN_SPEED'].sum().groupby(level=0).mean().reset_index(name='DownSpeed Average'))
    print("DownSpeed Monthly Average for 2015:")
    print(f)
    g = (d.groupby([pd.Grouper(freq='m', key = 'TIMESTAMP')])['UP_SPEED'].sum().groupby(level=0).mean().reset_index(name='Upspeed Average'))
    print("UpSpeed Monthly Average for 2015:")
    print(g)

        
def question_5():
    #Repeat question_2, but this time uses the data from 2015 only. Please draw a figure for monthly datasets per ID, a stacked bar of ID1, ID2, and ID3.
    #Show your figure. Please refer to the figure 1 given (not the same, but similar).
    #Reference: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html
    data_fn = "./speed-db.csv"
    db = pd.read_csv(data_fn)
    db['TIMESTAMP'] = pd.to_datetime(db['TIMESTAMP'])
    mask = (db["TIMESTAMP"] >= '2015-1-1') & (db["TIMESTAMP"] <= '2015-12-31')
    d = db.loc[mask]
    print("Data sets for 2015 per ID:")
    print(d["ID"].value_counts())
    g = (d.groupby([pd.Grouper(freq='m', key = 'TIMESTAMP')])['ID'].value_counts())
    print(g)
    ax = g.plot.bar(x = 'TIMESTAMP', stacked=True, color = ['tomato', 'lightseagreen', 'blue'], figsize=(24,12))
    ax.set_title('2015 Monthly Datasets per ID', fontsize = 20)
    fig = ax.get_figure()
    fig.savefig('fig.pdf')
    print('saved')

    

def bonus_question ():

    pass
    #NOTE: This is just a bonus, DO NOT SPEND too much time on this question. It's okay.
    #Using the latitude and logitude, indicate all the test locations 
    #Please refer to the figure 2 given (not the same, but similar).

def main():
    sample()

if __name__=="__main__":
    main()
