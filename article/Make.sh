#!/bin/bash

pdflatex article.tex
biber article
pdflatex article.tex
pdflatex article.tex

pdflatex article.tex
biber article
pdflatex article.tex
pdflatex article.tex

	
./clean.sh
