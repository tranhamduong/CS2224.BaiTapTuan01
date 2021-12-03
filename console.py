# Source: https://github.com/asadmohammad/Boolean-Retrieval-Model

import re
import json
from functools import reduce

from BIR import inverted_indexing, preprocessing_str
from config import title_file

indexes = inverted_indexing()

def processing_query(list_of_term):
    results = [] 
    not_results = []
    for term in list_of_term: 
        result = set()
        term = term.strip()
        if "NOT" in term: 
            result = query_from_indexes(term.split()[1]) # documents has the NOT term
            if result: 
                not_results.append(result)
        else: 
            result = query_from_indexes(term)
            if result:
                results.append(result)

    try:
        total_and_result = set.intersection(*map(set,results))  
    except TypeError: 
        total_and_result = set()
        
    try: 
        total_not_result = set.union(*map(set, not_results))
    except TypeError: 
        total_not_result = set() 
    
    final_result = total_and_result.difference(total_not_result)      
        
    return final_result
        

def query_from_indexes(term, operation=True):
    return fetchDoc(indexes, term.lower())
    
def fetchDoc(invInd, term):
    # wordList = [word for _, word in preprocessing_str(query) if word in indexes]
    if term not in indexes:
        return 
    fetchedResults = [set(invInd[tok].keys()) for tok in [term]]
    fdDocs = reduce(lambda tok,key : tok & key,fetchedResults) if fetchedResults else[]
    return fdDocs

if __name__ == '__main__': 
    
    print("Hello world!")
    with open(title_file, 'r') as f: 
        ref = f.read().splitlines()
    while True: 
        query = input("Insert Query:")
        # query = "tại AND NOT việt_nam"
        query = query.strip() 
        
        terms = query.split("AND")
        
        result = processing_query(terms)
        if result:
            for item in result: 
                docs_no = re.findall("\d+", item)[0]

                print("Found terms in this document " + str(docs_no))
                print(ref[int(docs_no)])
        else:
            print("No document found!")
            
        print("========================")