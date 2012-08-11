import re

def getKaputa(r):
    r = r.replace( "aa", "a`");
    r = r.replace( "sx", "z");
    r = r.replace("ooo", "/ au");
    r = r.replace("cx", "Z~");
    r = r.replace("hx", ":");
    
    r = r.replace("/k", "V|");
    r = r.replace("kh", "K|");
    r = r.replace("k", "k~");
    r = r.replace("gh", "G~");
    r = r.replace("/g", "M~");
    r = r.replace("g", "g~");
    
    
    r = r.replace("z", "X~");
    r = r.replace("/c", "z~");
    r = r.replace("ch", "C~");
    r = r.replace("c", "c|");
    
    
    r = r.replace("jh", "J|");
    r = r.replace("/j", "j~");
    r = r.replace("j", "j~");
    
    
    r = r.replace("w", "v");
    
    r = r.replace("txh", "}~");
    r = r.replace("w", "v|");
    r = r.replace("tx", "w~");
    r = r.replace("dxh", "{|");
    r = r.replace("/dx", "[~");
    r = r.replace("dx", "q~");
    r = r.replace("/n", "A");
    r = r.replace("nx", "N~");
    r = r.replace("n", "n~");
    
    r = r.replace("th", "T~");
    r = r.replace("t", "t|");
    r = r.replace("dh", "D~");
    r = r.replace("/d", "V|");
    r = r.replace("d", "d|");
    
    r = r.replace("ph", "P~");
    r = r.replace("p", "p~");
    r = r.replace("bh", "x~");
    r = r.replace("/b", "B|");
    r = r.replace("b", "b|");
    r = r.replace("m", "m|");
    
    r = r.replace("y", "y~");
    r = r.replace("rxx", "G^^");
    r = r.replace("rx", "G^");
    r = r.replace("r", "r\\");
    
    r = r.replace("lx", "L~");
    r = r.replace("l", "l~");
    r = r.replace("v", "v|");
    r = r.replace("sh", ";~");
    r = r.replace("s", "s~");
    r = r.replace("h", "h~");
    
    r = r.replace("~r\\", "Y~");
    r = r.replace("|r\\", "Y|");
    r = r.replace("~y~", "&~");
    r = r.replace("|y~", "&|");
    r = r.replace("f", "f~");
    
    r = r.replace("r\\aee", "rH");
    r = r.replace("r\\ae", "rF");
    r = r.replace("~aee", "$");
    r = r.replace("\\aee", "$");
    r = r.replace("|aee", "$");
    r = r.replace("aee", "a$");
    r = r.replace("~ae", "#");
    r = r.replace("\\ae", "#");
    r = r.replace("|ae", "#");
    r = r.replace("ae", "a#");
    r = r.replace("~aa", "`");
    r = r.replace("\\aa", "`");
    r = r.replace("|aa", "`");
    r = r.replace("aa", "a`");
    r = r.replace("~ai", "@@");
    r = r.replace("\\ai", "@@");
    r = r.replace("|ai", "@@");
    r = r.replace("~au", "@_");
    r = r.replace("\\au", "@_");
    r = r.replace("|au", "@_");
    r = r.replace("au", "o_");
    r = r.replace("~a", "");
    r = r.replace("\\a", "");
    r = r.replace("|a", "");
    
    r = r.replace("~ii", "W");
    r = r.replace("\\ii", "W");
    r = r.replace("|ii", "W");
    r = r.replace("ii", "I");
    r = r.replace("~i", "Q");
    r = r.replace("\\i", "Q");
    r = r.replace("|i", "Q");
    
    r = r.replace("k~uu", "kS");
    r = r.replace("k~u", "kO");
    r = r.replace("g~uu", "gS");
    r = r.replace("g~u", "gO");
    r = r.replace("M~uu", "MS");
    r = r.replace("M~u", "MO");
    r = r.replace("w~uu", "wS");
    r = r.replace("w~u", "wO");
    r = r.replace("X~uu", "XS");
    r = r.replace("X~u", "XO");
    r = r.replace("x~uu", "xS");
    r = r.replace("x~u", "xO");
    r = r.replace("L~uu", "U$");
    r = r.replace("L~u", "U");
    r = r.replace("Y~uu", "Y$");
    r = r.replace("Y~u", "Y#");
    r = r.replace("Y|uu", "Y$");
    r = r.replace("Y|u", "Y#");
    r = r.replace("r\\uu", "r$");
    r = r.replace("r\\u", "r#");
    r = r.replace("~uu", "R");
    r = r.replace("\\uu", "R");
    r = r.replace("|uu", "R");
    r = r.replace("uu", "u_");
    r = r.replace("~u", "E");
    r = r.replace("\\u", "E");
    r = r.replace("|u", "E");
    
    r = r.replace("~ee", "@~");
    r = r.replace("\\ee", "@\\");
    r = r.replace("|ee", "@|");
    r = r.replace("ee", "e~");
    r = r.replace("~e", "@");
    r = r.replace("\\e", "@");
    r = r.replace("|e", "@");
    
    r = r.replace("~oo", "@`~");
    r = r.replace("~o", "@`");
    r = r.replace("\\oo", "@`~");
    r = r.replace("\\o", "@`");
    r = r.replace("|oo", "@`~");
    r = r.replace("|o", "@`");
    r = r.replace("oo", "o|");
    
    r = r.replace("Y~", "^");
    r = r.replace("Y|", "^");
    r = r.replace("^r\\", "^^");
    
    r = r.replace("&~", "~y~");
    r = r.replace("&|", "|y~");
    
    r = re.sub(r"(.&?Y?)(@+)", r'\2\1',r);
    
    r = r.replace("ai", "@e");
    r = r.replace("/ ", "");
    r = r.replace("/-", "");
    r = r.replace("k~/+;", "]");
    r = r.replace("/+", "");
    return r;

def readKaputa(r):
    r = r.replace("WY", "YW")
    r = re.sub(r"\\|\|", "~", r)
    r = r.replace("]", "k~;")
    
    r = re.sub(r"(@@?)(.&?Y?)","\\2\\1",r)
    r = r.replace("U$", "Uu")
    r = r.replace("r#", "rE")
    r = r.replace("r$", "rR")
    r = re.sub(r"([[bcdfghjklmnpqrstvwxyzBCDGJKLMNPTVXYZ;{}])","\\1a",r)
    r = r.replace("&", "~ya")
    r = r.replace("Y", "~r")
    r = re.sub("#|F", "~ae", r)
    r = re.sub(r"\$|H", "~aee", r)
    r = r.replace("@@", "~ai")
    r = r.replace("@~", "~ee")
    r = r.replace("@`~", "~oo")
    r = r.replace("@`", "~o")
    r = r.replace("@_", "~au")
    r = r.replace("@", "~e")
    r = r.replace("Q", "~i")
    r = r.replace("W", "~ii")
    r = re.sub("[EO]", "~u", r)
    r = re.sub("[RS]", "~uu", r)
    r = r.replace("`", "a")
    r = r.replace("^^", "~rr")
    r = r.replace("^", "~r")
    r = re.sub(r"a[~|]", "", r)
    
    r = r.replace("x", "bh")
    r = r.replace("w", "tx")
    r = r.replace("q", "dx")
    r = r.replace("e~", "ee")
    r = r.replace("o~", "oo")
    r = r.replace("o_", "au")
    r = r.replace("u_", "uu")
    r = r.replace("A", "/n")
    r = r.replace("B", "/b")
    r = r.replace("C", "ch")
    r = r.replace("D", "dh")
    r = r.replace("G", "gh")
    r = r.replace("I", "ii")
    r = r.replace("J", "jh")
    r = r.replace("K", "kh")
    r = r.replace("L", "lx")
    r = r.replace("M", "/g")
    r = r.replace("N", "nx")
    r = r.replace("P", "ph")
    r = r.replace("T", "th")
    r = r.replace("U", "lxu")
    r = r.replace("V", "/d")
    r = r.replace("X", "sx")
    r = r.replace("Z", "cx")
    r = r.replace("{", "dxh")
    r = r.replace("}", "txh")
    r = r.replace("[", "/dx")
    r = r.replace(";", "sh")
    
    r = re.sub("[sG]r~r", "rxx", r)
    r = re.sub("[sG]r", "rx", r)
    r = re.sub(r"\/d([^aeiouxh])", "/k\\1", r)
    return r;


def getKaputaAll(s):
    return [getKaputa(s)]
