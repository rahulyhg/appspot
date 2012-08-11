#!/usr/bin/python
from datetime import *
from ccalculator import *

"""
planets_cal=array("Sun","Moon","Moon_Node","Apogee","Mercury",
"Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto",
"Chiron","Quaoar","Sedna","Sgr AGalCtr");"""

planets_cal=["Sun","Moon","Moon_Node","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]

planets=["Sun","Moon","Moon_Node","Moon_S_Node","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"]#,"Chiron"

bhavas=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"];
"""
def todms(val,&d,&m,&s)
{
	d=floor(val/3600);m=floor(val/60)%60;s=val%60;
}

def FormatDMS(str,val,plus='',minus='',zero='')
{
	trans=array();
	trans["%S"]=val<0?minus:val>0?plus:zero;
	val=val>0?val:-val;
	trans["%s"]=val%60;val=floor(val/60);
	trans["%m"]=val%60;val=floor(val/60);
	trans["%d"]=val;trans["%D"]=val%30;val=floor(val/30);
	trans["%r"]=val;
	return strtr(str,trans);
}
def calculator_epheint(str)
{
	a=array("Ari"=>0,"Tau"=>1,"Gem"=>2,"Cnc"=>3,"Leo"=>4,"Vir"=>5,"Lib"=>6,"Sco"=>7,"Sgr"=>8,"Cap"=>9,"Aqr"=>10,"Psc"=>11);
	return a[substr(str,3,3)]*30*3600+3600*(int)substr(str,0,2)+60*(int)substr(str,7,2)+(int)substr(str,10,2);
}

def GetSunrise(name)
{
	global name;
	long=name['Longitude'];lat=name['Latitude'];
	year=win_gmstrftime("%Y",name['GMT']);
	month=win_gmstrftime("%m",name['GMT']);
	day=win_gmstrftime("%d",name['GMT']);
	postdata ="year=".year.sprintf("&type=sunrise/sunset&xx0=%d&xx1=%d&xx2=%d&yy0=%d&yy1=%d&yy2=%d&zz0=1;zz1=0&",long>=0?1:-1,long/3600,(long/60)%60,lat>0?1:-1,lat/3600,(lat/60)%60);
//	echo postdata;
	http_response = post('aa.usno.navy.mil', '/cgi-bin/aa_rstablew.pl', postdata); 
	data=strstr(http_response,"Jan.");
//	echo "<br>".http_response."<br>";
	data=strstr(data,"01");
	data=split("\n",data);
	data=	data[day-1];
	data=split(" ",data);
	data=data[3*month-1];
//	echo year.month.day.substr(data,0,2).substr(data,2,2);
//	echo month.day;
	name["Sunrise"]=win_gmmktime(substr(data,0,2), substr(data,2,2), 0, month, day, year);
}
"""
def calculator_TYL(A,B,C,D,T):
	return (A+T*(B+T*(C+T*(D))))
def calculator_dSIN(A):return sin(deg2rad(A))
def calculator_dCOS(A):return cos(deg2rad(A))
def calculator_dTAN(A):return tan(deg2rad(A))
def calculator_AdSIN(A):return rad2deg(asin(A))
def calculator_AdCOS(A):return rad2deg(acos(A))
def calculator_AdTAN(sn,cs):
	ang=rad2deg(atan(sn/cs));
	if(cs>0):
		return ang
	return ang+180;

def calculator_MOD(A,B):
	if(A>B):
		return calculator_MOD(A-B,B)
	if(A<0):
		return calculator_MOD(A+B,B)
	return A


def GetBhava(name):
	#global name;
	#global bhavas;
	sdtm=name['Siderael Time']/240;
	#T=(name['GMT']-win_gmmktime(12,0,0,1,1,1900,0))/86400/36525;
	T=name["T"]
	LT=name['latitude']/3600.0;

	h=-120;dlt=H=X=0;
	a=calculator_TYL(23.452294,-0.0130125,-0.00000164,+0.000000503,T);
	for i in range(6):
		h+=30;
		dlt=calculator_AdSIN(calculator_dSIN(h)*calculator_dSIN(LT));
		if(LT==0):
			P=calculator_dSIN(h)
		else:
			P=calculator_dTAN(dlt)/calculator_dTAN(LT);
		if(P<-1):P=-1;
		if(P>1):P=1;
		H=calculator_AdCOS(P);
		X=sdtm-H;
		X=calculator_AdTAN((calculator_dSIN(X)*calculator_dCOS(a)+calculator_dTAN(dlt)*calculator_dSIN(a)),calculator_dCOS(X));
		X=calculator_MOD(X-90,360)*3600;
		name[bhavas[i]]=floor(X);
	for i in range(6,12):
		name[bhavas[i]]=(name[bhavas[i-6]]+180*3600)%(360*3600);

def GetAyanamsa(Dt):
	BDt=datetime(1900,6,30);
	x=Dt-BDt
	x=((50.26)*float(x.days*86400+x.seconds)/365.2425/24/3600);
	return 22*3600+21*60+37+x;

def GetKendraSayana(name):
	GetEphe(name);
	name["Moon_S_Node"]=(name["Moon_Node"]+180*3600)%(360*3600);
	GetBhava(name);
	#GetSunrise(name);
        
def GetKendraNirayana(name):
	GetKendraSayana(name);
	ayana=GetAyanamsa(name['GMT']);
	for x in planets+bhavas:
		name[x]+=360*3600-ayana;name[x]%=360*3600;

def str2int(s):
	if type(s)==int:
		return s
	r=int(s[:-2])*3600
	sgn=r/abs(r)
	r+=sgn*int(s[-2:])*60
	return r

