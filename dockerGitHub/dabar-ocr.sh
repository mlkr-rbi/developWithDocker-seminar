for filename in ../data/dabar-radovi/*.pdf; do
   python doc2json/grobid2json/process_pdf.py -i $filename -t temp_dabar/ -o ../data/grobid-output-dabar/
done