#######################################################################################################################################################################
#!/usr/bin/python
#python 3 based dictionary for words and their meanings
#Author aks
#need to run dictionary() first try to call any function
#check for various input test cases
#######################################################################################################################################################################

#######################################################################################################################################################################
import csv

#used for the dictionary file having the old words to read and write more words
#######################################################################################################################################################################
import collections

#used to order words in dictionary alphabetical
#######################################################################################################################################################################
dictj={}

#global declaration of dictionary variable 
#######################################################################################################################################################################
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
        key,value=a.split(',') #splits meaning from word so can enter descriptive meaning.

        if (dictj.get(key)==None):# checks if the word you adding  already existing in dictionary or not.
            d ={key:value}
            dictj.update(d)
            
    with open('mycsvfile.csv','w') as f:#add new words to the dictionary  file as csv.
        w = csv.writer(f)
        w.writerows(dictj.items())
    #return(dictj)


#######################################################################################################################################################################

#function for searching words existing in dictionary by all,or starting string characters as input



def listwords():
    print("Enter which words meaning you want:")
    n=input()
    str(n)
    
    if(n=='all'):
        df= collections.OrderedDict(sorted(dictj.items()))#reverse = True sorting
        print ("WORDS"+"\t", "MEANING")    
        for k , v in df.items(): # iterating items in dictionary
            print (k+"\t", v) #2 col format words and meaning
            
    else:
        df= collections.OrderedDict(sorted(dictj.items()))#reverse = True
        print ("WORDS"+"\t", "MEANING")
        for k,v in df.items():
            if k.startswith(n.lower()):
                print (k+"\t", v)
            if k.startswith(n.upper()):
                print (k+"\t", v)
            
#######################################################################################################################################################################
