import ROOT
import numpy as np

ROOT.gStyle.SetTextSize(0.05)

#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,yAxisTitle,xAxisTitle,legendtext):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.cd()
    datagraph = ROOT.TGraphAsymmErrors(data)
    for i in range(0,int(data.GetNbinsX())):
	    datagraph.SetPointEXhigh(i,0.0)
	    datagraph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.4,0.9,0.85,0.75)
    legend.SetLineWidth(0)
    legend.SetFillStyle(4000)
    legend.AddEntry(datagraph,legendtext,"p")

    datagraph.SetStats(0)
    datagraph.SetLineColor(ROOT.kBlack)
    datagraph.SetMarkerColor(ROOT.kBlack)
    datagraph.SetMarkerStyle(4)
    datagraph.GetYaxis().SetTitle(yAxisTitle)
    datagraph.GetXaxis().SetTitle(xAxisTitle)
    datagraph.GetXaxis().SetRangeUser(data.GetXaxis().GetXmin(),data.GetXaxis().GetXmax())
    datagraph.SetTitle("")
    #Set font size
    legend.SetTextSize(0.045)
    datagraph.SetMarkerSize(3)
    datagraph.SetLineWidth(2)
    datagraph.GetYaxis().SetLabelSize(0.045)
    datagraph.GetYaxis().SetTitleSize(0.05)
    datagraph.GetXaxis().SetLabelSize(0.045)
    datagraph.GetXaxis().SetTitleSize(0.05)
    #datagraph.GetYaxis().SetLabelOffset(0.01)
    #datagraph.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)

    datagraph.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/Pdf/"
inFileName = inDirectory+"PlotDijetAsymmetry_Run2023D.root"

RootFile = ROOT.TFile.Open(inFileName,"READ")

#Plot pt asymmetry
PtAsym =RootFile.Get("PtAsymmetry")
RootHisttoPdf(outDirectory+"Plot_DijetAsymmetry_Run2023D.pdf",PtAsym,"Events","(P_{t1}-P_{t2})/(P_{t1}+P_{t2})","Dijet Asymmetry Run3 D 2023")

#Plot phidiff
PhiDiff =RootFile.Get("PhiDifference")
RootHisttoPdf(outDirectory+"Plot_PhiDifference_Run2023D.pdf",PhiDiff,"Events","Degree","#phi Difference for Run3 D 2023")

#Plot thetadiff
ThetaDiff =RootFile.Get("ThetaDifference")
RootHisttoPdf(outDirectory+"Plot_ThetaDifference_Run2023D.pdf",ThetaDiff,"Events","Degree","#theta Difference for Run3 D 2023")

#Plot YDifference
YDiff =RootFile.Get("YDifference")
RootHisttoPdf(outDirectory+"Plot_YDifference_Run2023D.pdf",YDiff,"Events","Y_{1}-Y_{2}","Y Difference for Run3 D 2023")

#Plot EtaDifference
EtaDiff =RootFile.Get("EtaDifference")
RootHisttoPdf(outDirectory+"Plot_EtaDifference_Run2023D.pdf",EtaDiff,"Events","#eta_{1}-#eta_{2}","Eta Difference for Run3 D 2023")
