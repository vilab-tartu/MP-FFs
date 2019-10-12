cation="Ch"
anion="TFSI"
cation_len="21"
anion_len="15"
density="1.4"
mw="384.31"

source /gpfs/hpchome/karlkaru/.bashrc

for ratio in 322 332 333 432
#for ratio in 322 332
do
for package in CsCl
#for package in CsCl NaCl
do
mkdir -p "$package"_"$ratio"
cp -r ./template/* ./"$package"_"$ratio"
cd ./"$package"_"$ratio"

sed -i "s/SED_cation_SED/$cation/g" packmol.inp
sed -i "s/SED_anion_SED/$anion/g" packmol.inp

sed -i "s/SED_cation_SED/$cation/g" wells_"$package".py
sed -i "s/SED_anion_SED/$anion/g" wells_"$package".py
sed -i "s/SED_cation_len_SED/$cation_len/g" wells_"$package".py
sed -i "s/SED_anion_len_SED/$anion_len/g" wells_"$package".py
sed -i "s/SED_density_SED/$density/g" wells_"$package".py
sed -i "s/SED_mw_SED/$mw/g" wells_"$package".py
sed -i "s/SED_ratio_SED/$ratio/g" wells_"$package".py

python wells_"$package".py

x=$(head -n1 temp_"$package".tmp)
y=$(head -n2 temp_"$package".tmp | tail -n1)
z=$(head -n3 temp_"$package".tmp | tail -n1)
na=$(head -n4 temp_"$package".tmp | tail -n1)

sed -i "s/SED_x_SED/"$x"/g" ./packmol.inp
sed -i "s/SED_y_SED/"$y"/g" ./packmol.inp
sed -i "s/SED_z_SED/"$z"/g" ./packmol.inp
sed -i "s/SED_na_SED/"$na"/g" ./packmol.inp
sed -i "s/SED_na_SED/"$na"/g" ./STEEP.top
sed -i "s/SED_na_SED/"$na"/g" ./topol.top

pm < packmol.inp

gmx editconf -f packmol.pdb -o liquid.gro
echo q | gmx make_ndx -f liquid.gro -o STEEP.ndx

gmx grompp -f STEEP.mdp -c liquid.gro -n STEEP.ndx -p STEEP.top -o STEEP -maxwarn 9 

sed -i "s/SED_name_SED/"$package"_"$ratio"/g" ./1.run

cp table_gen.py table_10.py
sed -i "s/SED_intstr_SED/10.0/g" ./table_10.py
python table_10.py
sbatch 1.run

cd ..
done
done
