#!/bin/bash
#SBATCH --job-name=job_b
#SBATCH --output=job_b_output.txt
#SBATCH --dependency=afterok:

python f.py
python f.py
