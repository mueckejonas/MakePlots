import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):

    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    for i in range(0,int(data1.GetNbinsX())):
	    Efficiency.SetPointEXhigh(i,0.0)
	    Efficiency.SetPointEXlow(i,0.0)

    fit_template = "1/(1+exp(-(x/[0])-[1]))"
    #fit_template = "1/(1+exp(-((x-[0])/[1])))"
    fit_func = ROOT.TF1("fit_func",fit_template,2300,3000)
    fit_func.SetParameter(0,500)
    fit_func.SetParameter(1,0)
    Efficiency.Fit(fit_func,"E")

    canvas = ROOT.TCanvas("canvas")

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
    B = fit_func.GetParameter(0)
    BErr = fit_func.GetParError(0)
    C = fit_func.GetParameter(1)
    CErr = fit_func.GetParError(1)

    #get 99 percent point from fit
    nineninepercentpoint = B*(-np.log((1/y)-1)-C)
    nineninepercentpointErr = np.sqrt((((-np.log((1/y)-1)-C))*BErr)**2+(-B*CErr)**2)
    print("99 Percent Point = "+str(nineninepercentpoint))
    print("99 Percent Point Error = "+str(nineninepercentpointErr))

    y = 0.999

    #get 999 percent point from fit
    ninenineninepercentpoint = B*(-np.log((1/y)-1)-C)
    ninenineninepercentpointErr = np.sqrt((((-np.log((1/y)-1)-C))*BErr)**2+(-B*CErr)**2)
    print("99.9 Percent Point = "+str(ninenineninepercentpoint))
    print("99.9 Percent Point Error = "+str(ninenineninepercentpointErr))

    print("Chi^2 = "+str(fit_func.GetChisquare()))
    print("Ndof = "+str(fit_func.GetNDF()))
    print("Chi^2/Ndof = "+str(fit_func.GetChisquare()/fit_func.GetNDF()))


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023D_"
inFileName = inDirectory+"PlotFitFunctionTriggerEff_Run2023D.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
HLT_PFJet = histFile.Get("HLT_PFJet")
HLT_PFHTJet = histFile.Get("HLT_PFHT")

#HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")
#HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")
#RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet550_500asreference.pdf",HLT_PFJet550,HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","pt1 [GeV]","Run2023B","Trigger Efficiency pt>550")

HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")

Ref_HLT_PFJet500 = HLT_PFJet.Get("Ref_HLT_PFJet500")

RootHisttoPdf(outDirectory+"PlottriggerEfficiency_withFit_HLT_PFJet550.pdf",HLT_PFJet550,Ref_HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","Mjj [GeV]","Run2023D","Trigger Efficiency pt>550")
