import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):

    #Efficiency = ROOT.TEfficiency(data1,data2)

    Plot_Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Plot_Efficiency.BayesDivide(data1,data2)

    for i in range(0,int(data1.GetNbinsX())):
        Plot_Efficiency.SetPointEXhigh(i,0.0)
        Plot_Efficiency.SetPointEXlow(i,0.0)

    fit_template = "1/(1+exp(-(x/[0])+46))"
    #fit_template = "1/(1+exp(-((x-[0])/[1]))"
    fit_func = ROOT.TF1("fit_func",fit_template,2300,3000)
    fit_func.SetParameter(0,46)
    #fit_func.SetParameter(1,-46)
    Plot_Efficiency.Fit(fit_func)


    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)

    legend = ROOT.TLegend(0.6,0.5,0.85,0.65)
    legend.SetTextSize(0.02)
    Plot_Efficiency.SetStats(0)
    Plot_Efficiency.SetLineColor(ROOT.kBlack)
    Plot_Efficiency.GetYaxis().SetTitle(yAxisTitle)
    Plot_Efficiency.GetXaxis().SetTitle(xAxisTitle)
    Plot_Efficiency.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    Plot_Efficiency.SetTitle(title+undertitle)
    Plot_Efficiency.SetMarkerStyle(4)
    legend.AddEntry(Plot_Efficiency,yAxisTitle,"p")
    legend.AddEntry(fit_func,"Logistic function fit","l")
    legend.SetLineWidth(0)
    #Set font size
    legend.SetTextSize(0.045)
    Plot_Efficiency.SetMarkerSize(3)
    Plot_Efficiency.SetLineWidth(2)
    Plot_Efficiency.GetYaxis().SetLabelSize(0.045)
    Plot_Efficiency.GetYaxis().SetTitleSize(0.05)
    Plot_Efficiency.GetXaxis().SetLabelSize(0.045)
    Plot_Efficiency.GetXaxis().SetTitleSize(0.05)
    #Plot_Efficiency.GetYaxis().SetLabelOffset(0.01)
    #Plot_Efficiency.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)
    Plot_Efficiency.Draw("AP")
    fit_func.Draw("same")
    legend.Draw("same")
    canvas.Print(outFileName)

    """
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
    """


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/RootB/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023B_"
inFileName = inDirectory+"PlotFitFunctionTriggerEff_Run2023B.root"
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
