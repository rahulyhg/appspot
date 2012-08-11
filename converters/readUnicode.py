# -*- coding:utf-8 -*-

import re
def readUnicode(r):
    #r = r.replace("a", "b");
    #r=''
    
    r=r.encode('utf-8')
    v='‍'
    v1="/+"
    
    r = r.replace('‍', "/+");#chr(226)+chr(128)+chr(141)

    r = r.replace("්ය", "්/-ය");
    r = r.replace("්ර",  "්/-ර");
    r = r.replace("ෛ",  "්ai");


    r = r.replace("ෞ",  "්au");
    r = r.replace("ෑ",  "්aee");
    r = r.replace("ැ",  "්ae");
    r = r.replace("ා",  "්aa");
    r = r.replace("ී",  "්ii");
    r = r.replace("ි",  "්i");
    r = r.replace("ූ",  "්uu");
    r = r.replace("ු",  "්u");
    r = r.replace("ේ",  "්ee");
    r = r.replace("ෙ",  "්e");
    r = r.replace("ෝ",  "්oo");
    r = r.replace("ො",  "්o");
    r = r.replace("ෲ",  "්rr");#//gaetapili-2
    r = r.replace("ෘ",  "්r");#//gaetapili


    r = r.replace( "ඃ", "hx");#//"&#x0D83;"
    r = r.replace( "ං", "/n");
    r = r.replace( "ඞ", "/ka");
    r = r.replace( "ඛ", "kha");
    r = r.replace( "ක", "ka");
    r = r.replace( "ඟ", "/ga");
    r = r.replace( "ඝ", "gha");
    r = r.replace( "ග", "ga");
    r = r.replace( "ඥ", "cxa");
    r = r.replace( "ඤ", "/ca");
    r = r.replace( "ඡ", "cha");
    r = r.replace( "ච", "ca");
    r = r.replace( "ඦ", "/ja");
    r = r.replace( "ඣ", "jha");
    r = r.replace( "ජ", "ja");
    r = r.replace( "ඳ", "/dxa");
    r = r.replace( "ඬ", "/da");
    r = r.replace( "ථ", "txha");
    r = r.replace( "ත", "txa");
    r = r.replace( "ධ", "dxha");
    r = r.replace( "ද", "dxa");
    r = r.replace( "ඨ", "tha");
    r = r.replace( "ට", "ta");
    r = r.replace( "ඪ", "dha");
    r = r.replace( "ඩ", "da");
    r = r.replace( "ණ", "nxa");
    r = r.replace( "න", "na");
    r = r.replace( "ඵ", "pha");
    r = r.replace( "ප", "pa");
    r = r.replace( "භ", "bha");
    r = r.replace( "ඹ", "/ba");
    r = r.replace( "බ", "ba");
    r = r.replace( "ම", "ma");
    r = r.replace( "ය", "ya");
    r = r.replace( "ඎ", "rxx");
    r = r.replace( "ඍ", "rx");
    r = r.replace( "ර", "ra");
    r = r.replace( "ඐ", "lxxx");
    r = r.replace( "ඏ", "lxx");
    r = r.replace( "ළ", "lxa");
    r = r.replace( "ල", "la");
    r = r.replace( "ව", "va");
    r = r.replace( "ශ", "sxa");
    r = r.replace( "ෂ", "sha");
    r = r.replace( "ස", "sa");
    r = r.replace( "හ", "ha");
    r = r.replace( "ෆ", "fa");
    r = r.replace("a්",  "");


    r = r.replace( "ඓ", "/-ai");
    r = r.replace("ඖ",  "/-au");
    r = r.replace("ඈ",  "/-aee");
    r = r.replace("ඇ",  "/-ae");
    r = r.replace("ආ",  "/-aa");
    r = r.replace("අ",  "/-a");
    r = r.replace("ඊ",  "/-ii");
    r = r.replace("ඉ",  "/-i");
    r = r.replace("ඌ",  "/-uu");
    r = r.replace("උ",  "/-u");
    r = r.replace("ඒ",  "/-ee");
    r = r.replace( "එ", "/-e");
    r = r.replace( "ඕ", "/-oo");
    r = r.replace( "ඔ", "/-o");


    #r = r.replace( "්‍ර", "්ර");//rakaaraansa
    #r = r.replace( "්‍ය", "්ය");//yansa
    #r = r.replace("/+y",  "y");
    #r = r.replace("/+r",  "r");

    r = re.sub(r"[^a-z]/\-", "",r);
    r = re.sub(r"^/\-", "",r);
    r = re.sub(r"/\+([yr])",r"\1",r);
    r = r.replace("්", "//");
    
    r = re.sub(r"//([aeiour])",r"/\1",r)
    return r.decode('utf-8');


