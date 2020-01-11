import tabula
import slate3k as slate
import pandas as pd

colHead = ['Year','Month', 'Date Of Filing', 'GSTIN', 'Name', 'Taxable Value(Othe than Zero Rated)', 'Taxable Value Zero Rated', 'Value Exempted/Nil', 'Reverse Charge Value', 'Value of Non-GST Outward Supply', 'ITC-IGST', 'ITC-CGST', 'ITC-SGST', 'ITC-Cess', 'Tax-Paid ITC-IGST', 'Tax-Paid ITC-CGST', 'Tax-Paid ITC-SGST', 'Tax-Paid ITC-Cess', 'Cash-Paid Tax', 'Cash-Paid Interest', 'Cash-Paid Fine','Cash-Paid RCM'];
year = [];
month = [];
dof = [];
gstin = [];
name = [];
taxValwoZero = [];
taxValwZero = [];
valExemp = [];
revChargeVal = [];
valNonGstSupply = [];
itcIgst = [];
itcCgst = [];
itcSgst = [];
itcCess = [];
tpItcIgst = [];
tpItcCgst = [];
tpItcSgst = [];
tpItcCess = [];
cpTax = [];
cpInt = [];
cpFine = [];
cpRCM = [];

for i in range(2,4):
    print ("Amar_Cars_012018_GSTR3B.pdf")
    with open("Amar_Cars_012018_GSTR3B.pdf",'rb') as f:
        extracted_text = slate.PDF(f);
    text = extracted_text[0].split("\n");
    listOfTables = tabula.read_pdf("Amar_Cars_012018_GSTR3B.pdf", multiple_tables=True, pages = 'all');
    print("listOfTablesPg1\n",listOfTables)
    print("listOfTablesPg1\n",listOfTables[8])
    print (text)
    year.append(text[20]);
    month.append(text[22]);
    dof.append(text[26]);
    gstin.append(listOfTables[0].values[0][2]);
    name.append(listOfTables[0].values[1][2]);
    taxValwoZero.append(listOfTables[1].values[4][1]);
    taxValwZero.append(listOfTables[1].values[6][1]);
    valExemp.append(listOfTables[1].values[7][1]);
    revChargeVal.append(listOfTables[1].values[8][1]);
    valNonGstSupply.append(listOfTables[1].values[9][1]);
    # Will work with no hesitation upto here.
    # Changing code from here
    itcIgst.append(list(listOfTables[4].values)[list(listOfTables[4].values[:,0]).index('(C) Net ITC Available (A) – (B)')][1]);
    itcCgst.append(list(listOfTables[4].values)[list(listOfTables[4].values[:,0]).index('(C) Net ITC Available (A) – (B)')][2]);
    itcSgst.append(list(listOfTables[4].values)[list(listOfTables[4].values[:,0]).index('(C) Net ITC Available (A) – (B)')][3]);
    itcCess.append(list(listOfTables[4].values)[list(listOfTables[4].values[:,0]).index('(C) Net ITC Available (A) – (B)')][4]);
    try:
        tpItcIgst.append(listOfTables[7].values[10][0].split()[4]);
        tpItcCgst.append(listOfTables[7].values[10][0].split()[5]);
        tpItcSgst.append(listOfTables[7].values[10][0].split()[6]);
        tpItcCess.append(listOfTables[7].values[10][1]);
        cpTax.append(listOfTables[7].values[10][2].split()[0]);
        cpInt.append(listOfTables[7].values[10][2].split()[1]);
        cpFine.append(listOfTables[7].values[10][3]);
    except:
        tpItcIgst.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][4]);
        tpItcCgst.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][5]);
        tpItcSgst.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][6]);
        tpItcCess.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][7]);
        cpTax.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][8]);
        cpInt.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][9]);
        cpFine.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total')][10]);
        cpRCM.append(listOfTables[8].values[list(listOfTables[8].values[:,0]).index('Total',2)][8]);


zippedList = list(zip(year, month, dof, gstin, name, taxValwoZero, taxValwZero, valExemp, revChargeVal, valNonGstSupply, itcIgst, itcCgst, itcSgst, itcCess, tpItcIgst, tpItcCgst, tpItcSgst, tpItcCess, cpTax, cpInt, cpFine, cpRCM));
df = pd.DataFrame(zippedList, columns = colHead);
df.to_excel("pyexcel.xlsx")