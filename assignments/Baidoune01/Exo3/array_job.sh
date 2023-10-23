#!/bin/bash
#SBATCH --array=2-11

while IFS=$'\t' read -r -a line; do
    t_id=${line[0]}
    t_name=${line[1]}
    t_sex=${line[2]}
    echo "This is array task $t_id, the sample name is $t_name and the sex is $t_sex."
done < config.txt > output.txt