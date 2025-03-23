from fpdf import FPDF

pdf=FPDF(orientation="P", unit="pt", format="A4")
pdf.add_page()

pdf.image("tiger.jpeg", w=100, h=100)

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=50, txt="Malayan Tiger", align="C",border=1,ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=50, txt="The blessing of the forest.", align="C",ln=1)

pdf.set_font(family="Times", size=12)
txt1="""The Malayan tiger is a tiger from a
specific population of the Panthera tigris tigris
subspecies that is native to Peninsular Malaysia.
This population inhabits the southern and central parts 
of the Malay Peninsula, and has been classified as critically endangered. 
As of April 2014, the population was estimated at 80-120 mature individuals,
with a continuing downward trend."""

pdf.multi_cell(w=0, h=20, txt=txt1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Kingdom",border=1)

pdf.set_font(family="Times",  size=14)
pdf.cell(w=100, h=25, txt="Animalia",ln=1,border=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Phylum",border=1)

pdf.set_font(family="Times",  size=14)
pdf.cell(w=100, h=25, txt="Crodata",ln=1,border=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Order",border=1)

pdf.set_font(family="Times",  size=14)
pdf.cell(w=100, h=25, txt="Carnivora",ln=1,border=1)

pdf.output("output.pdf")