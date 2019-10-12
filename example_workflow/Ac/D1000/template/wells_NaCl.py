# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:03:11 2017

@author: KARL
"""
import os.path
import subprocess

#Data read in with prepare.sh
pairname="SED_cation_SEDSED_anion_SED"
cation_len=SED_cation_len_SED
anion_len=SED_anion_len_SED
mol_ty=["PDA","NDA"]
density=float(SED_density_SED)
ratio="SED_ratio_SED"
mw=float(SED_mw_SED)

#Calculating lattice parameters
vector=((0.5*mw/6.022e+23)/(int(ratio[0])*int(ratio[1])*int(ratio[2])*1e-21*density))**(1.0/3.0)
dx=vector*int(ratio[0]) 
dy=vector*int(ratio[1]) 
dz=vector*int(ratio[2])

#Replication factors
x_len=int(1+2.8//dx) 
y_len=int(1+2.8//dy)
z_len=int(1+2.8//dz)

if (x_len*y_len*z_len)%2==1:
  x_len=x_len+1

natom=int(0.5*x_len*y_len*z_len)
natoms=(cation_len+anion_len)*natom
NDAbuffer=""
#Appending well locations to buffer string    
buffer="Atomistic model of "+pairname+"\n "+str(x_len*y_len*z_len*2)+"\n"
counter=0
for x in range(x_len):
  for y in range(y_len):
    for z in range(z_len):
      counter+=1
      mol="PDA"
      xs=x*dx
      ys=y*dy
      zs=z*dz
      if (x%2+y%2+z%2)%2==1:
        mol="NDA"
        NDAbuffer=NDAbuffer+"  %3.i%s    %s %3.i   %.3f   %.3f   %.3f  0.0000  0.0000  0.0000\n"%(counter,mol,mol,counter,xs,ys,zs)
      else:
        buffer=buffer+"  %3.i%s    %s %3.i   %.3f   %.3f   %.3f  0.0000  0.0000  0.0000\n"%(counter,mol,mol,counter,xs,ys,zs)
buffer=buffer+NDAbuffer
buffer=buffer+"   %.5f   %.5f   %.5f\n"%(dx*x_len,dy*y_len,dz*z_len)

#Writing wells to gro or modifying packmol.inp

if os.path.isfile("./STEEP.gro"):
  with open("STEEP.gro","r") as input:
    with open("cluster.gro","w") as output: 
      for line in input:
        if " "+str(natoms)+"\n" not in line and "    %.4f" % (y_len*dy) not in line:
          output.write(line)
        elif " "+str(natoms)+"\n" in line:
          output.write("  "+str(natoms+2*natom)+"\n")
      output.write(buffer)
else:
  with open("temp_NaCl.tmp", "w") as output:
    output.write("%.4f\n" % (10*dx*x_len))
    output.write("%.4f\n" % (10*dy*y_len))
    output.write("%.4f\n" % (10*dz*z_len))
    output.write(str(natom))
