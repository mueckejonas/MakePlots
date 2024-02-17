import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,legendtitle,data2=None,data3=None):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()
    data1graph = ROOT.TGraphAsymmErrors(data1)
    for i in range(0,int(data1.GetNbinsX())):
	    data1graph.SetPointEXhigh(i,0.0)
	    data1graph.SetPointEXlow(i,0.0)

    if dataNumber > 2:
        data2graph = ROOT.TGraphAsymmErrors(data2)
        for i in range(0,int(data1.GetNbinsX())):
	        data2graph.SetPointEXhigh(i,0.0)
	        data2graph.SetPointEXlow(i,0.0)
        data3graph = ROOT.TGraphAsymmErrors(data3)
        for i in range(0,int(data1.GetNbinsX())):
	        data3graph.SetPointEXhigh(i,0.0)
	        data3graph.SetPointEXlow(i,0.0)
        legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
        legend.SetLineWidth(0)
        legend.SetFillStyle(4000)
        legend.AddEntry(data1graph,legendtitle+"_{1}","p")
        legend.AddEntry(data2graph,legendtitle+"_{2}","p")
        legend.AddEntry(data3graph,legendtitle+"_{3}","p")
    else:
        legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
        legend.SetLineWidth(0)
        legend.SetFillStyle(4000)
        legend.AddEntry(data1graph,legendtitle,"p")

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
        data2graph.SetMarkerSize(3)
        data2graph.SetLineWidth(2)
        data3graph.SetMarkerSize(3)
        data3graph.SetLineWidth(2)
    data1graph.GetYaxis().SetTitle(yAxisTitle)
    data1graph.GetXaxis().SetTitle(xAxisTitle)
    data1graph.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    data1graph.SetTitle("")
    #Set font size
    legend.SetTextSize(0.045)
    data1graph.SetMarkerSize(3)
    data1graph.SetLineWidth(2)
    data1graph.GetYaxis().SetLabelSize(0.045)
    data1graph.GetYaxis().SetTitleSize(0.05)
    data1graph.GetXaxis().SetLabelSize(0.045)
    data1graph.GetXaxis().SetTitleSize(0.05)
    #data1graph.GetYaxis().SetLabelOffset(0.01)
    #data1graph.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)


    data1graph.Draw("AP")
    if dataNumber > 2:
        data2graph.Draw("P same")
        data3graph.Draw("P same")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/Pdf/"
pdfnames = "PlotDijetJetID_Run2023D_"
inFileName = inDirectory+"PlotDijetJetID_Run2023D.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
Jet1 = histFile.Get("Jet1")
Jet2 = histFile.Get("Jet2")
Jet3 = histFile.Get("Jet3")
Kinematics = histFile.Get("Kinematics")

JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["P_{t} [GeV]","Y","#eta","#phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])
LegendArray = np.array(["Pt","Y","#eta","#phi","Mass","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create Jet pdfs
for i in range(0,14):
    data1 = Jet1.Get("data_"+JetNameArray[i]+"1")
    data2 = Jet2.Get("data_"+JetNameArray[i]+"2")
    data3 = Jet3.Get("data_"+JetNameArray[i]+"3")

    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+".pdf",data1,True,3,"N",XaxisArray[i],"Run3 D 2023 "+LegendArray[i],data2,data3)
    else:
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+".pdf",data1,False,3,"N",XaxisArray[i],"Run3 D 2023 "+LegendArray[i],data2,data3)

#create yboost pdf
yboostData = Kinematics.Get("data_yboost")
RootHisttoPdf(outDirectory+pdfnames+"yboost.pdf",yboostData,False,1,"N","Y_{boost}","Y_{boost} RunD 3 2023")
#create chi pdf
chiData = Kinematics.Get("data_chi")
RootHisttoPdf(outDirectory+pdfnames+"chi.pdf",chiData,False,1,"N","#chi_{dijet}","#chi_{dijet} RunD 3 2023")
#create mjj pdf
mjjData = Kinematics.Get("data_mjj")
RootHisttoPdf(outDirectory+pdfnames+"mjj.pdf",mjjData,True,1,"N","M_{jj} [GeV]","M_{jj} RunD 3 2023")
