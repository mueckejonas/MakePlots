import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,title,data2=None,data3=None,dataName="generated Jet1"):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1,dataName)
    if dataNumber > 2:
        legend.AddEntry(data2,"generated Jet2")
        legend.AddEntry(data3,"generated Jet3")
    else:
        legend.SetTextSize(0.03)

    data1.SetStats(0)
    data1.SetLineColor(ROOT.kBlack)
    data1.SetLineWidth(2)
    if dataNumber > 2:
        data2.SetStats(0)
        data2.SetLineColor(ROOT.kBlue)
        data2.SetLineWidth(2)
        data3.SetStats(0)
        data3.SetLineColor(ROOT.kRed)
        data3.SetLineWidth(2)
        data2.SetTitle("")
        data3.SetTitle("")
    data1.GetYaxis().SetTitle(yAxisTitle)
    data1.GetXaxis().SetTitle(xAxisTitle)
    data1.SetTitle("")
    data1.Draw("pe")
    if dataNumber > 2:
        data2.Draw("pe,same")
        data3.Draw("pe,same")
    legend.Draw("same")
    latex.DrawText(0.7,0.8,title)
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/Root/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/Pdf/"
inFileName = inDirectory+"_PlotSimulation_WithScale_Run32023_Gen.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
genJet1 = histFile.Get("Jet1")
genJet2 = histFile.Get("Jet2")
genJet3 = histFile.Get("Jet3")
Kinematics = histFile.Get("Kinematics")
pdfnames = "PlotSimulation_Run32023_Gen_AddedHist_"

genJetNameArray = np.array(["pt","y","eta","phi","mass"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]"])

#create Jet pdfs
for i in range(0,5):
    gen1 = genJet1.Get(genJetNameArray[i]+"1gen_hist")
    gen2 = genJet2.Get(genJetNameArray[i]+"2gen_hist")
    gen3 = genJet3.Get(genJetNameArray[i]+"3gen_hist")

    if genJetNameArray[i] == "pt" or genJetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+pdfnames+genJetNameArray[i]+".pdf",gen1,True,3,"#sigma [pb]",XaxisArray[i],XaxisArray[i]+" generated",gen2,gen3)
    else:
        RootHisttoPdf(outDirectory+pdfnames+genJetNameArray[i]+".pdf",gen1,False,3,"#sigma [pb]",XaxisArray[i],XaxisArray[i]+" generated",gen2,gen3)

#create yboost pdf
yboostData = Kinematics.Get("yboostgen_hist")
RootHisttoPdf(outDirectory+pdfnames+"yboost.pdf",yboostData,False,1,"#sigma [pb]","Yboost","Yboost generated","generated Yboost")
#create chi pdf
chiData = Kinematics.Get("chigen_hist")
RootHisttoPdf(outDirectory+pdfnames+"chi.pdf",chiData,False,1,"#sigma [pb]","Chi","Chi generated",None,None,"generated Chi")
#create mjj pdf
mjjData = Kinematics.Get("mjjgen_hist")
RootHisttoPdf(outDirectory+pdfnames+"mjj.pdf",mjjData,True,1,"#sigma [pb]","Mjj [GeV]","Mjj generated",None,None,"generated Mjj")
