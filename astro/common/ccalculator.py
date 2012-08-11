#include "stdafx.h"
#include "Kendra.h"
#include "Calculator.h"
#include <math.h>
from datetime import *
from math import *
def TYL(A,B,C,D,T):
	return A+T*(B+T*(C+T*D));


def MOD(a,b):
	if(a>=0):return a-b*((int)(a/b));
	return b+a+b*((int)(-a/b));


def MTYL(A,B,C,D,T):
	return MOD(TYL(A,B,C,D,T),360);

#define COS(A) cos((A)/deg)
"""
def sin(deg2rad(A)

 	return sin(deg2red(A));

"""
#define TAN(A) tan((A)/deg)
#define ACOS(A) deg*acos(A)
#define ASIN(A) deg*asin(A)
#define anati TYL(23.452294,-0.0130125,-0.00000164,+0.000000503)
deg=180/3.141592654;
PI=3.141592654;

def deg2rad(x):
	return x/deg

def rad2deg(x):
	return x*deg
	
def ATANP(sn,cs):

	if(cs==0):return 90;
	if(cs>0):return rad2deg(atan(sn/cs));
	return 180+rad2deg(atan(sn/cs));


"""
def Bhava(Sphuta,T,LT,sdtm)

	h=-120;
	a=anati;
	for(i=0;i<12;i++)
	
		h+=30;
		dlt=ASIN(SIN(h)*SIN(LT));
		P=((LT==0)?SIN(h):TAN(dlt)/TAN(LT));
		if(P<-1)P=-1;if(P>1)P=1;
		H=ACOS(P);
		X=sdtm-H;
		X=ATANP((SIN(X)*COS(a)+TAN(dlt)*SIN(a)),COS(X));
		X=MOD(X-90,360)*3600;
		Sphuta[i+I]=X;
	

"""

def E(M,e):
	E0,E1,i=M,0,0;
	while(E0!=E1):
		E0=E1;
		E1=M+e*rad2deg(sin(deg2rad(E0)));
		if(i>=10000):
			#echo "Error in E func",E0,E1,"<br>";
			return E1;
		i=i+1
	return E1



def GeoCentr(L,bita,alp, e, i, OHM, M, r, EE, bb, th, R):
#	echo L."---".bita."---".alp."---".e."---".i."---".OHM."---".M."---".r."---".EE."---".bb."---".th."---".R;
	v=2*ATANP(sqrt((1+e)/(1-e))*tan(deg2rad(EE/2)),1);v=MOD(v,360);
	r+=alp*(1-e*cos(deg2rad(EE)));
	u=MOD(L+v-M-OHM,360);
	l=ATANP(cos(deg2rad(i))*sin(deg2rad(u)),cos(deg2rad(u)))+OHM;
	b=rad2deg(asin( sin(deg2rad(u)) * sin(deg2rad(i)) ));
	bb+=b;b=bb;
	N=r*cos(deg2rad(b))*sin(deg2rad(l-th));
	D=r*cos(deg2rad(b))*cos(deg2rad(l-th))+R;
	L=MOD(ATANP(N,D)+th,360);
	DEL=N*N+D*D+r*sin(deg2rad(b))*r*sin(deg2rad(b));
	#echo "DEL==================".DEL."<br>";
	bita=rad2deg(asin( r*sin(deg2rad(b))/sqrt(DEL) ));
	return L,bita,r,bb

"""
void CCalculator::Graha(COleDateTime BirthTime,CEphe Sphuta[],int LATITUDE,int LONGITUDE)

	int Chk[30];Chk[0]=PLUTO-SUN+1;
	for(int i=SUN;i<=PLUTO;i++)Chk[i]=0;
	 d=0.001;
	CEphe TSphuta[30];
	Graha1(BirthTime,Sphuta,LATITUDE,LONGITUDE);
	for(;Chk[0];)
	
		BirthTime+=d;
		Graha1(BirthTime,TSphuta,LATITUDE,LONGITUDE);
		BirthTime-=d;
		for(int i=SUN;i<=PLUTO;i++)
		
			if(!Chk[i])
			
				TSphuta[i]-=Sphuta[i];
				if(TSphuta[i].Ephe!=0)
					if(TSphuta[i].Ephe<648000)
					
						Chk[i]=1;Chk[0]--;
						Sphuta[i].DIR=TRUE;
					
					if(TSphuta[i].Ephe>648000)
					
						Chk[i]=1;Chk[0]--;
						Sphuta[i].DIR=FALSE;
					
			
		
		d=d*10;
	

"""
def GetEphe(name):#""",BirthTime,Sphuta,LATITUDE,LONGITUDE""")

	#SUN
#	COleDateTime BaseDt;
#	BaseDt.SetDateTime(1899,12,31,12,0,0);
#	 T=(BirthTime-BaseDt)/36525;
#	global name;
#	T=(name['GMT']-win_gmmktime(12,0,0,12,31,1899,0))/86400/36525;
#	T=name['GMT']-datetime(1900,1,1,12,0,0);
	T=name['GMT']-datetime(1899,12,31,12,0,0);
	T=float(T.days*86400+T.seconds)/86400.0/36525.0;
	name["T"]=T
	"""
	echo name['GMT']."<br>";
	
	echo (name['GMT']-win_gmmktime(12,0,0,3,1,1978,0))/86400 ."<br>";
	
	printf("%.20f",(name['GMT']-win_gmmktime(12,0,0,12,31,1899,0))/86400/36525);
"""
	L,ohm,OHM,M,alp,e,i,r,EE,MM,b,decli=11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None],11*[None];
#	 c;
	
	L[3]=MTYL(	279.69668,	+36000.76892,	+0.0003025,		0,T);

	M[3]=MTYL(	358.47583,	+35999.04975,	-0.00015,		-0.0000033,T);
	e[3]=TYL(	0.01675104,	-0.0000418,		-0.000000126,	0,T);
	c=TYL(		1.91946,	-0.004789,		-0.000014,		0,T)*sin(deg2rad(M[3]))
	+TYL(	0.020094,	-0.0001,		0,				0,T)*sin(deg2rad(M[3]*2))
	+TYL(	0.000293,	0,				0,				0,T)*sin(deg2rad(M[3]*3));
		
	L[3]=MOD(L[3]+c,360);
	MM[3]=MOD(M[3]+c,360);
	r[3]=1.0000002*(1-e[3]*e[3])/(1+e[3]*cos(deg2rad(MM[3])));
	
	c=MTYL(		153.23,		+22518.7541,	0,				0,T);L[3]+=0.00134*cos(deg2rad(c));r[3]+=0.00000543*sin(deg2rad(c));
	c=MTYL(		216.57,		+45037.5082,	0,				0,T);L[3]+=0.00154*cos(deg2rad(c));r[3]+=0.00001575*sin(deg2rad(c));
	c=MTYL(		312.69,		+32964.3577,	0,				0,T);L[3]+=0.00200*cos(deg2rad(c));r[3]+=0.00001627*sin(deg2rad(c));
	c=MTYL(		350.74,		+445267.1142,	-0.00144,		0,T);L[3]+=0.00179*sin(deg2rad(c));r[3]+=0.00003076*cos(deg2rad(c));
	c=MTYL(		231.19,		+20.20,			0,				0,T);L[3]+=0.00178*sin(deg2rad(c));
	c=MTYL(		353.40,		+65928.7155,	0,				0,T);r[3]+=0.00000927*sin(deg2rad(c));

	L[3]=MOD(L[3],360);
	name["Sun"]=L[3]*3600;

	#MEAN PLANETS

	L[1]=MTYL(		178.179078,	+149474.07078,	+0.0003011,		0,T);
	alp[1]=			0.3870986;
	e[1]=TYL(		0.20561421,	+0.00002046,	-0.000000030,	0,T);
	i[1]=MTYL(		7.002881,	+0.0018608,		-0.0000183,		0,T);
	ohm[1]=MTYL(	28.753753,	+0.3702806,		+0.0001208,		0,T);
	OHM[1]=MTYL(	47.145944,	+1.1852083,		+0.0001739,		0,T);

	L[2]=MTYL(		342.767053,	+58519.21191,	+0.0003097,		0,T);
	alp[2]=			0.7233316;
	e[2]=TYL(		0.00682069,	-0.00004774,	+0.000000091,	0,T);
	i[2]=MTYL(		3.393631,	+0.0010058,		-0.0000010,		0,T);
	ohm[2]=MTYL(	54.384186,	+0.5081861,		-0.0013864,		0,T);
	OHM[2]=MTYL(	75.779647,	+0.8998500,		+0.0004100,		0,T);

	L[4]=MTYL(		293.737334,	+19141.69551,	+0.0003107,		0,T);
	alp[4]=			1.5236883;
	e[4]=TYL(		0.09331290,	+0.000092064,	-0.000000077,	0,T);
	i[4]=MTYL(		1.850333,	-0.0006750,		+0.0000126,		0,T);
	ohm[4]=MTYL(	285.431761,	+1.0697667,		+0.0001313,		+0.00000414,T);
	OHM[4]=MTYL(	48.786442,	+0.7709917,		-0.0000014,		-0.00000533,T);

	L[5]=MTYL(		238.049257,	+3036.301986,	+0.0003347,		-0.00000165,T);
	alp[5]=			5.202561;
	e[5]=TYL(		0.04833475,	+0.000164180,	-0.0000004676,	-0.0000000017,T);
	i[5]=MTYL(		1.308736,	-0.0056961,		+0.0000039,		0,T);
	ohm[5]=MTYL(	273.277558,	+0.5994317,		+0.00070405,	+0.00000508,T);
	OHM[5]=MTYL(	99.443414,	+1.0105300,		+0.00035222,	-0.00000851,T);

	L[6]=MTYL(		266.564377,	+1223.509884,	+0.0003245,		-0.0000058,T);
	alp[6]=			9.554747;
	e[6]=TYL(		0.05589232,	-0.00034550,	-0.000000728,	+0.00000000074,T);
	i[6]=MTYL(		2.492519,	-0.0039189,		-0.00001549,	+0.00000004,T);
	ohm[6]=MTYL(	338.307800,	+1.0852207,		+0.00097854,	+0.00000992,T);
	OHM[6]=MTYL(	112.790414,	+0.8731951,		-0.00015218,	-0.00000531,T);

	L[7]=MTYL(		244.197470,	+429.863546,	+0.0003160,		-0.00000060,T);
	alp[7]=			19.21814;
	e[7]=TYL(		0.0463444,	-0.00002658,	+0.000000077,	0,T);
	i[7]=MTYL(		0.772464,	+0.0006253,		+0.0000395,		0,T);
	ohm[7]=MTYL(	98.071581,	+0.9857650,		-0.0010745,		-0.00000061,T);
	OHM[7]=MTYL(	73.477111,	+0.4986678,		+0.0013117,		0,T);

	L[8]=MTYL(		84.457994,	+219.885914,	+0.0003205,		-0.00000060,T);
	alp[8]=			30.10957;
	e[8]=TYL(		0.00899704,	+0.000006330,	-0.000000002,	0,T);
	i[8]=MTYL(		1.779242,	-0.0095436,		-0.0000091,		0,T);
	ohm[8]=MTYL(	276.045975,	+0.3256394,		+0.00014095,	+0.000004113,T);
	OHM[8]=MTYL(	130.681389,	+1.0989350,		+0.00024987,	-0.000004718,T);

	M[1]=MTYL(		102.27938,	149472.51529,	+0.000007,		0,T);
	M[2]=MTYL(		212.60322,	58517.80387,	+0.001286,		0,T);
	M[4]=MTYL(		319.51913,	19139.85475,	+0.000181,		0,T);
	M[5]=MTYL(		225.32833,	3034.69202,		-0.000722,		0,T);
	M[6]=MTYL(		175.46622,	1221.55147,		-0.000502,		0,T);
	M[7]=MTYL(		72.64878,	428.37911,		+0.000079,		0,T);
	M[8]=MTYL(		37.73063,	218.46134,		-0.000070,		0,T);

	#CORRECTION TO MERCURY
	EE[1]=E(M[1],e[1]);
	L[1]+=	+0.00204		*cos(deg2rad(	5*M[2]	-2*M[1]	+12.220))
	+0.00103		*cos(deg2rad(	2*M[2]	-M[1]	-160.692))
	+0.00091		*cos(deg2rad(	2*M[5]	-M[1]	-37.003))
	+0.00078		*cos(deg2rad(	5*M[2]	-3*M[1]	+10.137));
	L[1]=MOD(L[1],360);
	r[1]=	+0.000007525	*cos(deg2rad(	2*M[5]	-M[1]	+53.013))
	+0.000006802	*cos(deg2rad(	5*M[2]	-3*M[1]	-259.918))
	+0.000005457	*cos(deg2rad(	2*M[2]	-2*M[1]	-71.188))
	+0.000003569	*cos(deg2rad(	5*M[2]	-M[1]	-77.75));
	b[1]=0;
	MM[1]=M[1];

	#CORRECTION TO VENUS
	c=	+0.00077		*sin(deg2rad(MTYL(237.24,		150.27,			0,0,T)));
	MM[2]=M[2]+c;
	L[2]+=c;
	EE[2]=E(MM[2],e[2]);
	L[2]+=	+0.00313		*cos(deg2rad(	2*M[3]	-2*M[2]	-148.225))
	+0.00198		*cos(deg2rad(	3*M[3]	-3*M[2]	+2.565))
	+0.00136		*cos(deg2rad(	M[3]	-M[2]	-119.107))
	+0.00096		*cos(deg2rad(	3*M[3]	-2*M[2]	-135.912))
	+0.00082		*cos(deg2rad(	M[5]	-M[2]	-208.087));
	r[2]=+0.000022501	*cos(deg2rad(	2*M[3]	-2*M[2]	-58.208))+0.000019045	*cos(deg2rad(	3*M[3]	-3*M[2]	+92.577))		+0.000006887	*cos(deg2rad(	M[5]	-M[2]	-118.090))+0.000005172	*cos(deg2rad(	M[3]	-M[2]	-29.110))+0.000003620	*cos(deg2rad(	5*M[3]	-4*M[2]	-104.208))+0.000003283	*cos(deg2rad(	4*M[3]	-4*M[2]	+63.513))+0.000003074	*cos(deg2rad(	2*M[5]	-2*M[2]	-55.167));
	b[2]=0;

	#CORRECTION TO MARS
	c=(	-0.01133		*sin(deg2rad(	3*M[5]	-8*M[4]	+4*M[3]))
		-0.00933		*cos(deg2rad(	3*M[5]	-8*M[4]	+4*M[3])));
	MM[4]=M[4]+c;
	L[4]+=c;
	EE[4]=E(MM[4],e[4]);
	L[4]+=+0.00705		*cos(deg2rad(	M[5]	-M[4]	-48.958))+0.00607		*cos(deg2rad(	2*M[5]	-M[4]	-188.350))+0.00445		*cos(deg2rad(	2*M[5]	-2*M[4]	-191.897))+0.00388		*cos(deg2rad(	M[3]	-2*M[4]	+20.495))+0.00238		*cos(deg2rad(	M[3]	-M[4]	+35.097))+0.00204		*cos(deg2rad(	2*M[3]	-3*M[4]	+158.638))+0.00177		*cos(deg2rad(	3*M[4]	-M[2]	-57.602))+0.00136		*cos(deg2rad(	2*M[3]	-4*M[4]	+154.093))+0.00104		*cos(deg2rad(	M[5]			+17.618));
	r[4]=+0.000053227	*cos(deg2rad(	M[5]	-M[4]	+41.1306))+0.000050989	*cos(deg2rad(	2*M[5]	-2*M[4]	-101.9847))+0.000038278	*cos(deg2rad(	2*M[5]	-M[4]	-98.3292))+0.000015996	*cos(deg2rad(	M[3]	-M[4]	-55.555))+0.000014764	*cos(deg2rad(	2*M[3]	-3*M[4]	+68.622))+0.000008966	*cos(deg2rad(	M[5]	-2*M[4]	+43.615))+0.000007914	*cos(deg2rad(	3*M[5]	-2*M[4]	-139.737))+0.000007004	*cos(deg2rad(	2*M[5]	-3*M[4]	-102.888))+0.000006620	*cos(deg2rad(	M[3]	-2*M[4]	+113.202))+0.000004930	*cos(deg2rad(	3*M[5]	-3*M[4]	-76.243))+0.000004693	*cos(deg2rad(	3*M[3]	-5*M[4]	+190.603))+0.000004571	*cos(deg2rad(	2*M[3]	-4*M[4]	+244.702))+0.000004409	*cos(deg2rad(	3*M[5]	-M[4]	-115.828));
	b[4]=0;
	
	#CORRECTION TO JUPITER
	# vj,Pj,Qj,Sj,Vj,Wj,Xj,Aj,Bj,Yj;

	vj=TYL(			0.1,		0.2,		0,	0,T);
	Pj=MTYL(		237.47555,	3034.9061,	0,	0,T);
	Qj=MTYL(		265.91650,	1222.1139,	0,	0,T);
	Sj=MTYL(		243.51721,	428.4677,	0,	0,T);
	Vj=MOD(5*Qj-2*Pj,360);
	Wj=MOD(2*Pj-6*Qj+3*Sj,360);
	Xj=MOD(Qj-Pj,360);
	Yj=MOD(Sj-Qj,360);

	Aj=(
		+(0.331364	-0.010281*vj	-0.004692*vj*vj)	*sin(deg2rad(Vj))
		+(0.003228	-0.064436*vj	+0.002075*vj*vj)	*cos(deg2rad(Vj))
		-(0.003083	+0.000275*vj	-0.000489*vj*vj)	*sin(deg2rad(2*Vj))
		+0.002472										*sin(deg2rad(Wj))
		+0.013619										*sin(deg2rad(Xj))
		+0.018472										*sin(deg2rad(Xj*2))
		+0.006717										*sin(deg2rad(Xj*3))
		+0.002775										*sin(deg2rad(Xj*4))
		+(0.007275	-0.001253*vj)			*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		+0.006417										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		+0.002439										*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-(0.033839	+0.001125*vj)			*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		-0.003767										*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj))
		-(0.035681	+0.001208*vj)			*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		-0.004261										*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		+0.002178										*cos(deg2rad(Qj))
		+(-0.006333	+0.001161*vj)		*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		-0.006675										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj))
		-0.002664										*cos(deg2rad(Xj*3))	*cos(deg2rad(Qj))
		-0.002572										*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		-0.003567										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+0.002094										*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+0.003342										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj*2))
        )
	Bj=(
		+(0.007192	-0.003147*vj)									*sin(deg2rad(Vj))
		+(-0.020428	-0.000675*vj	+0.000197*vj*vj)	*cos(deg2rad(Vj))
		+(0.007269	+0.000672*vj)									*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		-0.004344																*sin(deg2rad(Qj))
		+0.034036										*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		+0.005614										*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj))
		+0.002964										*cos(deg2rad(Xj*3))	*sin(deg2rad(Qj))
		+0.037761										*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		+0.006158										*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		-0.006603										*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		-0.005356										*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+0.002722										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+0.004483										*cos(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		-0.002642										*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj*2))
		+0.004403										*sin(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		-0.002536										*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+0.005547										*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		-0.002689										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj*2))
        )
	MM[5]=M[5]+Aj-Bj/e[5];

	e[5]+=(
		 (3606		+130*vj			-43*vj*vj)			*sin(deg2rad(Vj))
		+(1289		-580*vj)										*cos(deg2rad(Vj))
		-6764											*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		-1110											*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-224											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-204											*sin(deg2rad(Qj))
		+(1284		+116*vj)						*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		+188											*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj))
		+(1460		+130*vj)						*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		+224											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		-817											*cos(deg2rad(Qj))
		+6074											*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+992											*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj))
		+508											*cos(deg2rad(Xj*3))	*cos(deg2rad(Qj))
		+230											*cos(deg2rad(Xj*4))	*cos(deg2rad(Qj))
		+108											*cos(deg2rad(Xj*5))	*cos(deg2rad(Qj))
		-(956		+73*vj)						*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+448											*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+137											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj*2))
		+(-997		+108*vj)						*cos(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+480											*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj*2))
		+148											*cos(deg2rad(Xj*3))	*sin(deg2rad(Qj*2))
		+(-956		+99*vj)						*sin(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+490											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+158											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj*2))
		+179											*cos(deg2rad(Qj*2))
		+(1024		+75*vj)						*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		-437											*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj*2))
		-132											*cos(deg2rad(Xj*3))	*cos(deg2rad(Qj*2))
		)/10000000;

	alp[5]+=(
		-263											*cos(deg2rad(Vj))
		+205											*cos(deg2rad(Xj))
		+693											*cos(deg2rad(Xj*2))
		+312											*cos(deg2rad(Xj*3))
		+147											*cos(deg2rad(Xj*4))		
		+299											*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		+181											*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj))
		+204											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		+111											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj))
		-337											*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		-111											*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj))
		)/1000000;

	L[5]+=Aj;
	ohm[5]+=Bj;
	r[5]=0;b[5]=0;
	EE[5]=E(MM[5],e[5]);


	#CORRECTION TO SATURN
	Aj=(
		+(-0.814181	+0.018150*vj	+0.016714*vj*vj)	*sin(deg2rad(Vj))
		+(-0.010497	+0.160906*vj	-0.004100*vj*vj)	*cos(deg2rad(Vj))
		+0.007581										*sin(deg2rad(Vj*2))
		-0.007986										*sin(deg2rad(Wj))
		-0.148811										*sin(deg2rad(Xj))
		-0.040786										*sin(deg2rad(Xj*2))
		-0.015208										*sin(deg2rad(Xj*3))
		-0.006339										*sin(deg2rad(Xj*4))
		-0.006244										*sin(deg2rad(Qj))
		+(0.008931	+0.002728*vj)			*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		-0.016500										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-0.005775										*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		+(0.081344	+0.003206*vj)			*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		+0.015019										*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj))
		+(0.085581	+0.002494*vj)			*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		+(0.025328	-0.003117*vj)			*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+0.014394										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj))
		+0.006319										*cos(deg2rad(Xj*3))	*cos(deg2rad(Qj))
		+0.006369										*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+0.009156										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+0.007525										*sin(deg2rad(Yj*3))		*sin(deg2rad(Qj*2))
		-0.005236										*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		-0.007736										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj*2))
		-0.007528										*cos(deg2rad(Yj*3))	*cos(deg2rad(Qj*2))
        )
	Bj=(
		+(0.077108	+0.007186*vj	-0.001533*vj*vj)	*sin(deg2rad(Vj))
		+(0.045803	-0.014766*vj	-0.000536*vj*vj)	*cos(deg2rad(Vj))
		-0.007075										*sin(deg2rad(Xj))
		-0.075825										*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		-0.024839										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-0.008631										*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-0.072586										*cos(deg2rad(Qj))
		-0.150383										*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+0.026897										*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj))
		+0.010053										*cos(deg2rad(Xj*3))	*cos(deg2rad(Qj))
		-(0.013597	+0.001719*vj)			*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+(-0.007742	+0.001517*vj)		*cos(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+(0.013586	-0.001375*vj)			*cos(deg2rad(Xj*2))	*sin(deg2rad(Qj*2))
		+(-0.013667	+0.001239*vj)		*sin(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+0.011981										*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+(0.014861	+0.001136*vj)			*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		-(0.013064	+0.001628*vj)			*cos(deg2rad(Xj*2))	*cos(deg2rad(Qj*2))
        )
	MM[6]=M[6]+Aj-Bj/e[6];

	e[6]+=(
		(-7927		+2548*vj		+91*vj*vj)			*sin(deg2rad(Vj))
		+(13381		+1226*vj		-253*vj*vj)			*cos(deg2rad(Vj))
		+(248		-121*vj)							*sin(deg2rad(Vj*2))
		-(305		+91*vj)								*cos(deg2rad(Vj*2))
		+412											*sin(deg2rad(Xj*2))
		+12415															*sin(deg2rad(Qj))
		+(390		-617*vj)							*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		+(165		-204*vj)							*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		+26599											*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		-4687											*cos(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-1870											*cos(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-821											*cos(deg2rad(Xj*4))		*sin(deg2rad(Qj))
		-377											*cos(deg2rad(Xj*5))		*sin(deg2rad(Qj))
		+497											*cos(deg2rad(Yj*2))		*sin(deg2rad(Qj))
		+(163		-611*vj)											*cos(deg2rad(Qj))
		-12696											*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		-4200											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		-1503											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj))
		-619											*sin(deg2rad(Xj*4))		*cos(deg2rad(Qj))
		-268											*sin(deg2rad(Xj*5))		*cos(deg2rad(Qj))
		-(282		+1306*vj)							*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+(-86		+230*vj)							*cos(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		+461											*sin(deg2rad(Yj*2))		*cos(deg2rad(Qj))
		-350															*sin(deg2rad(Qj*2))
		+(2211		-286*vj)							*sin(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		-2208											*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		-568											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj*2))
		-346											*sin(deg2rad(Xj*4))		*sin(deg2rad(Qj*2))
		-(2780		+222*vj)							*cos(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+(2022		+263*vj)							*cos(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+248											*cos(deg2rad(Xj*3))		*sin(deg2rad(Qj*2))
		+242											*sin(deg2rad(Yj*3))		*sin(deg2rad(Qj*2))
		+467											*cos(deg2rad(Yj*3))		*sin(deg2rad(Qj*2))
		-490															*cos(deg2rad(Qj*2))
		-(2842		+279*vj)							*sin(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+(128		+226*vj)							*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+224											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj*2))
		+(-1594		+282*vj)							*cos(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+(2162		-207*vj)							*cos(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+561											*cos(deg2rad(Xj*3))		*cos(deg2rad(Qj*2))
		+343											*cos(deg2rad(Xj*4))		*cos(deg2rad(Qj*2))
		+469											*sin(deg2rad(Yj*3))		*cos(deg2rad(Qj*2))
		-242											*cos(deg2rad(Yj*3))		*cos(deg2rad(Qj*2))
		-205											*sin(deg2rad(Xj))		*sin(deg2rad(Qj*3))
		+262											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj*3))
		+208											*cos(deg2rad(Xj))		*cos(deg2rad(Qj*3))
		-271											*cos(deg2rad(Xj*3))		*cos(deg2rad(Qj*3))
		-382											*cos(deg2rad(Xj*3))		*sin(deg2rad(Qj*4))
		-376											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj*4))
		)/10000000;

	alp[6]+=(
		+572*vj											*sin(deg2rad(Vj))
		+2933											*cos(deg2rad(Vj))
		+33629											*cos(deg2rad(Xj))
		-3081											*cos(deg2rad(Xj*2))
		-1423											*cos(deg2rad(Xj*3))
		-671											*cos(deg2rad(Xj*4))
		-320											*cos(deg2rad(Xj*5))
		+1098															*sin(deg2rad(Qj))
		-2812											*sin(deg2rad(Xj))		*sin(deg2rad(Qj))
		+688											*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-393											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-228											*sin(deg2rad(Xj*4))		*sin(deg2rad(Qj))
		+2138											*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		-999											*cos(deg2rad(Xj*2))		*sin(deg2rad(Qj))
		-642											*cos(deg2rad(Xj*3))		*sin(deg2rad(Qj))
		-325											*cos(deg2rad(Xj*4))		*sin(deg2rad(Qj))
		-890															*cos(deg2rad(Qj))
		+2206											*sin(deg2rad(Xj))		*cos(deg2rad(Qj))
		-1590											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		-647											*sin(deg2rad(Xj*3))		*cos(deg2rad(Qj))
		-344											*sin(deg2rad(Xj*4))		*cos(deg2rad(Qj))
		+2885											*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+(2172		+102*vj)							*cos(deg2rad(Xj*2))		*cos(deg2rad(Qj))
		+296											*cos(deg2rad(Xj*3))		*cos(deg2rad(Qj))
		-267											*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		-778											*cos(deg2rad(Xj))		*sin(deg2rad(Qj*2))
		+495											*cos(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+250											*cos(deg2rad(Xj*3))		*sin(deg2rad(Qj*2))
		-856											*sin(deg2rad(Xj))		*cos(deg2rad(Qj*2))
		+441											*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+296											*cos(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		+211											*cos(deg2rad(Xj*3))		*cos(deg2rad(Qj*2))
		-427											*sin(deg2rad(Xj))		*sin(deg2rad(Qj*3))
		+398											*sin(deg2rad(Xj*3))		*sin(deg2rad(Qj*3))
		+344											*cos(deg2rad(Xj))		*cos(deg2rad(Qj*3))
		-427											*cos(deg2rad(Xj*3))		*cos(deg2rad(Qj*3))
		)/1000000;

	L[6]+=Aj;
	ohm[6]+=Bj;
	r[6]=0;
	EE[6]=E(MM[6],e[6]);
	b[6]=(
		+0.000747										*cos(deg2rad(Xj))		*sin(deg2rad(Qj))
		+0.001069										*cos(deg2rad(Xj))		*cos(deg2rad(Qj))
		+0.002108										*sin(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+0.001261										*cos(deg2rad(Xj*2))		*sin(deg2rad(Qj*2))
		+0.001236										*sin(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
		-0.002075										*cos(deg2rad(Xj*2))		*cos(deg2rad(Qj*2))
        )
	#CORRECTION TO URANUS
	# Gu,Hu,Nu,TH;
	Gu=MTYL(		83.76922,	218.4907,	0,	0,T);
	Hu=MOD(2*Gu-Sj,360);
	Xj=MOD(Sj-Pj,360);
	Nu=MOD(Sj-Qj,360);
	TH=MOD(Gu-Sj,360);

	Aj=(
		+(0.864319	-0.001583*vj)						*sin(deg2rad(Hu))
		+(0.082222	-0.006833*vj)						*cos(deg2rad(Hu))
		+0.036017										*sin(deg2rad(Hu*2))
		-0.003019										*cos(deg2rad(Hu*2))
		+0.008122										*sin(deg2rad(Wj))
        )

	Bj=(
		+0.120303										*sin(deg2rad(Hu))
		+(0.019472	-0.000947*vj)						*cos(deg2rad(Hu))
		+0.006197										*sin(deg2rad(Hu*2))
        )

	MM[7]=M[7]+Aj-Bj/e[7];

	e[7]+=(
		+(-3349		+163*vj)							*sin(deg2rad(Hu))
		+20981											*cos(deg2rad(Hu))
		+1311											*cos(deg2rad(Hu*2))
		)/10000000;

	alp[7]+=-0.003825									*cos(deg2rad(Hu));

	L[7]+=Aj;
	ohm[7]+=Bj;
	EE[7]=E(MM[7],e[7]);

	L[7]+=(
		+(0.010122	-0.000988*vj)						*sin(deg2rad(Sj+Nu))
		+(-0.038581	+0.002031*vj	-0.001910*vj*vj)	*cos(deg2rad(Sj+Nu))
		+(0.034964	-0.001038*vj	+0.000868*vj*vj)	*cos(deg2rad(Sj*2+Nu))
		+0.005594										*sin(deg2rad(Sj+TH*3))
		-0.014808										*sin(deg2rad(Xj))
		-0.005794										*sin(deg2rad(Nu))
		+0.002347										*cos(deg2rad(Nu))
		+0.009872										*sin(deg2rad(TH))
		+0.008803										*sin(deg2rad(TH*2))
		-0.004308										*sin(deg2rad(TH*3))
	)
	r[7]=(
		-25948
		+4985											*cos(deg2rad(Xj))
		-1230											*cos(deg2rad(Sj))
		+3354											*cos(deg2rad(Nu))
		+(5795	*cos(deg2rad(Sj))	-1165	*sin(deg2rad(Sj))	+1388	*cos(deg2rad(Sj*2)))	*sin(deg2rad(Nu))
		+(1351	*cos(deg2rad(Sj))	+5702	*sin(deg2rad(Sj))	+1388	*sin(deg2rad(Sj*2)))	*cos(deg2rad(Nu))
		+904											*cos(deg2rad(TH*2))
		+894											*(cos(deg2rad(TH))-cos(deg2rad(TH*3)))
		)/1000000;

	b[7]=(
		+0.000458										*sin(deg2rad(Nu))		*sin(deg2rad(Sj))
		-0.000642										*cos(deg2rad(Nu))		*sin(deg2rad(Sj))
		-0.000517										*cos(deg2rad(TH*4))		*sin(deg2rad(Sj))
		-0.000347										*sin(deg2rad(Nu))		*cos(deg2rad(Sj))
		-0.000853										*cos(deg2rad(Nu))		*cos(deg2rad(Sj))
		-0.000517										*sin(deg2rad(Nu*4))		*cos(deg2rad(Sj))
		+0.000403*(	cos(deg2rad(TH*2))	*sin(deg2rad(Sj*2))				+sin(deg2rad(TH*2))		*cos(deg2rad(Sj*2)))
        )
	#Neptune
	Xj=MOD(Gu-Pj,360);
	Nu=MOD(Gu-Qj,360);
	TH=MOD(Gu-Sj,360);

	Aj=(
		+(-0.589833	+0.001089*vj)						*sin(deg2rad(Hu))
		+(-0.056094	+0.004658*vj)						*cos(deg2rad(Hu))
		-0.024286										*sin(deg2rad(Hu*2))
        )
	Bj=(
		+0.024039										*sin(deg2rad(Hu))
		-0.025303										*cos(deg2rad(Hu))
		+0.006206										*sin(deg2rad(Hu*2))
		-0.005992										*cos(deg2rad(Hu*2))
        )
	MM[8]=M[8]+Aj-Bj/e[8];

	e[8]+=(
		+4389											*sin(deg2rad(Hu))
		+4262											*cos(deg2rad(Hu))
		+1129											*sin(deg2rad(Hu*2))
		+1089											*cos(deg2rad(Hu*2))
		)/10000000;

	alp[8]+=(
		-817											*sin(deg2rad(Hu))
		+8189											*cos(deg2rad(Hu))
		+781											*cos(deg2rad(Hu*2))
		)/1000000;

	L[8]+=Aj;
	ohm[8]+=Bj;
	EE[8]=E(MM[8],e[8]);

	L[8]+=(
		-0.009556										*sin(deg2rad(Xj))
		-0.005178										*sin(deg2rad(Nu))
		+0.002572										*sin(deg2rad(TH*2))
		-0.002972										*cos(deg2rad(TH*2))		*sin(deg2rad(Gu))
		-0.002833										*sin(deg2rad(TH*2))		*cos(deg2rad(Gu))
        )
	r[8]=(
		-40596
		+4992											*cos(deg2rad(Xj))
		+2744											*cos(deg2rad(Nu))
		+2044											*cos(deg2rad(TH))
		+1051											*cos(deg2rad(TH*2))
		)/1000000;

	b[8]=(
		+0.000336										*cos(deg2rad(TH*2))		*sin(deg2rad(Gu))
		+0.000364										*sin(deg2rad(TH*2))		*cos(deg2rad(Gu))
        )
	for k in range(1,9):#(k=1;k<9;k++)
		if(k!=3):
			L[k],decli[k],r[k],b[k]=GeoCentr(L[k],decli[k],alp[k],e[k],i[k],OHM[k],MM[k],r[k],EE[k],b[k],L[3],r[3]);

	name['Mercury']	=MOD(L[1],360)*3600;name['Mercury.Decli']	=MOD(decli[1],360)*3600;
	name['Venus']		=MOD(L[2],360)*3600;name['Venus.Decli']		=MOD(decli[2],360)*3600;
	name['Mars']		=MOD(L[4],360)*3600;name['Mars.Decli']		=MOD(decli[4],360)*3600;
	name['Jupiter']	=MOD(L[5],360)*3600;name['Jupiter.Decli']		=MOD(decli[5],360)*3600;
	name['Saturn']	=MOD(L[6],360)*3600;name['Saturn.Decli']		=MOD(decli[6],360)*3600;
	name['Uranus']	=MOD(L[7],360)*3600;name['Uranus.Decli']		=MOD(decli[7],360)*3600;
	name['Neptune']	=MOD(L[8],360)*3600;name['Neptune.Decli']	=MOD(decli[8],360)*3600;
	
#	 Dm,Fm,em,e2;
	L[9]=MTYL(		270.434164,	+481267.8831,	-0.001133,		+0.0000019,T);
#	M[3]=MTYL(		358.475833,	+35999.0498,	-0.000150,		-0.0000033);
	M[9]=MTYL(		296.104608,	+477198.8491,	+0.009192,		+0.0000144,T);
	Dm=MTYL(		350.737486,	+445267.1142,	-0.001436,		+0.0000019,T);
	Fm=MTYL(		11.250889,	+483202.0251,	-0.003211,		-0.0000003,T);
	OHM[9]=MTYL(	259.183275,	-1934.1420,		+0.002078,		+0.0000022,T);

	MM[3]=M[3];
	

	L[9]+=			+0.000233							*sin(deg2rad(51.2+20.2*T));
	MM[3]+=			-0.001778							*sin(deg2rad(51.2+20.2*T));
	M[9]+=			+0.000817							*sin(deg2rad(51.2+20.2*T));
	Dm+=			+0.002011							*sin(deg2rad(51.2+20.2*T));
	Xj=				+0.003964							*sin(deg2rad(MTYL(346.560,	132.870,	-0.0091731,	0,T)));
	L[9]+=			+0.001964							*sin(deg2rad(OHM[9]));
	M[9]+=			+0.002541							*sin(deg2rad(OHM[9]));
	Dm+=			+0.001964							*sin(deg2rad(OHM[9]));
	Fm+=			-0.024691							*sin(deg2rad(OHM[9]));
	Fm+=			-0.004328							*sin(deg2rad(OHM[9]+275.05-2.30*T));
	L[9]+=Xj;M[9]+=Xj;Dm+=Xj;Fm+=Xj;

	em=TYL(	1,	-0.002495,	-0.00000752,	0,T);
	e2=em*em;
	L[9]+=(
		+6.288750						*sin(deg2rad(	M[9]					))
		+1.274018						*sin(deg2rad(	2*Dm	-M[9]			))
		+0.658309						*sin(deg2rad(	2*Dm					))
		+0.213616						*sin(deg2rad(	2*M[9]					))
		-0.185596						*sin(deg2rad(	MM[3]					))*em
		-0.114336						*sin(deg2rad(	2*Fm					))
		+0.058793						*sin(deg2rad(	2*Dm	-2*M[9]			))
		+0.057212						*sin(deg2rad(	2*Dm	-MM[3]	-M[9]	))*em
		+0.053320						*sin(deg2rad(	2*Dm	+M[9]			))
		+0.045874						*sin(deg2rad(	2*Dm	-MM[3]			))*em
		+0.041024						*sin(deg2rad(	M[9]	-MM[3]			))*em
		-0.034718						*sin(deg2rad(	Dm						))
		-0.030465						*sin(deg2rad(	MM[3]	+M[9]			))*em
		+0.015326						*sin(deg2rad(	2*Dm	-2*Fm			))
		-0.012528						*sin(deg2rad(	2*Fm	+M[9]			))
		-0.010980						*sin(deg2rad(	2*Fm	-M[9]			))
		+0.010674						*sin(deg2rad(	4*Dm	-M[9]			))
		+0.010034						*sin(deg2rad(	3*M[9]					))
		+0.008548						*sin(deg2rad(	4*Dm	-2*M[9]			))
		-0.007910						*sin(deg2rad(	MM[3]	-M[9]	+2*Dm	))*em
		-0.006783						*sin(deg2rad(	2*Dm	+MM[3]			))*em
		+0.005162						*sin(deg2rad(	M[9]	-Dm				))
		+0.005000						*sin(deg2rad(	MM[3]	+Dm				))*em
		+0.004049						*sin(deg2rad(	M[9]	-MM[3]	+2*Dm	))*em
		+0.003996						*sin(deg2rad(	2*M[9]	+2*Dm			))
		+0.003862						*sin(deg2rad(	4*Dm					))
		+0.003665						*sin(deg2rad(	2*Dm	-3*M[9]			))
		+0.002695						*sin(deg2rad(	2*M[9]	-MM[3]			))*em
		+0.002602						*sin(deg2rad(	M[9]	-2*Fm	-2*Dm	))
		+0.002396						*sin(deg2rad(	2*Dm	-MM[3]	-2*M[9]	))*em
		-0.002349						*sin(deg2rad(	M[9]	+Dm				))
		+0.002249						*sin(deg2rad(	2*Dm	-2*MM[3]		))*e2
		-0.002125						*sin(deg2rad(	2*M[9]	+MM[3]			))*em
		-0.002079						*sin(deg2rad(	2*MM[3]					))*e2
		+0.002059						*sin(deg2rad(	2*Dm	-M[9]	-2*MM[3]))*e2
		-0.001773						*sin(deg2rad(	M[9]	+2*Dm	-2*Fm	))
		-0.001595						*sin(deg2rad(	2*Fm	+2*Dm			))
		+0.001220						*sin(deg2rad(	4*Dm	-MM[3]	-M[9]	))*em
		-0.001110						*sin(deg2rad(	2*M[9]	+2*Fm			))
		+0.000892						*sin(deg2rad(	M[9]	-3*Dm			))
		-0.000811						*sin(deg2rad(	MM[3]	+M[9]	+2*Dm	))*em
		+0.000761						*sin(deg2rad(	4*Dm	-MM[3]	-2*M[9]	))*em
		+0.000717						*sin(deg2rad(	M[9]	-2*MM[3]		))*e2
		+0.000704						*sin(deg2rad(	M[9]	-2*MM[3]-2*Dm	))*e2
		+0.000693						*sin(deg2rad(	MM[3]	-2*M[9]	+2*Dm	))*em
		+0.000598						*sin(deg2rad(	2*Dm	-MM[3]	-2*Fm	))*em
		+0.000550						*sin(deg2rad(	M[9]	+4*Dm			))
		+0.000538						*sin(deg2rad(	4*M[9]					))
		+0.000521						*sin(deg2rad(	4*Dm	-MM[3]			))*em
		+0.000486						*sin(deg2rad(	2*M[9]	-Dm				))
                )
	Bm=(
		+5.128189						*sin(deg2rad(	Fm						))
		+0.280606						*sin(deg2rad(	M[9]	+Fm				))
		+0.277693						*sin(deg2rad(	M[9]	-Fm				))
		+0.173238						*sin(deg2rad(	2*Dm	-Fm				))
		+0.055413						*sin(deg2rad(	2*Dm	+Fm		-M[9]	))
		+0.046272						*sin(deg2rad(	2*Dm	-Fm		-M[9]	))
		+0.032573						*sin(deg2rad(	2*Dm	+Fm				))
		+0.017198						*sin(deg2rad(	2*M[9]	+Fm				))
		+0.009267						*sin(deg2rad(	2*Dm	+M[9]	-Fm		))
		+0.008823						*sin(deg2rad(	2*M[9]	-Fm				))
		+0.008247						*sin(deg2rad(	2*Dm	-MM[3]	-Fm		))*em
		+0.004323						*sin(deg2rad(	2*Dm	-Fm		-2*M[9]	))
		+0.004200						*sin(deg2rad(	2*Dm	+Fm		+M[9]	))
		+0.003372						*sin(deg2rad(	Fm		-MM[3]	-2*Dm	))*em
		+0.002472						*sin(deg2rad(	2*Dm	+Fm		-MM[3]	-M[9]))*em
		+0.002222						*sin(deg2rad(	2*Dm	+Fm		-MM[3]	))*em
		+0.002072						*sin(deg2rad(	2*Dm	-Fm		-MM[3]	-M[9]))*em
		+0.001877						*sin(deg2rad(	Fm		-MM[3]	+M[9]	))*em
		+0.001828						*sin(deg2rad(	4*Dm	-Fm		-M[9]	))
		-0.001803						*sin(deg2rad(	Fm		+MM[3]			))*em
		-0.001750						*sin(deg2rad(	3*Fm					))
		+0.001570						*sin(deg2rad(	M[9]	-MM[3]	-Fm		))*em
		-0.001487						*sin(deg2rad(	Fm		+Dm				))
		-0.001481						*sin(deg2rad(	Fm		+MM[3]	+M[9]	))*em
		+0.001417						*sin(deg2rad(	Fm		-MM[3]	-M[9]	))*em
		+0.001350						*sin(deg2rad(	Fm		-MM[3]			))*em
		+0.001330						*sin(deg2rad(	Fm		-Dm				))
		+0.001106						*sin(deg2rad(	Fm		+3*M[9]			))
		+0.001020						*sin(deg2rad(	4*Dm	-Fm				))
		+0.000833						*sin(deg2rad(	Fm		+4*Dm	-M[9]	))
		+0.000781						*sin(deg2rad(	M[9]	-3*Fm			))
		+0.000670						*sin(deg2rad(	Fm		+4*Dm	-2*M[9]	))
		+0.000606						*sin(deg2rad(	2*Dm	-3*Fm			))
		+0.000597						*sin(deg2rad(	2*Dm	+2*M[9]	-Fm		))
		+0.000492						*sin(deg2rad(	2*Dm	+M[9]	-MM[3]	-Fm))*em
		+0.000450						*sin(deg2rad(	2*M[9]	-Fm		-2*Dm	))
		+0.000439						*sin(deg2rad(	3*M[9]	-Fm				))
		+0.000423						*sin(deg2rad(	Fm		+2*Dm	+2*M[9]	))
		+0.000422						*sin(deg2rad(	2*Dm	-Fm		-3*M[9]	))
		-0.000367						*sin(deg2rad(	MM[3]	+Fm		+2*Dm	-M[9]))*em
		-0.000353						*sin(deg2rad(	MM[3]	+Fm		+2*Dm	))*em
		+0.000331						*sin(deg2rad(	Fm		+4*Dm			))
		+0.000317						*sin(deg2rad(	2*Dm	+Fm		-MM[3]	+M[9]))*em
		+0.000306						*sin(deg2rad(	2*Dm	-2*MM[3]-Fm		))*e2
		-0.000283						*sin(deg2rad(	M[9]	+3*Fm			))
        )

	ohm1=0.0004664				*cos(deg2rad(	OHM[9]					));
	ohm2=0.0000754				*cos(deg2rad(	OHM[9]	+275.05	-2.30*T	));

	name['Moon']	=MOD(L[9],360)*3600;
	name['MoonDecli']=MOD(Bm*(1-ohm1-ohm2),360)*3600;

	name["Moon_Node"]	=MOD(OHM[9],360)*3600;

	#PLUTO
#	 Pp,Sp,Jp,bp;
	Jp=238.74+3034.9057*T;
	Sp=267.26+1222.1138*T;
	Pp=93.48+144.9600*T;

	L[10]=93.297471+144.9600*T+(
		-19977972	*sin(deg2rad(Pp))		-738	*sin(deg2rad(Sp+3*Pp))	+394	*sin(deg2rad(Jp+Pp))
		+19667536	*cos(deg2rad(Pp))		+3443	*cos(deg2rad(Sp+3*Pp))	-55		*cos(deg2rad(Jp+Pp))
		+987114		*sin(deg2rad(Pp*2))		+1234	*sin(deg2rad(2*Sp-2*Pp))	+119	*sin(deg2rad(Jp+2*Pp))
		-4939350	*cos(deg2rad(Pp*2))		+472	*cos(deg2rad(2*Sp-2*Pp))	-264	*cos(deg2rad(Jp+2*Pp))
		+577978		*sin(deg2rad(Pp*3))		+1101	*sin(deg2rad(2*Sp-Pp))	-46		*sin(deg2rad(Jp+3*Pp))
		+1226898	*cos(deg2rad(Pp*3))		-894	*cos(deg2rad(2*Sp-Pp))	-156	*cos(deg2rad(Jp+3*Pp))
		-334695		*sin(deg2rad(Pp*4))		+625	*sin(deg2rad(2*Sp))		-77		*sin(deg2rad(Jp+4*Pp))
		-201966		*cos(deg2rad(Pp*4))		-1214	*cos(deg2rad(2*Sp))		-33		*cos(deg2rad(Jp+4*Pp))
		+130519		*sin(deg2rad(Pp*5))		+2485	*sin(deg2rad(Jp-Sp))		-34		*sin(deg2rad(Jp+Sp-3*Pp))
		-29025		*cos(deg2rad(Pp*5))		-486	*cos(deg2rad(Jp-Sp))		-26		*cos(deg2rad(Jp+Sp-3*Pp))
		-39851		*sin(deg2rad(Pp*6))		+852	*sin(deg2rad(Jp-Sp+Pp))	-43		*sin(deg2rad(Jp+Sp-2*Pp))
		+28968		*cos(deg2rad(Pp*6))		-1407	*cos(deg2rad(Jp-Sp+Pp))	-15		*sin(deg2rad(Jp+Sp-Pp))
		+20387		*sin(deg2rad(Sp-Pp))		-948	*sin(deg2rad(Jp-3*Pp))	+21		*cos(deg2rad(Jp+Sp-Pp))
		-9832		*cos(deg2rad(Sp-Pp))		+1073	*cos(deg2rad(Jp-3*Pp))	+10		*sin(deg2rad(2*Jp-3*Pp))
		-3986		*sin(deg2rad(Sp))		-2309	*sin(deg2rad(Jp-2*Pp))	+22		*cos(deg2rad(2*Jp-3*Pp))
		-4954		*cos(deg2rad(Sp))		-1204	*cos(deg2rad(Jp-2*Pp))	-57		*sin(deg2rad(2*Jp-2*Pp))
		-5817		*sin(deg2rad(Sp+Pp))		+7047	*sin(deg2rad(Jp-Pp))		-32		*cos(deg2rad(2*Jp-2*Pp))
		-3365		*cos(deg2rad(Sp+Pp))		+770	*cos(deg2rad(Jp-Pp))		+158	*sin(deg2rad(2*Jp-Pp))
		-3903		*sin(deg2rad(Sp+Pp*2))	+1184	*sin(deg2rad(Jp))		-43		*cos(deg2rad(2*Jp-Pp))
		+2895		*cos(deg2rad(Sp+Pp*2))	-344	*cos(deg2rad(Jp))
		)/1000000;

	bp=-3.909434+(
		-5323113	*sin(deg2rad(Pp))		+312	*sin(deg2rad(Sp))		-177	*sin(deg2rad(Jp-Sp))
		-15024245	*cos(deg2rad(Pp))		-128	*cos(deg2rad(Sp))		+259	*cos(deg2rad(Jp-Sp))
		+3497557	*sin(deg2rad(Pp*2))		+2057	*sin(deg2rad(Sp+Pp))		+15		*sin(deg2rad(Jp-Sp+Pp))
		+1735457	*cos(deg2rad(Pp*2))		-904	*cos(deg2rad(Sp+Pp))		+235	*cos(deg2rad(Jp-Sp+Pp))
		-1059559	*sin(deg2rad(Pp*3))		+19		*sin(deg2rad(Sp+2*Pp))	+578	*sin(deg2rad(Jp-3*Pp))
		+299464		*cos(deg2rad(Pp*3))		-674	*cos(deg2rad(Sp+2*Pp))	-293	*cos(deg2rad(Jp-3*Pp))
		+189102		*sin(deg2rad(Pp*4))		-307	*sin(deg2rad(Sp+3*Pp))	-294	*sin(deg2rad(Jp-2*Pp))
		-285383		*cos(deg2rad(Pp*4))		-576	*cos(deg2rad(Sp+3*Pp))	+694	*cos(deg2rad(Jp-2*Pp))
		+14231		*sin(deg2rad(Pp*5))		-65		*sin(deg2rad(2*Sp-2*Pp))	+156	*sin(deg2rad(Jp-Pp))
		+101218		*cos(deg2rad(Pp*5))		+39		*cos(deg2rad(2*Sp-2*Pp))	+201	*cos(deg2rad(Jp-Pp))
		-29164		*sin(deg2rad(Pp*6))		-97		*sin(deg2rad(2*Sp-Pp))	+294	*sin(deg2rad(Jp))
		-27461		*cos(deg2rad(Pp*6))		+208	*cos(deg2rad(2*Sp-Pp))	+829	*cos(deg2rad(Jp))
		+4935		*sin(deg2rad(Sp-Pp))		-160	*cos(deg2rad(2*Sp))		-123	*sin(deg2rad(Jp+Pp))
		+11282		*cos(deg2rad(Sp-Pp))								-31		*cos(deg2rad(Jp+Pp))
		)/1000000;

	r[10]=40.724725+(
		+6623876	*sin(deg2rad(Pp))		-3		*sin(deg2rad(Sp+2*Pp))	-4		*sin(deg2rad(Jp-Pp))
		+6955990	*cos(deg2rad(Pp))		+79		*cos(deg2rad(Sp+2*Pp))	+4564	*cos(deg2rad(Jp-Pp))
		-1181808	*sin(deg2rad(2*Pp))		+50		*sin(deg2rad(Sp+3*Pp))	+852	*sin(deg2rad(Jp))
		-54836		*cos(deg2rad(2*Pp))		+54		*cos(deg2rad(Sp+3*Pp))	+855	*cos(deg2rad(Jp))
		+163227		*sin(deg2rad(3*Pp))		-1		*sin(deg2rad(2*Sp-2*Pp))	-88		*sin(deg2rad(Jp+Pp))
		-139603		*cos(deg2rad(3*Pp))		-22		*cos(deg2rad(2*Sp-2*Pp))	-82		*cos(deg2rad(Jp+Pp))
		-3644		*sin(deg2rad(4*Pp))		+84		*sin(deg2rad(2*Sp-Pp))	+21		*sin(deg2rad(Jp+2*Pp))
		+48144		*cos(deg2rad(4*Pp))		-48		*cos(deg2rad(2*Sp-Pp))	-12		*cos(deg2rad(Jp+2*Pp))
		-6268		*sin(deg2rad(5*Pp))		-30		*sin(deg2rad(2*Sp))		-14		*sin(deg2rad(Jp+3*Pp))
		-8851		*cos(deg2rad(5*Pp))		+61		*cos(deg2rad(2*Sp))		+6		*cos(deg2rad(Jp+3*Pp))
		+3111		*sin(deg2rad(6*Pp))		+26		*sin(deg2rad(Jp-Sp))		-6		*sin(deg2rad(2*Jp-3*Pp))
		-408		*cos(deg2rad(6*Pp))		-39		*cos(deg2rad(Jp-Sp))		+1		*cos(deg2rad(2*Jp-3*Pp))
		-621		*sin(deg2rad(Sp-Pp))		-19		*sin(deg2rad(Jp-Sp+Pp))	+13		*sin(deg2rad(2*Jp-2*Pp))
		+2223		*cos(deg2rad(Sp-Pp))		-40		*cos(deg2rad(Jp-Sp+Pp))	-23		*cos(deg2rad(2*Jp-2*Pp))
		+438		*sin(deg2rad(Sp))		-321	*sin(deg2rad(Jp-3*Pp))	+25		*sin(deg2rad(2*Jp-Pp))
		+450		*cos(deg2rad(Sp))		+42		*cos(deg2rad(Jp-3*Pp))	+107	*cos(deg2rad(2*Jp-Pp))
		-153		*sin(deg2rad(Sp+Pp))		+797	*sin(deg2rad(Jp-2*Pp))	+25		*sin(deg2rad(2*Jp))
		+61			*cos(deg2rad(Sp+Pp))		-792	*cos(deg2rad(Jp-2*Pp))	+16		*cos(deg2rad(2*Jp))
		)*0.000001;

	L[10]=MOD(L[3]+ATANP(r[10]*cos(deg2rad(bp))*sin(deg2rad(L[10]-L[3])),r[10]*cos(deg2rad(bp))*cos(deg2rad(L[10]-L[3]))+r[3]),360);
	name['Pluto']	=MOD(L[10],360)*3600;

	sdtm=MOD((T+0.5)*36525,1)*360;
	sdtm+=MOD(TYL(6.6460656,2400.051262,0.00002581,0,T),24)*360/24;
	sdtm+=name["longitude"]/3600.0;
#	echo name["Longitude"]/3600 ."===============".name["Longitude"]."<br>"; 
	name["Siderael Time"]=sdtm*240;
#	Bhava(name,T,((double )LATITUDE)/3600,sdtm);

"""
COleDateTime CompSdtm(COleDateTime Time,double sdtm);

COleDateTime CCalculator::SunRiseSet(COleDateTime Time,int LATITUDE,int LONGITUDE,int RiseSet)

	CEphe Sphuta[30];
	COleDateTime BaseDt;
	COleDateTime BT=Time,PT;
	PT.m_status=COleDateTime::null;
	BaseDt.SetDateTime(1899,12,31,12,0,0);
	double lt=LATITUDE,lg=LONGITUDE;lt=lt/3600;lg=lg/3600;
	for(;PT!=Time;)
	
		PT=Time;
		Graha1(Time,Sphuta,LATITUDE,LONGITUDE);
		double th=((double)Sphuta["Sun"].Ephe)/3600;
		double T=(Time-BaseDt)/36525;
		double alp=ATANP(COS(anati)*sin(deg2rad(th),COS(th));
		double dlt=ASIN(SIN(anati)*SIN(th));
		double cH=(-0.01454-SIN(lt)*SIN(dlt))/(COS(lt)*COS(dlt));
		cH=cH>1?1:(cH<-1?-1:cH);
		double H=(RiseSet==0)?-ACOS(cH):ACOS(cH);
		double sdtm=MOD(H+alp-lg,360);
		if(RiseSet!=0)
			Time.m_dt=SunRiseSet(BT,LATITUDE,LONGITUDE).m_dt+1;
		else
			Time=BT;
		Time=CompSdtm(Time,sdtm);
	
	return Time;


COleDateTime CompSdtm(COleDateTime Time,double sdtm)

	COleDateTime BaseDt;
	BaseDt.SetDateTime(1899,12,31,12,0,0);
	double T1,T2,T,s1,s2;
	T1=(Time-BaseDt)/36525;
	T1=T1-1.0/36525;
	T2=(Time-BaseDt)/36525;
	T=T1;
	s1=MOD((T+0.5)*36525,1)*360;
	s1+=MOD(TYL(6.6460656,2400.051262,0.00002581,0),24)*360/24;
	T=T2;
	s2=MOD((T+0.5)*36525,1)*360;
	s2+=MOD(TYL(6.6460656,2400.051262,0.00002581,0),24)*360/24;
	s1=MOD(s1,360);s2=MOD(s2,360)+360;
	sdtm+=360;
	if(sdtm>s2)sdtm-=360;
	T=T1+((sdtm-s1)*(T2-T1)/(s2-s1));
	BaseDt+=T*36525;
	return BaseDt;



int CCalculator::GetGeoCen(int GePh,int H)

	double f=0.99664719;
	double Gph=((double)GePh)/3600;
	double u=ATANP(f*TAN(Gph),1);
	double h=((double)H)/6378140;
	double r=ATANP(f*sin(deg2rad(u)+sin(deg2rad(Gph)*h,COS(u)+COS(Gph)*h);
	int R=r*3600;
	return R;


int CCalculator::GetGeoGph(int GeCn,int H)

	int X=ABS(GeCn);
	int R,MID;
	int Up=90*3600;
	int Dw=0;
	while(1)
	
		MID=(Up+Dw)/2;
		R=GetGeoCen(MID,H);
		if(ABS(X-R)<2)return SGN(X)*MID;
		if(X>R)Dw=MID;
		else Up=MID;
	


COleDateTime CCalculator::GetTime(int Planet, CEphe Pos, COleDateTime Time,BOOL FUTURE, BOOL NIRAYANA)

	CEphe Sphuta[30];
	Graha1(Time,Sphuta,0,0);
	int d=Sphuta[Planet].Ephe-Pos.Ephe;
	return Time;

"""
"""
require("../Common/loadkendra.php");
kendra=array();
loadkendra('kendra');
echo Graha1("kendra");
echo (1/3-0.333333333333333)*1000000000,"<br>";
echo (int)(1.3333);
"""
