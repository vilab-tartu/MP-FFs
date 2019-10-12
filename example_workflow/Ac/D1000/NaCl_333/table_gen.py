Eslope=SED_intstr_SED
const_r=0.0
linear_r=1.3
x1="Ac"
x2="PDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  #out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
  if step<const_r:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope,Eslope,0.0,0.0,0.0,0.0))
  elif step<(linear_r+const_r):
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope*(1-(step-const_r)/linear_r),Eslope*(1-(step-const_r)/linear_r),0.0,0.0,0.0,0.0))
  else:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))

out.close()
x1="Ch"
x2="NDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  #out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
  if step<const_r:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope,Eslope,0.0,0.0,0.0,0.0))
  elif step<(linear_r+const_r):
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope*(1-(step-const_r)/linear_r),Eslope*(1-(step-const_r)/linear_r),0.0,0.0,0.0,0.0))
  else:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))

out.close()
x1="Ch"
x2="PDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  #out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
  if step<const_r:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope,Eslope,0.0,0.0,0.0,0.0))
  elif step<(linear_r+const_r):
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope*(1-(step-const_r)/linear_r),Eslope*(1-(step-const_r)/linear_r),0.0,0.0,0.0,0.0))
  else:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()
x1="Ac"
x2="NDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  #out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
  if step<const_r:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope,Eslope,0.0,0.0,0.0,0.0))
  elif step<(linear_r+const_r):
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,Eslope*(1-(step-const_r)/linear_r),Eslope*(1-(step-const_r)/linear_r),0.0,0.0,0.0,0.0))
  else:
    out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()
x1="NDA"
x2="PDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()
x1="NDA"
x2="NDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()
x1="PDA"
x2="PDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()

x1="PDA"
x2="NDA"
out=open("table_"+x1+"_"+x2+".xvg","w")

out.write("#\n# Table for "+x1+" and "+x2+", ndisp=6 nrep=12\n#\n")

for i in range(0,2251,1):
  step=float(i)/500
  out.write("%.10e   %.10e %.10e   %.10e %.10e   %.10e %.10e\n" % (step,0.0,0.0,0.0,0.0,0.0,0.0))
out.close()
