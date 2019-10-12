# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:45:16 2017

@author: KARL
"""
mol_ty=["PDA","NDA"]



pos=""
neg=""
counter=0
coutner=0
chk=open("STEEP.gro","r").readlines()
natoms=int(chk[-2].split()[2])
natom=natoms/(int(21)+int(7))
   
with open("Cat.gro","r") as input:
  with open("rel_inp.gro","w") as output: 
    for line in input:
      if " "+str(natoms+2*natom)+"\n" in line:
        output.write(" "+str(natoms)+"\n")
      elif "NDA" not in line and "PDA" not in line:
        output.write(line)
