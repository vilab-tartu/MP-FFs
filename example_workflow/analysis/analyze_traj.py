import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
plt.rcParams['svg.fonttype'] = 'none'
plt.rcParams.update({'font.size': 14})
import sys, os
import glob
import shutil
matplotlib.rc('font',**{'family':'sans-serif','sans-serif':['arial']})
matplotlib.rc("text", usetex=True)

matplotlib.rcParams['text.latex.unicode']=True


root_dir="./../"

def running_mean(x,a=5):
  avg=[]
  for n in range(a):
    avg.append(0)
  x=x+avg
  res=[]
  for element in (x):  
    avg=avg[1:]+[element]    
    res.append(sum(avg)/len(avg))
  return res

def get_density(anion):
  anions=glob.glob(root_dir+"/%s/*" % anion) 
  result=[]
  for i in anions:
    if i.split("/")[-1][0]=="D":
      result.append(i.split("/")[-1])
  return result

expmelts={"BMIPF":282.,"BMITFM":285.,"PYRTFS":259.,"EMIBF":287.,"EMITFS":260.,"BPYTFS":299.,"BPYBF":280.,"Ac":345.0,"Ace":298.0,"Ben":320.0,"Cit":345.0,"Glt":312.0,"Ibu":342.0,"Iso":341.0,"Iva":334.0,"Mbu":363.0,"Sac":342.0,"Sal":323.0,"TFSI":306.0}

#List of anions ["Ac","Ace","Acs","Ben","Cit","Glt","Ibu","Iso","Iva","Lac","Mbu","Mal","Sac","Sal","TFSI"]:
for anion in ["Ac"]:
  temps=[]
  smth=[]
  for ratio in ["332", "333"]: #["322", "332", "333", "432"]
    for package in ["CsCl","NaCl"]:
      for density in get_density(anion): #may also write a list manually, e.g. ["D1000"]
        try:
          datadir="./%s_%s"%(anion,density)
          if not os.path.exists(datadir):
            os.makedirs(datadir)
          datadir2="./%s_%s/%s_%s"%(anion,density,package,ratio)
          if not os.path.exists(datadir2):
            os.makedirs(datadir2)
          tar=(root_dir+"/%s/%s/%s_%s"%(anion,density,package,ratio))
          for line in open(tar+"/melt.log"):
            if "annealing-time" in line:
              start_time=int(float(line.split()[3]))
              end_time=int(float(line.split()[4]))
            elif "annealing-temp" in line:
              start_temp=int(float(line.split()[3]))
              end_temp=int(float(line.split()[4]))
              break
          # THE FOLLOWING LINE NEEDS TO BE RUN THE FIRST TIME TO MAKE DATA FILES FROM .XTC. COMMENT OUT IF DATA FILES EXIST ALREADY.
          #os.system("sh msd.sh %s %s %s %s"%(start_time,end_time,tar,datadir2))  
          xs=[]
          ys=[]
          datadir2="./%s_%s/%s_%s"%(anion,density,package,ratio)
          slopes=[]
          intercepts=[]
          bestslope2=0
          bestcept2=0
          bestslope=0
          bestcept=0
          bestr=0
          counter=0
          counter2=0
          solidr=0
          liquidr=0

          for i in range(start_time,end_time-10,10):
            if os.path.isfile(datadir2+"/z_"+str(i)+".xvg"):
              plot=open(datadir2+"/z_"+str(i)+".xvg").readlines()
              if len(plot)>20:
                xs.append((-1/float((end_temp-start_temp)*(i-start_time)/(end_time-start_time)+start_temp)))
                ys.append(np.log(float(plot[18].split()[4])))

            
          for i,x in enumerate(xs):
             if i > 20 and i<(len(xs)-20):
              slope, intercept, r_value, p_value, std_err = stats.linregress(xs[:i],ys[:i]) 
              for ii,xx in enumerate(xs[i:i+1]):
                if True:
                  slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(xs[(i+ii):],ys[(i+ii):]) 
                  if 1*r_value*r_value+r_value2*r_value2 > bestr and ((slope/slope2)**2>(4./2.)**2 or (slope/slope2)**2<(1./2.)**2):
                    bestr=1*r_value*r_value+r_value2*r_value2
                    bestslope=slope
                    bestcept=intercept
                    bestcept2=intercept2
                    bestslope2=slope2
                    counter=i
                    counter2=(i+ii)
                    solidr=r_value*r_value
                    liquidr=r_value2*r_value2

          if solidr>0.7 and liquidr>0.9:
            first=-1/(1.0*(xs[counter]))  
            temps.append((first))
            smth.append(density+"_"+package+"_"+ratio)
          # Plotting starts here
          fig = plt.figure()
          ax = fig.add_subplot(111)
          ax.ticklabel_format(axis="both",style="sci",scilimits=(0,0),which="major",length=20)
          ax.ticklabel_format(axis="both",style="sci",scilimits=(0,0),which="minor",length=0.1)
          ax.set_xlabel(r'$-T^{-1} / \mathrm{K}^{-1}')
          ax.set_ylabel(r"$\ln (D / \mathrm{cm}^2\cdot \mathrm{s}^{–1})$")
          ax.minorticks_on()
          ticktemps=[175,200,225,250,275,300,325,350,375,400,425,450,475]
          ticktemps_str=[]
          tickxs=[-1/x for x in ticktemps]          
          for tix in ticktemps:
            ticktemps_str.append(r'$\frac{\displaystyle-1}{\displaystyle%d}$'%tix)
          plt.xlim([-1/175.,-1/475.])
          ax.xaxis.set_minor_locator(matplotlib.ticker.FixedLocator(tickxs))
          tickxs=[-1/x for x in ticktemps]
          for rem in [0,2,4,6,8,10,12][::-1]:
            del ticktemps_str[rem]
            del tickxs[rem]
          plt.xticks(tickxs,ticktemps_str)
          plt.plot(xs,ys,linewidth=0,marker="x", color="dimgrey")
          
          abline_values = [bestslope * i + bestcept for i in xs[:counter]]
          plt.plot(xs[:counter],abline_values, color="red",linewidth=4)

          abline_values = [bestslope2 * i + bestcept2 for i in xs[counter2:]]
          plt.plot(xs[counter2:],abline_values, color="#00ff00ff",linewidth=4)
          plt.tight_layout()

          if anion in expmelts:
            plt.axvline(x=-1/expmelts[anion],color='k', linestyle='--')
            plt.text(-1/expmelts[anion]-0.00066,(max(ys)-min(ys))/28.*23+min(ys), r"$\mathrm{exp.}\,%.0f\,\mathrm{K}_{\phantom{d}}$"%(expmelts[anion]),fontsize=14)
          plt.text((max(xs)-min(xs))/8.+min(xs),(max(ys)-min(ys))/7.*6+min(ys), r"$R^2_{\mathrm{solid\phantom{j}}}=%3.2f$"%(solidr),fontsize=14, bbox=dict(facecolor='red', alpha=0.5))
          plt.text((max(xs)-min(xs))/8.+min(xs),(max(ys)-min(ys))/4.*3+min(ys), r"$R^2_{\mathrm{liquid}}=%3.2f$"%(liquidr),fontsize=14, bbox=dict(facecolor="#00ff00ff", alpha=0.5))
          plt.savefig("./lntemp/%s_%s_%s_%s.pdf"%(anion,density,package,ratio))

          plt.close() 

        except: 
          pass
  try:
    with open("ln1p", "a") as myfile:
      myfile.write(anion+" "+str(max(temps))+" "+str(sum(temps)/len(temps))+"\n")
    with open("ln1psys", "a") as myfile:
      myfile.write(anion+"_"+smth[temps.index(max(temps))]+"\n")
    print(anion+" "+str(max(temps))+" "+str(sum(temps)/len(temps))) #max and avg 
    shutil.copy2("./lntemp/"+anion+"_"+smth[temps.index(max(temps))]+".pdf","./lnpub")
  except:
    print(anion)
