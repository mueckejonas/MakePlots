import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,sim2018,sim2023,yAxisTitle,xAxisTitle,title):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.cd()

    legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
    legend.SetLineWidth(0)
    legend.AddEntry(sim2018,"Sim 2018","p")
    legend.AddEntry(sim2023,"Sim 2023","p")

    sim2018.SetStats(0)
    sim2018.SetLineColor(ROOT.kBlack)
    sim2018.SetMarkerColor(ROOT.kBlack)
    sim2018.SetMarkerStyle(4)
    sim2018.GetYaxis().SetTitle(yAxisTitle)
    sim2018.GetXaxis().SetTitle(xAxisTitle)
    sim2018.SetTitle(title)
    sim2018.SetMarkerSize(3)
    sim2018.SetLineWidth(2)

    sim2023.SetStats(0)
    sim2023.SetLineColor(ROOT.kRed)
    sim2023.SetMarkerColor(ROOT.kRed)
    sim2023.SetMarkerStyle(4)
    sim2023.SetMarkerSize(3)
    sim2023.SetLineWidth(2)

    #Set font size
    legend.SetTextSize(0.045)
    sim2018.GetYaxis().SetLabelSize(0.045)
    sim2018.GetYaxis().SetTitleSize(0.05)
    sim2018.GetXaxis().SetLabelSize(0.045)
    sim2018.GetXaxis().SetTitleSize(0.05)
    sim2018.GetYaxis().SetLabelOffset(0.01)
    sim2018.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)

    sim2018.Draw()
    sim2023.Draw("same")
    legend.Draw("same")

    canvas.Draw()
    canvas.Print(outFileName)


#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Runs/Pdf/"

#load MC 2023 Data
#define directory
inDirectory2023 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
rootFile2023 = ROOT.TFile.Open(inDirectory2023+"_Plot_DijetAsymmetry_WithScale_Run32023_MC.root","READ")

#load MC 2018 Data
#define directory
inDirectory2018 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
rootFile2018 = ROOT.TFile.Open(inDirectory2018+"_Plot_DijetAsymmetry_WithScale_Run22018_MC.root","READ")



#create  pdf
PtAsymmetrysim_hist2023 = rootFile2023.Get("PtAsymmetrysim_hist")
PtAsymmetrysim_hist2018 = rootFile2018.Get("PtAsymmetrysim_hist")
RootHisttoPdf(outDirectory+"_PlotDijetAsymmetry_2018and2023.pdf",PtAsymmetrysim_hist2018,PtAsymmetrysim_hist2023,"#sigma [pb]","(Pt1-Pt2)/(Pt1+Pt2)","Dijet Asymmetry for 2018 and 2023 Simulation")

#create pdf
PhiDifferencesim_hist2023 = rootFile2023.Get("PhiDifferencesim_hist")
PhiDifferencesim_hist2018 = rootFile2018.Get("PhiDifferencesim_hist")
RootHisttoPdf(outDirectory+"_PlotPhiDifference_2018and2023.pdf",PhiDifferencesim_hist2018,PhiDifferencesim_hist2023,"#sigma [pb]","Phi1-Phi2","Phi Difference for 2018 and 2023 Simulation")

#create pdf
EtaDifferencesim_hist2023 = rootFile2023.Get("EtaDifferencesim_hist")
EtaDifferencesim_hist2018 = rootFile2018.Get("EtaDifferencesim_hist")
RootHisttoPdf(outDirectory+"_PlotEtaDifference_2018and2023.pdf",EtaDifferencesim_hist2018,EtaDifferencesim_hist2023,"#sigma [pb]","Eta1-Eta2","Eta Difference for 2018 and 2023 Simulation")

#create pdf
YDifferencesim_hist2023 = rootFile2023.Get("YDifferencesim_hist")
YDifferencesim_hist2018 = rootFile2018.Get("YDifferencesim_hist")
RootHisttoPdf(outDirectory+"_PlotYDifference_2018and2023.pdf",YDifferencesim_hist2018,YDifferencesim_hist2023,"#sigma [pb]","Y1-Y2","Y Difference for 2018 and 2023 Simulation")

#create pdf
ThetaDifferencesim_hist2023 = rootFile2023.Get("ThetaDifferencesim_hist")
ThetaDifferencesim_hist2018 = rootFile2018.Get("ThetaDifferencesim_hist")
RootHisttoPdf(outDirectory+"_PlotThetaDifference_2018and2023.pdf",ThetaDifferencesim_hist2018,ThetaDifferencesim_hist2023,"#sigma [pb]","Theta1-Thet2","Theta Difference for 2018 and 2023 Simulation")


"""
PtAsymmetrysim_hist
PhiDifferencesim_hist
EtaDifferencesim_hist
YDifferencesim_hist
ThetaDifferencesim_hist
"""
