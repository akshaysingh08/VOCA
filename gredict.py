#!/usr/bin/python


import csv
import collections

dictj={}

def dictionary():
    with open('mycsvfile.csv', 'r') as csv_file:
        g = dict(filter(None, csv.reader(csv_file)))
    dictj.update(g)

    
    n=input("Enter the number of words you want to enter:")
    n=int(n)

    

    for i in range(n):
        print("Enter the word and meaning as:  WORD , MEANING")
        a=input()
        a=a.upper()
        key,value=a.split(',')

        if (dictj.get(key)==None):
            d ={key:value}
            dictj.update(d)
            
    with open('mycsvfile.csv','w') as f:
        w = csv.writer(f)
        w.writerows(dictj.items())
    return(dictj)



def listwords():
    print("Enter which words meaning you want:")
    n=input()
    str(n)
    
    if(n=='all'):
        df= collections.OrderedDict(sorted(dictj.items()))#reverse = True
        print ("WORDS"+"\t", "MEANING")    
        for k , v in df.items(): # iterating items in dictionary
            print (k+"\t", v)
            
    else:
        df= collections.OrderedDict(sorted(dictj.items()))#reverse = True
        print ("WORDS"+"\t", "MEANING")
        for k,v in df.items():
            if k.startswith(n.lower()):
                print (k+"\t", v)
            if k.startswith(n.upper()):
                print (k+"\t", v)
            
