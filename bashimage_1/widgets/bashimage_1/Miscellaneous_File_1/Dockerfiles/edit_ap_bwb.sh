#!/bin/bash

# This script updates the exomiser application.properties file with the required values

new_file_path="/root/${5}"

if [ "$2" == "hg19" ]; then
  line38_replacement="exomiser.hg19.data-version=${3}"
  line53_replacement="#exomiser.hg38.data-version=${3}"
elif [ "$2" == "hg38" ]; then
  line38_replacement="#exomiser.hg19.data-version=${3}"
  line53_replacement="exomiser.hg38.data-version=${3}"
else
  echo "Invalid version specified: $2"
  exit 1
fi

sed -i -e "26s/.*/exomiser.data-directory=${1//\//\\/}/" \
       -e "38s/.*/${line38_replacement}/" \
       -e "53s/.*/${line53_replacement}/" \
       -e "61s/.*/exomiser.phenotype.data-version=${4}/" \
       "${new_file_path}"


# Assign the arguments to variables
vcf_file=$6
yml_file=$7


# Replace line 8 of the file with the new string
sed -i "8s/.*/    vcf: \/exomiser\/${vcf_file}/" /root/$yml_file

echo "Line 8 of $file has been replaced with \"vcf: /exomiser/${vcf_file}\""
