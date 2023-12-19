import ROOT
import numpy as np
#takes three hists and turn them into pdf
def Find99Percent(data1,data2):
    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    for i in range(0,int(data1.GetNbinsX())):
        if(0.98 < Efficiency.GetY()[i] < 1.):
            print(Efficiency.GetX()[i])
            print(Efficiency.GetY()[i])

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/RootB/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023B_"
inFileName = inDirectory+"PlotTriggerEfficientcy_Run2023B.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
HLT_PFJet = histFile.Get("HLT_PFJet")
HLT_PFHTJet = histFile.Get("HLT_PFHT")

#HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")
#HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")
#RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet550_500asreference.pdf",HLT_PFJet550,HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","pt1 [GeV]","Run2023B","Trigger Efficiency pt>550")

HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")

Ref_HLT_PFJet500 = HLT_PFJet.Get("Ref_HLT_PFJet500")

Find99Percent(HLT_PFJet550,Ref_HLT_PFJet500)
