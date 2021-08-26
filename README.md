### usage: pdfjoin2.py [-h] [-n NAME] files [files ...]

### python modules used:
- datetime
- argparse
- typing
- PyPDF2

### function list:
- join(name: str, to_join: List[str]):  
checks every element in 'to_join' and if not there, adds a .pdf ending, same thing with 'name'  
PdfFileMerger object is instatiated, it'll do the work to join all files added with append, after we just pick the name argument passed, write the pdf file and close the file.

- main():  
default_name is:                          
'result_PDF_dd_mm_yyyy_hh_mm.pdf' (date in day, month, year, hour and minute)  
after we start the Argument Parser, there's a  
-> help arg,   
-> name arg (optional, if blank uses default name)  
-> file list entry arg  
after all, the join function is called with the right parameters


  
  

#### Works with PyPDF2==1.26.0, try pip installing it: 'pip install PyPDF2'