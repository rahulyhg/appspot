# -*- coding:utf-8 -*-

sinhala_rashi=["මේෂ","වෘෂභ","මිථුන","කටක","සිංහ","කන්‍යා","තුලා","වෘශ්චික","ධනු","මකර","කුම්භ","මීන"]

sinhala_rashis_short=[
"මේ","වෘෂ","මිථු",
"කට","සිං","කං",
"තුලා","වෘශ්","ධනු",
"මක","කුම්","මීන"] 


sinhala_planets_short={
"Sun":"ර",
"Moon":"ච",
"Moon_Node":"රා",
"Moon_S_Node":"කේ",
"Mercury":"බු",
"Venus":"ශු",
"Mars":"කු",
"Jupiter":"ගු",
"Saturn":"ශ",
"Uranus":"යු",
"Neptune":"නැ",
"Pluto":"ප්",
"I":"ල",
"X":"10"
}

sinhala_planets={
"Sun":"රවි",
"Moon":"චන්ද්‍ර",
"Moon_Node":"රාහු",
"Moon_S_Node":"කේතු",
"Mercury":"බුධ",
"Venus":"ශුක්‍ර",
"Mars":"කුජ",
"Jupiter":"ගුරු",
"Saturn":"ශනි",
"Uranus":"යුරේනස්",
"Neptune":"නැප්චූන්",
"Pluto":"ප්ලුටෝ",
"I":"ලග්න",
"X":"10"
}

#sinhala_nakshatra=[
#"asvidxa(kee)","beranxa(sxu)",
#"kaetxi(ra)","rehenxa(ca)","muvasirasa(ku)","adxa(raa)","punaavasa(gu)","pusha(sxa)","aslisa(bu)","maa(kee)","puvapal(sxu)",
#"utxrapal(ra)","hatxa(ca)","sitxa(ku)","saa(raa)","visaa(gu)","anura(sxa)","dxeta(bu)","mula(kee)","puvasala(sxu)",
#"utxurusala(ra)","suvana(ca)","dxenata(ku)","siyaavasa(raa)","puvaputupa(gu)","utxraputupa(sxa)","reevatxii(bu)"]


sinhala_nakshatra=[
"අස්විද","බෙරණ",
"කැති","රෙහෙණ","මුවසිරස","අද","පුනාවස","පුෂ","අස්ලිස","මා","පුවපල්",
"උත්‍රපල්","හත","සිත","සා","විසා","අනුර","දෙට","මුල","පුවසල",
"උතුරුසල","සුවන","දෙනට","සියාවස","පුවපුටුප","උත්‍රපුටුප","රේවතී"]

sinhala_thithi=['පුර පෑළවිය','පුර දියවක','පුර තියවක','පුර ජාලවක','පුර විසේනිය','පුර සැටවක','පුර සතවක','පුර අටවක','පුර නවවක','පුර දසවක','පුර එකොළොස්වක','පුර දොළොස්වක','පුර තෙළෙස්වක','පුර තුදුස්වක','පුර පසළොස්වක','අව පෑළවිය','අව දියවක','අව තියවක','අව ජාලවක','අව විසේනිය','අව සැටවක','අව සතවක','අව අටවක','අව නවවක','අව දසවක','අව එකොළොස්වක','අව දොළොස්වක','අව තෙළෙස්වක','අව තුදුස්වක','අමාවක']
 
dasha_prama=[7,20,6,10,7,18,16,19,17]
dasha_prama_acc=[sum(dasha_prama[:i]) for i in range(len(dasha_prama))]
nakshatra_lords=['Moon_S_Node','Venus','Sun','Moon','Mars','Moon_Node','Jupiter','Saturn','Mercury']*3
