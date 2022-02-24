from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfCropMargins import crop
import minecart

# with open("2-003Y-SZ-02.pdf", "rb") as in_f:
#     input1 = PdfFileReader(in_f, strict = False)
#     output = PdfFileWriter()

#     numPages = input1.getNumPages()
#     print (f"document has {numPages} pages.")

#     wsp_finalne = {
#              'warstwa -4' : (0, 100, 1750, 550),
#              'warstwa -3' : (0, 550, 1750, 950), 
#              'warstwa -2' : (0, 950, 1750, 1350), 
#              'warstwa -1' : (0, 1300, 1750, 1717), # jest okej wsp_pomocnicze (225, 1310, 1750, 1665)
#              'warstwa  1' : (0, 1725, 1750, 2130), # jest okej wsp_pomocnicze (225, 1725, 1750, 2080)
#              'warstwa  2' : (0, 2080, 1750, 2530)  # jest okej wsp_pomocnicze (225, 2150, 1750, 2480)
#              } 

#--- wydruk pomocniczy do określenia prawej krawędzi wydruku oraz upewnienia się, że obszar zawiera ściany

    # for i in range(numPages):
    #     page = input1.getPage(i)
    #     print (page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
    #     # page.trimBox.lowerLeft = (0, 0)
    #     # page.trimBox.upperRight = (1225, 225)
    #     page.cropBox.lowerLeft = (225, 2150)
    #     page.cropBox.upperRight = (1750, 2480)
    #     output.addPage(page)

    # with open("out.pdf", "wb") as out_f:
    #     output.write(out_f)
 
#--- odnajdywanie ilości kolorów w pdfie
pdffile = open('out.pdf', 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(0)
for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):
     print (shape.path, shape.fill.color.as_rgb())
     
# m = page.images[0].as_pil()  # requires pillow
# im.show()

    # crop(["-p", "5", "-u", "-s", "-pdl", "out.pdf"])
    
    # with open("out_cropped.pdf", "rb") as in_g:
    #     input2 = PdfFileReader(in_g, strict = False)
    #     output = PdfFileWriter()
    #     numPages = input2.getNumPages()
        
    #     for i in range(numPages):
    #         page = input2.getPage(i)
    #         kraniec_wydruku = page.mediaBox.getUpperRight_x()
            
    # for i in range(numPages):
    #     page = input1.getPage(i)
    #     page.cropBox.lowerLeft = (0, 2080)
    #     page.cropBox.upperRight = (kraniec_wydruku, 2530)
    #     output.addPage(page)


    # with open("out.pdf", "wb") as out_f:
    #     output.write(out_f)