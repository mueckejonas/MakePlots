import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):

    fit_template = "[0]/(1+exp(-(x/[1])-[2]))"
    fit_func = ROOT.TF1("fit_func",fit_template,2000,3000)
    fit_func.SetParameter(0,1)
    fit_func.SetParameter(1,500)
    fit_func.SetParameter(2,0)
    fit_data = data1.Clone()
    fit_data.Divide(data2)
    fit_data.Fit(fit_func,"E")

    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    canvas = ROOT.TCanvas("canvas")

    for i in range(0,int(data1.GetNbinsX())):
	    Efficiency.SetPointEXhigh(i,0.0)
	    Efficiency.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetTextSize(0.02)
    Efficiency.SetStats(0)
    Efficiency.SetLineColor(ROOT.kBlack)
    Efficiency.SetLineWidth(1)
    Efficiency.GetYaxis().SetTitle(yAxisTitle)
    Efficiency.GetXaxis().SetTitle(xAxisTitle)
    Efficiency.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    Efficiency.SetTitle(title+undertitle)
    Efficiency.SetMarkerStyle(4)
    legend.AddEntry(Efficiency,yAxisTitle,"p")
    legend.AddEntry(fit_func,"Logistic function fit","l")
    legend.SetLineWidth(0)
    Efficiency.Draw("AP")
    fit_func.Draw("same")
    legend.Draw("same")
    canvas.Print(outFileName)

    y = 0.99
    A = fit_func.GetParameter(0)
    AErr = fit_func.GetParError(0)
    print(fit_func.GetParError(0))
    B = fit_func.GetParameter(1)
    BErr = fit_func.GetParError(1)
    C = fit_func.GetParameter(2)
    CErr = fit_func.GetParError(2)

    #get 99 percent point from fit
    nineninepercentpoint = B*(np.log(y/(A-y))-C)
    nineninepercentpointErr = np.sqrt(((-B/(A-y))*AErr)**2+((np.log(y/(A-y))-C)*BErr)**2+((-B)*CErr)**2)
    print(nineninepercentpoint)
    print(nineninepercentpointErr)


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023C_"
inFileName = inDirectory+"PlotFitFunctionTriggerEff_Run2023C.root"
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
