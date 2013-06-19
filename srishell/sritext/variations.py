import os
import re
import math
variations_keys_max_length = 0
Chars = []
m_variations = {}
Counts,OriginalCounts={},{}
Counts = {}
OriginalCounts = {}
totalCounts = 0

def SplitIntoChars(s):
    r = []
    if -1 == s.find('|'):
        while ("" != s):
            x = -1
            for i in range(len(Chars)):
                if s.startswith(Chars[i]) and (x == -1 or len(Chars[i]) > len(Chars[x])):
                    x = i
            if -1 == x:
                print "Split Error"
                return None
            r.append(x)
            s = s[len(Chars[x]):]
        return r
    for c in s.split('|'):
        if c:
            x = Chars.index(c)
            if x < 0:
                print "Split Error"
                return None
            r.append(x)
    return r

lines = open(os.path.join(os.path.dirname(__file__),"vars.csv")).readlines()
for line in lines:
    line=line.strip()
    if line:
        lst = line.split(',')
        for c in lst[0].split('|'):
            if not c in Chars:
                Chars.append(c)
        SplitedChars = SplitIntoChars(lst[0])
        Counts[lst[0]] = {}
        OriginalCounts[lst[0]] = {}
        for j in range(1,len(lst),2):
            if lst[j]:
                s = re.sub("^<null>$",'',lst[j])
                m_variations.setdefault(s,[]).append(SplitedChars)
                variations_keys_max_length = max(len(s), variations_keys_max_length)
                Counts[lst[0]][s] = int(lst[j + 1])
                OriginalCounts[lst[0]][s] = Counts[lst[0]][s]
                totalCounts += abs(Counts[lst[0]][s])

#Save(); 
#def Save():
#    s = ""
#    for l in Counts.Keys)
#    {
#        s+=l + ","
#        double S=0, So=0, P=0, Po=0
#        for k in Counts[l].Keys)
#        {
#            S += abs(Counts[l][k])
#            So += abs(OriginalCounts[l][k])
#            P += Counts[l][k] > 0 ? Counts[l][k] : 0
#            Po += OriginalCounts[l][k] > 0 ? OriginalCounts[l][k] : 0
#        }
#        for k in Counts[l].Keys)
#        {
#            double v = Counts[l][k]>0?Counts[l][k]:OriginalCounts[l][k]
#            v *= (v>0?Po/P:1)*S / So
#            s += k == "" ? "<null>" : k
#            s += "," +Math.Round(v).ToString() + ","
#        }
#        //s+=string.Format("S=,{0},So=,{1},P=,{2},Po=,{3}:\r\n",S,So,P,Po)
#        s += "\r\n"
#    }
#    File.WriteAllText("vars.csv", s)
#}
def consume(s):
    r = {}
    for i in range(min(len(s), variations_keys_max_length),-1,-1):
        if s[:i] in m_variations:
            r[i] = m_variations[s[:i]]
    return r

def MergeChars(l):
    r = ""
    for i in l:
        r += Chars[i]+"|"
    r=r[:-1]
    return r

#static public Dictionary<string, Dictionary<string, int>> Parse(s, List<int> chars)
#{
#    Dictionary<string, Dictionary<string, int>> r =
#        new Dictionary<string, Dictionary<string, int>>()
#    x
#    ParsePvt(s, chars, out x)
#    Match m=Regex.Match(x,@"(([^(]*)\(([^)]*)\)\|)*")
#    //m.Groups[0].Captures
#    for (i = 0; i < m.Groups[2].Captures.Count; i++)
#    {
#        b = m.Groups[2].Captures[i].ToString()
#        a = m.Groups[3].Captures[i].ToString()
#        Console.WriteLine("{0} {1}", a,b)
#        if (Counts[a].ContainsKey(b))
#        {
#            if (!r.ContainsKey(a)) r[a] = new Dictionary<string, int>()
#            if (!r[a].ContainsKey(b)) r[a][b] = 0
#            r[a][b]++
#        }
#    }
#    return r
#}
#static public Parse2String(s, List<int> chars)
#{
#    x
#    ParsePvt(s, chars, out x)
#    return x
#}
#static double ParsePvt(s, List<int> chars, out result)
#{
#    result = ""
#    if (chars.Count == 0)
#        if (s.Length == 0)
#            return 0
#        else
#            return -1000
#
#    double p = double.NegativeInfinity; 
#    Dictionary<int, List<List<int>>> consumes = variations.consume(s)
#    for i in consumes.Keys)
#        for List<int> candidate in consumes[i])
#        {
#            if (candidate.Count > chars.Count) continue
#            bool ok = true
#            for (j = 0; j < candidate.Count; j++)
#                if (candidate[j] != chars[j])
#                    ok = false
#            if (ok)
#            {
#                a = s.Substring(0, i)
#                cands = variations.MergeChars(candidate)
#                rtemp
#                //Console.WriteLine("\t{0}=>{1}", a, cands)
#                double ptemp =
#                    ParsePvt(s.Substring(i), chars.GetRange(candidate.Count, chars.Count - candidate.Count),out rtemp) +
#                    GetProbability(cands, a)
#                //Console.WriteLine("\t{0}=>{1} {2:N2} {3:N2} {4}", a, cands, ptemp, p,result)
#                if (ptemp >= p)
#                {
#                    p = ptemp
#                    result = a+"("+cands+")|"+rtemp
#                    //Console.WriteLine("OK: {0}",result)
#                }
#            }
#        }
#    if (result == "" && s=="")
#    {
#        for x in chars)
#            result += string.Format("({0})|", Chars[x])
#        p = -1000
#    }
#    //Console.WriteLine("{0} {1} {2:N2} {3}", s, variations.MergeChars(chars),p,result)
#    return p
#}
#static public void FeedBack(s,w)
#{
#    List<int> l= variations.SplitIntoChars(w.ToString())
#    if (l == null) return
#    Dictionary<string, Dictionary<string, int>> p = variations.Parse(s,l)
#    if (p == null) return
#    for chrs in p.Keys)
#        for inp in p[chrs].Keys)
#            if(Counts[chrs][inp]!=-1)
#            {
#                Counts[chrs][inp] += Math.Sign(Counts[chrs][inp]) * p[chrs][inp]
#                totalCounts +=abs(p[chrs][inp])
#            }
#    Save();    
#}

def GetProbability(chrs, s):
    return math.log(abs(Counts[chrs][s])) - math.log(totalCounts); 

