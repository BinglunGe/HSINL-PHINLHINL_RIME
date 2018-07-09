#import os;
#z=os.getcwd();
z=r"F:\PYTHON\RIMEC\\";
f=open("%sD"%z).read().decode("u8").split("\n");
z="%sE"%z;
l=len(f);
m=0;
s=[];
def r(h,k):
    for o in k:
        h=h.replace(o[0],o[1]);
    return h;
def e(g):
    #return r(g,[(str(p+1),["l","z","j","x","q"][p]) for p in range(5)]);
    g=" %s"%g;
    g=r(g,[("iu","iou"),("ju","jv"),("qu","qv"),("xu","xv"),("ong","ung"),]);
    g=r(g,[("zh","ZH"),("ch","CH"),("sh","SH"),]);
    g=r(g,[("h","X"),("j","HZ"),("q","HC"),("x","HS"),("b","P"),("p","PH"),("d","T"),("t","TH"),("ng","NG"),("g","K"),("k","KH"),]);
    g=r(g,[("iNG","ING"),("in","IN"),("un","UN"),("uo","O"),("iu","yu"),]);
    g=r(g,[("yu","v"),("y","i"),("w","u"),]);
    g=r(g,[(" a"," HA"),(" o"," HO"),(" e"," HE"),(" i"," Hi"),(" u"," HU"),(" v"," Hv"),]);
    g=r(g,[("ao","au"),("ie","ieh"),("je","jeh"),("ue","veh"),("ve","veh"),]);
    g=g.lower();
    g=r(g,[("iung","vung"),(" zhi"," zhrr"),(" chi"," chrr"),(" shi"," shrr"),(" zi"," zr"),(" ci"," cr"),(" si"," sr"),(" ri"," hrr"),("ui","uei"),]);
    g=r(g,[("v","iui"),("iuing","iuiung")]);
    g=r(g,[("ii","i"),("uu","u"),]);
    g=r(g,[(str(p+1),["l","z","j","x","q"][p]) for p in range(5)]);
    return g[1:];
    
def c(a):
    b=a.split("\t");
    if len(b)<3:#?^.?^.1^,dd%^,
        d="";
    else:
        d="\t%s"%b[2];
    b[1]=e(b[1]);
    return "%s\t%s%s"%(b[0],b[1],d);#S\N1\\TS\N1?^.?^.?^.1^,dd%^,^,
for i in f:
    if not i:
        s.append("");
        m+=1;
    elif i[0]=="#" or not i.count("\t"):
        s.append(i);
        m+=1;
    else:
        s.append(c(i));
        m+=1;
    print ("%d/%d"%(m,l));
z=r"E:\Rime\weasel-0.11.1\data\e.dict.yaml"
open(z,"w").write(("\n".join(s)).encode("u8"));
print (">")