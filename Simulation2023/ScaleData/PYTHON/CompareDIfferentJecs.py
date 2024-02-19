import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,normal,raw,nom,yAxisTitle,xAxisTitle,title):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.SetBottomMargin(0.18)
    canvas.SetTopMargin(0.05)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)

    legend = ROOT.TLegend(0.4,0.6,0.65,0.85)
    legend.SetFillStyle(4000)
    legend.SetTextSize(0.045)
    legend.SetLineWidth(0)

    normalgraph = ROOT.TGraphAsymmErrors(normal)
    for i in range(0,int(normal.GetNbinsX())):
        normalgraph.SetPointEXhigh(i,0.0)
        normalgraph.SetPointEXlow(i,0.0)

    rawgraph = ROOT.TGraphAsymmErrors(raw)
    for i in range(0,int(raw.GetNbinsX())):
        rawgraph.SetPointEXhigh(i,0.0)
        rawgraph.SetPointEXlow(i,0.0)

    nomgraph = ROOT.TGraphAsymmErrors(nom)
    for i in range(0,int(nom.GetNbinsX())):
        nomgraph.SetPointEXhigh(i,0.0)
        nomgraph.SetPointEXlow(i,0.0)

    #draw sim
    normalgraph.SetStats(0)
    normalgraph.SetLineColor(ROOT.kBlack)
    normalgraph.SetLineWidth(2)
    normalgraph.SetTitle("")
    normalgraph.SetMarkerColor(ROOT.kBlack)
    normalgraph.SetMarkerStyle(4)
    normalgraph.SetMarkerSize(3)
    rawgraph.SetStats(0)
    rawgraph.SetLineColor(ROOT.kBlue)
    rawgraph.SetLineWidth(2)
    rawgraph.SetTitle("")
    rawgraph.SetMarkerColor(ROOT.kBlue)
    rawgraph.SetMarkerStyle(4)
    rawgraph.SetMarkerSize(3)
    nomgraph.SetStats(0)
    nomgraph.SetLineColor(ROOT.kGreen)
    nomgraph.SetLineWidth(2)
    nomgraph.SetTitle("")
    nomgraph.SetMarkerColor(ROOT.kGreen)
    nomgraph.SetMarkerStyle(4)
    nomgraph.SetMarkerSize(3)

    normalgraph.GetYaxis().SetTitle(yAxisTitle)
    normalgraph.GetXaxis().SetTitleSize(0.06)
    normalgraph.GetXaxis().SetTitle(xAxisTitle)
    normalgraph.GetXaxis().SetLabelSize(0.06)
    normalgraph.GetXaxis().SetNdivisions(207)
    normalgraph.GetYaxis().SetLabelSize(0.06)
    normalgraph.GetYaxis().SetTitleSize(0.08)
    normalgraph.GetYaxis().SetTitleOffset(0.8)

    legend.AddEntry(normalgraph,title+" old JEC","p")
    legend.AddEntry(rawgraph,title+" no JEC","p")
    legend.AddEntry(nomgraph,title+" new JEC","p")

    normalgraph.Draw("AP")
    rawgraph.Draw("P same")
    nomgraph.Draw("P same")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/Pdf/"

#load Asymmetry hists
#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"
rootFile = ROOT.TFile.Open(inDirectory+"_PlotSimulation_WithScale_Run32023_MC.root","READ")

#load pt Jet1
pt1sim_hist = rootFile.Get("pt1sim_hist")
pt1rawsim_hist = rootFile.Get("pt1rawsim_hist")
pt1nomsim_hist = rootFile.Get("pt1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt1.pdf",pt1sim_hist,pt1rawsim_hist,pt1nomsim_hist,"#sigma [pb]","P_{t1}","P_{t1}")

#load pt Jet2
pt2sim_hist = rootFile.Get("pt2sim_hist")
pt2rawsim_hist = rootFile.Get("pt2rawsim_hist")
pt2nomsim_hist = rootFile.Get("pt2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt2.pdf",pt2sim_hist,pt2rawsim_hist,pt2nomsim_hist,"#sigma [pb]","P_{t2}","P_{t2}")

#load pt Jet3
pt3sim_hist = rootFile.Get("pt3sim_hist")
pt3rawsim_hist = rootFile.Get("pt3rawsim_hist")
pt3nomsim_hist = rootFile.Get("pt3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt3.pdf",pt3sim_hist,pt3rawsim_hist,pt3nomsim_hist,"#sigma [pb]","P_{t3}","P_{t3}")

#load Mjj
mjjsim_hist = rootFile.Get("mjjsim_hist")
mjjrawsim_hist = rootFile.Get("mjjrawsim_hist")
mjjnomsim_hist = rootFile.Get("mjjnomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Mjj.pdf",mjjsim_hist,mjjrawsim_hist,mjjnomsim_hist,"#sigma [pb]","M_{jj}","M_{jj}")
