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
    normalgraph.GetXaxis().SetTitleSize(0.08)
    normalgraph.GetXaxis().SetTitle(xAxisTitle)
    normalgraph.GetXaxis().SetLabelSize(0.06)
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
rootFile = ROOT.TFile.Open(inDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023-15Jan2023_MC.root","READ")

#create PtAsymmetry compare hists pdf
PtAsymmetryNom = rootFile.Get("PtAsymmetryNomsim_hist")
PtAsymmetryRaw = rootFile.Get("PtAsymmetryRawsim_hist")
PtAsymmetry = rootFile.Get("PtAsymmetrysim_hist")
RootHisttoPdf(outDirectory+"PlotDijetAsymmetry_Jan2023_AllRuns.pdf",PtAsymmetry,PtAsymmetryRaw,PtAsymmetryNom,"#sigma [pb]","P_{t1}-P_{t2}/P_{t1}+P_{t2}","Dijet Asymm")

#create PhiDifference compare hists pdf
PhiDifferenceNom = rootFile.Get("PhiDifferenceNomsim_hist")
PhiDifferenceRaw = rootFile.Get("PhiDifferenceRawsim_hist")
PhiDifference = rootFile.Get("PhiDifferencesim_hist")
RootHisttoPdf(outDirectory+"PlotPhiDifference_Jan2023_AllRuns.pdf",PhiDifference,PhiDifferenceRaw,PhiDifferenceNom,"#sigma [pb]","#Delta#phi","#phi Diff")

#create ThetaDifference compare hists pdf
ThetaDifferenceNom = rootFile.Get("ThetaDifferenceNomsim_hist")
ThetaDifferenceRaw = rootFile.Get("ThetaDifferenceRawsim_hist")
ThetaDifference = rootFile.Get("ThetaDifferencesim_hist")
RootHisttoPdf(outDirectory+"PlotThetaDifference_Jan2023_AllRuns.pdf",ThetaDifference,ThetaDifferenceRaw,ThetaDifferenceNom,"#sigma [pb]","#Delta#theta","#theta Diff")

#create YDifference compare hists pdf
YDifferenceNom = rootFile.Get("YDifferenceNomsim_hist")
YDifferenceRaw = rootFile.Get("YDifferenceRawsim_hist")
YDifference = rootFile.Get("YDifferencesim_hist")
RootHisttoPdf(outDirectory+"PlotYDifference_Jan2023_AllRuns.pdf",YDifference,YDifferenceRaw,YDifferenceNom,"#sigma [pb]","#DeltaY","Y Diff")

#create EtaDifference compare hists pdf
EtaDifferenceNom = rootFile.Get("EtaDifferenceNomsim_hist")
EtaDifferenceRaw = rootFile.Get("EtaDifferenceRawsim_hist")
EtaDifference = rootFile.Get("EtaDifferencesim_hist")
RootHisttoPdf(outDirectory+"PlotEtaDifference_Jan2023_AllRuns.pdf",EtaDifference,EtaDifferenceRaw,EtaDifferenceNom,"#sigma [pb]","#Delta#eta","eta Diff")
