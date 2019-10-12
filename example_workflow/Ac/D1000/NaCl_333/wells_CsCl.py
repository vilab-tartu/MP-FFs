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
vector=((mw/6.022e+23)/(int(ratio[0])*int(ratio[1])*int(ratio[2])*1e-21*density))**(1.0/3.0)
dx=vector*int(ratio[0]) 
dy=vector*int(ratio[1]) 
dz=vector*int(ratio[2])

#Replication factors
x_len=int(1+2.8//dx) 
y_len=int(1+2.8//dy)
z_len=int(1+2.8//dz)
natom=x_len*y_len*z_len
natoms=(cation_len+anion_len)*natom

#Appending well locations to buffer string    
buffer="Atomistic model of "+pairname+"\n "+str(x_len*y_len*z_len*2)+"\n"
counter=0
for mol in mol_ty:
  for x in range(x_len):
    for y in range(y_len):
      for z in range(z_len):
        counter+=1
        xs=x*dx
        ys=y*dy
        zs=z*dz
        if mol=="NDA":
          xs=xs+dx*1/2
          ys=ys+dy*1/2   
          zs=zs+dz*1/2          
        buffer=buffer+"  %3.i%s    %s %3.i   %.3f   %.3f   %.3f \n"%(counter+2*natom,mol,mol,counter+natoms,xs,ys,zs)
buffer=buffer+"   %.5f   %.5f   %.5f\n"%(dx*x_len,dy*y_len,dz*z_len)

'''
an=0.175
dx=0.85*(0.6185+an) #smallest measure, in between carion-cation and anion-anion
dy=0.85*(0.6185+an) #change this for thicker anions
dz=0.85*(0.6185+an) #change this if lengthy anions
x_len=5 #replication factors
y_len=5
z_len=4
an_drift=1/2
al_drift=0

f=open("gen_NaCl.gro","w")
f.write("Atomistic model of "+pairname+"\n "+str(x_len*y_len*z_len*2)+"\n")
counter=0
for mol in mol_ty:
  for x in range(x_len):
    for y in range(y_len):
      for z in range(z_len):
        counter+=1
        xs=x*dx
        if (counter%2==0 and mol=="PDA") or ((counter-x*y*z)%2==1 and mol=="NDA"):
          xs=(x+0.5)*dx
        ys=y*dy
        zs=z*dz
        f.write("  %3.i%s    %s %3.i   %.3f   %.3f   %.3f  0.0000  0.0000  0.0000\n"%(counter,mol,mol,counter,xs,ys,zs))
f.write("   %.5f   %.5f   %.5f\n"%(dx*x_len,dy*y_len,dz*z_len))
f.close()'''

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
  with open("temp_CsCl.tmp", "w") as output:
    output.write("%.4f\n" % (10*dx*x_len))
    output.write("%.4f\n" % (10*dy*y_len))
    output.write("%.4f\n" % (10*dz*z_len))
    output.write(str(natom))
