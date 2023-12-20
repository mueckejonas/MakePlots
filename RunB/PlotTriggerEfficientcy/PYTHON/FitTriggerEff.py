import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):

    fit_template = "[0]/(1+exp(-[1]*x-[2]))"
    fit_func = ROOT.TF1("fit_func",fit_template,2200,4000)
    fit_func.SetParameter(0,1)
    fit_func.SetParameter(1,1)
    fit_func.SetParameter(2,1)

    data1.Divide(data2)

    canvas = ROOT.TCanvas("canvas")

    data1.Fit(fit_func,"E")
    data1.Draw("pe")

    canvas.Print(outFileName)


    """
    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    canvas = ROOT.TCanvas("canvas")

    for i in range(0,int(data1.GetNbinsX())):
	    Efficiency.SetPointEXhigh(i,0.0)
	    Efficiency.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    Efficiency.SetStats(0)
    Efficiency.SetLineColor(ROOT.kBlack)
    Efficiency.SetLineWidth(1)
    Efficiency.GetYaxis().SetTitle(yAxisTitle)
    Efficiency.GetXaxis().SetTitle(xAxisTitle)
    Efficiency.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    Efficiency.SetTitle(title+undertitle)
    Efficiency.SetMarkerStyle(4)
    legend.AddEntry(Efficiency,yAxisTitle,"p")
    legend.SetLineWidth(0)
    Efficiency.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)
    """


#get fit parameters
#param1 = fit.GetParameter(0)

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

RootHisttoPdf(outDirectory+"PlottriggerEfficiency_withFit_HLT_PFJet550.pdf",HLT_PFJet550,Ref_HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","Mjj [GeV]","Run2023B","Trigger Efficiency pt>550")
