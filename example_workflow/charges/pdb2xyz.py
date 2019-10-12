import glob
pdbs=glob.glob('./*.pdb')

for i in pdbs:
  counter=0
  gmxjama=0

  output=''
  with open(i,"r") as fin:
    with open(i[:-4]+".xyz","w") as fout:
      for line in fin:
        gmxhalb=0
        if line.split()[0]!="ATOM":
          pass
        else:
          counter+=1
          for k in range(6,12):
            if line.split()[k]=="1.00" and line.split()[k+1]=="0.00":
              gmxjama=k
              break
          if line.split()[2][0] in ["1","2","3","4","5","6","7","8","9","0"]:
            gmxhalb=1
          output+=("%s  %s  %s  %s\n"%(line.split()[2][0+gmxhalb],line.split()[gmxjama-3],line.split()[gmxjama-2],line.split()[gmxjama-1]))
      output=str(counter)+"\n\n"+output
      fout.write(output)
