import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):
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
    data1.Divide(data2)
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

HLT_PFJet400 = HLT_PFJet.Get("HLT_PFJet400")

HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")

RootHisttoPdf(outDirectory+"PlotTriggerEfficientcy_HLT_PFJet500.pdf",HLT_PFJet400,HLT_PFJet500,"HLT_PFJet500/HLT_PFJet400","Mjj [GeV]","Run2023B","Trigger Efficiency pt>500")
