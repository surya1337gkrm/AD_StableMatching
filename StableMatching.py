import random
import time

n=int(input("Men and Women should be equal. Enter Number of men/Women: "))

def randomList(n):
    l=[x for x in range(0,n)]
    random.shuffle(l)
    return l

def createPrefLists(n):
    menPref={x:None for x in range(0,n)}
    womenPref={x:None for x in range(0,n)}
    
    for i in range(0,n):
        
        menPref[i]=randomList(n)
        womenPref[i]=randomList(n)
    
    return menPref,womenPref

def findWomenPref(pairlist,woman):    
    for i in range(0,len(pairlist)):
        if pairlist[i][1] == woman:
            return pairlist[i], i
    #return None


def findStableMatch():
    start=time.time()
    random.seed(0)
    menPref,womenPref=(createPrefLists(n)[0]),(createPrefLists(n)[1])
    menPrefList=list(menPref.values())
    womenPrefList=list(womenPref.values())
    
    menPaired=[0]*n
    womenPaired=[0]*n
    pairs=[]

    while 0 in menPaired:
        man=menPaired.index(0)
        for i in range(0,n):
            woman=menPrefList[man][i]
            if womenPaired[woman]==0:
                pair=(man,woman)
                
                menPaired[man]=1
                womenPaired[woman]=1
                pairs.append(pair)
                break
            else:
                manRank=womenPrefList[woman].index(man)
                currPair,pos=findWomenPref(pairs,woman)
                currMan=currPair[0]
                currManRank=womenPrefList[woman].index(currMan)

                if manRank<currManRank:
                    newPair=(man,woman)
                    
                    del pairs[pos]
                    menPaired[man]=1
                    menPaired[currMan]=0
                    pairs.append(newPair)
                    break
                else:
                    continue
    end=time.time()
    execTime=(end-start)*1000           
    return pairs,menPref,womenPref,execTime           

def verifyStableMatch(pairs,mlist,wlist):
    for i in pairs:
        
      currMan=i[0]
      currWoman=i[1]
      currManRank=wlist[currWoman].index(currMan)
      currWomanRank=mlist[currMan].index(currWoman)

      currWomanList=wlist[currWoman]

      for m in currWomanList:
          if currWomanList.index(m)<currManRank:
              manList=mlist[m]
              womanRankinMan=manList.index(currWoman)
              manPair=(list(filter(lambda x:x[0]==m,pairs)))[0][1]
              manPairRank=manList.index(manPair)
              if(womanRankinMan<manPairRank):
                  print("Unstable Pair Found.")
                  return False        
            

pairs,mlist,wlist,execTime=findStableMatch()   
   

print("Men Preference List : \n {0}".format(mlist)) 
print("Women Preference List : \n {0}".format(wlist))
print("Stable Matching : \n {0}".format(pairs))
l="For n={0}\nMen Preference List : {1}\nWomen Preference List : {2}\nStable Matching: {3}\n".format(n,mlist,wlist,pairs)
resultFile=open("resultFile.txt",'a')
resultFile.writelines(l+'\n')

print("Total time for Execution: {0}".format(execTime))


verifiedStableMatch=verifyStableMatch(pairs,mlist,wlist)
#verifiedStableMatch=verifyStableMatch([(0,1),(3,2),(2,3),(1,0)],mlist,wlist)

if verifiedStableMatch==False:
    print('Matching isnt stable.')
else:
    print('Matching is Stable.') 