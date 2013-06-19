import math
from variations import SplitIntoChars, Chars
from struct import pack, unpack
def NewLoad(br, tr):
    return word(tr).Load(br)

maxl=[0 for i in range(9)]
class word:# : IComparable
    def Load(self, br):
        self.m_index = br.tell()
        length = unpack('<b',br.read(1))[0]
        wd_str = map(lambda x:Chars[x],unpack('<'+'b'*length,br.read(length)))
        wd_str = '|'.join(wd_str) 
        self.m_word = wd_str
        self.count, self.xCount, length = unpack('<ifb', br.read(9))
#        for i in range(length):
#            self.children[unpack('<b', br.read(1))[0]] = unpack('<i', br.read(4))[0]
        self.children = dict([unpack('<bi', br.read(5)) for i in range(length)])
        self.grandChildren = []
        length = unpack('<b', br.read(1))[0]
        self.grandChildren = list(unpack("<"+'i'*length, br.read(4*length)))
        return self;
    
    def Save(self, bw, csvfile, NewWordsOnly):
        if csvfile and (self.count and ((not NewWordsOnly) or 0>self.m_index)):
            csvfile.write(str(self) + ","+str(self.count)+'\n')
        for cV in self.children.values():
            self.Trie.GetSavedIndex(cV, bw,csvfile,NewWordsOnly);
        r = bw.tell()
        splited=SplitIntoChars(self.m_word)
        bw.write(pack('<b', len(splited)))
        maxl[0]=max(len(splited), maxl[0])
        bw.write(pack("<"+"b"*len(splited), *splited))
        bw.write(pack('<ifb', self.count, self.xCount, len(self.children)));
        maxl[1]=max(self.count,maxl[1])
        maxl[2]=max(self.xCount,maxl[2])
        maxl[3]=max(len(self.children),maxl[3])
        for cK,cV in self.children.items():
            bw.write(pack('<b',cK));
            maxl[4]=max(cK,maxl[4])
            savedIdx=self.Trie.GetSavedIndex(cV, None, None, False)
            bw.write(pack('<i',savedIdx))
            maxl[5]=max(savedIdx,maxl[5])
        grand = self.GetAllChildrenIndexes()
        bw.write(pack("<b",len(grand)))
        maxl[6]=max(len(grand),maxl[6])
        for g in grand:
            if self.m_index==g:
                bw.write(pack("<i",r))
                maxl[7]=max(r,maxl[7])
            else:
                savedIdx = self.Trie.GetSavedIndex(g, None, None, False)
                bw.write((pack('<i', savedIdx)))
                maxl[8]=max(savedIdx,maxl[8])
        bw.flush()
        return r

    def __init__(self, tr=None, index=None):
        if index != None:
            self.m_index = index
        self.Trie = tr
        self.count = 0
        self.xCount = -float('inf')
        self.TravelProbability = -float('inf')
        self.m_word = ""
        
        self.children = {}
        self.grandChildren = None
        self.m_index = 0

    def Add(self, s, c, complete_word):
        self.grandChildren = None
        if not s:
            self.count = c;
            self.m_word = complete_word;
            return self;
        ky = s[0]
        if not ky in self.children:
            w = word(self.Trie);
            self.children[ky] = self.Trie.Add2List(w);
            w.m_index = self.children[ky];
        return self.Trie.GetIndexedWord(self.children[ky]).Add(s[1:], c, complete_word);

    def GetAllChildrenIndexes(self):
        if self.grandChildren == None:
            r = []
            wr = []
            self.grandChildren = []
            if self.count != 0:
                r.append(self.m_index)
            for cValue in self.children.values():
                r+=self.Trie.GetIndexedWord(cValue).GetAllChildrenIndexes()
            for i in r:
                wr.append(self.Trie.GetIndexedWord(i))
            wr.sort()
            self.grandChildren += [w.m_index for w in wr[:self.Trie.MaxItems+1]]
        return self.grandChildren
    
    def GetAllChildren(self):
        r = []
        ri = self.GetAllChildrenIndexes();
        ri = ri[:self.Trie.MaxItems]
        for i in ri:
            r.append(self.Trie.GetIndexedWord(i));
        return r;
    
    def __str__(self):
        return self.m_word
    def __lt__(self, o): 
        return o.Probability() < self.Probability()
    def __eq__(self, o): 
        return o.Probability() == self.Probability()
    def OriginalProbability(self):
        if self.count == 0:
            return -float('inf')
        return math.log(self.count) - math.log(self.Trie.totalWordCount);
    def Probability(self):
        if self.TravelProbability == -float('inf'):
            return self.OriginalProbability()
        return self.OriginalProbability() + self.xCount + self.TravelProbability

def DummyWord(s):
    r=word()
    r.m_word=s
    return r

#    static public word DummyWord(string s,int count)
#    {
#        word r = DummyWord(s);
#        r.count = count;
#        return r;
#    }

def CompundWord(s_word, p_count, xcnt, tr):
    r = word()
    r.m_word = s_word;
    r.count = p_count;
    r.xCount = xcnt;
    r.Trie = tr
    return r