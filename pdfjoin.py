from datetime import datetime
import os
import argparse
from tabnanny import check
from tracemalloc import start
from typing import List
try:
    from PyPDF2 import PdfFileMerger
except ImportError:
    print("You don\'t have PyPDF installed")

#os.chdir('to_join/')

def check_folders():
    if not os.path.exists('to_join/'):
        os.mkdir('to_join/')
        
    if not os.path.exists('end/'):
        os.mkdir('end/')
        
    os.chdir('to_join/')


# Defining a whole function just to join (maybe create a wrapper class ? Someday ?)
def join(name: str, to_join: List[str]):
    pdfs = []
    for el in to_join:
        if not(el.endswith('.pdf')):
            el = el + '.pdf'
        pdfs.append(el)
    if not(name.endswith('.pdf')):
        name = name + '.pdf'

    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    file_name = name
    
    merger.write('../end/'+file_name)
    merger.close()


# Changed to use real argument parsing
def main():
    check_folders()
    default_name = 'result_PDF_' + datetime.now().strftime("%d_%m_%Y_%H_%M") + '.pdf'

    parser = argparse.ArgumentParser(description='*pdfjoin.py is my tool to join pdfs, I\'m always working on it*')
    parser.add_argument('-n', '--name', default=default_name, help='Name of the result file, default value is \'resultPDF_day_month_year_hour_min.pdf\'')
    parser.add_argument('-s', '--start', action='store_true', help='Only generate to_join and end folders')

    parser.add_argument('files', help='Type all files to join', nargs='*')
    all_args = parser.parse_args()

    if all_args.start:
        return
        
    else:
        check
        if len(all_args.files) == 0:
            raise argparse.ArgumentError(None,'No files were typed')
        join(all_args.name, all_args.files)


main()