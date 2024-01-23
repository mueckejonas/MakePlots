import ROOT
import numpy as np
import csv
from array import array

euler_num = 2.718281828459045

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

    #Plot FWHM as line with fit and simulation
    hist_graph = ROOT.TGraphAsymmErrors(fit_hist)

    canvas = ROOT.TCanvas("canvas")

    for i in range(0,int(hist.GetNbinsX())):
	    hist_graph.SetPointEXhigh(i,0.0)
	    hist_graph.SetPointEXlow(i,0.0)

    FWHMLine = ROOT.TLine(B,A*(1-1/euler_num),B+C,A*(1-1/euler_num))
    FWHMLine.SetLineColor(ROOT.kBlack)
    FWHMLine.SetLineWidth(2)

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
    legend.AddEntry(fit_func,"Gauss Fit","l")
    legend.AddEntry(FWHMLine,"Sigma "+"("+str(round(C*100,2))+"+-"+str(round(CErr*100,6))+")"+"%","l")
    hist_graph.Draw("AP")
    fit_func.Draw("same")
    FWHMLine.Draw("same")
    legend.Draw("same")
    canvas.Print(outFileName)
    return abs(C), abs(CErr)


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"PlotJetResolution_Jet3_Run2023C.root"

histFiles = ROOT.TFile.Open(inFileName,"READ")

#Calculate resolution for Eta0to1p3
#Get Hist and Calculate Jet Resolution
Eta0to1p3Response50to80 = histFiles.Get("Eta0to1p3ResponseJet350to80")
Eta0to1p3Response80to120 = histFiles.Get("Eta0to1p3ResponseJet380to120")
Eta0to1p3Response120to170 = histFiles.Get("Eta0to1p3ResponseJet3120to170")
Eta0to1p3Response170to300 = histFiles.Get("Eta0to1p3ResponseJet3170to300")
Eta0to1p3Response300to470 = histFiles.Get("Eta0to1p3ResponseJet3300to470")
Eta0to1p3Response470to600 = histFiles.Get("Eta0to1p3ResponseJet3470to600")
Eta0to1p3Response600to800 = histFiles.Get("Eta0to1p3ResponseJet3600to800")
Eta0to1p3Response800to1000 = histFiles.Get("Eta0to1p3ResponseJet3800to1000")
Eta0to1p3Response1000to1400 = histFiles.Get("Eta0to1p3ResponseJet31000to1400")
Eta0to1p3Response1400to1800 = histFiles.Get("Eta0to1p3ResponseJet31400to1800")
Eta0to1p3Response1800to2400 = histFiles.Get("Eta0to1p3ResponseJet31800to2400")
Eta0to1p3Response2400to3200 = histFiles.Get("Eta0to1p3ResponseJet32400to3200")
Eta0to1p3Response3200 = histFiles.Get("Eta0to1p3ResponseJet33200")

Eta0to1p3JetResolution50to80, Eta0to1p3JetResolutionErr50to80 = CalcResolution(Eta0to1p3Response50to80,outDirectory+"Eta0to1p3_Response_Jet3_50to80_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 50to80",10000,0,0.05)
Eta0to1p3JetResolution80to120, Eta0to1p3JetResolutionErr80to120 = CalcResolution(Eta0to1p3Response80to120,outDirectory+"Eta0to1p3_Response_Jet3_80to120_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 80to120",10000,0,0.05)
Eta0to1p3JetResolution120to170, Eta0to1p3JetResolutionErr120to170 = CalcResolution(Eta0to1p3Response120to170,outDirectory+"Eta0to1p3_Response_Jet3_120to170_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 120to170",10000,0,0.05)
Eta0to1p3JetResolution170to300, Eta0to1p3JetResolutionErr170to300 = CalcResolution(Eta0to1p3Response170to300,outDirectory+"Eta0to1p3_Response_Jet3_170to300_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 170to300",10000,0,0.05)
Eta0to1p3JetResolution300to470, Eta0to1p3JetResolutionErr300to470 = CalcResolution(Eta0to1p3Response300to470,outDirectory+"Eta0to1p3_Response_Jet3_300to470_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 300to470",10000,0,0.05)
Eta0to1p3JetResolution470to600, Eta0to1p3JetResolutionErr470to600 = CalcResolution(Eta0to1p3Response470to600,outDirectory+"Eta0to1p3_Response_Jet3_470to600_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 470to600",10000,0,0.05)
Eta0to1p3JetResolution600to800, Eta0to1p3JetResolutionErr600to800 = CalcResolution(Eta0to1p3Response600to800,outDirectory+"Eta0to1p3_Response_Jet3_600to800_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 600to800",10000,0,0.05)
Eta0to1p3JetResolution800to1000, Eta0to1p3JetResolutionErr800to1000 = CalcResolution(Eta0to1p3Response800to1000,outDirectory+"Eta0to1p3_Response_Jet3_800to1000_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 800to1000",10000,0,0.05)
Eta0to1p3JetResolution1000to1400, Eta0to1p3JetResolutionErr1000to1400 = CalcResolution(Eta0to1p3Response1000to1400,outDirectory+"Eta0to1p3_Response_Jet3_1000to1400_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 1000to1400",10000,0,0.05)
Eta0to1p3JetResolution1400to1800, Eta0to1p3JetResolutionErr1400to1800 = CalcResolution(Eta0to1p3Response1400to1800,outDirectory+"Eta0to1p3_Response_Jet3_1400to1800_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 1400to1800",2500000,0,0.1)
Eta0to1p3JetResolution1800to2400, Eta0to1p3JetResolutionErr1800to2400 = CalcResolution(Eta0to1p3Response1800to2400,outDirectory+"Eta0to1p3_Response_Jet3_1800to2400_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 1800to2400",140000,0,0.08)
Eta0to1p3JetResolution2400to3200, Eta0to1p3JetResolutionErr2400to3200 = CalcResolution(Eta0to1p3Response2400to3200,outDirectory+"Eta0to1p3_Response_Jet3_2400to3200_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 2400to3200",10000,0,0.05)
Eta0to1p3JetResolution3200, Eta0to1p3JetResolutionErr3200 = CalcResolution(Eta0to1p3Response3200,outDirectory+"Eta0to1p3_Response_Jet3_3200_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt3 3200",10000,0,0.05)

Eta0to1p3JetResolution = np.array([Eta0to1p3JetResolution50to80,Eta0to1p3JetResolution80to120,Eta0to1p3JetResolution120to170,Eta0to1p3JetResolution170to300,Eta0to1p3JetResolution300to470,Eta0to1p3JetResolution470to600,Eta0to1p3JetResolution600to800,Eta0to1p3JetResolution800to1000,Eta0to1p3JetResolution1000to1400,Eta0to1p3JetResolution1400to1800,Eta0to1p3JetResolution1800to2400,Eta0to1p3JetResolution2400to3200,Eta0to1p3JetResolution3200])
Eta0to1p3JetResolutionErr = np.array([Eta0to1p3JetResolutionErr50to80,Eta0to1p3JetResolutionErr80to120,Eta0to1p3JetResolutionErr120to170,Eta0to1p3JetResolutionErr170to300,Eta0to1p3JetResolutionErr300to470,Eta0to1p3JetResolutionErr470to600,Eta0to1p3JetResolutionErr600to800,Eta0to1p3JetResolutionErr800to1000,Eta0to1p3JetResolutionErr1000to1400,Eta0to1p3JetResolutionErr1400to1800,Eta0to1p3JetResolutionErr1800to2400,Eta0to1p3JetResolutionErr2400to3200,Eta0to1p3JetResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#Eta0to1p3JetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(Eta0to1p3JetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(Eta0to1p3JetResolutionErr[i])
    yl.append(Eta0to1p3JetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
Eta0to1p3JetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(Eta0to1p3JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,Eta0to1p3JetResolutionGraph.GetY()[i]+0.0015,Eta0to1p3JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta0to1p3JetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(Eta0to1p3JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,Eta0to1p3JetResolutionGraph.GetY()[i]+0.0015,Eta0to1p3JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta0to1p3JetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

Eta0to1p3JetResolutionGraph.SetStats(0)
Eta0to1p3JetResolutionGraph.SetLineColor(ROOT.kBlack)
Eta0to1p3JetResolutionGraph.SetLineWidth(2)
Eta0to1p3JetResolutionGraph.GetXaxis().SetTitle("Pt3 [GeV]")
Eta0to1p3JetResolutionGraph.GetYaxis().SetTitle("JetResolution")
Eta0to1p3JetResolutionGraph.SetTitle("Eta 0 to 1.3 JetResolution for Jet3")
Eta0to1p3JetResolutionGraph.SetMarkerColor(ROOT.kBlack)
Eta0to1p3JetResolutionGraph.SetMarkerStyle(33)
Eta0to1p3JetResolutionGraph.SetMarkerSize(0)
Eta0to1p3JetResolutionGraph.GetXaxis().SetMoreLogLabels()
Eta0to1p3JetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(Eta0to1p3JetResolutionGraph,"JetResolution","l")

Eta0to1p3JetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta0to1p3JetResolutionfromPt3_Run2023Sim.pdf")

header = ['PtRange', 'Eta0to1p3JetResolution', 'Eta0to1p3JetResolutionErr']
data = [
    ['50to80', Eta0to1p3JetResolution50to80,Eta0to1p3JetResolutionErr50to80],
    ['80to120', Eta0to1p3JetResolution80to120,Eta0to1p3JetResolutionErr80to120],
    ['120to170', Eta0to1p3JetResolution120to170,Eta0to1p3JetResolutionErr120to170],
    ['170to300', Eta0to1p3JetResolution170to300,Eta0to1p3JetResolutionErr170to300],
    ['300to470', Eta0to1p3JetResolution300to470,Eta0to1p3JetResolutionErr300to470],
    ['470to600', Eta0to1p3JetResolution470to600,Eta0to1p3JetResolutionErr470to600],
    ['600to800', Eta0to1p3JetResolution600to800,Eta0to1p3JetResolutionErr600to800],
    ['800to1000', Eta0to1p3JetResolution800to1000,Eta0to1p3JetResolutionErr800to1000],
    ['1000to1400', Eta0to1p3JetResolution1000to1400,Eta0to1p3JetResolutionErr1000to1400],
    ['1400to1800', Eta0to1p3JetResolution1400to1800,Eta0to1p3JetResolutionErr1400to1800],
    ['1800to2400', Eta0to1p3JetResolution1800to2400,Eta0to1p3JetResolutionErr1800to2400],
    ['2400to3200', Eta0to1p3JetResolution2400to3200,Eta0to1p3JetResolutionErr2400to3200],
    ['3200', Eta0to1p3JetResolution3200,Eta0to1p3JetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta0to1p3JetResolutionPt3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

#Calculate resolution for Eta1p3to2p5
#Get Hist and Calculate Jet Resolution
Eta1p3to2p5Response50to80 = histFiles.Get("Eta1p3to2p5ResponseJet350to80")
Eta1p3to2p5Response80to120 = histFiles.Get("Eta1p3to2p5ResponseJet380to120")
Eta1p3to2p5Response120to170 = histFiles.Get("Eta1p3to2p5ResponseJet3120to170")
Eta1p3to2p5Response170to300 = histFiles.Get("Eta1p3to2p5ResponseJet3170to300")
Eta1p3to2p5Response300to470 = histFiles.Get("Eta1p3to2p5ResponseJet3300to470")
Eta1p3to2p5Response470to600 = histFiles.Get("Eta1p3to2p5ResponseJet3470to600")
Eta1p3to2p5Response600to800 = histFiles.Get("Eta1p3to2p5ResponseJet3600to800")
Eta1p3to2p5Response800to1000 = histFiles.Get("Eta1p3to2p5ResponseJet3800to1000")
Eta1p3to2p5Response1000to1400 = histFiles.Get("Eta1p3to2p5ResponseJet31000to1400")
Eta1p3to2p5Response1400to1800 = histFiles.Get("Eta1p3to2p5ResponseJet31400to1800")
Eta1p3to2p5Response1800to2400 = histFiles.Get("Eta1p3to2p5ResponseJet31800to2400")
Eta1p3to2p5Response2400to3200 = histFiles.Get("Eta1p3to2p5ResponseJet32400to3200")
Eta1p3to2p5Response3200 = histFiles.Get("Eta1p3to2p5ResponseJet33200")

Eta1p3to2p5JetResolution50to80, Eta1p3to2p5JetResolutionErr50to80 = CalcResolution(Eta1p3to2p5Response50to80,outDirectory+"Eta1p3to2p5_Response_Jet3_50to80_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 50to80",10000,0,0.05)
Eta1p3to2p5JetResolution80to120, Eta1p3to2p5JetResolutionErr80to120 = CalcResolution(Eta1p3to2p5Response80to120,outDirectory+"Eta1p3to2p5_Response_Jet3_80to120_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 80to120",10000,0,0.05)
Eta1p3to2p5JetResolution120to170, Eta1p3to2p5JetResolutionErr120to170 = CalcResolution(Eta1p3to2p5Response120to170,outDirectory+"Eta1p3to2p5_Response_Jet3_120to170_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 120to170",10000,0,0.05)
Eta1p3to2p5JetResolution170to300, Eta1p3to2p5JetResolutionErr170to300 = CalcResolution(Eta1p3to2p5Response170to300,outDirectory+"Eta1p3to2p5_Response_Jet3_170to300_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 170to300",10000,0,0.05)
Eta1p3to2p5JetResolution300to470, Eta1p3to2p5JetResolutionErr300to470 = CalcResolution(Eta1p3to2p5Response300to470,outDirectory+"Eta1p3to2p5_Response_Jet3_300to470_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 300to470",10000,0,0.05)
Eta1p3to2p5JetResolution470to600, Eta1p3to2p5JetResolutionErr470to600 = CalcResolution(Eta1p3to2p5Response470to600,outDirectory+"Eta1p3to2p5_Response_Jet3_470to600_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 470to600",10000,0,0.05)
Eta1p3to2p5JetResolution600to800, Eta1p3to2p5JetResolutionErr600to800 = CalcResolution(Eta1p3to2p5Response600to800,outDirectory+"Eta1p3to2p5_Response_Jet3_600to800_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 600to800",10000,0,0.05)
Eta1p3to2p5JetResolution800to1000, Eta1p3to2p5JetResolutionErr800to1000 = CalcResolution(Eta1p3to2p5Response800to1000,outDirectory+"Eta1p3to2p5_Response_Jet3_800to1000_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 800to1000",10000,0,0.05)
Eta1p3to2p5JetResolution1000to1400, Eta1p3to2p5JetResolutionErr1000to1400 = CalcResolution(Eta1p3to2p5Response1000to1400,outDirectory+"Eta1p3to2p5_Response_Jet3_1000to1400_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 1000to1400",10000,0,0.05)
Eta1p3to2p5JetResolution1400to1800, Eta1p3to2p5JetResolutionErr1400to1800 = CalcResolution(Eta1p3to2p5Response1400to1800,outDirectory+"Eta1p3to2p5_Response_Jet3_1400to1800_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 1400to1800",2500000,0,0.1)
Eta1p3to2p5JetResolution1800to2400, Eta1p3to2p5JetResolutionErr1800to2400 = CalcResolution(Eta1p3to2p5Response1800to2400,outDirectory+"Eta1p3to2p5_Response_Jet3_1800to2400_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 1800to2400",140000,0,0.08)
Eta1p3to2p5JetResolution2400to3200, Eta1p3to2p5JetResolutionErr2400to3200 = CalcResolution(Eta1p3to2p5Response2400to3200,outDirectory+"Eta1p3to2p5_Response_Jet3_2400to3200_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 2400to3200",10000,0,0.05)
Eta1p3to2p5JetResolution3200, Eta1p3to2p5JetResolutionErr3200 = CalcResolution(Eta1p3to2p5Response3200,outDirectory+"Eta1p3to2p5_Response_Jet3_3200_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt3 3200",10000,0,0.05)

Eta1p3to2p5JetResolution = np.array([Eta1p3to2p5JetResolution50to80,Eta1p3to2p5JetResolution80to120,Eta1p3to2p5JetResolution120to170,Eta1p3to2p5JetResolution170to300,Eta1p3to2p5JetResolution300to470,Eta1p3to2p5JetResolution470to600,Eta1p3to2p5JetResolution600to800,Eta1p3to2p5JetResolution800to1000,Eta1p3to2p5JetResolution1000to1400,Eta1p3to2p5JetResolution1400to1800,Eta1p3to2p5JetResolution1800to2400,Eta1p3to2p5JetResolution2400to3200,Eta1p3to2p5JetResolution3200])
Eta1p3to2p5JetResolutionErr = np.array([Eta1p3to2p5JetResolutionErr50to80,Eta1p3to2p5JetResolutionErr80to120,Eta1p3to2p5JetResolutionErr120to170,Eta1p3to2p5JetResolutionErr170to300,Eta1p3to2p5JetResolutionErr300to470,Eta1p3to2p5JetResolutionErr470to600,Eta1p3to2p5JetResolutionErr600to800,Eta1p3to2p5JetResolutionErr800to1000,Eta1p3to2p5JetResolutionErr1000to1400,Eta1p3to2p5JetResolutionErr1400to1800,Eta1p3to2p5JetResolutionErr1800to2400,Eta1p3to2p5JetResolutionErr2400to3200,Eta1p3to2p5JetResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#Eta1p3to2p5JetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(Eta1p3to2p5JetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(Eta1p3to2p5JetResolutionErr[i])
    yl.append(Eta1p3to2p5JetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
Eta1p3to2p5JetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(Eta1p3to2p5JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,Eta1p3to2p5JetResolutionGraph.GetY()[i]+0.0015,Eta1p3to2p5JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta1p3to2p5JetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(Eta1p3to2p5JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,Eta1p3to2p5JetResolutionGraph.GetY()[i]+0.0015,Eta1p3to2p5JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta1p3to2p5JetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

Eta1p3to2p5JetResolutionGraph.SetStats(0)
Eta1p3to2p5JetResolutionGraph.SetLineColor(ROOT.kBlack)
Eta1p3to2p5JetResolutionGraph.SetLineWidth(2)
Eta1p3to2p5JetResolutionGraph.GetXaxis().SetTitle("Pt3 [GeV]")
Eta1p3to2p5JetResolutionGraph.GetYaxis().SetTitle("JetResolution")
Eta1p3to2p5JetResolutionGraph.SetTitle("Eta 1.3 to 2.5 JetResolution for Jet3")
Eta1p3to2p5JetResolutionGraph.SetMarkerColor(ROOT.kBlack)
Eta1p3to2p5JetResolutionGraph.SetMarkerStyle(33)
Eta1p3to2p5JetResolutionGraph.SetMarkerSize(0)
Eta1p3to2p5JetResolutionGraph.GetXaxis().SetMoreLogLabels()
Eta1p3to2p5JetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(Eta1p3to2p5JetResolutionGraph,"JetResolution","l")

Eta1p3to2p5JetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta1p3to2p5JetResolutionfromPt3_Run2023Sim.pdf")

header = ['PtRange', 'Eta1p3to2p5JetResolution', 'Eta1p3to2p5JetResolutionErr']
data = [
    ['50to80', Eta1p3to2p5JetResolution50to80,Eta1p3to2p5JetResolutionErr50to80],
    ['80to120', Eta1p3to2p5JetResolution80to120,Eta1p3to2p5JetResolutionErr80to120],
    ['120to170', Eta1p3to2p5JetResolution120to170,Eta1p3to2p5JetResolutionErr120to170],
    ['170to300', Eta1p3to2p5JetResolution170to300,Eta1p3to2p5JetResolutionErr170to300],
    ['300to470', Eta1p3to2p5JetResolution300to470,Eta1p3to2p5JetResolutionErr300to470],
    ['470to600', Eta1p3to2p5JetResolution470to600,Eta1p3to2p5JetResolutionErr470to600],
    ['600to800', Eta1p3to2p5JetResolution600to800,Eta1p3to2p5JetResolutionErr600to800],
    ['800to1000', Eta1p3to2p5JetResolution800to1000,Eta1p3to2p5JetResolutionErr800to1000],
    ['1000to1400', Eta1p3to2p5JetResolution1000to1400,Eta1p3to2p5JetResolutionErr1000to1400],
    ['1400to1800', Eta1p3to2p5JetResolution1400to1800,Eta1p3to2p5JetResolutionErr1400to1800],
    ['1800to2400', Eta1p3to2p5JetResolution1800to2400,Eta1p3to2p5JetResolutionErr1800to2400],
    ['2400to3200', Eta1p3to2p5JetResolution2400to3200,Eta1p3to2p5JetResolutionErr2400to3200],
    ['3200', Eta1p3to2p5JetResolution3200,Eta1p3to2p5JetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta1p3to2p5JetResolutionPt3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

#Calculate resolution for Eta2p5to3
#Get Hist and Calculate Jet Resolution
Eta2p5to3Response50to80 = histFiles.Get("Eta2p5to3ResponseJet350to80")
Eta2p5to3Response80to120 = histFiles.Get("Eta2p5to3ResponseJet380to120")
Eta2p5to3Response120to170 = histFiles.Get("Eta2p5to3ResponseJet3120to170")
Eta2p5to3Response170to300 = histFiles.Get("Eta2p5to3ResponseJet3170to300")
Eta2p5to3Response300to470 = histFiles.Get("Eta2p5to3ResponseJet3300to470")
Eta2p5to3Response470to600 = histFiles.Get("Eta2p5to3ResponseJet3470to600")
Eta2p5to3Response600to800 = histFiles.Get("Eta2p5to3ResponseJet3600to800")
Eta2p5to3Response800to1000 = histFiles.Get("Eta2p5to3ResponseJet3800to1000")
Eta2p5to3Response1000to1400 = histFiles.Get("Eta2p5to3ResponseJet31000to1400")
Eta2p5to3Response1400to1800 = histFiles.Get("Eta2p5to3ResponseJet31400to1800")
Eta2p5to3Response1800to2400 = histFiles.Get("Eta2p5to3ResponseJet31800to2400")
Eta2p5to3Response2400to3200 = histFiles.Get("Eta2p5to3ResponseJet32400to3200")
Eta2p5to3Response3200 = histFiles.Get("Eta2p5to3ResponseJet33200")

Eta2p5to3JetResolution50to80, Eta2p5to3JetResolutionErr50to80 = CalcResolution(Eta2p5to3Response50to80,outDirectory+"Eta2p5to3_Response_Jet3_50to80_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 50to80",10000,0,0.05)
Eta2p5to3JetResolution80to120, Eta2p5to3JetResolutionErr80to120 = CalcResolution(Eta2p5to3Response80to120,outDirectory+"Eta2p5to3_Response_Jet3_80to120_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 80to120",10000,0,0.05)
Eta2p5to3JetResolution120to170, Eta2p5to3JetResolutionErr120to170 = CalcResolution(Eta2p5to3Response120to170,outDirectory+"Eta2p5to3_Response_Jet3_120to170_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 120to170",10000,0,0.05)
Eta2p5to3JetResolution170to300, Eta2p5to3JetResolutionErr170to300 = CalcResolution(Eta2p5to3Response170to300,outDirectory+"Eta2p5to3_Response_Jet3_170to300_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 170to300",10000,0,0.05)
Eta2p5to3JetResolution300to470, Eta2p5to3JetResolutionErr300to470 = CalcResolution(Eta2p5to3Response300to470,outDirectory+"Eta2p5to3_Response_Jet3_300to470_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 300to470",10000,0,0.05)
Eta2p5to3JetResolution470to600, Eta2p5to3JetResolutionErr470to600 = CalcResolution(Eta2p5to3Response470to600,outDirectory+"Eta2p5to3_Response_Jet3_470to600_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 470to600",10000,0,0.05)
Eta2p5to3JetResolution600to800, Eta2p5to3JetResolutionErr600to800 = CalcResolution(Eta2p5to3Response600to800,outDirectory+"Eta2p5to3_Response_Jet3_600to800_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 600to800",10000,0,0.05)
Eta2p5to3JetResolution800to1000, Eta2p5to3JetResolutionErr800to1000 = CalcResolution(Eta2p5to3Response800to1000,outDirectory+"Eta2p5to3_Response_Jet3_800to1000_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 800to1000",10000,0,0.05)
Eta2p5to3JetResolution1000to1400, Eta2p5to3JetResolutionErr1000to1400 = CalcResolution(Eta2p5to3Response1000to1400,outDirectory+"Eta2p5to3_Response_Jet3_1000to1400_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 1000to1400",10000,0,0.05)
Eta2p5to3JetResolution1400to1800, Eta2p5to3JetResolutionErr1400to1800 = CalcResolution(Eta2p5to3Response1400to1800,outDirectory+"Eta2p5to3_Response_Jet3_1400to1800_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 1400to1800",2500000,0,0.1)
Eta2p5to3JetResolution1800to2400, Eta2p5to3JetResolutionErr1800to2400 = CalcResolution(Eta2p5to3Response1800to2400,outDirectory+"Eta2p5to3_Response_Jet3_1800to2400_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 1800to2400",140000,0,0.08)
Eta2p5to3JetResolution2400to3200, Eta2p5to3JetResolutionErr2400to3200 = CalcResolution(Eta2p5to3Response2400to3200,outDirectory+"Eta2p5to3_Response_Jet3_2400to3200_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 2400to3200",10000,0,0.05)
Eta2p5to3JetResolution3200, Eta2p5to3JetResolutionErr3200 = CalcResolution(Eta2p5to3Response3200,outDirectory+"Eta2p5to3_Response_Jet3_3200_Run2023.pdf","Events","Eta 2.5 to 3 Response","Eta 2.5 to 3 Response for pt3 3200",10000,0,0.05)

Eta2p5to3JetResolution = np.array([Eta2p5to3JetResolution50to80,Eta2p5to3JetResolution80to120,Eta2p5to3JetResolution120to170,Eta2p5to3JetResolution170to300,Eta2p5to3JetResolution300to470,Eta2p5to3JetResolution470to600,Eta2p5to3JetResolution600to800,Eta2p5to3JetResolution800to1000,Eta2p5to3JetResolution1000to1400,Eta2p5to3JetResolution1400to1800,Eta2p5to3JetResolution1800to2400,Eta2p5to3JetResolution2400to3200,Eta2p5to3JetResolution3200])
Eta2p5to3JetResolutionErr = np.array([Eta2p5to3JetResolutionErr50to80,Eta2p5to3JetResolutionErr80to120,Eta2p5to3JetResolutionErr120to170,Eta2p5to3JetResolutionErr170to300,Eta2p5to3JetResolutionErr300to470,Eta2p5to3JetResolutionErr470to600,Eta2p5to3JetResolutionErr600to800,Eta2p5to3JetResolutionErr800to1000,Eta2p5to3JetResolutionErr1000to1400,Eta2p5to3JetResolutionErr1400to1800,Eta2p5to3JetResolutionErr1800to2400,Eta2p5to3JetResolutionErr2400to3200,Eta2p5to3JetResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#Eta2p5to3JetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(Eta2p5to3JetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(Eta2p5to3JetResolutionErr[i])
    yl.append(Eta2p5to3JetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
Eta2p5to3JetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(Eta2p5to3JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,Eta2p5to3JetResolutionGraph.GetY()[i]+0.0015,Eta2p5to3JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta2p5to3JetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(Eta2p5to3JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,Eta2p5to3JetResolutionGraph.GetY()[i]+0.0015,Eta2p5to3JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta2p5to3JetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

Eta2p5to3JetResolutionGraph.SetStats(0)
Eta2p5to3JetResolutionGraph.SetLineColor(ROOT.kBlack)
Eta2p5to3JetResolutionGraph.SetLineWidth(2)
Eta2p5to3JetResolutionGraph.GetXaxis().SetTitle("Pt3 [GeV]")
Eta2p5to3JetResolutionGraph.GetYaxis().SetTitle("JetResolution")
Eta2p5to3JetResolutionGraph.SetTitle("Eta 2.5 to 3 JetResolution for Jet3")
Eta2p5to3JetResolutionGraph.SetMarkerColor(ROOT.kBlack)
Eta2p5to3JetResolutionGraph.SetMarkerStyle(33)
Eta2p5to3JetResolutionGraph.SetMarkerSize(0)
Eta2p5to3JetResolutionGraph.GetXaxis().SetMoreLogLabels()
Eta2p5to3JetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(Eta2p5to3JetResolutionGraph,"JetResolution","l")

Eta2p5to3JetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta2p5to3JetResolutionfromPt3_Run2023Sim.pdf")

header = ['PtRange', 'Eta2p5to3JetResolution', 'Eta2p5to3JetResolutionErr']
data = [
    ['50to80', Eta2p5to3JetResolution50to80,Eta2p5to3JetResolutionErr50to80],
    ['80to120', Eta2p5to3JetResolution80to120,Eta2p5to3JetResolutionErr80to120],
    ['120to170', Eta2p5to3JetResolution120to170,Eta2p5to3JetResolutionErr120to170],
    ['170to300', Eta2p5to3JetResolution170to300,Eta2p5to3JetResolutionErr170to300],
    ['300to470', Eta2p5to3JetResolution300to470,Eta2p5to3JetResolutionErr300to470],
    ['470to600', Eta2p5to3JetResolution470to600,Eta2p5to3JetResolutionErr470to600],
    ['600to800', Eta2p5to3JetResolution600to800,Eta2p5to3JetResolutionErr600to800],
    ['800to1000', Eta2p5to3JetResolution800to1000,Eta2p5to3JetResolutionErr800to1000],
    ['1000to1400', Eta2p5to3JetResolution1000to1400,Eta2p5to3JetResolutionErr1000to1400],
    ['1400to1800', Eta2p5to3JetResolution1400to1800,Eta2p5to3JetResolutionErr1400to1800],
    ['1800to2400', Eta2p5to3JetResolution1800to2400,Eta2p5to3JetResolutionErr1800to2400],
    ['2400to3200', Eta2p5to3JetResolution2400to3200,Eta2p5to3JetResolutionErr2400to3200],
    ['3200', Eta2p5to3JetResolution3200,Eta2p5to3JetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta2p5to3JetResolutionPt3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

#Calculate resolution for Eta3to5
#Get Hist and Calculate Jet Resolution
Eta3to5Response50to80 = histFiles.Get("Eta3to5ResponseJet350to80")
Eta3to5Response80to120 = histFiles.Get("Eta3to5ResponseJet380to120")
Eta3to5Response120to170 = histFiles.Get("Eta3to5ResponseJet3120to170")
Eta3to5Response170to300 = histFiles.Get("Eta3to5ResponseJet3170to300")
Eta3to5Response300to470 = histFiles.Get("Eta3to5ResponseJet3300to470")
Eta3to5Response470to600 = histFiles.Get("Eta3to5ResponseJet3470to600")
Eta3to5Response600to800 = histFiles.Get("Eta3to5ResponseJet3600to800")
Eta3to5Response800to1000 = histFiles.Get("Eta3to5ResponseJet3800to1000")
Eta3to5Response1000to1400 = histFiles.Get("Eta3to5ResponseJet31000to1400")
Eta3to5Response1400to1800 = histFiles.Get("Eta3to5ResponseJet31400to1800")
Eta3to5Response1800to2400 = histFiles.Get("Eta3to5ResponseJet31800to2400")
Eta3to5Response2400to3200 = histFiles.Get("Eta3to5ResponseJet32400to3200")
Eta3to5Response3200 = histFiles.Get("Eta3to5ResponseJet33200")

Eta3to5JetResolution50to80, Eta3to5JetResolutionErr50to80 = CalcResolution(Eta3to5Response50to80,outDirectory+"Eta3to5_Response_Jet3_50to80_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 50to80",10000,0,0.05)
Eta3to5JetResolution80to120, Eta3to5JetResolutionErr80to120 = CalcResolution(Eta3to5Response80to120,outDirectory+"Eta3to5_Response_Jet3_80to120_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 80to120",10000,0,0.05)
Eta3to5JetResolution120to170, Eta3to5JetResolutionErr120to170 = CalcResolution(Eta3to5Response120to170,outDirectory+"Eta3to5_Response_Jet3_120to170_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 120to170",10000,0,0.05)
Eta3to5JetResolution170to300, Eta3to5JetResolutionErr170to300 = CalcResolution(Eta3to5Response170to300,outDirectory+"Eta3to5_Response_Jet3_170to300_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 170to300",10000,0,0.05)
Eta3to5JetResolution300to470, Eta3to5JetResolutionErr300to470 = CalcResolution(Eta3to5Response300to470,outDirectory+"Eta3to5_Response_Jet3_300to470_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 300to470",10000,0,0.05)
Eta3to5JetResolution470to600, Eta3to5JetResolutionErr470to600 = CalcResolution(Eta3to5Response470to600,outDirectory+"Eta3to5_Response_Jet3_470to600_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 470to600",10000,0,0.05)
Eta3to5JetResolution600to800, Eta3to5JetResolutionErr600to800 = CalcResolution(Eta3to5Response600to800,outDirectory+"Eta3to5_Response_Jet3_600to800_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 600to800",10000,0,0.05)
Eta3to5JetResolution800to1000, Eta3to5JetResolutionErr800to1000 = CalcResolution(Eta3to5Response800to1000,outDirectory+"Eta3to5_Response_Jet3_800to1000_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 800to1000",10000,0,0.05)
Eta3to5JetResolution1000to1400, Eta3to5JetResolutionErr1000to1400 = CalcResolution(Eta3to5Response1000to1400,outDirectory+"Eta3to5_Response_Jet3_1000to1400_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 1000to1400",10000,0,0.05)
Eta3to5JetResolution1400to1800, Eta3to5JetResolutionErr1400to1800 = CalcResolution(Eta3to5Response1400to1800,outDirectory+"Eta3to5_Response_Jet3_1400to1800_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 1400to1800",2500000,0,0.1)
Eta3to5JetResolution1800to2400, Eta3to5JetResolutionErr1800to2400 = CalcResolution(Eta3to5Response1800to2400,outDirectory+"Eta3to5_Response_Jet3_1800to2400_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 1800to2400",140000,0,0.08)
Eta3to5JetResolution2400to3200, Eta3to5JetResolutionErr2400to3200 = CalcResolution(Eta3to5Response2400to3200,outDirectory+"Eta3to5_Response_Jet3_2400to3200_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 2400to3200",10000,0,0.05)
Eta3to5JetResolution3200, Eta3to5JetResolutionErr3200 = CalcResolution(Eta3to5Response3200,outDirectory+"Eta3to5_Response_Jet3_3200_Run2023.pdf","Events","Eta 3 to 5 Response","Eta 3 to 5 Response for pt3 3200",10000,0,0.05)

Eta3to5JetResolution = np.array([Eta3to5JetResolution50to80,Eta3to5JetResolution80to120,Eta3to5JetResolution120to170,Eta3to5JetResolution170to300,Eta3to5JetResolution300to470,Eta3to5JetResolution470to600,Eta3to5JetResolution600to800,Eta3to5JetResolution800to1000,Eta3to5JetResolution1000to1400,Eta3to5JetResolution1400to1800,Eta3to5JetResolution1800to2400,Eta3to5JetResolution2400to3200,Eta3to5JetResolution3200])
Eta3to5JetResolutionErr = np.array([Eta3to5JetResolutionErr50to80,Eta3to5JetResolutionErr80to120,Eta3to5JetResolutionErr120to170,Eta3to5JetResolutionErr170to300,Eta3to5JetResolutionErr300to470,Eta3to5JetResolutionErr470to600,Eta3to5JetResolutionErr600to800,Eta3to5JetResolutionErr800to1000,Eta3to5JetResolutionErr1000to1400,Eta3to5JetResolutionErr1400to1800,Eta3to5JetResolutionErr1800to2400,Eta3to5JetResolutionErr2400to3200,Eta3to5JetResolutionErr3200])
PtRanges = np.array([(50+80)/2,(80+120)/2,(120+170)/2,(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([30/2,40/2,50/2,130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#Eta3to5JetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 13
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(Eta3to5JetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(Eta3to5JetResolutionErr[i])
    yl.append(Eta3to5JetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
Eta3to5JetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(Eta3to5JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,Eta3to5JetResolutionGraph.GetY()[i]+0.0015,Eta3to5JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta3to5JetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(Eta3to5JetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,Eta3to5JetResolutionGraph.GetY()[i]+0.0015,Eta3to5JetResolutionLabels[i])
        latex.SetTextSize(0.02)
        Eta3to5JetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

Eta3to5JetResolutionGraph.SetStats(0)
Eta3to5JetResolutionGraph.SetLineColor(ROOT.kBlack)
Eta3to5JetResolutionGraph.SetLineWidth(2)
Eta3to5JetResolutionGraph.GetXaxis().SetTitle("Pt3 [GeV]")
Eta3to5JetResolutionGraph.GetYaxis().SetTitle("JetResolution")
Eta3to5JetResolutionGraph.SetTitle("Eta 3 to 5 JetResolution for Jet3")
Eta3to5JetResolutionGraph.SetMarkerColor(ROOT.kBlack)
Eta3to5JetResolutionGraph.SetMarkerStyle(33)
Eta3to5JetResolutionGraph.SetMarkerSize(0)
Eta3to5JetResolutionGraph.GetXaxis().SetMoreLogLabels()
Eta3to5JetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(Eta3to5JetResolutionGraph,"JetResolution","l")

Eta3to5JetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta3to5JetResolutionfromPt3_Run2023Sim.pdf")

header = ['PtRange', 'Eta3to5JetResolution', 'Eta3to5JetResolutionErr']
data = [
    ['50to80', Eta3to5JetResolution50to80,Eta3to5JetResolutionErr50to80],
    ['80to120', Eta3to5JetResolution80to120,Eta3to5JetResolutionErr80to120],
    ['120to170', Eta3to5JetResolution120to170,Eta3to5JetResolutionErr120to170],
    ['170to300', Eta3to5JetResolution170to300,Eta3to5JetResolutionErr170to300],
    ['300to470', Eta3to5JetResolution300to470,Eta3to5JetResolutionErr300to470],
    ['470to600', Eta3to5JetResolution470to600,Eta3to5JetResolutionErr470to600],
    ['600to800', Eta3to5JetResolution600to800,Eta3to5JetResolutionErr600to800],
    ['800to1000', Eta3to5JetResolution800to1000,Eta3to5JetResolutionErr800to1000],
    ['1000to1400', Eta3to5JetResolution1000to1400,Eta3to5JetResolutionErr1000to1400],
    ['1400to1800', Eta3to5JetResolution1400to1800,Eta3to5JetResolutionErr1400to1800],
    ['1800to2400', Eta3to5JetResolution1800to2400,Eta3to5JetResolutionErr1800to2400],
    ['2400to3200', Eta3to5JetResolution2400to3200,Eta3to5JetResolutionErr2400to3200],
    ['3200', Eta3to5JetResolution3200,Eta3to5JetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta3to5JetResolutionPt3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)