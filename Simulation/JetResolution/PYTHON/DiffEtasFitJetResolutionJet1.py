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

    FWHMLine = ROOT.TLine(2*B-FWHMPoint,A/2,FWHMPoint,A/2)
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
    legend.AddEntry(FWHMLine,"FWHM "+"("+str(round(FWHM*100,2))+"+-"+str(round(FWHM_Err,6))+")"+"%","l")
    hist_graph.Draw("AP")
    fit_func.Draw("same")
    FWHMLine.Draw("same")
    legend.Draw("same")
    canvas.Print(outFileName)
    return FWHM, FWHM_Err


#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"PlotJetResolution_Jet1_Run2023C.root"

histFiles = ROOT.TFile.Open(inFileName,"READ")

#Get Hist and Calculate Jet Resolution
SmallEtaResponse50to80 = histFiles.Get("SmallEtaResponseJet150to80")
SmallEtaResponse80to120 = histFiles.Get("SmallEtaResponseJet180to120")
SmallEtaResponse120to170 = histFiles.Get("SmallEtaResponseJet1120to170")
SmallEtaResponse170to300 = histFiles.Get("SmallEtaResponseJet1170to300")
SmallEtaResponse300to470 = histFiles.Get("SmallEtaResponseJet1300to470")
SmallEtaResponse470to600 = histFiles.Get("SmallEtaResponseJet1470to600")
SmallEtaResponse600to800 = histFiles.Get("SmallEtaResponseJet1600to800")
SmallEtaResponse800to1000 = histFiles.Get("SmallEtaResponseJet1800to1000")
SmallEtaResponse1000to1400 = histFiles.Get("SmallEtaResponseJet11000to1400")
SmallEtaResponse1400to1800 = histFiles.Get("SmallEtaResponseJet11400to1800")
SmallEtaResponse1800to2400 = histFiles.Get("SmallEtaResponseJet11800to2400")
SmallEtaResponse2400to3200 = histFiles.Get("SmallEtaResponseJet12400to3200")
SmallEtaResponse3200 = histFiles.Get("SmallEtaResponseJet13200")

SmallEtaJetResolution50to80, SmallEtaJetResolutionErr50to80 = CalcResolution(SmallEtaResponse50to80,outDirectory+"Eta0to1p3_Response_Jet1_50to80_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 50to80",10000,0,0.05)
SmallEtaJetResolution80to120, SmallEtaJetResolutionErr80to120 = CalcResolution(SmallEtaResponse80to120,outDirectory+"Eta0to1p3_Response_Jet1_80to120_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 80to120",10000,0,0.05)
SmallEtaJetResolution120to170, SmallEtaJetResolutionErr120to170 = CalcResolution(SmallEtaResponse120to170,outDirectory+"Eta0to1p3_Response_Jet1_120to170_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 120to170",10000,0,0.05)
SmallEtaJetResolution170to300, SmallEtaJetResolutionErr170to300 = CalcResolution(SmallEtaResponse170to300,outDirectory+"Eta0to1p3_Response_Jet1_170to300_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 170to300",10000,0,0.05)
SmallEtaJetResolution300to470, SmallEtaJetResolutionErr300to470 = CalcResolution(SmallEtaResponse300to470,outDirectory+"Eta0to1p3_Response_Jet1_300to470_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 300to470",10000,0,0.05)
SmallEtaJetResolution470to600, SmallEtaJetResolutionErr470to600 = CalcResolution(SmallEtaResponse470to600,outDirectory+"Eta0to1p3_Response_Jet1_470to600_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 470to600",10000,0,0.05)
SmallEtaJetResolution600to800, SmallEtaJetResolutionErr600to800 = CalcResolution(SmallEtaResponse600to800,outDirectory+"Eta0to1p3_Response_Jet1_600to800_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 600to800",10000,0,0.05)
SmallEtaJetResolution800to1000, SmallEtaJetResolutionErr800to1000 = CalcResolution(SmallEtaResponse800to1000,outDirectory+"Eta0to1p3_Response_Jet1_800to1000_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 800to1000",10000,0,0.05)
SmallEtaJetResolution1000to1400, SmallEtaJetResolutionErr1000to1400 = CalcResolution(SmallEtaResponse1000to1400,outDirectory+"Eta0to1p3_Response_Jet1_1000to1400_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 1000to1400",10000,0,0.05)
SmallEtaJetResolution1400to1800, SmallEtaJetResolutionErr1400to1800 = CalcResolution(SmallEtaResponse1400to1800,outDirectory+"Eta0to1p3_Response_Jet1_1400to1800_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 1400to1800",2500000,0,0.1)
SmallEtaJetResolution1800to2400, SmallEtaJetResolutionErr1800to2400 = CalcResolution(SmallEtaResponse1800to2400,outDirectory+"Eta0to1p3_Response_Jet1_1800to2400_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 1800to2400",10000,0,0.05)
SmallEtaJetResolution2400to3200, SmallEtaJetResolutionErr2400to3200 = CalcResolution(SmallEtaResponse2400to3200,outDirectory+"Eta0to1p3_Response_Jet1_2400to3200_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 2400to3200",10000,0,0.05)
SmallEtaJetResolution3200, SmallEtaJetResolutionErr3200 = CalcResolution(SmallEtaResponse3200,outDirectory+"Eta0to1p3_Response_Jet1_3200_Run2023.pdf","Events","Eta 0 to 1.3 Response","Eta 0 to 1.3 Response for pt1 3200",10000,0,0.05)

SmallEtaJetResolution = np.array([SmallEtaJetResolution170to300,SmallEtaJetResolution300to470,SmallEtaJetResolution470to600,SmallEtaJetResolution600to800,SmallEtaJetResolution800to1000,SmallEtaJetResolution1000to1400,SmallEtaJetResolution1400to1800,SmallEtaJetResolution1800to2400,SmallEtaJetResolution2400to3200,SmallEtaJetResolution3200])
SmallEtaJetResolutionErr = np.array([SmallEtaJetResolutionErr170to300,SmallEtaJetResolutionErr300to470,SmallEtaJetResolutionErr470to600,SmallEtaJetResolutionErr600to800,SmallEtaJetResolutionErr800to1000,SmallEtaJetResolutionErr1000to1400,SmallEtaJetResolutionErr1400to1800,SmallEtaJetResolutionErr1800to2400,SmallEtaJetResolutionErr2400to3200,SmallEtaJetResolutionErr3200])
PtRanges = np.array([(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#SmallEtaJetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 10
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(SmallEtaJetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(SmallEtaJetResolutionErr[i])
    yl.append(SmallEtaJetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
SmallEtaJetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(SmallEtaJetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,SmallEtaJetResolutionGraph.GetY()[i]+0.0015,SmallEtaJetResolutionLabels[i])
        latex.SetTextSize(0.02)
        SmallEtaJetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(SmallEtaJetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,SmallEtaJetResolutionGraph.GetY()[i]+0.0015,SmallEtaJetResolutionLabels[i])
        latex.SetTextSize(0.02)
        SmallEtaJetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

SmallEtaJetResolutionGraph.SetStats(0)
SmallEtaJetResolutionGraph.SetLineColor(ROOT.kBlack)
SmallEtaJetResolutionGraph.SetLineWidth(2)
SmallEtaJetResolutionGraph.GetXaxis().SetTitle("Pt1 [GeV]")
SmallEtaJetResolutionGraph.GetYaxis().SetTitle("JetResolution")
SmallEtaJetResolutionGraph.SetTitle("Eta 0 to 1.3 JetResolution for Jet1")
SmallEtaJetResolutionGraph.SetMarkerColor(ROOT.kBlack)
SmallEtaJetResolutionGraph.SetMarkerStyle(33)
SmallEtaJetResolutionGraph.SetMarkerSize(0)
SmallEtaJetResolutionGraph.GetXaxis().SetMoreLogLabels()
SmallEtaJetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(SmallEtaJetResolutionGraph,"JetResolution","l")

SmallEtaJetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta0to1p3JetResolutionfromPt1_Run2023Sim.pdf")

header = ['PtRange', 'Eta0to1p3JetResolution', 'Eta0to1p3JetResolutionErr']
data = [
    ['50to80', SmallEtaJetResolution50to80,SmallEtaJetResolutionErr50to80],
    ['80to120', SmallEtaJetResolution80to120,SmallEtaJetResolutionErr80to120],
    ['120to170', SmallEtaJetResolution120to170,SmallEtaJetResolutionErr120to170],
    ['170to300', SmallEtaJetResolution170to300,SmallEtaJetResolutionErr170to300],
    ['300to470', SmallEtaJetResolution300to470,SmallEtaJetResolutionErr300to470],
    ['470to600', SmallEtaJetResolution470to600,SmallEtaJetResolutionErr470to600],
    ['600to800', SmallEtaJetResolution600to800,SmallEtaJetResolutionErr600to800],
    ['800to1000', SmallEtaJetResolution800to1000,SmallEtaJetResolutionErr800to1000],
    ['1000to1400', SmallEtaJetResolution1000to1400,SmallEtaJetResolutionErr1000to1400],
    ['1400to1800', SmallEtaJetResolution1400to1800,SmallEtaJetResolutionErr1400to1800],
    ['1800to2400', SmallEtaJetResolution1800to2400,SmallEtaJetResolutionErr1800to2400],
    ['2400to3200', SmallEtaJetResolution2400to3200,SmallEtaJetResolutionErr2400to3200],
    ['3200', SmallEtaJetResolution3200,SmallEtaJetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta0to1p3JetResolutionPt1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

#Get Hist and Calculate Jet Resolution
BigEtaResponse50to80 = histFiles.Get("BigEtaResponseJet150to80")
BigEtaResponse80to120 = histFiles.Get("BigEtaResponseJet180to120")
BigEtaResponse120to170 = histFiles.Get("BigEtaResponseJet1120to170")
BigEtaResponse170to300 = histFiles.Get("BigEtaResponseJet1170to300")
BigEtaResponse300to470 = histFiles.Get("BigEtaResponseJet1300to470")
BigEtaResponse470to600 = histFiles.Get("BigEtaResponseJet1470to600")
BigEtaResponse600to800 = histFiles.Get("BigEtaResponseJet1600to800")
BigEtaResponse800to1000 = histFiles.Get("BigEtaResponseJet1800to1000")
BigEtaResponse1000to1400 = histFiles.Get("BigEtaResponseJet11000to1400")
BigEtaResponse1400to1800 = histFiles.Get("BigEtaResponseJet11400to1800")
BigEtaResponse1800to2400 = histFiles.Get("BigEtaResponseJet11800to2400")
BigEtaResponse2400to3200 = histFiles.Get("BigEtaResponseJet12400to3200")
BigEtaResponse3200 = histFiles.Get("BigEtaResponseJet13200")

BigEtaJetResolution50to80, BigEtaJetResolutionErr50to80 = CalcResolution(BigEtaResponse50to80,outDirectory+"Eta1p3to2p5p3_Response_Jet1_50to80_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 50to80",10000,0,0.05)
BigEtaJetResolution80to120, BigEtaJetResolutionErr80to120 = CalcResolution(BigEtaResponse80to120,outDirectory+"Eta1p3to2p5p3_Response_Jet1_80to120_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 80to120",10000,0,0.05)
BigEtaJetResolution120to170, BigEtaJetResolutionErr120to170 = CalcResolution(BigEtaResponse120to170,outDirectory+"Eta1p3to2p5p3_Response_Jet1_120to170_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 120to170",10000,0,0.05)
BigEtaJetResolution170to300, BigEtaJetResolutionErr170to300 = CalcResolution(BigEtaResponse170to300,outDirectory+"Eta1p3to2p5p3_Response_Jet1_170to300_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 170to300",10000,0,0.05)
BigEtaJetResolution300to470, BigEtaJetResolutionErr300to470 = CalcResolution(BigEtaResponse300to470,outDirectory+"Eta1p3to2p5p3_Response_Jet1_300to470_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 300to470",10000,0,0.05)
BigEtaJetResolution470to600, BigEtaJetResolutionErr470to600 = CalcResolution(BigEtaResponse470to600,outDirectory+"Eta1p3to2p5p3_Response_Jet1_470to600_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 470to600",10000,0,0.05)
BigEtaJetResolution600to800, BigEtaJetResolutionErr600to800 = CalcResolution(BigEtaResponse600to800,outDirectory+"Eta1p3to2p5p3_Response_Jet1_600to800_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 600to800",10000,0,0.05)
BigEtaJetResolution800to1000, BigEtaJetResolutionErr800to1000 = CalcResolution(BigEtaResponse800to1000,outDirectory+"Eta1p3to2p5p3_Response_Jet1_800to1000_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 800to1000",10000,0,0.05)
BigEtaJetResolution1000to1400, BigEtaJetResolutionErr1000to1400 = CalcResolution(BigEtaResponse1000to1400,outDirectory+"Eta1p3to2p5p3_Response_Jet1_1000to1400_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 1000to1400",10000,0,0.05)
BigEtaJetResolution1400to1800, BigEtaJetResolutionErr1400to1800 = CalcResolution(BigEtaResponse1400to1800,outDirectory+"Eta1p3to2p5p3_Response_Jet1_1400to1800_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 1400to1800",2500000,0,0.1)
BigEtaJetResolution1800to2400, BigEtaJetResolutionErr1800to2400 = CalcResolution(BigEtaResponse1800to2400,outDirectory+"Eta1p3to2p5p3_Response_Jet1_1800to2400_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 1800to2400",10000,0,0.05)
BigEtaJetResolution2400to3200, BigEtaJetResolutionErr2400to3200 = CalcResolution(BigEtaResponse2400to3200,outDirectory+"Eta1p3to2p5p3_Response_Jet1_2400to3200_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 2400to3200",10000,0,0.05)
BigEtaJetResolution3200, BigEtaJetResolutionErr3200 = CalcResolution(BigEtaResponse3200,outDirectory+"Eta1p3to2p5p3_Response_Jet1_3200_Run2023.pdf","Events","Eta 1.3 to 2.5 Response","Eta 1.3 to 2.5 Response for pt1 3200",10000,0,0.05)

BigEtaJetResolution = np.array([BigEtaJetResolution170to300,BigEtaJetResolution300to470,BigEtaJetResolution470to600,BigEtaJetResolution600to800,BigEtaJetResolution800to1000,BigEtaJetResolution1000to1400,BigEtaJetResolution1400to1800,BigEtaJetResolution1800to2400,BigEtaJetResolution2400to3200,BigEtaJetResolution3200])
BigEtaJetResolutionErr = np.array([BigEtaJetResolutionErr170to300,BigEtaJetResolutionErr300to470,BigEtaJetResolutionErr470to600,BigEtaJetResolutionErr600to800,BigEtaJetResolutionErr800to1000,BigEtaJetResolutionErr1000to1400,BigEtaJetResolutionErr1400to1800,BigEtaJetResolutionErr1800to2400,BigEtaJetResolutionErr2400to3200,BigEtaJetResolutionErr3200])
PtRanges = np.array([(170+300)/2,(300+470)/2,(470+600)/2,(600+800)/2,(800+1000)/2,(1000+1400)/2,(1400+1800)/2,(1800+2400)/2,(2400+3200)/2,3500])
PtRangesErrh = np.array([130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,300])
PtRangesErrl = np.array([130/2,170/2,130/2,200/2,200/2,400/2,400/2,600/2,800/2,0])
#BigEtaJetResolutionLabels = np.array(["170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","<3200"])

n = 10
x = array('d')
y = array('d')
xh = array('d')
xl = array('d')
yh = array('d')
yl = array('d')
for i in range(0,n):
    x.append(PtRanges[i])
    y.append(BigEtaJetResolution[i])
    xh.append(PtRangesErrh[i])
    xl.append(PtRangesErrl[i])
    yh.append(BigEtaJetResolutionErr[i])
    yl.append(BigEtaJetResolutionErr[i])

canvas = ROOT.TCanvas("canvas")
canvas.SetLogx()
BigEtaJetResolutionGraph = ROOT.TGraphAsymmErrors(n,x,y,xh,xl,yh,yl)

"""
for i in range(0,n):
    if i != 5:
        latex = ROOT.TLatex(BigEtaJetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.9,BigEtaJetResolutionGraph.GetY()[i]+0.0015,BigEtaJetResolutionLabels[i])
        latex.SetTextSize(0.02)
        BigEtaJetResolutionGraph.GetListOfFunctions().Add(latex)
    else:
        latex = ROOT.TLatex(BigEtaJetResolutionGraph.GetX()[i]-PtRangesErrh[i]*0.8,BigEtaJetResolutionGraph.GetY()[i]+0.0015,BigEtaJetResolutionLabels[i])
        latex.SetTextSize(0.02)
        BigEtaJetResolutionGraph.GetListOfFunctions().Add(latex)
"""

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)

BigEtaJetResolutionGraph.SetStats(0)
BigEtaJetResolutionGraph.SetLineColor(ROOT.kBlack)
BigEtaJetResolutionGraph.SetLineWidth(2)
BigEtaJetResolutionGraph.GetXaxis().SetTitle("Pt1 [GeV]")
BigEtaJetResolutionGraph.GetYaxis().SetTitle("JetResolution")
BigEtaJetResolutionGraph.SetTitle("Eta 1.3 to 2.5 JetResolution for Jet1")
BigEtaJetResolutionGraph.SetMarkerColor(ROOT.kBlack)
BigEtaJetResolutionGraph.SetMarkerStyle(33)
BigEtaJetResolutionGraph.SetMarkerSize(0)
BigEtaJetResolutionGraph.GetXaxis().SetMoreLogLabels()
BigEtaJetResolutionGraph.GetXaxis().SetNoExponent()

legend.AddEntry(BigEtaJetResolutionGraph,"JetResolution","l")

BigEtaJetResolutionGraph.Draw("AP")
legend.Draw("same")

canvas.Print(outDirectory+"Eta1p3to2p5p3JetResolutionfromPt1_Run2023Sim.pdf")

header = ['PtRange', 'Eta1p3to2p5p3JetResolution', 'Eta1p3to2p5p3JetResolutionErr']
data = [
    ['50to80', BigEtaJetResolution50to80,BigEtaJetResolutionErr50to80],
    ['80to120', BigEtaJetResolution80to120,BigEtaJetResolutionErr80to120],
    ['120to170', BigEtaJetResolution120to170,BigEtaJetResolutionErr120to170],
    ['170to300', BigEtaJetResolution170to300,BigEtaJetResolutionErr170to300],
    ['300to470', BigEtaJetResolution300to470,BigEtaJetResolutionErr300to470],
    ['470to600', BigEtaJetResolution470to600,BigEtaJetResolutionErr470to600],
    ['600to800', BigEtaJetResolution600to800,BigEtaJetResolutionErr600to800],
    ['800to1000', BigEtaJetResolution800to1000,BigEtaJetResolutionErr800to1000],
    ['1000to1400', BigEtaJetResolution1000to1400,BigEtaJetResolutionErr1000to1400],
    ['1400to1800', BigEtaJetResolution1400to1800,BigEtaJetResolutionErr1400to1800],
    ['1800to2400', BigEtaJetResolution1800to2400,BigEtaJetResolutionErr1800to2400],
    ['2400to3200', BigEtaJetResolution2400to3200,BigEtaJetResolutionErr2400to3200],
    ['3200', BigEtaJetResolution3200,BigEtaJetResolutionErr3200]
]

with open('/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/CSV/Eta1p3to2p5p3JetResolutionPt1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
