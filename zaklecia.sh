#!/bin/bash -x

mkdir zawieszki
python ejc18_zawieszki.py
pdfnup --nup 2x2 --no-landscape --paper a4paper --noautoscale true --outfile a4.pdf zawieszki/*pdf

n=$(ls zawieszki|wc -l)
mkdir backtmp
for ((i=0; i<${n}; i++)); do cp projekty/rewers.pdf backtmp/rewers_1000${i}.pdf; done
pdfnup --nup 2x2 --no-landscape --paper a4paper --noautoscale true --outfile a4_back.pdf backtmp/*pdf
# rm -rf backtmp
#bash make_rewerse.sh

pdftk A=a4.pdf B=a4_back.pdf shuffle A B output bedges.pdf
gs -dNoOutputFonts -sDEVICE=pdfwrite -o vectorized_bedges.pdf bedges.pdf
rm -rf a4.pdf bedges.pdf backtmp a4_back.pdf zawieszki
