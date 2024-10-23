
print('-'*60)
rassist='October 22, 2024 READER-ASSISTANT-ZM.py'
print(rassist)
print('-'*60)
##################################################
# Use Adobe Acrobat DC to export .PDF to .DOCX.
# Be sure to CLOSE WORD after the conversion.
##################################################
import  docx2txt     #https://pypi.org/project/doc2text/
import  nltk         # https://www.nltk.org/
from    nltk import word_tokenize
nltk.download('punkt')
from    tkinter.filedialog import askopenfilename
####CLEANUP#######################################
punct=["'",',','.','<','>','?','(',')',':',';','*','+',
       '!','@','#','$','%','^','&','_','-','=']
def cleanup(str):
    corpus=str
    for p in punct:
        corpus=corpus.replace(p,' '+p+' ')
    return corpus
def filer():
    global file
    global name
    global path
    global extn
    path=corpusfile[:corpusfile.find('DOCX')+5]
    file=corpusfile[corpusfile.find('DOCX')+5:]
    name=file[:file.find('.docx')]+'.txt'
    extn=file[-4:]
    f=open(path+name,'ab')
    f.write((rassist).encode("utf8"))
    f.write(('\n').encode("utf8"))
    f.write((name).encode("utf8"))
    f.write(('\n').encode("utf8"))
    f.close()

def filetag(filename):
    x=file[:file.find('.docx')]
    p=x.find('/')+1
    return '('+x[p:]+' '+')'
    
def start():
    global best
    global wordlist
    global sentlist
    global corpusfile
    global freqtester
    global corpusfile
    global corpustext
    corpusfile=askopenfilename()
    filer()
    print('-'*60)
    print('CORPUS = ',corpusfile)
    print('-'*60)
    if extn == '.txt':
        print('corpustext = Open and read .txt file.')
        with open(corpusfile) as f:
            textlist=f.readlines()                      # list of strings
            f.close()
            corpustext=' '.join(textlist)               # <class 'str'>
    else:
        print('do doc2txt')
        corpustext=docx2txt.process(corpusfile)         # <class 'str'>
    print('cleanup underway...')
    corpustext=cleanup(corpustext)
    wordlist=word_tokenize(corpustext)                  # <class 'list'>
    nltkwordlist=nltk.Text(wordlist)                    # <class 'nltk.text.Text'>
    sentlist=nltk.sent_tokenize(corpustext)             # <class 'list'>
    f=open(path+name,'ab')
    report=str(len(corpustext))+' '+str(len(wordlist))+' '+str(len(sentlist))+'\n'
    f.write(('-'*60+'\n').encode("utf8"))
    f.write(('Number of characters, words, sentences = '+report).encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    f.close()
    print('Number of characters, words, sentences = ',len(corpustext),len(wordlist),len(sentlist))
    print('-'*60)
    freqtester=nltk.FreqDist(nltkwordlist)# <class 'nltk.probability.FreqDist'>
    tms=freqtester.items()          # <class 'dict_items'>
    tmslist=list(tms)               # <class 'list'>  
    most=freqtester.most_common(100)# <class 'list'>
    ml=int(input('Enter minimum key-word length: '))
    minwordlength = ml
    best=[x for x,y in most if len(x) > minwordlength]  # <class 'list'>
    print('Most common words with length > ',minwordlength,' = ')
    for i in range(0,len(best)):
        print(best[i])
    
def instructions():
    print('wordlist         =any non-empty list of words')
    print('best             =wordlist of most frequent words of length > 6.')
    print('sentlist         =actual list of all sentences')
    print('wlf(wordlist)    =frequencies of those words in sentlist.')
    print('wordlist         =any of "best", "qt", "qu", "qv", "qw", "philo", "theo", or "proc".')
    print('gistit(wordlist,sentlist) percentage of hits.')
    print('tamale(wordlist) =count of words of wordlist in sentlist')
    print('pairmax(best,sentlist) = for each pair in best, count number of sentences, return sentences of pair with maximum number of sentences')
    print('triplemax(best,sentlist) = for each triple in best, count number of sentences, return sentences of triple with maximum number of sentences')
    print('-------------------------------------------------------------------------')
instructions()
print('-------------------------------------------------------------------------')
##################################################
# FUNCTION DEFINITIONS
##################################################
def tester(wordlist,sentence):      # list of strings and string
    lw=len(wordlist)
    b=True
    z=sentence.split()              # z is a list
    for i in range(0,lw):
        b = b and wordlist[i] in z  # string in a list
    return b                        # they are all there

def ortester(wordlist,sentence):    # list of strings and string
    lw=len(wordlist)
    b=False
    z=sentence.split()              # z is a list
    for i in range(0,lw):
        b = b or wordlist[i] in z   # string in a list
    return b                        # at least one is there

def upperizer(sent,word):           # string and string
    return sent.replace(word,word.upper())

import re

def cleanit(s):
    pattern = re.escape('\n') + r'+'
    replacement = ' '
    s=re.sub(pattern, replacement, s)
    return s.replace(' - ','-')\
            .replace(' .','.')\
            .replace(' ,',',')\
            .replace('  ',' ')\
            .replace('- ','-')

def cleanitup(s):
    s = re.sub(r'\n+', '\n', s)
    s = re.sub(r' +', ' ', s)
    return s.replace(' - ','-')\
            .replace('- ','-')\
            .replace(' -','-')\
            .replace(' .','.')\
            .replace('. ','.')\
            .replace(' . ','.')\
            .replace(' ,',',')\
            .replace(', ',',')\
            .replace(' , ',',')
            #.replace('  ',' ')

##################################################            
def andgist(wordlist):
    f=open(path+name,'ab')
    f.write(('-'*60+'\n').encode("utf8"))
    f.write((file+'\n').encode("utf8"))
    #f.write(('-'*60+'\n').encode("utf8"))
    f.write(('----andgist--------------------'+'\n').encode("utf8"))
    for w in wordlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    print('keyword list = ',wordlist,'\n')
    tag=filetag(file)
    for k in range(0,len(sentlist)):
        if tester(wordlist,sentlist[k]):
            sent=sentlist[k]                    # string
            for w in range(0,len(wordlist)):
                sent=upperizer(sent,wordlist[w])# string
                sent=cleanit(sent)
            out=tag+str(k)+' '+sent+'\n'
            f.write((out).encode("utf8"))
            f.write(('\n').encode("utf8"))
            print(out)
    f.close()

def newandgist(wlist,slist):
    sl=[]
    f=open(path+name,'ab')
    f.write(('-'*60+'\n').encode("utf8"))
    f.write((file+'\n').encode("utf8"))
    f.write(('----newandgist-----------------'+'\n').encode("utf8"))
    for w in wlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    print('keyword list = ',wlist,'\n')
    tag=filetag(file)
    for k in range(0,len(slist)):
        if tester(wlist,slist[k]):
            sent=slist[k]                    # string
            for w in range(0,len(wlist)):
                sent=upperizer(sent,wlist[w])# string
            out=tag+str(k)+' '+sent+'\n'
            f.write((out).encode("utf8"))
            print(out)
            sl.append(sent)
    f.close()
    return sl    

def orgist(wordlist):
    f=open(path+name,'ab')
    f.write(('-'*60+'\n').encode("utf8"))
    f.write((file+'\n').encode("utf8"))
    #f.write(('-'*60+'\n').encode("utf8"))
    f.write(('----orgist---------------------'+'\n').encode("utf8"))
    for w in wordlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    print('keyword list = ',wordlist,'\n')
    tag=filetag(file)
    for k in range(0,len(sentlist)):
        if ortester(wordlist,sentlist[k]):
            sent=sentlist[k]                    # string
            L=sent.split()                      # list of strings
            for w in wordlist:
                if w in L:
                    sent=upperizer(sent,w)      # string
                    sent=cleanit(sent)
                    sent.encode("utf8")
            out=tag+str(k)+' '+sent+'\n'
            f.write((out).encode("utf8"))
            print(out)
    f.close()

def neworgist(wlist,slist):
    sl=[]
    f=open(path+name,'ab')
    f.write(('-'*60+'\n').encode("utf8"))
    f.write((file+'\n').encode("utf8"))
    #f.write(('-'*60+'\n').encode("utf8"))
    f.write(('----neworgist---------------------'+'\n').encode("utf8"))
    for w in wlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    print('keyword list = ',wlist,'\n')
    tag=filetag(file)
    for k in range(0,len(slist)):
        if ortester(wlist,slist[k]):
            sent=slist[k]                       # string
            L=sent.split()                      # list of strings
            for w in wlist:
                if w in L:
                    sent=upperizer(sent,w)      # string
                    sent.encode("utf8")
            out=tag+str(k)+' '+sent+'\n'
            f.write((out).encode("utf8"))
            print(out)
            sl.append(sent)
    f.close()
    return sl
##################################################

def gistindices(wordlist,corpus):
    output=[]
    for k in range(0,len(corpus)):
        if tester(wordlist,corpus[k]):
            output=output+[k]
    return output

def printgistindices(wordlist,corpus):
    print(wordlist,'\n')
    x=gistindices(wordlist,corpus)
    for i in range(0,len(x)):
        print(x[i])
        
def concatter(corpus,n):
    output=''
    for i in range(0,n):
        output=output+corpus[i]
    return output

def printer(list,n):
    for i in range(0,n):
        print(list[i])

def printgist(indexlist):
        f=open(path+name,'ab')
        f.write((rassist).encode("utf8"))
        f.write(('\n').encode("utf8"))
        f.write((name).encode("utf8"))
        f.write(('\n').encode("utf8"))
        for i in indexlist:
            print(i,'    ',sentlist[i])
            f.write(('\n'+'--------------------------------'+'\n').encode("utf8"))
            f.write((str(i)+'    '+str(sentlist[i])).encode("utf8"))
        f.close()
    
##################################################
# 221013 New Developments
# Which pair of distinct key-words both occur in the largest number of
# sentences?

def keylistofsentidx(frequlist,sentindx):
    return list(set(word_tokenize(sentlist[sentindx])).intersection(set(frequlist)))

from itertools import combinations

def keypairs(frequlist):
    return [list(x) for x in combinations(frequlist,2)]

def maxgister(frequlist,corpus):
    kp=keypairs(frequlist)
    c=0
    g=[]
    pp=[]
    for p in kp:
        gl=gistindices(p,corpus)
        if len(gl)>c:
            c=len(gl)
            g=gl
            pp=p
    return [pp,g]

def gistit(frequlist,corpus):
    gist=maxgister(frequlist,corpus)
    for x in gist[1]:
        print(gist[0],'    ',x,'  ',sentlist[x],'\n')
    print('Number of key-words    ',len(frequlist))
    print('Two main key-words     ',gist[0])
    print('Number of hits         ',len(gist[1]))
    print('Number of sentences    ',len(corpus))
    print('Percentage of hits     ', "{:.2%}".format(len(gist[1])/len(corpus)))
##################################################
# 221022 New Developments
# What are all the sentences with any of these words?
# Display such a sentence with uppercase version of found word(s).
# What is the frequency of a word in the text?

def wfrequ(word):
    lots=freqtester.most_common(10000)
    keys=[w for w,c in lots]
    if word in keys:
        return [c for w,c in lots if w==word][0]
    else:
        return 0

def wlistfrequ(wlist):
    if len(wlist) > 0:
        for w in wlist:
            print(w.ljust(20),wfrequ(w))
    else:
        print('Oops, no list.')

def wlf(wordlist):
    lots=freqtester.most_common(10000)
    d=dict(lots)
    vkp=((value,key) for (key,value) in d.items() if key in wordlist)
    sorted_vkp=sorted(vkp,reverse=True)
    listsorted=list(sorted_vkp)
    for (v,k) in listsorted:
        print(k.ljust(20),v)  
    
##################################################
qu=[
    'challenge',
    'difficulty',
    'problem',
    'problems',
    'difficulties',
    'issue',
    'issues',
    'puzzle',
    'answer',
    'answers',
    'understood',
    'understand',
    'understanding',
    'explain',
    'explanation',
    'paradox',
    'question',
    'problematic',
    'surprise',
    'surprising',
    'account'
    ]

inference = ['so',
             'proof',
             'therefore',
             'consequently',
             'conclusion',
             'deduce',
             'deudction',
             'infer',
             'inference',
             'conclude',
             'derive',
             'assume',
             'construe',
             'glean',
             'interpret',
             'presuppose',
             'axiom',
             'axiomatic',
             'reckon',
             'reason',
             'reasonable',
             'speculate',
             'surmise',
             'conjecture',
             'induce',
             'induction',
             'suppose',
             'understand',
             'intuit',
             'intuition',
             'intuitive',
             'gather',
             'judge',
             'think',
             'conclusion',
             'believe',
             'trust',
             'faith'
    ]

##################################################

def bigtester(qwordlist,sentence):
    b=False
    sent=sentence
    for qw in qwordlist:
        if tester([qw],sent):
            sent=upperizer(sent,qw)
            print('---------------------------')
            print('Found----> ',qw)
            print('---------------------------')
            b=True
    if b:
        print(sent)
        return b

def tamale(qwordlist):
    print('---------------------------')
    print(qwordlist)
    print('---------------------------')
    count=0
    for s in sentlist:
        if bigtester(qwordlist,s):
            count=count+1
    print('---------------------------')
    print(corpusfile)
    print('---------------------------')
    print('query words -------> ',qwordlist)
    print('---------------------------')
    print('found count -------> ',count)
    print('---------------------------')

#-------------------------------------------------
# November 11, 2023
#-------------------------------------------------
from itertools import combinations
# Return list of pairs of distinct members in a list
def pairs(L):
    return [list(tuple(sorted(comb))) for comb in combinations(L, 2)]

def triples(L):
    return [list(tuple(sorted(comb))) for comb in combinations(L, 3)]

# Return key word pair of key word index pairs in key word list
def kpair_to_wpair(klist,pidx):
    return [klist[pidx[0]],klist[pidx[1]]]

def ktriple_to_wtriple(klist,tidx):
    return [klist[tidx[0]],klist[tidx[1]],klist[tidx[2]]]
            
# Return list of sentence indices that contain words in key word list
def ander(slist,klist):
    return[s for s in range(len(slist)) if tester(klist,slist[s])]

def pairmax(wlist,slist):
            A=[[kpair_to_wpair(best,[i,j]),len(ander(sentlist,kpair_to_wpair(best,[i,j])))]\
            for [i,j] in pairs(range(len(best)))]
            ANEW = sorted(A, key=lambda x: x[1], reverse=True)
            andgist(ANEW[0][0])

def triplemax(wlist,slist):
            B=[[ktriple_to_wtriple(best,[i,j,k]),len(ander(sentlist,ktriple_to_wtriple(best,[i,j,k])))]\
            for [i,j,k] in triples(range(len(best)))]
            BNEW = sorted(B, key=lambda x: x[1], reverse=True)
            andgist(BNEW[0][0])
            
def phraser(phrasestring):
    global pattern
    f=open(path+name,'ab')
    f.write(('-'*60+'\n').encode("utf8"))
    f.write((file+'\n').encode("utf8"))
    f.write(('-'*4+'phraser'+'-'*49+'\n').encode("utf8"))
    f.write((phrasestring+'\n').encode("utf8"))
    f.write(('-'*60+'\n').encode("utf8"))
    print('phrase = ',phrasestring,'\n')
    phr=cleanitup(phrasestring)
    tag=filetag(file)
    for k in range(0,len(sentlist)):
        s=cleanitup(sentlist[k])
        match = re.search(phr, s, re.IGNORECASE)
        if  match:
            sent=cleanit(sentlist[k])
            sent=upperizer(sent,phr)
            out=tag+str(k)+' '+sent+'\n'
            f.write((out).encode("utf8"))
            f.write(('\n').encode("utf8"))
            print(out)
    f.close()

def phraser2(phrasestring):
    global pattern
    print('phrase = ',phrasestring,'\n')
    phr=cleanitup(phrasestring)
    for k in range(0,len(sentlist)):
        s=cleanitup(sentlist[k])
        match = re.search(phr, s, re.IGNORECASE)
        if  match:
            sent=cleanit(sentlist[k])
            sent=upperizer(sent,phr)
            print(k,sent,'\n')

def doitall():
    andgist(['feeling','emotion'])
    pairmax(best,sentlist)
    phraser('conscious thought')
    phraser('stream')
    phraser('intuit')
    phraser('specious present')
    triplemax(best,sentlist)
    orgist(['retention','impression','protention'])

def redoitall():
    triplemax(best,sentlist)
    phraser('conscious thought')
    phraser('specious present')
    orgist(['pulse','wave','stream','metaphor','motion','imagination','behavior','model'])

def newdo():
    phraser('inner')
    phraser('mental model')
    phraser('conscious thought')
    phraser('temporal consciousness')
    phraser('temporal awareness')
    phraser('infinite regress')
    phraser('living present')
    phraser('specious present')
    phraser('absolute')
    
