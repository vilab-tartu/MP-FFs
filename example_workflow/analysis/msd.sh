for i in `seq "$1" 10 "$2"`
do
j=$(($i+10))
echo "$j"
gmx msd -f "$3"/melt.xtc -n "$3"/STEEP.ndx -s "$3"/melt.tpr -o "$4"/z_"$i".xvg -b "$i" -e "$j" -beginfit 0 -endfit 10 << EOF
0
EOF

done
