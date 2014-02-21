#! /usr/bin/python

## Copyright 2014 Kalanand Mishra

## iCite is a free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License or any later version: <http://www.gnu.org/licenses/>.
## This software is distributed WITHOUT ANY WARRANTY. 

## Instructions: The main executable is 'analyzer.py'. You can 
## modify input definitions in 'globals.py' according to your needs.
## You can either run a brand-new query (which is the default) or 
## analyze data stored in a text file from a previous query. 


from matplotlib import pyplot as plt
import math
import datetime
import numpy as np

##  ____  _       _       
## |  _ \| | ___ | |_ ___ 
## | |_) | |/ _ \| __/ __|
## |  __/| | (_) | |_\__ \
## |_|   |_|\___/ \__|___/
                       
def BarChart(X, Y, title, outputFileName):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    width = .35
    ind = np.arange(len(Y))
    rects1 = ax.bar(ind, Y, width, color='r')
    plt.xticks(ind + width / 2, X)
    plt.rcParams.update({'font.size': 20})

    low = min(Y)
    high = max(Y)
    plt.ylim([max(0, math.ceil(low-0.5*(high-low))), math.ceil(high+0.5*(high-low))])
    fig.autofmt_xdate()
    ax.set_ylabel('h-Index')
    
    def autolabel(rects):
        for rect in rects:
            h = rect.get_height()
            ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                    ha='center', va='bottom')

    autolabel(rects1)
    timestr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    plt.title(title + '    iCite   ' + timestr, size="small", color="blue")
    #plt.show(block=True)
    plt.savefig(outputFileName)
