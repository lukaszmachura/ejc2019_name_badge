pdfnup --nup 2x2 --no-landscape --paper a4paper --noautoscale true --outfile a4.pdf zawieszki/*pdf
pdftk A=a4.pdf B=a4_back.pdf shuffle A B output bedges.pdf
