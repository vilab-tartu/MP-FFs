import os.path
def cat_atchges_hirsh(f,anion_len,cation_len,ioncount):
  chglist=[[],[],[]]
  for i in range(cation_len):
    chglist[0].append([])
  for j in range(ioncount):
    for k,atom in enumerate(f[anion_len*ioncount+cation_len*j:anion_len*ioncount+cation_len*(j+1)]):
      chglist[0][k].append(float(atom.strip()))
  return chglist

def cat_dists(f,anion_len,cation_len,ioncount):
  distlist=[]
  coordlist=[[],[],[]]
  for i, line in enumerate(f):
    if "Cart. coordinates" in line:
      for j in range(anion_len*ioncount+i+1,anion_len*ioncount+i+1+cation_len*ioncount):
        coordlist[0].append(float(f[j].split()[-3]))
        coordlist[1].append(float(f[j].split()[-2]))
        coordlist[2].append(float(f[j].split()[-1]))
      break
  cent_x=(max(coordlist[0])-min(coordlist[0]))*0.5
  cent_y=(max(coordlist[1])-min(coordlist[1]))*0.5
  cent_z=(max(coordlist[2])-min(coordlist[2]))*0.5
  for i in range(ioncount):
    ion_x=(sum(coordlist[0][i*cation_len:(i+1)*cation_len]))/float(cation_len)
    ion_y=(sum(coordlist[1][i*cation_len:(i+1)*cation_len]))/float(cation_len)
    ion_z=(sum(coordlist[2][i*cation_len:(i+1)*cation_len]))/float(cation_len)
    distlist.append(((ion_x-cent_x)**2.+(ion_y-cent_y)**2.+(ion_z-cent_z)**2.)**0.5*0.529177) #the last value is to get A from Bohr   
  return distlist
  
def atchges_hirsh(f,anion_len,ioncount):
  chglist=[[],[],[]]
  for i in range(anion_len):
    chglist[0].append([])
  for j in range(ioncount):
    for k,atom in enumerate(f[anion_len*j:anion_len*(j+1)]):
      chglist[0][k].append(float(atom.strip()))
  return chglist

def dists(f,anion_len,ioncount):
  distlist=[]
  coordlist=[[],[],[]]
  for i, line in enumerate(f):
    if "Cart. coordinates" in line:
      for j in range(i+1,i+1+anion_len*ioncount):
        coordlist[0].append(float(f[j].split()[-3]))
        coordlist[1].append(float(f[j].split()[-2]))
        coordlist[2].append(float(f[j].split()[-1]))
      break
  cent_x=(max(coordlist[0])-min(coordlist[0]))*0.5
  cent_y=(max(coordlist[1])-min(coordlist[1]))*0.5
  cent_z=(max(coordlist[2])-min(coordlist[2]))*0.5
  for i in range(ioncount):
    ion_x=(sum(coordlist[0][i*anion_len:(i+1)*anion_len]))/float(anion_len)
    ion_y=(sum(coordlist[1][i*anion_len:(i+1)*anion_len]))/float(anion_len)
    ion_z=(sum(coordlist[2][i*anion_len:(i+1)*anion_len]))/float(anion_len)
    distlist.append(((ion_x-cent_x)**2.+(ion_y-cent_y)**2.+(ion_z-cent_z)**2.)**0.5*0.529177) #the last value is to get A from Bohr   
  return distlist

for anion in ["Ac"]: #cit glt Ibu
  print(anion)
  chgdict={}
  cat_chgdict={}
  timesfirst=["CsCl_322","CsCl_332","CsCl_333","CsCl_432","NaCl_322","NaCl_332","NaCl_333","NaCl_432"]
  times=[]
  for time in timesfirst:
    if os.path.isfile("%s/%s_%s.out"%(anion,anion,time)) and "wall time for all" in open("%s/%s_%s.out"%(anion,anion,time)).readlines()[-1]:
      times.append(time)
  for k in times: #do it wtih all snapshots
    ioncount=int(1/2*int(open(anion+"_"+k+".pdb").readlines()[-4].split()[4]))
    print(ioncount)
    cation_len=21
    atomcount=int(open(anion+"/"+anion+"_"+k+".xyz").readlines()[0].split()[0])
    anion_len=int(((atomcount-ioncount*cation_len)/ioncount))
    f=open("%s/%s_%s.out"%(anion,anion,k)).readlines() #
    f2=open("%s/charges_%s_%s"%(anion,anion,k)).readlines() #
    chglist=atchges_hirsh(f2,anion_len,ioncount)
    distlist=dists(f,anion_len,ioncount)
    cat_chglist=cat_atchges_hirsh(f2,anion_len,cation_len,ioncount)
    cat_distlist=cat_dists(f,anion_len,cation_len,ioncount)
  
    chgdict[k]=[]
    for j,atom in enumerate(chglist[0]): 
      tempchg=0.0
      counter=0
      for i in range(ioncount):
        if distlist[i]<12:
          counter+=1
          tempchg+=atom[i]
      chgdict[k].append(round(tempchg/float(counter),4))

    cat_chgdict[k]=[]
    for j,atom in enumerate(cat_chglist[0]): 
      tempchg=0.0
      counter=0
      for i in range(ioncount):
        if cat_distlist[i]<12:
          counter+=1
          tempchg+=atom[i]
      cat_chgdict[k].append(round(tempchg/float(counter),4))


  for k in times:
    checksum=0.0  #offset from 0 total charge
    checksum+=sum(chgdict[k])
    checksum+=sum(cat_chgdict[k]) 
    corrector=round(-1*checksum/float(anion_len+cation_len),4)
    for i in range(anion_len):
      chgdict[k][i]=round(chgdict[k][i]+corrector,4)
    for j in range(cation_len):
      cat_chgdict[k][j]=round(cat_chgdict[k][j]+corrector,4)

  summ=0.0 #checking for errors
  for k in times:
    summ+=sum(chgdict[k])
    summ+=sum(cat_chgdict[k])
  print(summ/4.)
  outfile=open("../Ch_"+anion,'w')
  outfile.write("ANION\n") #PRINT INTO Cat_An
  for i in range(anion_len):
    tempchg=0.0
    counter=0 
    for k in times:
      tempchg+=chgdict[k][i]
      counter+=1
    outfile.write("%.4f\n"%(tempchg/counter))

  outfile.write("CATION\n")
  for i in range(cation_len):
    tempchg=0.0
    counter=0 
    for k in times:
      tempchg+=cat_chgdict[k][i]
      counter+=1
    outfile.write("%.4f"%(tempchg/counter))
    if i<cation_len-1:
      outfile.write("\n")
  outfile.close()
