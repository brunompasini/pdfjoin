def pdfjoin():
  try:
    import os
    from PyPDF2 import PdfFileMerger
    os.chdir("../pdfjoin")
  except ImportError:
    print("Could not import")
  
  nome = None
  pdfs = []

  while nome != "0":
    nome = input("Type the name of the PDF file or enter 0 to finish: ")
    if str(nome) == "0":
      break
    if not(nome.endswith(".pdf")):
      nome = nome+".pdf"
    pdfs.append(nome)
    print("%d Files already loaded: "%(len(pdfs)))
    for el in pdfs:
      print(el,end=", ")
    print('\n')

  merger = PdfFileMerger()
  for pdf in pdfs:
      merger.append(pdf)
  
  fileName = input("Name of the result file: ")
  if not(fileName.endswith(".pdf")):
    fileName = fileName+".pdf"

  merger.write(fileName)
  merger.close()
  print("Finished")

pdfjoin()