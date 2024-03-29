import ROOT
import numpy as np
import csv
from array import array

euler_num = 2.718281828459045

#takes three hists and turn them into pdf
def CalcResolution(hist,outFileName,yAxisTitle,xAxisTitle,title,param1,param2,param3):

    #fit and calculate FWHM
    fit_template = "[0]*exp(-(x-[1])**2/(2*[2]**2))"
    fit_func = ROOT.TF1("fit_func",fit_template,-0.4,0.4)
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

    #Plot FWHM as line with fit and simulation
    hist_graph = ROOT.TGraphAsymmErrors(fit_hist)

    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)

    for i in range(0,int(hist.GetNbinsX())):
	    hist_graph.SetPointEXhigh(i,0.0)
	    hist_graph.SetPointEXlow(i,0.0)

    FWHMLine = ROOT.TLine(B,A*(1-1/euler_num),B+C,A*(1-1/euler_num))
    FWHMLine.SetLineColor(ROOT.kBlack)
    FWHMLine.SetLineWidth(2)

    legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
    legend.SetLineWidth(0)

    hist_graph.SetStats(0)
    hist_graph.SetLineColor(ROOT.kBlack)
    hist_graph.SetLineWidth(2)
    hist_graph.GetYaxis().SetTitle(yAxisTitle)
    hist_graph.GetXaxis().SetTitle(xAxisTitle)
    hist_graph.GetXaxis().SetRangeUser(hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
    hist_graph.SetTitle(title)
    legend.AddEntry(hist_graph,"Response","p")
    legend.AddEntry(fit_func,"Gauss Fit","l")
    legend.AddEntry(FWHMLine,"Sigma "+"("+str(round(C*100,2))+"+-"+str(round(CErr*100,6))+")"+"%","l")
    #Set font size
    legend.SetTextSize(0.045)
    hist_graph.SetMarkerSize(3)
    hist_graph.SetLineWidth(2)
    hist_graph.GetYaxis().SetLabelSize(0.045)
    hist_graph.GetYaxis().SetTitleSize(0.05)
    hist_graph.GetXaxis().SetLabelSize(0.045)
    hist_graph.GetXaxis().SetTitleSize(0.05)
    #hist_graph.GetYaxis().SetLabelOffset(0.01)
    #hist_graph.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)
    hist_graph.Draw("AP")
    fit_func.Draw("same")
    FWHMLine.Draw("same")
    legend.Draw("same")
    canvas.Print(outFileName)
    return abs(C), abs(CErr), B, BErr


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"PlotJetResolution_Jet1_Run2023_Sim.root"

histFiles = ROOT.TFile.Open(inFileName,"READ")

#Get Hist and Calculate Jet Resolution
Response50to80 = histFiles.Get("ResponseJet150to80")
Response80to120 = histFiles.Get("ResponseJet180to120")
Response120to170 = histFiles.Get("ResponseJet1120to170")
Response170to300 = histFiles.Get("ResponseJet1170to300")
Response300to470 = histFiles.Get("ResponseJet1300to470")
Response470to600 = histFiles.Get("ResponseJet1470to600")
Response600to800 = histFiles.Get("ResponseJet1600to800")
Response800to1000 = histFiles.Get("ResponseJet1800to1000")
Response1000to1400 = histFiles.Get("ResponseJet11000to1400")
Response1400to1800 = histFiles.Get("ResponseJet11400to1800")
Response1800to2400 = histFiles.Get("ResponseJet11800to2400")
Response2400to3200 = histFiles.Get("ResponseJet12400to3200")
Response3200 = histFiles.Get("ResponseJet13200")

JetResolution50to80, JetResolutionErr50to80, MeanResolution50to80, MeanResolutionErr50to80 = CalcResolution(Response50to80,outDirectory+"Response_Jet1_50to80_Run2023.pdf","Events","Response","Response for pt1 50to80",100000,0,0.05)
JetResolution80to120, JetResolutionErr80to120, MeanResolution80to120, MeanResolutionErr80to120 = CalcResolution(Response80to120,outDirectory+"Response_Jet1_80to120_Run2023.pdf","Events","Response","Response for pt1 80to120",100000,0,0.05)
JetResolution120to170, JetResolutionErr120to170, MeanResolution120to170, MeanResolutionErr120to170 = CalcResolution(Response120to170,outDirectory+"Response_Jet1_120to170_Run2023.pdf","Events","Response","Response for pt1 120to170",100000,0,0.05)
JetResolution170to300, JetResolutionErr170to300, MeanResolution170to300, MeanResolutionErr170to300 = CalcResolution(Response170to300,outDirectory+"Response_Jet1_170to300_Run2023.pdf","Events","Response","Response for pt1 170to300",100000,0,0.05)
JetResolution300to470, JetResolutionErr300to470, MeanResolution300to470, MeanResolutionErr300to470 = CalcResolution(Response300to470,outDirectory+"Response_Jet1_300to470_Run2023.pdf","Events","Response","Response for pt1 300to470",100000,0,0.05)
JetResolution470to600, JetResolutionErr470to600, MeanResolution470to600, MeanResolutionErr470to600 = CalcResolution(Response470to600,outDirectory+"Response_Jet1_470to600_Run2023.pdf","Events","Response","Response for pt1 470to600",100000,0,0.05)
JetResolution600to800, JetResolutionErr600to800, MeanResolution600to800, MeanResolutionErr600to800 = CalcResolution(Response600to800,outDirectory+"Response_Jet1_600to800_Run2023.pdf","Events","Response","Response for pt1 600to800",100000,0,0.05)
JetResolution800to1000, JetResolutionErr800to1000, MeanResolution800to1000, MeanResolutionErr800to1000 = CalcResolution(Response800to1000,outDirectory+"Response_Jet1_800to1000_Run2023.pdf","Events","Response","Response for pt1 800to1000",1600000,0,0.06)
JetResolution1000to1400, JetResolutionErr1000to1400, MeanResolution1000to1400, MeanResolutionErr1000to1400 = CalcResolution(Response1000to1400,outDirectory+"Response_Jet1_1000to1400_Run2023.pdf","Events","Response","Response for pt1 1000to1400",100000,0,0.05)
JetResolution1400to1800, JetResolutionErr1400to1800, MeanResolution1400to1800, MeanResolutionErr1400to1800 = CalcResolution(Response1400to1800,outDirectory+"Response_Jet1_1400to1800_Run2023.pdf","Events","Response","Response for pt1 1400to1800",2500000,0,0.1)
JetResolution1800to2400, JetResolutionErr1800to2400, MeanResolution1800to2400, MeanResolutionErr1800to2400 = CalcResolution(Response1800to2400,outDirectory+"Response_Jet1_1800to2400_Run2023.pdf","Events","Response","Response for pt1 1800to2400",1400000,0,0.05)
JetResolution2400to3200, JetResolutionErr2400to3200, MeanResolution2400to3200, MeanResolutionErr2400to3200 = CalcResolution(Response2400to3200,outDirectory+"Response_Jet1_2400to3200_Run2023.pdf","Events","Response","Response for pt1 2400to3200",100000,0,0.05)
JetResolution3200, JetResolutionErr3200, MeanResolution3200, MeanResolutionErr3200 = CalcResolution(Response3200,outDirectory+"Response_Jet1_3200_Run2023.pdf","Events","Response","Response for pt1 3200",10000,0,0.05)

JetResolution = np.array([JetResolution50to80,JetResolution80to120,JetResolution120to170,JetResolution170to300,JetResolution300to470,JetResolution470to600,JetResolution600to800,JetResolution800to1000,JetResolution1000to1400,JetResolution1400to1800,JetResolution1800to2400,JetResolution2400to3200,JetResolution3200])
JetResolutionErr = np.array([JetResolutionErr50to80,JetResolutionErr80to120,JetResolutionErr120to170,JetResolutionErr170to300,JetResolutionErr300to470,JetResolutionErr470to600,JetResolutionErr600to800,JetResolutionErr800to1000,JetResolutionErr1000to1400,JetResolutionErr1400to1800,JetResolutionErr1800to2400,JetResolutionErr2400to3200,JetResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,50/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,50/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#JetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(JetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(JetResolutionErr[i])
    yl.append(JetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetCanvasSize(1600,1100)
canvas.SetLogx()
JetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)
SaveJetResolutionGraph = JetResolutionGraph.Clone()

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,JetResolutionGraph.GetY()[i]+0.0015,JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        JetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,JetResolutionGraph.GetY()[i]+0.0015,JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        JetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
legend.SetLineWidth(0)

JetResolutionGraph.SetStats(0)
JetResolutionGraph.SetLineColor(ROOT.kBlack)
JetResolutionGraph.SetLineWidth(2)
JetResolutionGraph.GetXaxis().SetTitle("Pt1 [GeV]")
JetResolutionGraph.GetYaxis().SetTitle("JetResolution")
JetResolutionGraph.SetTitle("JetResolution for Jet1")
JetResolutionGraph.SetMarkerColor(ROOT.kBlack)
JetResolutionGraph.SetMarkerStyle(33)
JetResolutionGraph.SetMarkerSize(0)
JetResolutionGraph.GetXaxis().SetMoreLogLabels()
JetResolutionGraph.GetXaxis().SetNoExponent()
#Set font size
legend.SetTextSize(0.045)
JetResolutionGraph.SetMarkerSize(3)
JetResolutionGraph.SetLineWidth(2)
JetResolutionGraph.GetYaxis().SetLabelSize(0.045)
JetResolutionGraph.GetYaxis().SetTitleSize(0.05)
JetResolutionGraph.GetXaxis().SetLabelSize(0.045)
JetResolutionGraph.GetXaxis().SetTitleSize(0.05)
#JetResolutionGraph.GetYaxis().SetLabelOffset(0.01)
#JetResolutionGraph.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)

legend.AddEntry(JetResolutionGraph,"JetResolution","l")

JetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"JetResolutionfromPt1_Run2023Sim.pdf")

MeanResolution = np.array([MeanResolution50to80,MeanResolution80to120,MeanResolution120to170,MeanResolution170to300,MeanResolution300to470,MeanResolution470to600,MeanResolution600to800,MeanResolution800to1000,MeanResolution1000to1400,MeanResolution1400to1800,MeanResolution1800to2400,MeanResolution2400to3200,MeanResolution3200])
MeanResolutionErr = np.array([MeanResolutionErr50to80,MeanResolutionErr80to120,MeanResolutionErr120to170,MeanResolutionErr170to300,MeanResolutionErr300to470,MeanResolutionErr470to600,MeanResolutionErr600to800,MeanResolutionErr800to1000,MeanResolutionErr1000to1400,MeanResolutionErr1400to1800,MeanResolutionErr1800to2400,MeanResolutionErr2400to3200,MeanResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,50/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,50/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#MeanResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(MeanResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(MeanResolutionErr[i])
    yl.append(MeanResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetCanvasSize(1600,1100)
canvas.SetLogx()
MeanResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)
SaveMeanResolutionGraph = MeanResolutionGraph.Clone()

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(MeanResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,MeanResolutionGraph.GetY()[i]+0.0015,MeanResolutionLabels[i])
        latex.SetTextSize(0.02)
        MeanResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(MeanResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,MeanResolutionGraph.GetY()[i]+0.0015,MeanResolutionLabels[i])
        latex.SetTextSize(0.02)
        MeanResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
legend.SetLineWidth(0)

MeanResolutionGraph.SetStats(0)
MeanResolutionGraph.SetLineColor(ROOT.kBlack)
MeanResolutionGraph.SetLineWidth(2)
MeanResolutionGraph.GetXaxis().SetTitle("Pt1 [GeV]")
MeanResolutionGraph.GetYaxis().SetTitle("MeanResolution")
MeanResolutionGraph.SetTitle("MeanResolution for Jet1")
MeanResolutionGraph.SetMarkerColor(ROOT.kBlack)
MeanResolutionGraph.SetMarkerStyle(33)
MeanResolutionGraph.SetMarkerSize(0)
MeanResolutionGraph.GetXaxis().SetMoreLogLabels()
MeanResolutionGraph.GetXaxis().SetNoExponent()
#Set font size
legend.SetTextSize(0.045)
MeanResolutionGraph.SetMarkerSize(3)
MeanResolutionGraph.SetLineWidth(2)
MeanResolutionGraph.GetYaxis().SetLabelSize(0.045)
MeanResolutionGraph.GetYaxis().SetTitleSize(0.05)
MeanResolutionGraph.GetXaxis().SetLabelSize(0.045)
MeanResolutionGraph.GetXaxis().SetTitleSize(0.05)
#MeanResolutionGraph.GetYaxis().SetLabelOffset(0.01)
#MeanResolutionGraph.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)

legend.AddEntry(MeanResolutionGraph,"MeanResolution","l")

MeanResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"MeanResolutionfromPt1_Run2023Sim.pdf")

#create and save root file with all added hists
outHistFile = ROOT.TFile.Open("/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/FitJetResolutionJet1.root","RECREATE")
SaveJetResolutionGraph.Write()
SaveMeanResolutionGraph.Write()
outHistFile.Close()
