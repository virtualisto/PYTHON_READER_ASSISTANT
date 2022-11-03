print('-------------------------------')
rassist='221026 READER-ASSISTANT-T.py'
print(rassist)
print('-------------------------------')
##################################################
# Use Adobe Acrobat DC to convert .PDF to .DOCX.
# Be sure to CLOSE WORD after the conversion.
##################################################
import  docx2txt     #https://pypi.org/project/doc2text/
import  nltk         # https://www.nltk.org/
from    nltk import word_tokenize
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
    print('-------------------------------')
    print('CORPUS = ',corpusfile)
    print('-------------------------------')
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
    f.write(('-------------------------------'+'\n').encode("utf8"))
    f.write(('Number of characters, words, sentences = '+report).encode("utf8"))
    f.write(('-------------------------------'+'\n').encode("utf8"))
    f.close()
    print('Number of characters, words, sentences = ',len(corpustext),len(wordlist),len(sentlist))
    print('-------------------------------')
    freqtester=nltk.FreqDist(nltkwordlist)# <class 'nltk.probability.FreqDist'>
    tms=freqtester.items()          # <class 'dict_items'>
    tmslist=list(tms)               # <class 'list'>  
    most=freqtester.most_common(100)# <class 'list'>
    minwordlength = 6
    best=[x for x,y in most if len(x) > minwordlength]  # <class 'list'>
    print('Most common words with length > ',minwordlength,' = ')
    for i in range(0,len(best)):
        print(best[i])
    
def instructions():
    print('wordlist         =any non-empty list of words')
    print('best             =wordlist of most frequent words of length > 6.')
    print('sentlist         =actual list of all sentences')
    print('gist(wordlist)   =sentences with those words in UPPERCASE.')
    print('wlf(wordlist)    =frequencies of those words in sentlist.')
    print('wordlist         =any of "best", "qt", "qu", "qv", "qw", "philo", "theo", or "proc".')
    print('gistit(wordlist,sentlist) percentage of hits.')
    print('tamale(wordlist) =count of words of wordlist in sentlist')
print('-------------------------------------------------------------------------')
instructions()
print('-------------------------------------------------------------------------')
##################################################
# FUNCTION DEFINITIONS
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

def andgist(wordlist):
    f=open(path+name,'ab')
    f.write(('----andgist--------------------'+'\n').encode("utf8"))
    for w in wordlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-------------------------------'+'\n').encode("utf8"))
    print('keyword list = ',wordlist,'\n')
    for k in range(0,len(sentlist)):
        if tester(wordlist,sentlist[k]):
            sent=sentlist[k]                    # string
            for w in range(0,len(wordlist)):
                sent=upperizer(sent,wordlist[w])# string
            f.write((str(k)+' '+sent+'\n').encode("utf8"))
            f.write(('\n').encode("utf8"))
            print(k,sent,'\n')
    f.close()

def orgist(wordlist):
    f=open(path+name,'ab')
    f.write(('----orgist---------------------'+'\n').encode("utf8"))
    for w in wordlist:
        f.write((w+'\n').encode("utf8"))
    f.write(('-------------------------------'+'\n').encode("utf8"))
    print('keyword list = ',wordlist,'\n')
    for k in range(0,len(sentlist)):
        if ortester(wordlist,sentlist[k]):
            sent=sentlist[k]                    # string
            L=sent.split()                      # list of strings
            for w in wordlist:
                if w in L:
                    sent=upperizer(sent,w)      # string
                    sent.encode("utf8")
            print(k,sent,'\n')
            f.write((str(k)+' '+sent+'\n').encode("utf8"))
            f.write('\n'.encode("utf8"))
    f.close()
    
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
    return [list(x) for x in combinations(best,2)]

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
    gist=maxgister(best,sentlist)
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
qt=[
    'philosophical',
    'theoretical',
    'process',
    'systems'
    ]
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
qv=['Varela',
    'Moreno',
    'Longo',
    'Mossio',
    'Tononi',
    'Soto',
    'Sherrington',
    'Mirazo'
    ]
qw=[
    'Jonas',
    'delbruck',
    'Descartes',
    'Herder',
    'Goethe',
    'Schelling',
    'Peirce',
    'Bergson',
    'Husserl',
    'Kant',
    'Aristotle',
    'Brentano',
    'Scheler',
    'Whitehead',
    'Bertalanffy',
    'Uexkull',
    'Buytendijk',
    'Plessner',
    'Merleau',
    'Ponty',
    'Merleau-Ponty',
    'Lorenz',
    'Thorpe',
    'Sebeok',
    'Hoffmeyer',
    'Kull',
    'Krampen',
    'Chebanov',
    'Markos',
    'Witzany',
    'Bohr',
    'Schrodinger',
    'Neumann',
    'Pauli',
    'Rashevksy',
    'Bohm',
    'Elsasser',
    'Pattee',
    'Thomson',
    'Waddington',
    'Needham',
    'Goodwin',
    'Kauffman',
    'Ho',
    'Simon',
    'Prigogine',
    'Haken',
    'Allen',
    'Salthe',
    'Rosen',
    'Crick',
    'Watson',
    'Monod',
    'Hamilton',
    'Dawkins',
    'Hobbes',
    'Galileo',
    'Pythagoras',
    'Newton',
    'Hilbert',
    'Church',
    'Turing',
    'Godel',
    'Kercel',
    'Kepler',
    'Mikulecky',
    'Bruno',
    'Herder',
    'Goethe',
    'Fichte',
    'Holderlin',
    'Bogdanov',
    'Oersted',
    'Grassmann',
    'Herz',
    'Juarrero',
    'Salthe',
    'Piaget',
    'Hoffmeyer',
    'Kull',
    'Cottam',
    'Ranson',
    'Vounckx'
    ]


philo=['Aristotle',
'Bergson',
'Church',
'Crick',
'Dawkins',
'Delbruck',
'Descartes',
'Elsasser',
'Galileo',
'Goethe',
'Hamilton',
'Hilbert',
'Hobbes',
'Jonas',
'Kepler',
'Merleau',
'Mikulecky',
'Monod',
'Newton',
'Pattee',
'Pythagoras',
'Turing',
'Watson',
]

theo=[
'Allen',
'Bohr',
'Brentano',
'Buytendijk',
'Chebanov',
'Goodwin',
'Haken',
'Ho',
'Husserl',
'Kant',
'Kauffman',
'Krampen',
'Lorenz',
'Markos',
'Merleau-Ponty',
'Needham',
'Neumann',
'Pauli',
'Plessner',
'Rashevksy',
'Rosen',
'Scheler',
'Schrodinger',
'Simon',
'Thomson',
'Thorpe',
'Uexkull',
'Waddington',
'Witzany',
]

proc=[
'Bertalanffy',
'Bogdanov',
'Bohm',
'Bruno',
'Cottam',
'Fichte',
'Grassmann',
'Herder',
'Herz',
'Hoffmeyer',
'Holderlin',
'Juarrero',
'Kercel',
'Kull',
'Oersted',
'Peirce',
'Piaget',
'Prigogine',
'Ranson',
'Salthe',
'Schelling',
'Sebeok',
'Vounckx',
'Whitehead',
]
    
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
