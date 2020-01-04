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
    print ("24AAACG6864F1ZO_0"+str(i)+"2019_GSTR3B")
    with open("24AAACG6864F1ZO_0"+str(i)+"2019_GSTR3B.pdf",'rb') as f:
        extracted_text = slate.PDF(f);
    text = extracted_text[0].split("\n");
    listOfTablesPg1 = tabula.read_pdf("24AAACG6864F1ZO_0"+str(i)+"2019_GSTR3B.pdf", multiple_tables=True, pages = 1);
    listOfTablesPg2 = tabula.read_pdf("24AAACG6864F1ZO_0"+str(i)+"2019_GSTR3B.pdf", multiple_tables=True, pages = 2);
    listOfTablesPg3 = tabula.read_pdf("24AAACG6864F1ZO_0"+str(i)+"2019_GSTR3B.pdf", multiple_tables=True, pages = 3);
    print("listOfTablesPg1\n",listOfTablesPg1);
    print("listOfTablesPg2\n",listOfTablesPg2[3].values);
    print("listOfTablesPg3\n",listOfTablesPg3[0].values);

    year.append(text[20]);
    month.append(text[22]);
    dof.append(text[26]);
    gstin.append(listOfTablesPg1[0].values[0][2]);
    name.append(listOfTablesPg1[0].values[1][2]);
    taxValwoZero.append(listOfTablesPg1[1].values[4][1]);
    taxValwZero.append(listOfTablesPg1[1].values[6][1]);
    valExemp.append(listOfTablesPg1[1].values[7][1]);
    revChargeVal.append(listOfTablesPg1[1].values[8][1]);
    valNonGstSupply.append(listOfTablesPg1[1].values[9][1]);
    itcIgst.append(list(listOfTablesPg2[0].values)[list(listOfTablesPg2[0].values[:,0]).index('(C) Net ITC Available (A) – (B)')][1]);
    itcCgst.append(list(listOfTablesPg2[0].values)[list(listOfTablesPg2[0].values[:,0]).index('(C) Net ITC Available (A) – (B)')][2]);
    itcSgst.append(list(listOfTablesPg2[0].values)[list(listOfTablesPg2[0].values[:,0]).index('(C) Net ITC Available (A) – (B)')][3]);
    itcCess.append(list(listOfTablesPg2[0].values)[list(listOfTablesPg2[0].values[:,0]).index('(C) Net ITC Available (A) – (B)')][4]);
    try:
        tpItcIgst.append(listOfTablesPg2[3].values[10][0].split()[4]);
        tpItcCgst.append(listOfTablesPg2[3].values[10][0].split()[5]);
        tpItcSgst.append(listOfTablesPg2[3].values[10][0].split()[6]);
        tpItcCess.append(listOfTablesPg2[3].values[10][1]);
        cpTax.append(listOfTablesPg2[3].values[10][2].split()[0]);
        cpInt.append(listOfTablesPg2[3].values[10][2].split()[1]);
        cpFine.append(listOfTablesPg2[3].values[10][3]);
    except:
        tpItcIgst.append(listOfTablesPg3[0].values[0][4]);
        tpItcCgst.append(listOfTablesPg3[0].values[0][5]);
        tpItcSgst.append(listOfTablesPg3[0].values[0][6]);
        tpItcCess.append(listOfTablesPg3[0].values[0][7]);
        cpTax.append(listOfTablesPg3[0].values[0][8]);
        cpInt.append(listOfTablesPg3[0].values[0][9]);
        cpFine.append(listOfTablesPg3[0].values[0][10]);
        cpRCM.append(listOfTablesPg3[0].values[6][8]);


zippedList = list(zip(year, month, dof, gstin, name, taxValwoZero, taxValwZero, valExemp, revChargeVal, valNonGstSupply, itcIgst, itcCgst, itcSgst, itcCess, tpItcIgst, tpItcCgst, tpItcSgst, tpItcCess, cpTax, cpInt, cpFine, cpRCM));
df = pd.DataFrame(zippedList, columns = colHead);
df.to_excel("pyexcel.xlsx")