import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,sim2018,sim2023,yAxisTitle,xAxisTitle,title,xmin,xmax,ymax=0.1):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.SetLogx()

    legend = ROOT.TLegend(0.6,0.6,0.85,0.85)
    legend.SetTextSize(0.07)
    legend.SetLineWidth(0)
    legend.SetFillStyle(4000)

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
    sim2018.GetXaxis().SetRangeUser(xmin,xmax)
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
inDirectory2023 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
inDirectory2018 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"


#load and plot Jet1 Data
#define directory
rootFile2023Jet1 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet1_DiffEtas.root","READ")
rootFile2018Jet1 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet1_DiffEtas.root","READ")
#eta 0 to 1.3
Jet1eta0to1p3ResolutionGraph2023 = rootFile2023Jet1.Get("Eta0to1p3JetResolutionGraph")
Jet1eta0to1p3ResolutionGraph2018 = rootFile2018Jet1.Get("Eta0to1p3JetResolutionGraph")
RootHisttoPdf(outDirectory+"PlotJetResolution_Jet1_Eta0to1p3_sim2018and2023.pdf",Jet1eta0to1p3ResolutionGraph2018,Jet1eta0to1p3ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet1 Eta 0 to 1.3 Resolution for MC 2018 and 2023",170,3200)
#eta 1.3 to 2.5
Jet1eta1p3to2p5ResolutionGraph2023 = rootFile2023Jet1.Get("Eta1p3to2p5JetResolutionGraph")
Jet1eta1p3to2p5ResolutionGraph2018 = rootFile2018Jet1.Get("Eta1p3to2p5JetResolutionGraph")
RootHisttoPdf(outDirectory+"PlotJetResolution_Jet1_Eta1p3to2p5_sim2018and2023.pdf",Jet1eta1p3to2p5ResolutionGraph2018,Jet1eta1p3to2p5ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet1 Eta 1.3 to 2.5 Resolution for MC 2018 and 2023",170,2400)
#eta 2.5 to 3
Jet1eta2p5to3ResolutionGraph2023 = rootFile2023Jet1.Get("Eta2p5to3JetResolutionGraph")
Jet1eta2p5to3ResolutionGraph2018 = rootFile2018Jet1.Get("Eta2p5to3JetResolutionGraph")
RootHisttoPdf(outDirectory+"PlotJetResolution_Jet1_Eta2p5to3_sim2018and2023.pdf",Jet1eta2p5to3ResolutionGraph2018,Jet1eta2p5to3ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet1 Eta 2.5 to 3 Resolution for MC 2018 and 2023",170,1000)
#eta 3 to 5
#Jet1eta0to1p3ResolutionGraph2023 = rootFile2023Jet1.Get("Eta0to1p3JetResolutionGraph")
#Jet1eta0to1p3ResolutionGraph2018 = rootFile2018Jet1.Get("Eta0to1p3JetResolutionGraph")


#load and plot Jet2 Data
#define directory
#rootFile2023Jet2 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet2_DiffEtas.root","READ")
#rootFile2018Jet2 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet2_DiffEtas.root","READ")
#eta 0 to 1.3
#Jet2eta0to1p3ResolutionGraph2023 = rootFile2023Jet2.Get("Eta0to1p3JetResolutionGraph")
#Jet2eta0to1p3ResolutionGraph2018 = rootFile2018Jet2.Get("Eta0to1p3JetResolutionGraph")
#RootHisttoPdf(outDirectory+"PlotJetResolution_Jet2_Eta0to1p3_sim2018and2023.pdf",Jet2eta0to1p3ResolutionGraph2018,Jet2eta0to1p3ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet2 Eta 0 to 1.3 Resolution for MC 2018 and 2023")
#eta 1.3 to 2.5
#Jet2eta1p3to2p5ResolutionGraph2023 = rootFile2023Jet2.Get("Eta1p3to2p5JetResolutionGraph")
#Jet2eta1p3to2p5ResolutionGraph2018 = rootFile2018Jet2.Get("Eta1p3to2p5JetResolutionGraph")
#RootHisttoPdf(outDirectory+"PlotJetResolution_Jet2_Eta1p3to2p5_sim2018and2023.pdf",Jet2eta1p3to2p5ResolutionGraph2018,Jet2eta1p3to2p5ResolutionGraph2023,"Jet Resolution","Pt [GeV]","Jet2 Eta 1.3 to 2.5 Resolution for MC 2018 and 2023")
#eta 2.5 to 3
#Jet2eta0to1p3ResolutionGraph2023 = rootFile2023Jet2.Get("Eta0to1p3JetResolutionGraph")
#Jet2eta0to1p3ResolutionGraph2018 = rootFile2018Jet2.Get("Eta0to1p3JetResolutionGraph")
#eta 3 to 5
#Jet2eta0to1p3ResolutionGraph2023 = rootFile2023Jet2.Get("Eta0to1p3JetResolutionGraph")
#Jet2eta0to1p3ResolutionGraph2018 = rootFile2018Jet2.Get("Eta0to1p3JetResolutionGraph")

#load and plot Jet3 Data
#define directory
#rootFile2023Jet3 = ROOT.TFile.Open(inDirectory2023+"FitJetResolutionJet3_DiffEtas.root","READ")
#rootFile2018Jet3 = ROOT.TFile.Open(inDirectory2018+"FitJetResolutionJet3_DiffEtas.root","READ")
#eta 0 to 1.3
#Jet3eta0to1p3ResolutionGraph2023 = rootFile2023Jet3.Get("Eta0to1p3JetResolutionGraph")
#Jet3eta0to1p3ResolutionGraph2018 = rootFile2018Jet3.Get("Eta0to1p3JetResolutionGraph")
#eta 1.3 to 2.5
#Jet3eta0to1p3ResolutionGraph2023 = rootFile2023Jet3.Get("Eta0to1p3JetResolutionGraph")
#Jet3eta0to1p3ResolutionGraph2018 = rootFile2018Jet3.Get("Eta0to1p3JetResolutionGraph")
#eta 2.5 to 3
#Jet3eta0to1p3ResolutionGraph2023 = rootFile2023Jet3.Get("Eta0to1p3JetResolutionGraph")
#Jet3eta0to1p3ResolutionGraph2018 = rootFile2018Jet3.Get("Eta0to1p3JetResolutionGraph")
#eta 3 to 5
#Jet3eta0to1p3ResolutionGraph2023 = rootFile2023Jet3.Get("Eta0to1p3JetResolutionGraph")
#Jet3eta0to1p3ResolutionGraph2018 = rootFile2018Jet3.Get("Eta0to1p3JetResolutionGraph")
