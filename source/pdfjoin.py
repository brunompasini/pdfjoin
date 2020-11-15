def joinPDF():
  try:
    import os
    from PyPDF2 import PdfFileMerger
    os.chdir("../PDFjoin")
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

joinPDF()
"""
from PyPDF2 import PdfFileMerger
pdfs=['0_Capa.pdf', '01_Sumario.pdf', '1_Introdução.pdf', '2_Transformada_Laplace.pdf', '3_Representação_Sistemas.pdf', '4_Estudo_Caso.pdf', '5_Respostas_Temporais.pdf', '6_Método_Lugar_Raízes.pdf', '7_Resposta_Frequencia.pdf', '8_Compensação.pdf']
merger = PdfFileMerger(strict=False)
for pdf in pdfs:
  merger.append(pdf)

merger.write("result.pdf")
merger.close()
print("Finished")
"""