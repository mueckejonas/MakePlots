import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,yAxisTitle,xAxisTitle,title,legendtext):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.cd()
    datagraph = ROOT.TGraphAsymmErrors(data)
    for i in range(0,int(data.GetNbinsX())):
	    datagraph.SetPointEXhigh(i,0.0)
	    datagraph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(datagraph,legendtext,"p")

    datagraph.SetStats(0)
    datagraph.SetLineColor(ROOT.kBlack)
    datagraph.SetMarkerColor(ROOT.kBlack)
    datagraph.SetMarkerStyle(4)
    datagraph.GetYaxis().SetTitle(yAxisTitle)
    datagraph.GetXaxis().SetTitle(xAxisTitle)
    datagraph.GetXaxis().SetRangeUser(data.GetXaxis().GetXmin(),data.GetXaxis().GetXmax())
    datagraph.SetTitle(title)
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
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_Plot_DijetAsymmetry_WithScale_Run32023_MC.root"

RootFile = ROOT.TFile.Open(inFileName,"READ")

#Plot pt asymmetry
PtAsym =RootFile.Get("PtAsymmetrysim_hist")
RootHisttoPdf(outDirectory+"Plot_DijetAsymmetry_Run2023_Simulation.pdf",PtAsym,"#sigma [pb]","(Pt1-Pt2)/(Pt1+Pt2)","Dijet Asymmetry for Run 2023 Simulation","(Pt1-Pt2)/(Pt1+Pt2)")

#Plot phidiff
PhiDiff =RootFile.Get("PhiDifferencesim_hist")
RootHisttoPdf(outDirectory+"Plot_PhiDifference_Run2023_Simulation.pdf",PhiDiff,"#sigma [pb]","Degree","Phi Difference for Run 2023 Simulation","Phi1-Phi2")

#Plot thetadiff
ThetaDiff =RootFile.Get("ThetaDifferencesim_hist")
RootHisttoPdf(outDirectory+"Plot_ThetaDifference_Run2023_Simulation.pdf",ThetaDiff,"#sigma [pb]","Degree","Theta Difference for Run 2023 Simulation","Theta1-Theta2")

#Plot YDifference
YDiff =RootFile.Get("YDifferencesim_hist")
RootHisttoPdf(outDirectory+"Plot_YDifference_Run2023_Simulation.pdf",YDiff,"#sigma [pb]","YDifference","Y Difference for Run 2023 Simulation","Y1-Y2")

#Plot EtaDifference
EtaDiff =RootFile.Get("EtaDifferencesim_hist")
RootHisttoPdf(outDirectory+"Plot_EtaDifference_Run2023_Simulation.pdf",EtaDiff,"#sigma [pb]","EtaDifference","Eta Difference for Run 2023 Simulation","Eta1-Eta2")
