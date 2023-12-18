import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,title,data2=None,data3=None,dataName="Jet1 data"):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()
    data1graph = ROOT.TGraphAsymmErrors(data1)
    for i in range(0,int(data1.GetNbinsX())):
	    data1graph.SetPointEXhigh(i,0.0)
	    data1graph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1graph,dataName,"p")
    if dataNumber > 2:
        data2graph = ROOT.TGraphAsymmErrors(data2)
        for i in range(0,int(data1.GetNbinsX())):
	        data2graph.SetPointEXhigh(i,0.0)
	        data2graph.SetPointEXlow(i,0.0)
        data3graph = ROOT.TGraphAsymmErrors(data3)
        for i in range(0,int(data1.GetNbinsX())):
	        data3graph.SetPointEXhigh(i,0.0)
	        data3graph.SetPointEXlow(i,0.0)
        legend.AddEntry(data2graph,"Jet2 data","p")
        legend.AddEntry(data3graph,"Jet3 data","p")
    else:
        legend.SetTextSize(0.03)

    data1graph.SetStats(0)
    data1graph.SetLineColor(ROOT.kBlack)
    data1graph.SetMarkerColor(ROOT.kBlack)
    data1graph.SetLineWidth(2)
    data1graph.SetMarkerStyle(4)
    if dataNumber > 2:
        data2graph.SetStats(0)
        data2graph.SetLineColor(ROOT.kBlue)
        data2graph.SetMarkerColor(ROOT.kBlue)
        data2graph.SetLineWidth(2)
        data2graph.SetMarkerStyle(4)
        data3graph.SetStats(0)
        data3graph.SetLineColor(ROOT.kRed)
        data3graph.SetMarkerColor(ROOT.kRed)
        data3graph.SetLineWidth(2)
        data3graph.SetMarkerStyle(4)
        data2graph.SetTitle("")
        data3graph.SetTitle("")
    data1graph.GetYaxis().SetTitle(yAxisTitle)
    data1graph.GetXaxis().SetTitle(xAxisTitle)
    data1graph.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    data1graph.SetTitle(title)
    data1graph.Draw("AP")
    if dataNumber > 2:
        data2graph.Draw("P same")
        data3graph.Draw("P same")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/Pdf/"
pdfnames = "PlotDijetSelection_Run2023C_"
inFileName = inDirectory+"PlotDijetSelection_Run2023C.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
Jet1 = histFile.Get("Jet1")
Jet2 = histFile.Get("Jet2")
Jet3 = histFile.Get("Jet3")
Kinematics = histFile.Get("Kinematics")

JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create Jet pdfs
for i in range(0,14):
    data1 = Jet1.Get("data_"+JetNameArray[i]+"1")
    data2 = Jet2.Get("data_"+JetNameArray[i]+"2")
    data3 = Jet3.Get("data_"+JetNameArray[i]+"3")

    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+".pdf",data1,True,3,"N",XaxisArray[i],XaxisArray[i]+" values",data2,data3)
    else:
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+".pdf",data1,False,3,"N",XaxisArray[i],XaxisArray[i]+" values",data2,data3)

#create yboost pdf
yboostData = Kinematics.Get("data_yboost")
RootHisttoPdf(outDirectory+pdfnames+"yboost.pdf",yboostData,False,1,"N","Yboost","Yboost values","Yboost")
#create chi pdf
chiData = Kinematics.Get("data_chi")
RootHisttoPdf(outDirectory+pdfnames+"chi.pdf",chiData,False,1,"N","Chi","Chi values",None,None,"Chi")
#create mjj pdf
mjjData = Kinematics.Get("data_mjj")
RootHisttoPdf(outDirectory+pdfnames+"mjj.pdf",mjjData,True,1,"N","Mjj [GeV]","Mjj values",None,None,"Mjj")
