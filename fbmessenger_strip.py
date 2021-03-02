# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:35:55 2021

@author: shane
"""

from bs4 import BeautifulSoup
import pandas as pd


def fbmessagestrip(filename):
    with open(filename, encoding='utf8') as infile:
        html = BeautifulSoup(infile, "html.parser")
    """
    lenght=0
    
    for row in html.find_all('div',attrs={"class" : "_3-95"}):
        print(row.text)
        if len(row.text)!=lenght:
            lenght=len(row.text)
            print("length changed")
        #)3-94 is all dates and times of messages
        #_3-96 is messages without dates or times
        #_3-95 is messages ending in date and time
    #this was code to explore the data. No longer needed.
    """
    #converting available information into lists 
    dattetimes= [row.text for row in html.find_all('div',attrs={"class" : "_3-94"})]
    messages= [row.text for row in html.find_all('div',attrs={"class" : "_3-96"})]
    compound= [row.text for row in html.find_all('div',attrs={"class" : "_3-95"})]
    
    names=[i for ix,i in enumerate(messages) if ix%2==0]
    message=[i for ix,i in enumerate(messages) if ix%2!=0]
    
    
    # initialize list of lists  
    data=[[i,names[ix],message[ix]] for ix,i in enumerate(dattetimes)]
      
    # Create the pandas DataFrame  
    df = pd.DataFrame(data, columns = ['Send Time', 'User','Message'])  
    return(df)

def fbm_main(filename,outfile):
    df=fbmessagestrip(filename)
    df.to_excel(outfile)


if __name__=="__main__":
    fbm_main(FILENAME,OUTFILE)
