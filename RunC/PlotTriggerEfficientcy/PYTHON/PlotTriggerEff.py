import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,yAxisTitle,xAxisTitle,title,undertitle):
    canvas = ROOT.TCanvas("canvas")

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1,yAxisTitle)

    data1.SetStats(0)
    data1.SetLineColor(ROOT.kBlack)
    data1.SetLineWidth(2)
    data1.GetYaxis().SetTitle(yAxisTitle)
    data1.GetXaxis().SetTitle(xAxisTitle)
    data1.SetTitle("")
    #data1.Divide(data2)
    data1.Draw("pe")
    legend.Draw("same")
    latex.DrawText(0.7,0.8,title)
    latex.SetTextSize(0.04)
    latex.DrawText(0.7,0.77,undertitle)
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023C_"
inFileName = inDirectory+"PlotTriggerEfficientcy_Run2023C.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
HLT_PFJet = histFile.Get("HLT_PFJet")
HLT_PFHTJet = histFile.Get("HLT_PFHT")

HLT_PFJet40 = HLT_PFJet.Get("HLT_PFJet40")
HLT_PFJet60 = HLT_PFJet.Get("HLT_PFJet60")
HLT_PFJet80 = HLT_PFJet.Get("HLT_PFJet80")
HLT_PFJet110 = HLT_PFJet.Get("HLT_PFJet110")
HLT_PFJet140 = HLT_PFJet.Get("HLT_PFJet140")
HLT_PFJet200 = HLT_PFJet.Get("HLT_PFJet200")
HLT_PFJet260 = HLT_PFJet.Get("HLT_PFJet260")
HLT_PFJet320 = HLT_PFJet.Get("HLT_PFJet320")
HLT_PFJet400 = HLT_PFJet.Get("HLT_PFJet400")
HLT_PFJet450 = HLT_PFJet.Get("HLT_PFJet450")
HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")
HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")

RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFJet40.pdf",HLT_PFJet40,"HLT_PFJet40","pt1 [GeV]","Run2023B","Trigger pt>40")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFJet60.pdf",HLT_PFJet60,"HLT_PFJet60","pt1 [GeV]","Run2023B","Trigger pt>60")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFJet80.pdf",HLT_PFJet80,"HLT_PFJet80","pt1 [GeV]","Run2023B","Trigger pt>80")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet110.pdf",HLT_PFJet110,"HLT_PFJet110","pt1 [GeV]","Run2023B","Trigger pt>110")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet140.pdf",HLT_PFJet140,"HLT_PFJet140","pt1 [GeV]","Run2023B","Trigger pt>140")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet200.pdf",HLT_PFJet200,"HLT_PFJet200","pt1 [GeV]","Run2023B","Trigger pt>200")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet260.pdf",HLT_PFJet260,"HLT_PFJet260","pt1 [GeV]","Run2023B","Trigger pt>260")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet320.pdf",HLT_PFJet320,"HLT_PFJet320","pt1 [GeV]","Run2023B","Trigger pt>320")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet400.pdf",HLT_PFJet400,"HLT_PFJet400","pt1 [GeV]","Run2023B","Trigger pt>400")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet450.pdf",HLT_PFJet450,"HLT_PFJet450","pt1 [GeV]","Run2023B","Trigger pt>450")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet500.pdf",HLT_PFJet500,"HLT_PFJet500","pt1 [GeV]","Run2023B","Trigger pt>500")
RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet550.pdf",HLT_PFJet550,"HLT_PFJet550","pt1 [GeV]","Run2023B","Trigger pt>550")


HLT_PFHT180 = HLT_PFHTJet.Get("HLT_PFHT180")
HLT_PFHT250 = HLT_PFHTJet.Get("HLT_PFHT250")
HLT_PFHT350 = HLT_PFHTJet.Get("HLT_PFHT350")
HLT_PFHT370 = HLT_PFHTJet.Get("HLT_PFHT370")
HLT_PFHT430 = HLT_PFHTJet.Get("HLT_PFHT430")
HLT_PFHT510 = HLT_PFHTJet.Get("HLT_PFHT510")
HLT_PFHT590 = HLT_PFHTJet.Get("HLT_PFHT590")
HLT_PFHT680 = HLT_PFHTJet.Get("HLT_PFHT680")
HLT_PFHT780 = HLT_PFHTJet.Get("HLT_PFHT780")
HLT_PFHT890 = HLT_PFHTJet.Get("HLT_PFHT890")
HLT_PFHT1050 = HLT_PFHTJet.Get("HLT_PFHT1050")

RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT180.pdf",HLT_PFHT180,"HLT_PFHT180","pt1 [GeV]","Run2023B","Trigger pt>180")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT250.pdf",HLT_PFHT250,"HLT_PFHT250","pt1 [GeV]","Run2023B","Trigger pt>250")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT350.pdf",HLT_PFHT350,"HLT_PFHT350","pt1 [GeV]","Run2023B","Trigger pt>350")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT370.pdf",HLT_PFHT370,"HLT_PFHT370","pt1 [GeV]","Run2023B","Trigger pt>370")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT430.pdf",HLT_PFHT430,"HLT_PFHT430","pt1 [GeV]","Run2023B","Trigger pt>430")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT510.pdf",HLT_PFHT510,"HLT_PFHT510","pt1 [GeV]","Run2023B","Trigger pt>510")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT590.pdf",HLT_PFHT590,"HLT_PFHT590","pt1 [GeV]","Run2023B","Trigger pt>590")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT680.pdf",HLT_PFHT680,"HLT_PFHT680","pt1 [GeV]","Run2023B","Trigger pt>680")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT780.pdf",HLT_PFHT780,"HLT_PFHT780","pt1 [GeV]","Run2023B","Trigger pt>780")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT890.pdf",HLT_PFHT890,"HLT_PFHT890","pt1 [GeV]","Run2023B","Trigger pt>890")
RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFHT1050.pdf",HLT_PFHT1050,"HLT_PFHT1050","pt1 [GeV]","Run2023B","Trigger pt>1050")
