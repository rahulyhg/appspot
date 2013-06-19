import variations
from word import word, NewLoad, DummyWord, CompundWord, maxl
import re
import math
from struct import pack, unpack
import os
class dummyfile():
    def __init__(self):
        self.t = 0
    def write(self, x):
        print self.t, len(x), x.encode('hex')
        self.t += len(x)
        
    def flush(self):
        pass
    def tell(self):
        return self.t
    def seek(self,t):
        self.t=t
    def close(self):
        pass
    
class find_return:
    def __init__(self):
        self.Completes=[]
        self.Partials=[]
        self.Bigrams = {}
        self.TravelProbabilies = {}
    def Add2CompletesPartials(self, w, TravelProbability): 
        if w.count:
            if w in self.Completes:
                w.TravelProbability = max(w.TravelProbability, TravelProbability)
            else:
                self.Completes.append(w)
                w.TravelProbability = TravelProbability
                #//TravelProbabilities[w.ToString()+":"+u] = TravelProbability
            #//print w, TravelProbability
        self.Add2Partials(w);                 

    def Add2Completes(self, wl):
        self.Add2Set(self.Completes, wl)
    def Add2Partials(self, w):
        self.Add2Set(self.Partials, w)
    def Add2Bigrams(self, s, w, TravelProbability):
        if not w.count:
            return
        if not s in self.Bigrams:
            self.Bigrams[s] = []
        if not w in self.Completes:
            if w in self.Bigrams[s]:
                w.TravelProbability = max(w.TravelProbability, TravelProbability)
            else:
                w.TravelProbability = TravelProbability
        self.Add2Set(self.Bigrams[s], w)
    def Add2Set(self, l, w):
        if isinstance(w, list):
            for wx in w:
                self.Add2Set(l, wx)
        else:
            if not w in l:
                l.append(w)

class trie:
#{
#    public static int[] him
#    enum hime { nin, pra, itm }
#
   
#    BinaryReader self.trieReader
    def GetIndexedWord(self, index):
        if not index in self.allWords:
            #//if (self.trieReader == null) self.trieReader = new BinaryReader(File.OpenRead("trie.dat"))
            self.trieReader.seek(index)
            self.allWords[index] = NewLoad(self.trieReader, self)
        return self.allWords[index]
    
    def findAll(self, s, NoTrvelProb):
#        if (thread != null&&!thread.IsAlive):
#        {
#            thread.Abort()
#            thread = null
#            self.trieReader.close()
#            File.Delete("trieold.dat"); File.Move("trie.dat", "trieold.dat")
#            File.Delete("trie.dat"); File.Move("out.dat", "trie.dat")
#            File.Delete("modified.csv"); File.Move("modified.tmp", "modified.csv")
#            self.trieReader = new BinaryReader(File.OpenRead("trie.dat"))
#            self.totalWordCount = self.trieReader.ReadInt32()
#            self.BaseWord = self.trieReader.ReadInt32()
#            allWords.Clear()
#        }
        found = find_return()
#//            if(variations.qList.ContainsKey("^"+s+"$"))
#//                for w in variations.qList["^" + s + "$"].Keys)
#//                {
#//                    //found.Completes.Add(word.DummyWord(w.Substring(1,w.Length-2)))
#//                }
        self.find(self.GetIndexedWord(self.BaseWord), s, -float('inf') if NoTrvelProb else 0, found)
        found.Completes.sort()
        """
        if len(found.Completes) < self.MaxItems - 1:
            PartialChildren = []
            for w in found.Partials:
                PartialChildren += w.GetAllChildren()
            for w in PartialChildren:
                if not w in found.Completes:
                    w.TravelProbability = -float('inf')
            PartialChildren.sort()
            found.Add2Completes(PartialChildren)
        if len(found.Completes) < self.MaxItems - 1:
            bi = []
            for sx in found.Bigrams.keys():
                w1s=found.Bigrams[sx]
                w1s.sort(); 
                if len(w1s) > self.MaxItems:
                    w1s =w1s[:self.MaxItems]
                bfound = self.find(self.GetIndexedWord(self.BaseWord), sx, -float('inf') if NoTrvelProb else 0, find_return())
                bfound.Completes.sort()
                bfound.Completes=bfound.Completes[:self.MaxItems]
                for w in w1s:
                    for w2 in bfound.Completes:
                        xw = CompundWord(str(w) + " |" + str(w2), w.count * w2.count/self.totalWordCount, w.xCount + w2.xCount, TRIE)
                        xw.TravelProbability = -float('inf') if NoTrvelProb else\
                            found.TravelProbabilies[str(w.m_index) + sx]\
                            + w2.TravelProbability
                        bi.append(xw)
            bi.sort()
            if bi:
                found.Add2Completes(bi[:min(self.MaxItems,len(bi))])
        """
        r=found.Completes[:self.MaxItems]
        for w in found.Completes:
            if str(w).replace("|", "") == s:
                if not w in r:
                    r.Add(w)
                return r
        r.append(DummyWord(s))
        return r

    def find(self, w, s, p, r):#find(w, s, p, r /*NoTrvelProb*/):
        if not w:
            return r
        key = str(w.m_index) + s
        if key in r.TravelProbabilies and p<r.TravelProbabilies[key]:
            return r
        r.TravelProbabilies[key] = p
        if (s == ""):
            r.Add2CompletesPartials(w, p)
        else:
            r.Add2Bigrams(s, w,  p)
        consumes = variations.consume(s)
        for i in consumes.keys():
            for candidate in consumes[i]:
                    tmp = w
                    pv = variations.GetProbability(variations.MergeChars(candidate), s[0:i])
                    for c in candidate:
                        if c in tmp.children:
                            tmp = self.GetIndexedWord(tmp.children[c])
                        else:
                            tmp = None
                            break
                    self.find(tmp, s[i:], p + pv,r);                       
        return r
    def List2Trie(self, filename):
        self.CharCounts = {}
        totalCharCount = 0
        self.CharCounts = dict([(i,1) for i in range(len(variations.Chars))])
        self.allWords = {}
        self.allWords[-1] = word(self, -1)
        self.BaseWord = -1
    
        splited_words = open(os.path.join(os.path.dirname(__file__),"splited.csv")).readlines()#[:10000]
        c = 0
        self.totalWordCount = 0
        for s in splited_words:
            c+=1
            m = re.match("(.*?),([0-9]+)", s)
            if len(m.groups()) == 2:
                st1 = m.groups()[0]
                chrs = variations.SplitIntoChars(st1)
                cnt = int(m.groups()[1])
                self.totalWordCount += cnt
                for i in chrs:
                    self.CharCounts[i] += cnt
                totalCharCount += len(chrs) * cnt
                self.GetIndexedWord(self.BaseWord).Add(chrs,cnt, st1)
        bw=open("charprobabilities.dat",'wb')
        charprobabilities = ""
        for i in range(len(variations.Chars)):
            self.CharCounts[i] = math.log(self.CharCounts[i]) - math.log(totalCharCount)
            charprobabilities += variations.Chars[i] + "," + str(self.CharCounts[i]) + "\n"
            bw.write(pack('d', self.CharCounts[i]))
        bw.close()
        open("charprobabilities.csv",'w').write(charprobabilities)
        self.xCountCalcAll(self.BaseWord, 0)
        self.Save(filename,"modified.csv")

    def GetSavedIndex(self, index, bw, csvfile,NewWordsOnly):
        if not index in self.SavedAt:
            self.SavedAt[index] = self.GetIndexedWord(index).Save(bw, csvfile,NewWordsOnly)
        return self.SavedAt[index]

    def Save(self, filename, csvfilename):
        self.SavedAt = {}
        bw = open(filename, 'wb')
#        bw = dummyfile() 
#        print self.totalWordCount
        bw.write(pack('<ii', self.totalWordCount, 0))
        bw.flush()
#        print bw.tell()
        csvfile= open(csvfilename, 'w')
        x = self.GetSavedIndex(self.BaseWord, bw, csvfile, False)
        csvfile.close()
        bw.seek(4)
        bw.write(pack('<i',x))
        bw.flush()
        bw.close()

    def xCountCalcAll(self, w, p):
        x=self.GetIndexedWord(w)
        x.xCount = - p
        for k,v in x.children.items():
            self.xCountCalcAll(v, self.CharCounts[k] + p)

#    def xCountCalc(w)
#    {
#        w.xCount = 0
#        foreach(chr in variations.SplitIntoChars(w.ToString()))
#            w.xCount-=self.CharCounts[chr]
#    }
#    //public Sec sec
    def __init__(self):
#    {
#        //sec = new Sec()
#        /*if (self.self.trieReader == null)*/ 
        self.BaseWord = 0
        self.MaxItems = 100
        self.allWords = {}
        self.CharCounts = {}
        self.totalWordCount = 0
        fromcsv = False
        if fromcsv:
            self.List2Trie('trie.dat')
        else:
            self.trieReader = open(os.path.join(os.path.dirname(__file__),"trie.dat"), 'rb') 
            self.totalWordCount, self.BaseWord = unpack('<ii', self.trieReader.read(8))
#            print self.totalWordCount, hex(self.BaseWord)
            if os.path.isfile("charprobabilities.dat"):
                bw = open("charprobabilities.dat", 'rb')
                for i in range(len(variations.Chars)):
                    self.CharCounts[i] = unpack('d', bw.read(8))
                bw.close()

#    /*~trie()
#    {
#        TRIE.List2Trie("20090613.dat")
#    }*/
    def Add2List(self, w):
        self.allWords[-len(self.allWords)-1]=w
        return -len(self.allWords)

#    BinaryReader ThreadReader
#    csvfile
#    bw
#    def ThreadFunction()
#    {
#        File.Copy("trie.dat", "out.tmp", true)
#        //File.Copy("modified.csv", "modified.tmp", true)
#        csvfile = File.CreateText("modified.tmp");// AppendText("modified.tmp")
#        ThreadReader = new BinaryReader(File.OpenRead("out.tmp"))
#        ThreadReader.BaseStream.Position = 8
#        bw = new BinaryWriter(File.OpenWrite("out.dat"))
#        bw.Write(self.totalWordCount)
#        bw.Write((int)0)
#        SavedAt = new Dictionary<int, int>()
#        tmpWord = new word(this)
#        tmpWord.grandChildren = new List<int>()
#        while (ThreadReader.BaseStream.Position < ThreadReader.BaseStream.Length)
#        {                
#            tmpWord.Load(ThreadReader)
#            if (!ThreadParameters.Contains(tmpWord.m_index))
#            {
#                SavedAt[tmpWord.m_index] = (int)bw.BaseStream.Position
#                tmpWord.Save(bw, csvfile,false)
#            }
#        }
#        x = GetSavedIndex(self.BaseWord, bw, csvfile,true)
#        csvfile.close()
#        bw.BaseStream.Position = 4
#        bw.Write(x)
#        bw.close()
#        ThreadReader.close()
#        ThreadParameters.Clear()
#    }
#    
#    Thread thread = null
#    List<int> ThreadParameters=new List<int>()
#    
#    public def FeedBack(s, w)
#    {
#        if(w.ToString().IndexOf(" ")!=-1)
#            return
#        if (allWords.ContainsValue(w))
#        {
#            if (w.m_index > 0 && thread == null)
#            {
#                if (self.trieReader != null)
#                {
#                    self.trieReader.close()
#                    self.trieReader = null
#                }
#                variations.FeedBack(s, w.ToString())
#                self.totalWordCount++
#                w.count ++
#                FileStream fs = File.OpenWrite("trie.dat")
#                bw = new BinaryWriter(fs)
#                bw.Write(self.totalWordCount)
#                bw.Flush()
#                fs.Position = w.m_index
#                fs.Position += w.ToString().Length + 1
#                bw.Write(w.count)
#                bw.Write(w.xCount)
#                bw.close()
#                fs.close()
#                self.trieReader = new BinaryReader(File.OpenRead("trie.dat"))
#            }
#        }
#        else
#        {
#            List<int> chrs=variations.SplitIntoChars(w.ToString())
#            if (chrs == null) return
#            nw=GetIndexedWord(self.BaseWord).Add(chrs,1,variations.MergeChars(chrs)+"|")
#            self.totalWordCount++
#            xCountCalc(nw)
#            ThreadParameters.Add(now.m_index)
#            for chr in chrs)
#            {
#                now = GetIndexedWord(now.children[chr])
#                Console.WriteLine("{0} {1}",variations.Chars[chr],now.m_index)
#                if (now.m_index > 0)
#                    ThreadParameters.Add(now.m_index)
#            }
#            if (thread != null)
#            {
#                thread.Abort()
#                ThreadReader.close()
#                bw.close()
#                csvfile.close()
#            }
#            thread = new Thread(ThreadFunction)
#            thread.Start()
#        }
#    }
#}

TRIE = trie()
#print maxl
#print [str(w) for w in TRIE.findAll("da", False)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          