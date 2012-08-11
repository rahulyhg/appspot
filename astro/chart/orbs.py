'''
Created on Jan 1, 2011

@author: Sandeva Goonetilleke
'''

import re
class Orbs():
    def getAspectColor(self,p1,p2,a,r=1.0):
        a=min(a,360-a)
        for orb in self.orbs:
            if re.match("^(%s)$"%orb[0], p1) and re.match("^(%s)$"%orb[1], p2):
                for aspct in orb[2]:
                    #print orb,aspct
                    if(r*orb[3]>abs(a-aspct)):
                        return self.aspects[aspct]
        return ""
    aspects =   dict()
    orbs    =   list()  

west=Orbs()
west.aspects={-1:"",0:"red",180:"red",90:"red",120:"blue",60:"blue",150:"green",30:"green",45:"black",135:"black"}
west.orbs=[
            (".*Node",".*Node",[-1],360),
            ("Sun|Moon",".*",[0,180],10),
            (".*","Sun|Moon",[0,180],10),
            ("Sun|Moon",".*",[150],3),
            (".*","Sun|Moon",[150],3),
            (".*",".*",[0,180],8),
            (".*",".*",[150],2),
            (".*",".*",[120,90],8),
            (".*",".*",[60],6),
            (".*",".*",[45,135,30],2)
            ]

seiyo=Orbs()
seiyo.aspects={-1:"",0:"red",180:"red",90:"red",120:"blue",60:"blue",45:"black",135:"black"}
seiyo.orbs=[
            (".*Node",".*",[-1],360),
            (".*",".*Node",[-1],360),
            ("I|X","I|X",[-1],360),
            ("I|X",".*",[0,60,90,120,180],10),
            (".*","I|X",[0,60,90,120,180],10),
            ("Sun|Moon",".*",[0,60,90,120,180],6),
            (".*","Sun|Moon",[0,60,90,120,180],6),
            ("Mercury|Venus|Mars|Jupiter|Saturn",".*",[0,60,90,120,180],5),
            (".*","Mercury|Venus|Mars|Jupiter|Saturn",[0,60,90,120,180],5),
            ("Uranus|Neptune|Pluto","Uranus|Neptune|Pluto",[0,60,90,120,180],4),
            (".*",".*",[45,135],1)
            ]


seiyo_trans=Orbs()
seiyo_trans.aspects={-1:"",0:"red",180:"red",90:"red",120:"blue",60:"blue",45:"black",135:"black"}
seiyo_trans.orbs=[
            (".*Node",".*",[-1],360),
            (".*",".*Node",[-1],360),
            ("I|X","I|X",[-1],360),
            ("I|X|Sun|Moon","Sun|Mercury|Venus|Mars|Jupiter|Saturn",[0,60,90,120,180],5),
            ("I|X|Sun|Moon","Uranus|Neptune|Pluto",[0,60,90,120,180],3),
            ("Mercury|Venus|Mars","Sun|Mercury|Venus|Mars|Jupiter|Saturn",[0,60,90,120,180],3),
            ("Mercury|Venus|Mars","Uranus|Neptune|Pluto",[0,60,90,120,180],2),
            ("Jupiter|Saturn|Uranus|Neptune|Pluto","Sun|Mercury|Venus|Mars|Jupiter|Saturn",[0,60,90,120,180],2),
            ("Jupiter|Saturn|Uranus|Neptune|Pluto","Uranus|Neptune|Pluto",[0,60,90,120,180],1),
            (".*",".*",[45,135],1)
            ]

seiyo_partner=Orbs()
seiyo_partner.aspects={-1:"",0:"red",180:"red",90:"red",120:"blue",60:"blue",45:"black",135:"black"}
seiyo_partner.orbs=[
            (".*Node",".*",[-1],360),
            (".*",".*Node",[-1],360),
            (".*",".*",[0,45,60,90,120,135,180],2)]
