"""
Author : Mouli M
email : murugesanmouli@gmail.com

Notes:
In this program the output of the program which contain replaced words is Output_t8.shakespeare
stored separetely kindly check that file
And Occurence_eachWord.csv is a csv file which contain the frequency of the words
Important Notes:
This program run more the 6 minutes
"""

import csv
import re
import os, psutil
import time
start_time=time.time()
#First read all the find words which we want to find and replace with french word
findwords=[]
with open("find_words.txt","r") as file:
    findwords=list(map(str,file.read().split("\n")))
#Now read the french dictionary
with open('french_dictionary.csv', 'r') as file:
    frenchDict = dict(csv.reader(file))
# Read the text file
with open("t8.shakespeare.txt","r") as file:
    textFile=(file.read())
# Now find the word in textFile and replace word with french word
listcsv=dict()
for i in findwords:
    #check the word is present in textFile
    if i.casefold() in textFile.casefold():
        frenchword=frenchDict[i]
        # count the number of occurence of each word
        listcsv[i]=[i,frenchword,textFile.casefold().count(i)]
        # replace with french word
        redata = re.compile(re.escape(i), re.IGNORECASE)
        textFile=redata.sub(frenchword,textFile)
# The output text file replaced the words that in findwords with french word
with open("Output_t8.shakespeare.txt","w") as file:
    file.write(textFile)
# CSV file that contains number of occurence of each word
with open("Occurence_eachWord.csv","w") as file:
    write=csv.writer(file)
    field=["Word","frenchWord","frequency"]
    write.writerow(field)
    write.writerows(listcsv.values())
end_time=time.time()
# print the memory taken to the process
process = psutil.Process(os.getpid())
print("The Memory taken to the process",process.memory_info().rss)
#print the time taken to process
print("The Time taken to process",end_time-start_time,"Seconds")
print("Replacing the english words with french word was done successfully")
print("Kindly check the file Output_t8.shakespeare.txt and Occurence_eachWord.csv to verify the output ")
