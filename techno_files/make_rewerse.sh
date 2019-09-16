#!/bin/bash

n=$(ls zawieszki|wc -l)
mkdir backtmp
for ((i=0; i<${n}; i++)); do cp ../rewers.pdf backtmp/rewers_1000${i}.pdf; done
pdfnup --nup 2x2 --no-landscape --paper a4paper --noautoscale true --outfile a4_back.pdf backtmp/*pdf
rm backtmp
