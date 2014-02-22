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

##  _   _                                                          
## | \ | | _____      __   __ _ _   _  ___ _ __ _   _    ___  _ __ 
## |  \| |/ _ \ \ /\ / /  / _` | | | |/ _ \ '__| | | |  / _ \| '__|
## | |\  |  __/\ V  V /  | (_| | |_| |  __/ |  | |_| | | (_) | |   
## |_| \_|\___| \_/\_/    \__, |\__,_|\___|_|   \__, |  \___/|_|   
##                           |_|                |___/              
##                     _    __                        __ _ _      
##  _ __ ___  __ _  __| |  / _|_ __ ___  _ __ ___    / _(_) | ___ 
## | '__/ _ \/ _` |/ _` | | |_| '__/ _ \| '_ ` _ \  | |_| | |/ _ \
## | | |  __/ (_| | (_| | |  _| | | (_) | | | | | | |  _| | |  __/
## |_|  \___|\__,_|\__,_| |_| |_|  \___/|_| |_| |_| |_| |_|_|\___|
##                                                                

doNewQuery = True

##  _                            _   
## (_)_ __ ___  _ __   ___  _ __| |_ 
## | | '_ ` _ \| '_ \ / _ \| '__| __|
## | | | | | | | |_) | (_) | |  | |_ 
## |_|_| |_| |_| .__/ \___/|_|   \__|
##             |_|                   

import sys, os, getopt, re, urllib
import numpy as np
from numpy import loadtxt


from globals import *
from plotter import *

##   ___                          _   _               _    ____ ___ 
##  / _ \ _   _  ___ _ __ _   _  | |_| |__   ___     / \  |  _ \_ _|
## | | | | | | |/ _ \ '__| | | | | __| '_ \ / _ \   / _ \ | |_) | | 
## | |_| | |_| |  __/ |  | |_| | | |_| | | |  __/  / ___ \|  __/| | 
##  \__\_\\__,_|\___|_|   \__, |  \__|_| |_|\___| /_/   \_\_|  |___|
##                        |___/                                     
################ The function to query Inspire API ###############

def getHindex(ref):
    query = 'p=' + ref
    weburl = 'http://inspirehep.net/search?'
    ## Need to filter papers that are published
    ## Take into account subtlties for PDG, GEANT, Pythia, CTEQ 
    filter = '+and+eprint+arxiv'
    if ('Particle' in ref or 'GEANT' in ref or 'FERMILAB' in ref or 'cteq' in ref):
       filter = ''
    if not ('Particle' in ref or 'GEANT' in ref or 'FERMILAB' in ref): 
	   filter = filter + '+and+tc+p'
    filter = filter + '&of=hcs'
    Hindex = urllib.urlopen(weburl + query + filter).read()

    if 'No records' in Hindex :
        return "no records found in INSPIRE, please try again"

    Hindex = Hindex[Hindex.find('citation-metrics#citesummary_h-index'):]
    Hindex = Hindex[Hindex.find('\"right\">')+8:]
    Hindex1 = Hindex[:Hindex.find('</td>')]

        
    #print Hindex 
    #print Hindex1 
    return Hindex1


##  ____       _       _              _   
## |  _ \ _ __(_)_ __ | |_ ___  _   _| |_ 
## | |_) | '__| | '_ \| __/ _ \| | | | __|
## |  __/| |  | | | | | || (_) | |_| | |_ 
## |_|   |_|  |_|_| |_|\__\___/ \__,_|\__|                                      

################ Print the query output ########################

def printHindex(name, queryString):
    result = getHindex(queryString) 
    print name, result 
    return result



##   ____                                 _                     
##  / ___|___  _ __ ___  _ __   __ _ _ __(_)___  ___  _ __  ___ 
## | |   / _ \| '_ ` _ \| '_ \ / _` | '__| / __|/ _ \| '_ \/ __|
## | |__| (_) | | | | | | |_) | (_| | |  | \__ \ (_) | | | \__ \
##  \____\___/|_| |_| |_| .__/ \__,_|_|  |_|___/\___/|_| |_|___/
##                      |_|                                     

################ Make comparison plots ###################
def compareGroups(category, plottitle, txtfile, readFromFile):
    OX = eval(category).keys()
    OY = []
    Vals = eval(category).values()
    
    if readFromFile:
       col1 = np.genfromtxt(txtfile.name, usecols=(0), delimiter=',', dtype=str)
       col2 = np.genfromtxt(txtfile.name, usecols=(1), delimiter=',', dtype=int)

       for i, item in enumerate(col1):
           if item in OX:
              OY.append(col2[i])
    else:
       for i in range(0, len(OX)):
          OY.append(int(printHindex(OX[i], Vals[i])))
          txtfile.write(OX[i] + ',' + str(OY[i])+'\n')

    plotname = txtfile.name.replace("txt","plot", 1)
    plotname = plotname.replace(".txt", '_' + category + '.png')
    BarChart(OX, OY, plottitle, plotname)   
    


##  __  __       _       
## |  \/  | __ _(_)_ __  
## | |\/| |/ _` | | '_ \ 
## | |  | | (_| | | | | |
## |_|  |_|\__,_|_|_| |_|
##                       
################ The main function ########################

if __name__ == "__main__":
    #getHindex('mishra+kalanand')

    prefix = 'hindex'
    txtfile = open('txt_' + prefix + '.txt', 'w' if doNewQuery else 'r')

    for i, item in enumerate(groups.keys()):
        compareGroups(item, groups.values()[i], txtfile, not doNewQuery)

    txtfile.close()
