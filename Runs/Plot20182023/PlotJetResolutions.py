import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,sim2018,sim2023,yAxisTitle,xAxisTitle,title,ymax=0.1):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.SetLogx()

    legend = ROOT.TLegend(0.6,0.6,0.85,0.85)
    legend.SetTextSize(0.07)
    legend.SetLineWidth(0)

    sim2018.SetStats(0)
    sim2018.SetLineColor(ROOT.kBlack)
    sim2018.SetLineWidth(2)
    sim2018.SetTitle(title)
    sim2018.GetYaxis().SetTitle(yAxisTitle)
    sim2018.SetMarkerColor(ROOT.kBlack)
    sim2018.SetMarkerStyle(33)
    sim2018.SetLineColor(ROOT.kBlack)

    sim2023.SetStats(0)
    sim2023.SetLineColor(ROOT.kBlue)
    sim2023.SetLineWidth(2)
    sim2023.SetTitle("")
    sim2023.SetMarkerColor(ROOT.kBlue)
    sim2023.SetMarkerStyle(33)
    sim2023.SetLineColor(ROOT.kBlue)

    legend.AddEntry(sim2018,"2018 Sim","p")
    legend.AddEntry(sim2023,"2023 Sim","p")

    #Set font size
    sim2018.SetMarkerSize(3)
    sim2023.SetMarkerSize(3)
    sim2018.GetYaxis().SetLabelSize(0.06)
    sim2018.GetYaxis().SetTitleSize(0.07)
    sim2018.GetYaxis().SetTitleOffset(1)
    sim2018.GetXaxis().SetMoreLogLabels()
    sim2018.GetXaxis().SetNoExponent()
    sim2018.GetXaxis().SetRangeUser(0,3200)
    sim2018.GetYaxis().SetRangeUser(0,ymax)
    sim2018.GetXaxis().SetLabelSize(0.06)
    sim2018.GetXaxis().SetTitleSize(0.07)
    sim2018.GetXaxis().SetTitle(xAxisTitle)

    sim2018.Draw("AP")
    sim2023.Draw("P same")
    legend.Draw("same")

    #draw whole plot
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)
    canvas.Draw()
    canvas.Print(outFileName)


#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Runs/Pdf/"

#load MC 2023 Data
#define directory
inDirectory2023 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
rootFile2023Jet1 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet1.root","READ")
Jet1ResolutionGraph2023 = rootFile2023Jet1.Get("Graph")
rootFile2023Jet2 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet2.root","READ")
Jet2ResolutionGraph2023 = rootFile2023Jet2.Get("Graph")
rootFile2023Jet3 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet3.root","READ")
Jet3ResolutionGraph2023 = rootFile2023Jet3.Get("Graph")

#load MC 2018 Data
#define directory
inDirectory2018 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
rootFile2018Jet1 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet1.root","READ")
Jet1ResolutionGraph2018 = rootFile2018Jet1.Get("Graph")
rootFile2018Jet2 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet2.root","READ")
Jet2ResolutionGraph2018 = rootFile2018Jet2.Get("Graph")
rootFile2018Jet3 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet3.root","READ")
Jet3ResolutionGraph2018 = rootFile2018Jet3.Get("Graph")



#create Jet1 pdf
RootHisttoPdf(outDirectory+"_PlotJetResolution_2018and2023_Jet1.pdf",Jet1ResolutionGraph2018,Jet1ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet1 Resolution for 2018 and 2023 MC")

#create Jet2 pdf
RootHisttoPdf(outDirectory+"_PlotJetResolution_2018and2023_Jet2.pdf",Jet2ResolutionGraph2018,Jet2ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet2 Resolution for 2018 and 2023 MC",0.12)

#create Jet3 pdf
RootHisttoPdf(outDirectory+"_PlotJetResolution_2018and2023_Jet3.pdf",Jet3ResolutionGraph2018,Jet3ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet3 Resolution for 2018 and 2023 MC")
