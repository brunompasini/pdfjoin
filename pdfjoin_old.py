def main():
  try:
    import sys
    import os
    from PyPDF2 import PdfFileMerger
    #os.chdir("../pdfjoin")
  except ImportError:
    print("Could not import")
  
  pdfs = []
  nome = ''

  if len(sys.argv) > 1:
    pdfs = sys.argv[1:]
  for el in pdfs:
    if not(el.endswith(".pdf")):
      el = el+".pdf"

  merger = PdfFileMerger()
  for pdf in pdfs:
      merger.append(pdf)
  fileName = input("Name of the result file: ")
  if fileName!="0" and fileName!="":
    if not(fileName.endswith(".pdf")):
      fileName = fileName+".pdf"

    merger.write(fileName)
    merger.close()
    print("Finished")
  else:
    print("Error: PDF was not made")

main()