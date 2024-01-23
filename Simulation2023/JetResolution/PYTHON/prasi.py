import ROOT
import numpy as np
import csv
from array import array

#takes three hists and turn them into pdf
def CalcResolution(hist,outFileName,yAxisTitle,xAxisTitle,title,param1,param2,param3):

    #fit and calculate FWHM
    fit_template = "[0]*exp(-(x-[1])**2/(2*[2]**2))"
    fit_func = ROOT.TF1("fit_func",fit_template,-0.2,0.2)
    fit_func.SetParameter(0,param1)
    fit_func.SetParameter(1,param2)
    fit_func.SetParameter(2,param3)
    fit_hist = hist.Clone()
    fit_hist.Fit(fit_func,"E")

    A = fit_func.GetParameter(0)
    AErr = fit_func.GetParError(0)
    B = fit_func.GetParameter(1)
    BErr = fit_func.GetParError(1)
    C = fit_func.GetParameter(2)
    CErr = fit_func.GetParError(2)

    FWHMPoint = np.sqrt(np.log(2)*2*C**2)+B
    FWHM = 2*(FWHMPoint-B)
    FWHM_Err=np.sqrt(8*np.log(2))*CErr

    #Plot FWHM as line with fit and simulation
    hist_graph = ROOT.TGraphAsymmErrors(fit_hist)

    canvas = ROOT.TCanvas("canvas")

    for i in range(0,int(hist.GetNbinsX())):
	    hist_graph.SetPointEXhigh(i,0.0)
	    hist_graph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)

    hist_graph.SetStats(0)
    hist_graph.SetLineColor(ROOT.kBlack)
    hist_graph.SetLineWidth(2)
    hist_graph.GetYaxis().SetTitle(yAxisTitle)
    hist_graph.GetXaxis().SetTitle(xAxisTitle)
    hist_graph.GetXaxis().SetRangeUser(hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
    hist_graph.SetTitle(title)
    legend.AddEntry(hist_graph,"Response","p")
    hist_graph.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"PlotJetResolution_Jet1_Run2023C.root"

histFiles = ROOT.TFile.Open(inFileName,"READ")

#Get Hist and Calculate Jet Resolution
Response3200 = histFiles.Get("ResponseJet13200")

CalcResolution(Response3200,outDirectory+"Response_Jet1_3200_Run2023_Test.pdf","Events","Response","Response for pt1 3200",10000,0,0.05)
