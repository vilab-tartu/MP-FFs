xtb=/home/user/software/xtb2/xtb
for i in Ac
do
for j in CsCl_322 CsCl_332 CsCl_333 CsCl_432 NaCl_322 NaCl_332 NaCl_333 NaCl_432
do
mkdir -p "$i"
cp "$i"_"$j".xyz "$i"
cd "$i"
$xtb "$i"_"$j".xyz > "$i"_"$j".out
sleep 1
mv charges charges_"$i"_"$j"
rm wfn.xtb
cd ..
done
done
