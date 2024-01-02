import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,title,data2=None,data3=None,dataName="simulated Jet1"):
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
        legend.AddEntry(data2,"simulated Jet2")
        legend.AddEntry(data3,"simulated Jet3")
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
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"_PlotSimulation_WithScale_Run32023_MC.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
MCJet1 = histFile.Get("Jet1")
MCJet2 = histFile.Get("Jet2")
MCJet3 = histFile.Get("Jet3")
Kinematics = histFile.Get("Kinematics")
pdfnames = "PlotSimulation_Run32023_MC_AddedHist_"

MCJetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create Jet pdfs
for i in range(0,14):
    MC1 = MCJet1.Get(MCJetNameArray[i]+"1sim_hist")
    MC2 = MCJet2.Get(MCJetNameArray[i]+"2sim_hist")
    MC3 = MCJet3.Get(MCJetNameArray[i]+"3sim_hist")

    if MCJetNameArray[i] == "pt" or MCJetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+pdfnames+MCJetNameArray[i]+".pdf",MC1,True,3,"#sigma [pb]",XaxisArray[i],XaxisArray[i]+" simulation",MC2,MC3)
    else:
        RootHisttoPdf(outDirectory+pdfnames+MCJetNameArray[i]+".pdf",MC1,False,3,"#sigma [pb]",XaxisArray[i],XaxisArray[i]+" simulation",MC2,MC3)

#create yboost pdf
yboostData = Kinematics.Get("yboostsim_hist")
RootHisttoPdf(outDirectory+pdfnames+"yboost.pdf",yboostData,False,1,"#sigma [pb]","Yboost","Yboost simulation","simulated Yboost")
#create chi pdf
chiData = Kinematics.Get("chisim_hist")
RootHisttoPdf(outDirectory+pdfnames+"chi.pdf",chiData,False,1,"#sigma [pb]","Chi","Chi simulation",None,None,"simulated Chi")
#create mjj pdf
mjjData = Kinematics.Get("mjjsim_hist")
RootHisttoPdf(outDirectory+pdfnames+"mjj.pdf",mjjData,True,1,"#sigma [pb]","Mjj [GeV]","Mjj simulation",None,None,"simulated Mjj")
