#!/usr/bin/python

"""Extract a list of pages from a pdf file into a new single pdf file.  

Prerequisites:
==============
* `pyPdf` (available through pip).

Usage:
======
`python pdfsplit.py <input_file> <output_file> <pages>`

For example, to create a new pdf named out.pdf from pages 1, 3, 5, 
and 7, use::

	$ python pdfsplit.py in.pdf out.pdf 1 3 5 7

Or, if you've followed the "How to..." below::

	$ pdfsplit in.pdf out.pdf 1 3 5 7

How to make this script executable from anywhere (on mac or linux):
===================================================================
1. Make sure the first line of this script is #!/usr/bin/python
2. Make script executable::

    $ chmod 775 pdfsplit.py

3. Make a link so that the terminal will find this script::

    $ sudo ln -s "$PWD"/pdfsplit.py /usr/bin/pdfsplit

"""

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
	print(__doc__)


if __name__ == "__main__":
	main(sys.argv[1:])
