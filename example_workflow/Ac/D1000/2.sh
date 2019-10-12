cation="Ch"
anion="Ac"
cation_len="21"
anion_len="7"
density="1.0"
mw="163.21"


for ratio in 322 332 333 432 
do
for package in CsCl NaCl
do
cd "$package"_"$ratio"
python wells_"$package".py
na=$(head -n4 temp_"$package".tmp | tail -n1)
natom_b=$((($cation_len+$anion_len)*$na+3))
natom_e=$(($natom_b+2))
sed -i ""$natom_b","$natom_e"d" cluster.gro

echo q | gmx make_ndx -f cluster.gro -o index.ndx

gmx grompp -f NVT.mdp -c cluster.gro -n index.ndx -p topol.top -o NVT -maxwarn 9 

sed -i "s/SED_name_SED/2"$ratio$package"/g" ./2.run

sbatch 2.run

cd ..
done
done
