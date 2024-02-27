import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,yAxisTitle,xAxisTitle,title,legendtext):
    canvas = ROOT.TCanvas("canvas")
    canvas.cd()
    datagraph = ROOT.TGraphAsymmErrors(data)
    for i in range(0,int(data.GetNbinsX())):
	    datagraph.SetPointEXhigh(i,0.0)
	    datagraph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.SetTextSize(0.03)
    legend.AddEntry(datagraph,legendtext,"p")

    datagraph.SetStats(0)
    datagraph.SetLineColor(ROOT.kBlack)
    datagraph.SetMarkerColor(ROOT.kBlack)
    datagraph.SetLineWidth(2)
    datagraph.SetMarkerStyle(4)
    datagraph.GetYaxis().SetTitle(yAxisTitle)
    datagraph.GetXaxis().SetTitle(xAxisTitle)
    datagraph.GetXaxis().SetRangeUser(data.GetXaxis().GetXmin(),data.GetXaxis().GetXmax())
    datagraph.SetTitle(title)
    datagraph.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
inFileName = inDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023_MC.root"

RootFile = ROOT.TFile.Open(inFileName,"READ")

#Plot pt asymmetry
PtAsym =RootFile.Get("PtAsymmetry")
RootHisttoPdf(outDirectory+"Plot_DijetAsymmetry_Run2023_Simulation.pdf",PtAsym,"Events","(Pt1-Pt2)/(Pt1+Pt2)","Dijet Asymmetry for Run 2023 Simulation","(Pt1-Pt2)/(Pt1+Pt2)")

#Plot phidiff
PhiDiff =RootFile.Get("PhiDifference")
RootHisttoPdf(outDirectory+"Plot_PhiDifference_Run2023_Simulation.pdf",PhiDiff,"Events","Degree","Phi Difference for Run 2023 Simulation","Phi1-Phi2")

#Plot thetadiff
ThetaDiff =RootFile.Get("ThetaDifference")
RootHisttoPdf(outDirectory+"Plot_ThetaDifference_Run2023_Simulation.pdf",ThetaDiff,"Events","Degree","Theta Difference for Run 2023 Simulation","Theta1-Theta2")

#Plot YDifference
YDiff =RootFile.Get("YDifference")
RootHisttoPdf(outDirectory+"Plot_YDifference_Run2023_Simulation.pdf",YDiff,"Events","YDifference","Y Difference for Run 2023 Simulation","Y1-Y2")

#Plot EtaDifference
EtaDiff =RootFile.Get("EtaDifference")
RootHisttoPdf(outDirectory+"Plot_EtaDifference_Run2023_Simulation.pdf",EtaDiff,"Events","EtaDifference","Eta Difference for Run 2023 Simulation","Eta1-Eta2")
