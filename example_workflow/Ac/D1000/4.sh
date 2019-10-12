cation="Ch"
anion="Ac"
cation_len="21"
anion_len="7"
density="1.0"
mw="163.21"

source /gpfs/hpchome/karlkaru/.bashrc

for ratio in 322 332 333 432 
do
for package in CsCl NaCl
do
cd "$package"_"$ratio"
rm *xtc
cle
sed -i "s/SED_anionlen_SED/"$anion_len"/g" ./unwells.py
sed -i "s/SED_cationlen_SED/"$cation_len"/g" ./unwells.py
sed -i "s/SED_name_SED/4"$ratio$package"/g" ./4.run
python unwells.py
gmx grompp -f melt.mdp -c rel_inp.gro -n STEEP.ndx -p STEEP.top -o melt -maxwarn 9
sbatch 4.run


cd ..
done
done
