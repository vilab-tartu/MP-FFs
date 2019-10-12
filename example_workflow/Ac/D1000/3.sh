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
cp ./template/An.mdp "$package"_"$ratio"
cd "$package"_"$ratio"

sed -i "s/SED_name_SED/3"$ratio$package"/g" ./3.run

sbatch 3.run

cd ..
done
done
