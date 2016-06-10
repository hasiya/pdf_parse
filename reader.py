#   https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167

#

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re


def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        # a = page.contents[0].rawdata
        # print ('u', a)
        # print
        # splitData = a.split('\n')
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    # print ('u', text)
    # print
    # print(text)
    return text


def getCompanyFileData():
    text = convert('company.pdf')

    reg_annualS = '(?<=Annual Sales: )[^A-Za-z0-9]\d*.\d* \w*'
    annual_sales = re.findall(reg_annualS,text)[0]
    print 'Annual Sales:', annual_sales

    reg_totalE = '(?<=Total Employees: )\d*'
    total_emp = re.findall(reg_totalE, text)[0]
    print 'Total Employees:', total_emp

    reg_empAtLoc = '(?<=Employees at This Location: )\d*'
    emp_loc = re.findall(reg_empAtLoc, text)[0]
    print 'Employees at This Location:', emp_loc

    reg_busiLine= '(?<=Primary Line of Business: )\w.*'
    business_line = re.findall(reg_busiLine, text)[0]
    print 'Primary Line of Business:', business_line




getCompanyFileData()
