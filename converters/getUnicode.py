# -*- coding:utf-8 -*-

import re
def getUnicode(r):
    #r = r.replace("a", "b");
    #r=''
    r = r.replace("/+",u'\u200d');#chr(226)+chr(128)+chr(141)

    r = r.replace( unicode("්/-ය",'utf8'),unicode("්ය",'utf8'));
    r = r.replace( unicode( "්/-ර",'utf8'),unicode("්ර",'utf8'));


    r = r.replace( unicode("hx",'utf8'),unicode( "ඃ",'utf8'));#//"&#x0D83;"
    r = r.replace( unicode("/n",'utf8'),unicode( "ං",'utf8'));
    r = r.replace( unicode("/k",'utf8'),unicode( "ඞ්",'utf8'));
    r = r.replace( unicode("kh",'utf8'),unicode( "ඛ්",'utf8'));
    r = r.replace( unicode("k",'utf8'),unicode( "ක්",'utf8'));
    r = r.replace( unicode("/g",'utf8'),unicode( "ඟ්",'utf8'));
    r = r.replace( unicode("gh",'utf8'),unicode( "ඝ්",'utf8'));
    r = r.replace( unicode("g",'utf8'),unicode( "ග්",'utf8'));
    r = r.replace( unicode("cx",'utf8'),unicode( "ඥ්",'utf8'));
    r = r.replace( unicode("/c",'utf8'),unicode( "ඤ්",'utf8'));
    r = r.replace( unicode("ch",'utf8'),unicode( "ඡ්",'utf8'));
    r = r.replace( unicode("c",'utf8'),unicode( "ච්",'utf8'));
    r = r.replace( unicode("/j",'utf8'),unicode( "ඦ්",'utf8'));
    r = r.replace( unicode("jh",'utf8'),unicode( "ඣ්",'utf8'));
    r = r.replace( unicode("j",'utf8'),unicode( "ජ්",'utf8'));
    r = r.replace( unicode("/dx",'utf8'),unicode( "ඳ්",'utf8'));
    r = r.replace( unicode("/d",'utf8'),unicode( "ඬ්",'utf8'));
    r = r.replace( unicode("txh",'utf8'),unicode( "ථ්",'utf8'));
    r = r.replace( unicode("tx",'utf8'),unicode( "ත්",'utf8'));
    r = r.replace( unicode("dxh",'utf8'),unicode( "ධ්",'utf8'));
    r = r.replace( unicode("dx",'utf8'),unicode( "ද්",'utf8'));
    r = r.replace( unicode("th",'utf8'),unicode( "ඨ්",'utf8'));
    r = r.replace( unicode("t",'utf8'),unicode( "ට්",'utf8'));
    r = r.replace( unicode("dh",'utf8'),unicode( "ඪ්",'utf8'));
    r = r.replace( unicode("d",'utf8'),unicode( "ඩ්",'utf8'));
    r = r.replace( unicode("nx",'utf8'),unicode( "ණ්",'utf8'));
    r = r.replace( unicode("n",'utf8'),unicode( "න්",'utf8'));
    r = r.replace( unicode("ph",'utf8'),unicode( "ඵ්",'utf8'));
    r = r.replace( unicode("p",'utf8'),unicode( "ප්",'utf8'));
    r = r.replace( unicode("bh",'utf8'),unicode( "භ්",'utf8'));
    r = r.replace( unicode("/b",'utf8'),unicode( "ඹ්",'utf8'));
    r = r.replace( unicode("b",'utf8'),unicode( "බ්",'utf8'));
    r = r.replace( unicode("m",'utf8'),unicode( "ම්",'utf8'));
    r = r.replace( unicode("y",'utf8'),unicode( "ය්",'utf8'));
    r = r.replace( unicode("rxx",'utf8'),unicode( "ඎ",'utf8'));
    r = r.replace( unicode("rx",'utf8'),unicode( "ඍ",'utf8'));
    r = r.replace( unicode("r",'utf8'),unicode( "ර්",'utf8'));
    r = r.replace( unicode("lxxx",'utf8'),unicode( "ඐ",'utf8'));
    r = r.replace( unicode("lxx",'utf8'),unicode( "ඏ",'utf8'));
    r = r.replace( unicode("lx",'utf8'),unicode( "ළ්",'utf8'));
    r = r.replace( unicode("l",'utf8'),unicode( "ල්",'utf8'));
    r = r.replace( unicode("v",'utf8'),unicode( "ව්",'utf8'));
    r = r.replace( unicode("sx",'utf8'),unicode( "ශ්",'utf8'));
    r = r.replace( unicode("sh",'utf8'),unicode( "ෂ්",'utf8'));
    r = r.replace( unicode("s",'utf8'),unicode( "ස්",'utf8'));
    r = r.replace( unicode("h",'utf8'),unicode( "හ්",'utf8'));
    r = r.replace( unicode("f",'utf8'),unicode( "ෆ්",'utf8'));

    r = r.replace( unicode( "්ai",'utf8'),unicode("ෛ",'utf8'));
    r = r.replace( unicode( "්au",'utf8'),unicode("ෞ",'utf8'));
    r = r.replace( unicode( "්aee",'utf8'),unicode("ෑ",'utf8'));
    r = r.replace( unicode( "්ae",'utf8'),unicode("ැ",'utf8'));
    r = r.replace( unicode( "්aa",'utf8'),unicode("ා",'utf8'));
    r = r.replace( unicode( "්ii",'utf8'),unicode("ී",'utf8'));
    r = r.replace( unicode( "්i",'utf8'),unicode("ි",'utf8'));
    r = r.replace( unicode( "්uu",'utf8'),unicode("ූ",'utf8'));
    r = r.replace( unicode( "්u",'utf8'),unicode("ු",'utf8'));
    r = r.replace( unicode( "්ee",'utf8'),unicode("ේ",'utf8'));
    r = r.replace( unicode( "්e",'utf8'),unicode("ෙ",'utf8'));
    r = r.replace( unicode( "්oo",'utf8'),unicode("ෝ",'utf8'));
    r = r.replace( unicode( "්o",'utf8'),unicode("ො",'utf8'));
    r = r.replace( unicode( "්rr",'utf8'),unicode("ෲ",'utf8'));#//gaetapili-2
    r = r.replace( unicode( "්r",'utf8'),unicode("ෘ",'utf8'));#//gaetapili
    r = r.replace( unicode( "්a",'utf8'),unicode("",'utf8'));

    r = r.replace( unicode("ai",'utf8'),unicode( "ඓ",'utf8'));
    r = r.replace( unicode( "au",'utf8'),unicode("ඖ",'utf8'));
    r = r.replace( unicode( "aee",'utf8'),unicode("ඈ",'utf8'));
    r = r.replace( unicode( "ae",'utf8'),unicode("ඇ",'utf8'));
    r = r.replace( unicode( "aa",'utf8'),unicode("ආ",'utf8'));
    r = r.replace( unicode( "a",'utf8'),unicode("අ",'utf8'));
    r = r.replace( unicode( "ii",'utf8'),unicode("ඊ",'utf8'));
    r = r.replace( unicode( "i",'utf8'),unicode("ඉ",'utf8'));
    r = r.replace( unicode( "uu",'utf8'),unicode("ඌ",'utf8'));
    r = r.replace( unicode( "u",'utf8'),unicode("උ",'utf8'));
    r = r.replace( unicode( "ee",'utf8'),unicode("ඒ",'utf8'));
    r = r.replace( unicode("e",'utf8'),unicode( "එ",'utf8'));
    r = r.replace( unicode("oo",'utf8'),unicode( "ඕ",'utf8'));
    r = r.replace( unicode("o",'utf8'),unicode( "ඔ",'utf8'));
    


    r = r.replace( unicode("්ර",'utf8'),unicode( "්‍ර",'utf8'));#//rakaaraansa
    r = r.replace( unicode("්ය",'utf8'),unicode( "්‍ය",'utf8'));#//yansa
    #r = r.replace( unicode( "y",'utf8'),unicode("/+y",'utf8'));
    #r = r.replace( unicode( "r",'utf8'),unicode("/+r",'utf8'));

    #r = re.sub(r"[^a-z]/\-", "",r);
    #r = re.sub(r"^/\-", "",r);
    #r = re.sub(r"/\+([yr])",r"\1",r);
    r=r.replace("/-","");
    return r;

