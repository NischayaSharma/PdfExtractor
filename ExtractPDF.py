import tabula
import slate3k as slate
import pandas as pd

year = []
month = []
dof = []
gstin = []
name = []
taxValwoZero = []
taxValwZero = []
valExemp = []
revChargeVal = []
valNonGstSupply = []
itcIgst = []
itcCgst = []
itcSgst = []
itcCess = []
tpItcIgst = []
tpItcCgst = []
tpItcSgst = []
tpItcCess = []
cpTax = []
cpInt = []
cpFine = []
cpRCM = []
for i in range(2, 3):
    tpNull = True
    print("Amar_Cars_012018_GSTR3B.pdf")
    with open("Amar_Cars_012018_GSTR3B.pdf", 'rb') as f:
        extracted_text = slate.PDF(f)
    text = extracted_text[0].split("\n")
    listOfTables = tabula.read_pdf("Amar_Cars_012018_GSTR3B.pdf", multiple_tables=True, pages='all')
    print("listOfTablesPg1\n", listOfTables)
    print (text)
    year.append(text[20])
    month.append(text[22])
    dof.append(text[26])
    gstin.append(listOfTables[0].values[0][2])
    name.append(listOfTables[0].values[1][2])
    taxValwoZero.append(listOfTables[1].values[4][1])
    taxValwZero.append(listOfTables[1].values[6][1])
    valExemp.append(listOfTables[1].values[7][1])
    revChargeVal.append(listOfTables[1].values[8][1])
    valNonGstSupply.append(listOfTables[1].values[9][1])
    # Will work with no hesitation upto here.
    # Changing code from here

    # [:,0] slicing of 2d lists
    # first argument for rows and 2nd is the column number
    for table in listOfTables:
        try:
            itcIgst.append(list(table.values)[list(table.values[:, 0]).index('(C) Net ITC Available (A) – (B)')][1])
            itcCgst.append(list(table.values)[list(table.values[:, 0]).index('(C) Net ITC Available (A) – (B)')][2])
            itcSgst.append(list(table.values)[list(table.values[:, 0]).index('(C) Net ITC Available (A) – (B)')][3])
            itcCess.append(list(table.values)[list(table.values[:, 0]).index('(C) Net ITC Available (A) – (B)')][4])
        except:
            print(" Not in table")
        for word in list(table.values[:,0]):
            if(word == 'Other than Reverse' and tpNull == True):
                try:
                    tpItcIgst.append(list(table.values)[list(table.values[:,0]).index(word)+6][0].split()[4]);
                    tpItcCgst.append(list(table.values)[list(table.values[:,0]).index(word)+6][0].split()[5]);
                    tpItcSgst.append(list(table.values)[list(table.values[:,0]).index(word)+6][0].split()[6]);
                    tpItcCess.append(list(table.values)[list(table.values[:,0]).index(word)+6][1])
                    cpTax.append(list(table.values)[list(table.values[:,0]).index(word)+6][2].split()[0])
                    cpInt.append(list(table.values)[list(table.values[:,0]).index(word)+6][2].split()[1])
                    cpFine.append(list(table.values)[list(table.values[:,0]).index(word)+6][2].split()[2])
                    cpRCM.append(list(table.values)[list(table.values[:,0]).index(word)+12][2].split()[0])
                    tpNull = False;
                except:
                    print()
            elif(word == 'Reverse Charge' and tpNull == True):
                try:
                    tpItcIgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][0].split()[4]);
                    tpItcCgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][0].split()[5]);
                    tpItcSgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][0].split()[6]);
                    tpItcCess.append(list(table.values)[list(table.values[:,0]).index(word)-1][1])
                    cpTax.append(list(table.values)[list(table.values[:,0]).index(word)-1][2].split()[0])
                    cpInt.append(list(table.values)[list(table.values[:,0]).index(word)-1][2].split()[1])
                    cpFine.append(list(table.values)[list(table.values[:,0]).index(word)-1][2].split()[2])
                    cpRCM.append(list(table.values)[list(table.values[:,0]).index(word)+5][2].split()[0])
                    tpNull = False
                except:
                    tpItcIgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][4]);
                    tpItcCgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][5]);
                    tpItcSgst.append(list(table.values)[list(table.values[:,0]).index(word)-1][6]);
                    tpItcCess.append(list(table.values)[list(table.values[:,0]).index(word)-1][7]);
                    cpTax.append(list(table.values)[list(table.values[:,0]).index(word)-1][8])
                    cpInt.append(list(table.values)[list(table.values[:,0]).index(word)-1][9])
                    cpFine.append(list(table.values)[list(table.values[:,0]).index(word)-1][10])
                    cpRCM.append(list(table.values)[list(table.values[:,0]).index(word)+5][8])
                    tpNull = False

colHead = ['Year', 'Month', 'Date Of Filing', 'GSTIN', 'Name', 'Taxable Value(Othe than Zero Rated)', 'Taxable Value Zero Rated', 'Value Exempted/Nil', 'Reverse Charge Value', 'Value of Non-GST Outward Supply',
           'ITC-IGST', 'ITC-CGST', 'ITC-SGST', 'ITC-Cess', 'Tax-Paid ITC-IGST', 'Tax-Paid ITC-CGST', 'Tax-Paid ITC-SGST', 'Tax-Paid ITC-Cess', 'Cash-Paid Tax', 'Cash-Paid Interest', 'Cash-Paid Fine', 'Cash-Paid RCM']
zippedList = list(zip(year, month, dof, gstin, name, taxValwoZero, taxValwZero, valExemp, revChargeVal, valNonGstSupply,
                      itcIgst, itcCgst, itcSgst, itcCess, tpItcIgst, tpItcCgst, tpItcSgst, tpItcCess, cpTax, cpInt, cpFine, cpRCM))
df = pd.DataFrame(zippedList, columns=colHead)
print(colHead)
print(year,month, dof, gstin, name, taxValwoZero, taxValwZero, valExemp, revChargeVal, valNonGstSupply,
                      itcIgst, itcCgst, itcSgst, itcCess, tpItcIgst, tpItcCgst, tpItcSgst, tpItcCess, cpTax, cpInt, cpFine, cpRCM)
df.to_excel("pyexcel.xlsx")
