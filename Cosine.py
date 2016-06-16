
import numpy as np
import os
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import rbf_kernel


def tf(tfidf_matrix):
    print "Using TFIDF with cosine similarity"
    Ke = cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]
 
def tf_sig(tfidf_matrix):
    print "Using TFIDF with sigmoid kernel"
    Ke = sigmoid_kernel(tfidf_matrix[0:1],tfidf_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]
 
def cnt(count_matrix):
    print "Using Count with cosine similarity"
    Ke = cosine_similarity(count_matrix[0:1],count_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]

def cnt_sig(count_matrix):
    print "Using Count with sigmoid kernel"
    Ke = sigmoid_kernel(count_matrix[0:1],count_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]
 
    
def hsh(hash_matrix):
    print "Using Hashing with cosine similarity"
    Ke = cosine_similarity(hash_matrix[0:1],hash_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]
 
def hsh_sig(hash_matrix):
    print "Using Hashing with sigmoid kernel"
    Ke = sigmoid_kernel(hash_matrix[0:1],hash_matrix)
    K=Ke[0]
    top = np.argsort(K)[-11:]
    for i in range(10):
        print (10-i),Total[top[9-i]-1]
 
    
outputfile=raw_input("Output file name?\n")
ng=int(input("Ngram?\n"))

#Begin Initialization
start=time.time()
Actors = os.listdir("Actors/")
Movies = os.listdir("Movies/")
Total=[]
for i in Actors:
    print i
    Total.append(i)
for i in Movies:
    Total.append(i)
total=[]
for j in Actors:
    f=open("Actors/"+j)
    i=f.read()
    total.append(i)
for j in Movies:
    f=open("Movies/"+j)
    i=f.read()
    total.append(i)
tfsum=0
tfsigsum=0
cntsum=0
cntsigsum=0
hshsum=0
hshsigsum=0
end=time.time()-start
print "Init took",end,"seconds"
#End Initialization

#Begin File Creation
out=open(outputfile,"w")
rounds=0

#Begin testing
while True:
    rounds+=1
    query=raw_input("What is the query?\n")
    print("\n\n")
    total.insert(0,query)
    out.write("\n\nQuery: "+query+"\n")
    print "Calculating Tfidf Matrix"
    start=time.time()
    vectorizer = TfidfVectorizer(ngram_range=(ng,ng))
    matrix = vectorizer.fit_transform(total)
    end=time.time()-start
    print "Calculation of Tfidf matrix took",end,"seconds\n"
    
    tf(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Tfidf Cosine: "+str(score)+"\n")
    tfsum+=score
    
    tf_sig(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Tfidf Sigmoid: "+str(score)+"\n")
    tfsigsum+=score
    
    print "Calculating Count Matrix"
    start=time.time()
    vectorizer = CountVectorizer(ngram_range=(ng,ng))
    matrix = vectorizer.fit_transform(total)
    end=time.time()-start
    print "Calculation of Count matrix took",end,"seconds\n"

    
    cnt(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Count Cosine: "+str(score)+"\n")
    cntsum+=score
    
    cnt_sig(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Count Sigmoid: "+str(score)+"\n")
    cntsigsum+=score

    
    print "Calculating Hashing Matrix"
    start=time.time()
    vectorizer = HashingVectorizer(ngram_range=(ng,ng))
    matrix = vectorizer.fit_transform(total)
    end=time.time()-start
    print "Calculation of Hashing matrix took",end,"seconds\n"
                   
    hsh(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Hashing Cosine: "+str(score)+"\n")
    hshsum+=score

    hsh_sig(matrix)
    print "Your query was ",query
    score=int(input("Which number is your movie? Enter 0 if it's not there\n"))
    out.write("Hashing Sigmoid: "+str(score)+"\n")
    hshsigsum+=score

    total.pop(0)
    z=int(input( "\nDid you get all zeros? Enter 1 for Yes and 0 for No\n"))
    if(z==1):
        out.write("ALL ZEROS IN THIS ROUND\n")
        temp=raw_input("What was your movie?\n")
        out.write(temp+"\n")
    done =int(input("\nAre you done? Enter 1 for Yes and 0 for No\n"))
    if(done==1):
        break
#End testing
out.write("\n\nRounds: "+str(rounds)+"\nScores:\n")
out.write("Tfidf with cosine similarity earned "+str(tfsum)+"\n")
out.write("Tfidf with sigmoid kernel earned "+str(tfsigsum)+"\n")
out.write("Count with cosine similarity earned "+str(cntsum)+"\n")
out.write("Count with sigmoid kernel earned "+str(cntsigsum)+"\n")
out.write("Hashing with cosine similarity earned "+str(hshsum)+"\n")
out.write("Hashing with sigmoid kernel earned "+str(hshsigsum)+"\n")
out.close()
print "\nThank you for playing!!\n"
