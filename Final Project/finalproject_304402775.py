# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 14:09:31 2017

@author: kevin_000
"""
import matplotlib.pyplot as plt
import re
import numpy as np
import math
from numpy import linalg as LA
import copy
np.set_printoptions(threshold=np.inf)

#exerpt from harry potter 1 
string0 = "Almost as though this thought had fluttered through the open window, Vernon Dursley, Harry’s uncle, suddenly spoke. Harry had never been inside Filch's office before; it was a place most students avoided. The room was dingy and windowless, lit by a single oil lamp dangling from the low ceiling. A faint smell of fried fish lingered about the place. Wooden filing cabinets stood around the walls; from their labels, Harry could see that they contained details of every pupil Filch had ever punished. Fred and George Weasley had an entire drawer to themselves. A highly polished collection of chains and manacles hung on the wall behind Filch's desk. It was common knowledge that he was always begging Dumbledore to let him suspend students by their ankles from the ceiling. October arrived, spreading a damp chill over the grounds and into the castle. Madam Pomfrey, the nurse, was kept busy by a sudden spate of colds among the staff and students. Her Pepperup potion worked instantly, though it left the drinker smoking at the ears for several hours afterward. Ginny Weasley, who had been looking pale, was bullied into taking some by Percy. The steam pouring from under her vivid hair gave the impression that her whole head was on fire. I mean, nobody wishes more than I do that it had all been quick and clean, and my head had come off properly, I mean, it would have saved me a great deal of pain and ridicule. However - Nearly Headless Nick shook his letter open and read furiously: We can only accept huntsmen whose heads have parted company with their bodies. You will appreciate that it would be impossible otherwise for members to participate in hunt activities such as Horseback Head-Juggling and Head Polo. It is with the greatest regret, therefore, that I must inform you that you do not fulfill our requirements. With very best wishes, Sir Patrick Delaney-Podmore." 
string1 = "Yes, yes, it's all very sad, but get a grip on yourself, Hagrid, or we'll be found, Professor McGonagall whispered, patting Hagrid gingerly on the arm as Dumbledore stepped over the low garden wall and walked to the front door. He laid Harry gently on the doorstep, took a letter out of his cloak, tucked it inside Harry's blankets, and then came back to the other two. For a full minute the three of them stood and looked at the little bundle; Hagrid's shoulders shook, Professor McGonagall blinked furiously, and the twinkling light that usually shone from Dumbledore's eyes seemed to have gone out."
string2 = "Dumbledore and Professor McGonagall bent forward over the bundle of blankets. Inside, just visible, was a baby boy, fast asleep. Under a tuft of jet-black hair over his forehead they could see a curiously shaped cut, like a bolt of lightning."
string = string0 + string1 + string2

# lord of the rings 1
with open('lordoftherings1.txt', 'r') as myfile:
    lord=myfile.read().replace('\n', '')
    
# harry potter 1
with open('harrypotter1.txt', 'r') as myfile:
    harry=myfile.read().replace('\n', '')   
class character_network(object):
    wordsToRemove = ['While','Which','Look','Good-bye','Take','Chapter','Now','Before','Could','Mr','Mrs','Men','What','Too','Here','That','Then','When','This','The','It','We','You','With','Her','Him','She','He','They','Them','Why','Who','How','An','Yes','No','And','But','So','Me','There','For']   # list of common words found to be capitalized in dialogue
    def __init__(self,story,maxNumberOfCharacters,specificityConstant):
        self.story = story
        self.names = []
        self.network = [[]]
        self.matrixColumn1 = [[]]
        self.ranks = []
        self.maxNOC = maxNumberOfCharacters
        self.sC = specificityConstant
    def createCharacterNetwork(self):   # all the commented code in this function are attempts at filtering out non characters
        sentences = self.story.split(".")   # split by sentence
        self.names = list(set(self.findProperNouns(sentences)))   # establish a list of names
        # attempts at filtering the findProperNouns process more
#==============================================================================
#         namesToRemove1 = []
#         for i in range(len(self.names))[:len(self.names)-1]:
#             for j in range(len(self.names))[i+1:]:
#                 if self.names[i] in self.names[j]:
#                     namesToRemove1.append(self.names[i])  
#         for i in namesToRemove1:
#             if i in self.names:
#                 self.names.remove(i)
#         namesToRemove3 = [i.lower() for i in self.names]
#         anotherList = []
#         for i in namesToRemove3:
#             if i in self.story:
#                 indexOf = namesToRemove3.index(i)
#                 anotherList.append(self.names[indexOf])
#         for i in anotherList:
#             if i in self.names:
#                 self.names.remove(i)
#==============================================================================
        network = self.createMatrixForPlotting(sentences)
        self.network = self.cleanseMatrix(network)   # establish network
        self.matrixColumn1 = self.makeColumnsSumTo1()   # establish a matrix to perform PageRank on
        self.ranks = self.pagerank()   # establish rank list 
        self.network_plot_circle("Character Network")   # plot
        
    def findProperNouns(self,sentences):   # finds proper nouns 
        properNouns = []
        # omit the first word in every sentence 
        for i in sentences:
            sentenceArray = i.split(" ")
            if sentenceArray[0] == '':
                sentenceArray = sentenceArray[2:]
            else:
                sentenceArray = sentenceArray[1:]
            s = ' '
            sentence = s.join(sentenceArray)
            
            properNouns.extend(re.findall(r'(?:[A-Z][a-zA-Z\-\.]+ )*[A-Z][a-zA-Z\-\.]+',sentence))
        # character dialogue begins with a capital letter so 'wordsToRemove is tries to combat that
        # when characters shout, the text sometimes makes the word completely capitalized, i.upper() != i combats this
        properNouns = [i for i in properNouns if i not in self.wordsToRemove and i.upper() != i and len(i) > 2]
        return properNouns
    
    def createMatrixForPlotting(self,sentences):
        names = self.names
        superDict = [[0]*len(names)]*len(names)
        superDict = np.array(superDict, dtype='float')
        # find all the names that appear in a sentence
        for i in sentences:
            listOfNamesForSentences = []
            for j in names:
                if j in i:
                    listOfNamesForSentences.append(j)
            indexList = [names.index(i) for i in listOfNamesForSentences]   # find all the indexes for these names
            # create symmetric weighted adjacency matrix
            if len(indexList) > 0:
                minimum = indexList[0]   # find minimum index
                for k in indexList[1:]:
                    if k < minimum:
                        minimum = k
                indexList.remove(minimum)
                for z in indexList:   # popular column and row
                    superDict[minimum][z] += 1
                    superDict[z][minimum] += 1
        return superDict
    # cleanse as in remove columns and rows whose sum is 0 aka remove the names that have no relation to other names
    # make sure the diagonal entries are 0
    def cleanseMatrix(self,N):
        for i in range(len(N)):
            N[i][i] = 0
                
        specificityConstant = self.sC
        counter = []
        for i in range(len(N)):
            sum1 = np.sum(N[i])
            if sum1 == 0:
                counter.append(i)
                continue
            aboveConstant = False
            for j in N[i]:
                if j >= specificityConstant:
                    aboveConstant = True
                    break
            if aboveConstant == False:
                counter.append(i)
        names = copy.copy(self.names)
        for i in counter:
            self.names.remove(names[i])

        N = np.delete(N,counter,0)
        N = np.transpose(N)
        return np.delete(N,counter,0)
    
    # summing up the network row, diving each entry by the sum,  and then transposing it
    def makeColumnsSumTo1(self):
        newMatrix = copy.copy(self.network)
        for i in range(len(newMatrix)):
            sum1 = np.sum(newMatrix[i])
            for j in range(len(newMatrix[i])):
                newMatrix[i][j] = newMatrix[i][j]/sum1

        return np.transpose(newMatrix)
    
    # http://www.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html
    def pagerank(self):
        N = self.matrixColumn1
        n,v = LA.eig(N)
        nTF = np.iscomplex(n)
        nReal = n.real
        for i in range(len(n)):
            if math.ceil(nReal[i]) == 1 and nTF[i] == False:
                outputRanks = np.array([v[j][i] for j in range(len(N[0]))])
                normalize = np.sum(outputRanks)
                outputRanks = np.array([i/normalize for i in outputRanks])
                rankOrder = dict([(i,outputRanks[i]) for i in range(len(outputRanks))])
                return sorted(rankOrder, key=rankOrder.get)[::-1]
            
    def network_plot_circle(self,title):
        fig = plt.figure()
        graph = fig.add_subplot(111)
        matrixRow1 = np.transpose(self.matrixColumn1)
        listOfNewCenters = [(0,0)]
        # potentially try different cluster centers
#==============================================================================
#         counter = 1
#         while (len(listOfNewCenters) <= numberOfCharacters):
#             listOfNewCenters.extend([(2*counter,-2*counter),(-2*counter,-2*counter),(2*counter,2*counter),(-2*counter,2*counter)])
#             counter += 1
#         while (len(listOfNewCenters) > numberOfCharacters):
#             listOfNewCenters.pop()
#==============================================================================

        characterPoints = {}
        popularCharacterIndex = self.ranks[0]
        nonZeroIndexList = [j for j in range(len(self.network[popularCharacterIndex])) if self.network[popularCharacterIndex][j] >=self.sC] 
        factor = [matrixRow1[popularCharacterIndex][j] for j in nonZeroIndexList]
        n = len(factor)
        mean1 = np.mean(factor)
        factor = [mean1/z for z in factor]
        x=[factor[k]*np.cos(2*np.pi*k/n)+listOfNewCenters[0][0] for k in range(n)]
        y=[factor[k]*np.sin(2*np.pi*k/n)+listOfNewCenters[0][1] for k in range(n)]
        for z in range(n):
            if self.ranks.index(nonZeroIndexList[z]) < self.maxNOC:               
 
                characterPoints[nonZeroIndexList[z]] = (x[z],y[z])
        pointConnections = {}   # what nodes are adjacent 
        dicList = list(characterPoints.keys())
        for i in range(len(dicList))[:len(dicList)-1]:
            networkI = dicList[i]
            for j in range(len(dicList))[i+1:]:
                networkJ = dicList[j]
                factor = matrixRow1[networkI,networkJ]
                if factor != 0:
                    try:
                        pointConnections[networkI].append(networkJ)
                    except KeyError:
                        pointConnections[networkI] = [networkJ]
                    x1 = characterPoints[networkI][0]
                    y1 = characterPoints[networkI][1]
                    x2 = characterPoints[networkJ][0]
                    y2 = characterPoints[networkJ][1]
                    newx = (1-factor)*x1+factor*x2
                    newy = (1-factor)*y1+factor*y2
                    characterPoints[networkI] = (newx,newy)
                    newx = (1-factor)*x2+factor*x1
                    newy = (1-factor)*y2+factor*y1
                    characterPoints[networkJ] = (newx,newy)
        for point in pointConnections:
            for b in pointConnections[point]:
                graph.plot([characterPoints[point][0],characterPoints[b][0]],[characterPoints[point][1],characterPoints[b][1]],'k')
        for g in characterPoints:
            graph.plot(characterPoints[g][0],characterPoints[g][1],'yo')
            graph.annotate(self.names[g]+', rank: '+str(self.ranks.index(g)+1), xy=(characterPoints[g][0],characterPoints[g][1]), xytext=(characterPoints[g][0]-0.03,characterPoints[g][1]-0.1),horizontalalignment='left', verticalalignment='bottom',color='blue')
            graph.plot([characterPoints[g][0],listOfNewCenters[0][0]],[characterPoints[g][1],listOfNewCenters[0][1]],'k')
        graph.plot(listOfNewCenters[0][0],listOfNewCenters[0][1],'y*',markersize=15,label=self.names[popularCharacterIndex]+', rank: '+str(1)+ ' ' +str((listOfNewCenters[0][0],listOfNewCenters[0][1])))
        graph.legend()
        
# THE FOLLOWING IS AN ATTEMPT BY ME TO CLUSTER
#==============================================================================
#     def network_plot_circle(self,title):
#         numberOfCharacters = self.maxNOC
#         specificityConstant = self.sC
#         fig = plt.figure()
#         graph = fig.add_subplot(111)
#         matrixRow1 = np.transpose(self.matrixColumn1)
#         listOfNewCenters = [(0,0)]
#         counter = 1
#         while (len(listOfNewCenters) <= numberOfCharacters):
#             listOfNewCenters.extend([(2*counter,-2*counter),(-2*counter,-2*counter),(2*counter,2*counter),(-2*counter,2*counter)])
#             counter += 1
#         while (len(listOfNewCenters) > numberOfCharacters):
#             listOfNewCenters.pop()
#             
#         for i in range(numberOfCharacters):
#             indexOfInterest = i
#             popularCharacterIndex = self.ranks[indexOfInterest]
#             nonZeroIndexList = [j for j in range(len(self.network[popularCharacterIndex])) if self.network[popularCharacterIndex][j] >=specificityConstant] 
#             factor = [matrixRow1[popularCharacterIndex][j] for j in nonZeroIndexList]
# #==============================================================================
# #             factor.sort()
# #             factor = factor[::-1]
# #             factor = factor[:10]
# #             factorForIndex = factor
# #==============================================================================
#             n = len(factor)
#             mean1 = np.mean(factor)
#             factor = [mean1/z for z in factor]
#             x=[factor[k]*np.cos(2*np.pi*k/n)+listOfNewCenters[indexOfInterest][0] for k in range(n)]
#             y=[factor[k]*np.sin(2*np.pi*k/n)+listOfNewCenters[indexOfInterest][1] for k in range(n)]
#             for z in range(n):
#                 graph.plot([listOfNewCenters[indexOfInterest][0],x[z]],[listOfNewCenters[indexOfInterest][1],y[z]],'k',gid=nonZeroIndexList[z])
#             for z in range(n):
#                 graph.plot(x[z],y[z],'bo',gid=nonZeroIndexList[z])
#             graph.plot(listOfNewCenters[indexOfInterest][0],listOfNewCenters[indexOfInterest][1],'y*',label=self.names[popularCharacterIndex]+', rank: '+str(indexOfInterest+1)+ ' ' +str((listOfNewCenters[indexOfInterest][0],listOfNewCenters[indexOfInterest][1])),gid=0)
#             break;
#         graph.legend()
#         
#         annotation = None
#         counter = 0
#         ff = (-5,5)   # I have to manually do this part
#         def onClick(event):
#             global annotation
#             for point in graph.get_lines():
#                 if point.contains(event)[0]:
#                     annotation = graph.annotate(self.names[point.get_gid()]+', rank: '+str(self.ranks.index(point.get_gid())+1),xy=ff) 
# #==============================================================================
# #         def remove_annot(event):
# #             ann.remove()
# #             fig.canvas.draw()
# #==============================================================================
# 
#         
#         fig.canvas.mpl_connect('button_press_event', onClick)
# #==============================================================================
# #         fig.canvas.mpl_connect('button_release_event', remove_annot)  
# #==============================================================================
# #==============================================================================
# #                     num = 255 - 255*matrixRow1[i][j]
# #                     g = hex(int(num))
# #                     if len(g)==3:
# #                         string = "0"
# #                     color = '#ff' + string + g[2:] + '00'
# #                     graph.plot([x[i],x[j]],[y[i],y[j]],color)   # the colors are determined by magnitude
# #==============================================================================
# #==============================================================================
# #         for i in range(n):
# #             num = 50
# #             graph.plot(x[i],y[i],'bs')   #blue square for males
# #             # xytext=(x[i]-1,y[i]+2)
# #             graph.annotate(self.names[i]+', rank: '+str(self.ranks.index(i)+1), xy=(x[i],y[i]), xytext=(x[i],y[i]-3),arrowprops=dict(facecolor='black', shrink=0.05),horizontalalignment='left', verticalalignment='bottom',)
# #         graph.set_title(title)
# #         return fig
# #==============================================================================
#==============================================================================

character = character_network(lord,10,2)
character.createCharacterNetwork()
for i in range(10):
    print (character.names[character.ranks[i]])
#print (character.names)