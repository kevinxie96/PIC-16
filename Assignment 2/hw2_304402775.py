# -*- coding: utf-8 -*-

# Challenge 1
#%%
"""
mytype(var) performs the same action as type(), and can recognize integers, floats, strings,
and lists.
"""
import re

def mytype(var):   
    analyzeString = str(var).replace(" ","")
    returnType = ""
    if re.search(r'^\[[\w\'\.]+\]$',analyzeString) or re.search(r"^\[([\w\'\.]+,)+[\w\'\.]+\]$", analyzeString):
        returnType = "list"
    elif re.search(r'[^0-9(?!\.)(?!\-)]',analyzeString):
        returnType = "string"
    elif re.search(r'\d',analyzeString):
        if re.search(r'\.',analyzeString):
            returnType = "float"
        else:
            returnType = "integer"
    else:
        returnType = "string"
    
    
    #detect some obscure strings
    if re.search(r'^\.$', analyzeString):
        returnType = "string"
    if analyzeString == "":
        returnType = "string"
    print (returnType)
    return returnType

mytype(2)
mytype(-2.3)
mytype([2,4.5])
mytype('[1,]')


# Challenge 2
#%%
"""
findpfds(filenames) takes as input a list L of filenames (such as “IMG2309.jpg”, “lecture1.pdf”,
“homework.py”), and lists the names of all PDF files, without extension (“lecture1”). Assume that
filenames may contain only letters and numbers.
"""
def findpfds(filenames):
    k = re.findall(r'\w+(?=\.pdf(?!\w+))',str(filenames))
    print (k)
    return k

L=['pdf.py', 'hw2.pdf', 'hw3.pdft']
findpfds(L)

# Challenge 3
#%%
"""
nameorder(name) is a function which takes names of the form “Firstname Lastname” and outputs them in the form
“Lastname, Firstname M.”.
"""
def nameorder(name):
    k = re.findall(r'\w+',name)
    if (len(k) < 2):
        print ("Please enter atleast a lastname and a firstname.")
        return
    else:
        formattedName = k[len(k)-1] + ', ' + k[0]
        for i in k[1:len(k)-1]:
            formattedName += ' ' + i[0] + '.'
    print (formattedName)    
    return formattedName

nameorder('Minnie Shulman')
nameorder('Susie Badger Rombach')

# Challenge 4
#%%
"""
findemail(url) takes as input a URL, and outputs any email addresses on this page. Focus
on academic personal pages, and write a script that gets around tricks people use to hide their email
addresses, such as “rombach AT ucla DOT edu”, or even “firstname DOT lastname AT ucla DOT
edu”. For the latter, you can, for example, use the fact that the name will certainly appear somewhere
on the page.
"""

#python2

#python 3
import urllib

def findemail(url):
    page=urllib.request.urlopen(url).read()
    page=str(page)
    outputList = re.findall(r'\w+\@(?:\w+\.)+\w+',page)
    outputList1 = re.findall(r'\w+ \[at\](?: \w+ \[dot\])+ \w+',page)
    outputList.extend(outputList1)
    outputList = list(set(outputList))
    print (outputList)
    return outputList
    
findemail("http://www.math.ucla.edu/~bertozzi/")
findemail('http://www.math.ucla.edu/~mason/cover.html')

# Challenge 5
#%%
"""
happiness(text) uses the Dodds et al happiness dictionary to rate the happiness of a piece of
english text (input as a single string). The happiness score is the the average score over all words in
the text that appear in the dictionary.
"""

from happiness_dictionary import happiness_dictionary as hd

def happiness(s):
    #we allow words to contain word characters, hyphens, apostrophes
    words=re.findall('[\w\']+',s.lower())
    #we need to keep track of both the total score and the total number of 
    #words found which appear in the dictionary, to get the mean value.
    score=0
    count=0
    for word in words:
        if word in hd.keys():
            score+=hd[word]
            count+=1
    print (score/count)
    return score/count
    
    
happiness("Hear the sledges with the bells-- Silver bells!What a world of merriment their melody foretells! How they tinkle, tinkle, tinkle, In the icy air of night! While the stars that oversprinkle All the heavens, seem to twinkle With a crystalline delight; Keeping time, time, time, In a sort of Runic rhyme,To the tintinnabulation that so musically wells From the bells, bells, bells, bells, Bells, bells, bells-- From the jingling and the tinkling of the bells.")
happiness("Hear the mellow wedding bells Golden bells!What a world of happiness their harmony foretells! Through the balmy air of night How they ring out their delight! From the molten-golden notes, And all in tune, What a liquid ditty floats To the turtle-dove that listens, while she gloats On the moon! Oh, from out the sounding cells,What a gush of euphony voluminously wells! How it swells! How it dwells On the Future! how it tells Of the rapture that impels To the swinging and the ringing Of the bells, bells, bells, Of the bells, bells, bells, bells, Bells, bells, bells-- To the rhyming and the chiming of the bells!")
happiness("Hear the loud alarum bells-- Brazen bells!What tale of terror, now, their turbulency tells! In the startled ear of night How they scream out their affright! Too much horrified to speak, They can only shriek, shriek, Out of tune,In a clamorous appealing to the mercy of the fire,In a mad expostulation with the deaf and frantic fire, Leaping higher, higher, higher, With a desperate desire, And a resolute endeavor Now--now to sit or never, By the side of the pale-faced moon. Oh, the bells, bells, bells! What a tale their terror tells Of Despair! How they clang, and clash, and roar! What a horror they outpourOn the bosom of the palpitating air! Yet the ear, it fully knows, By the twanging, And the clanging, How the danger ebbs and flows ; Yet, the ear distinctly tells, In the jangling, And the wrangling, How the danger sinks and swells,By the sinking or the swelling in the anger of the bells-- Of the bells-- Of the bells, bells, bells, bells, Bells, bells, bells-- In the clamour and the clangour of the bells!")
happiness("Hear the tolling of the bells-- Iron bells!What a world of solemn thought their monody compels! In the silence of the night, How we shiver with affright At the melancholy meaning of their tone! For every sound that floats From the rust within their throats Is a groan. And the people--ah, the people-- They that dwell up in the steeple, All alone, And who, tolling, tolling, tolling, In that muffled monotone, Feel a glory in so rolling On the human heart a stone-- They are neither man nor woman-- They are neither brute nor human-- They are Ghouls:-- And their king it is who tolls ; And he rolls, rolls, rolls, rolls, Rolls A p\u00e6an from the bells! And his merry bosom swells With the p\u00e6an of the bells! And he dances, and he yells ; Keeping time, time, time, In a sort of Runic rhyme, To the p\u00e6an of the bells-- Of the bells : Keeping time, time, time, In a sort of Runic rhyme, To the throbbing of the bells-- Of the bells, bells, bells-- To the sobbing of the bells ; Keeping time, time, time, As he knells, knells, knells, In a happy Runic rhyme, To the rolling of the bells-- Of the bells, bells, bells-- To the tolling of the bells, Of the bells, bells, bells, bells-- Bells, bells, bells-- To the moaning and the groaning of the bells.")