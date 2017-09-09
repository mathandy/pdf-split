#! /usr/bin/env python

"""This is a tool to extract a list of pages from a pdf file.  It 
requires the package `pyPdf` (available through pip).

Usage:
======
python pdfsplit.py <input_file> <output_file> <pages>
E.g.
python pdfsplit.py in.pdf out.pdf 1 3 5 7

Note: 
=====
You can make this executable on (on Unix) with:
cd /usr/local/bin
sudo ln -s "/location/of/file/pdfsplit.py" pdfsplit

Then you can execute with 
pdfsplit in.pdf out.pdf 1 3 5 7"""

import sys
import os
import getopt
from pyPdf import PdfFileWriter, PdfFileReader


def split(input_file, output_file, pages):
	inputpdf = PdfFileReader(open(input_file, "rb"))
	outputpdf = PdfFileWriter()
	for i in pages:
		outputpdf.addPage(inputpdf.getPage(i - 1))
	with open(output_file, "wb") as outf:
	    outputpdf.write(outf)


def main(argv):
	try:
		INPUT = argv[0]
		OUTPUT = argv[1]
		PAGES = [int(x) for x in argv[2:]]
	except:
		usage()
		sys.exit(2)

	split(INPUT, OUTPUT, PAGES)
    

def usage():
	print("Usage: python pdfsplit.py <input_file> <output file> <pages>")
	print("For example: python pdfsplit.py in.pdf out.pdf 1 3 5 7")


if __name__ == "__main__":
	main(sys.argv[1:])
