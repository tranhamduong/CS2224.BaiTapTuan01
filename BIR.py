# Source: https://github.com/asadmohammad/Boolean-Retrieval-Model

import re
import json
from functools import reduce

from config import title_file


def splitWords(string):
    words = []
    words = re.split('\W+',string)
    return words

def tokeniseWords(wordList):
    newWord = []
    newWord = re.sub(r'[^\w]', '', wordList)
    #print(newWord)
    return newWord
    

def toLowerCase(wordList):
    i = 0
    lowCaseWord = []
    for word in wordList:
        i = i + 1
        lcWord = word.lower()
        lowCaseWord.append((i, lcWord))
    return lowCaseWord
    #print(lowCaseWord)
    #removeStopWords(lowCaseWord)


def readFromFile():
    stories = []
    
    with open(title_file, 'r') as f: 
        stories = f.read().splitlines()
    
    return stories


def preprocessing_str(string): 
    return menuEmulat(string)


def menuEmulat(string):
    words = splitWords(string)
    words = toLowerCase(words)
    return words # <- format as list of tuple (index, word)


def fetchDoc(invInd, query):
    wordList = [tok for _, tok in menuEmulat(query) if tok in invInd]
    fetchedResults = [set(invInd[tok].keys()) for tok in wordList]
    fdDocs = reduce(lambda tok,key : tok & key,fetchedResults) if fetchedResults else[]
    # print(type(fdDocs))
    return fdDocs


def trialInvInd(words):
    invInd = {}           #Dictionary
    for i, word in menuEmulat(words):
        positions = invInd.setdefault(word,[])         #value of item with key/ Dictionary
        positions.append(i)                             #storing positions of word in a document
    return invInd


def invertedIndex(invInd, postings, lex):
    for word, pos in lex.items():
        i = invInd.setdefault(word,{})         #Setting dictionary for each 
        i[postings] = pos
    return invInd

    
def printInvIndFile(inv_Index):
    fop = open("Dictionary_segmented.txt","w")
    #fop.write(json.dumps(iv))
    for tokens, wpos in inv_Index.items():
        fop.write(tokens)
        fop.write("  ===>  ")
        fop.write(json.dumps(wpos))
        fop.write("\n")
        fop.write("\n")
        
    fop.close()
    
    
def inverted_indexing(): 
    documentID = []
    corpus = {}
    inv_Index = {}
    stories = readFromFile()
    
    for x in range(0, len(stories)):                   #DOCUMENT'S   ID      LIST
        documentID.append("doc"+str(x))
        #print("****")    
    for y in range(0,len(documentID)):
       corpus.update({documentID[y] : stories[y]})
       #print("****") 
    
    for ID, story in corpus.items():        #INVERTED   INDEX   CREATION
        docInCorp = trialInvInd(story) # Tao word dict, 
        iv = invertedIndex(inv_Index,ID,docInCorp)
    
    return iv


if __name__ == '__main__':
    inv_Index = {}
    corpus = {}
    documentID = []
    inputString = []
    wonL = []
    flatResult = []
    hav = []
    z = []
    fin = 0
    ac = 0
    av = 0
    stories = readFromFile()
    
    for x in range(0, len(stories)):                   #DOCUMENT'S   ID      LIST
        documentID.append("doc"+str(x))
        #print("****")    
    for y in range(0,len(documentID)):
       corpus.update({documentID[y] : stories[y]})
       #print("****")    
       
    for ID, story in corpus.items():        #INVERTED   INDEX   CREATION
        docInCorp = trialInvInd(story) # Tao word dict, 
        iv = invertedIndex(inv_Index,ID,docInCorp)
        #print("****")
    printInvIndFile(iv)              #INVERTED       INDEX       PRINTING IN     FOLDER