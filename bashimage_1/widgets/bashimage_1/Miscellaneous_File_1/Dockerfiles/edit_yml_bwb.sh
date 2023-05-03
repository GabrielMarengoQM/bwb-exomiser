#!/bin/bash

# Assign the arguments to variables
vcf_file=$6
yml_file=$7

# Check that the script is being called with at least one argument
if [ $# -lt 1 ]; then
    echo "Usage: $0 [vcf_file] [yml_file]"
    exit 1
fi

# Replace line 8 of the file with the new string
sed -i "8s/.*/    vcf: \/exomiser\/${vcf_file}/" /root/$yml_file

echo "Line 8 of $file has been replaced with \"vcf: /exomiser/${vcf_file}\""

