import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,legendtitle):
    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)

    for i in range(0,int(data1.GetNbinsX())):
	    Efficiency.SetPointEXhigh(i,0.0)
	    Efficiency.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.35,0.1,0.6,0.35)
    Efficiency.SetStats(0)
    Efficiency.SetLineColor(ROOT.kBlack)
    Efficiency.SetLineWidth(1)
    Efficiency.GetYaxis().SetTitle(yAxisTitle)
    Efficiency.GetXaxis().SetTitle(xAxisTitle)
    Efficiency.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    Efficiency.SetTitle("")
    Efficiency.SetMarkerStyle(4)
    legend.AddEntry(Efficiency,legendtitle,"p")
    legend.SetFillStyle(4000)
    legend.SetLineWidth(0)
    #Set font size
    legend.SetTextSize(0.045)
    Efficiency.SetMarkerSize(3)
    Efficiency.SetLineWidth(2)
    Efficiency.GetYaxis().SetLabelSize(0.045)
    Efficiency.GetYaxis().SetTitleSize(0.05)
    Efficiency.GetXaxis().SetLabelSize(0.045)
    Efficiency.GetXaxis().SetTitleSize(0.05)
    #Efficiency.GetYaxis().SetLabelOffset(0.01)
    #Efficiency.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.1)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)
    Efficiency.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/RootB/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023B_"
inFileName = inDirectory+"PlotTriggerEfficientcy_Run2023B.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
HLT_PFJet = histFile.Get("HLT_PFJet")
HLT_PFHTJet = histFile.Get("HLT_PFHT")

#HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")
#HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")
#RootHisttoPdf(outDirectory+"PlottriggerEfficientcy_HLT_PFJet550_500asreference.pdf",HLT_PFJet550,HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","pt1 [GeV]","Run2023B","Trigger Efficiency pt>550")


HLT_PFJet40 = HLT_PFJet.Get("HLT_PFJet40")
HLT_PFJet60 = HLT_PFJet.Get("HLT_PFJet60")
HLT_PFJet80 = HLT_PFJet.Get("HLT_PFJet80")
HLT_PFJet110 = HLT_PFJet.Get("HLT_PFJet110")
HLT_PFJet140 = HLT_PFJet.Get("HLT_PFJet140")
HLT_PFJet200 = HLT_PFJet.Get("HLT_PFJet200")
HLT_PFJet260 = HLT_PFJet.Get("HLT_PFJet260")
HLT_PFJet320 = HLT_PFJet.Get("HLT_PFJet320")
HLT_PFJet400 = HLT_PFJet.Get("HLT_PFJet400")
HLT_PFJet450 = HLT_PFJet.Get("HLT_PFJet450")
HLT_PFJet500 = HLT_PFJet.Get("HLT_PFJet500")
HLT_PFJet550 = HLT_PFJet.Get("HLT_PFJet550")

Ref_HLT_PFJet40 = HLT_PFJet.Get("Ref_HLT_PFJet40")
Ref_HLT_PFJet60 = HLT_PFJet.Get("Ref_HLT_PFJet60")
Ref_HLT_PFJet80 = HLT_PFJet.Get("Ref_HLT_PFJet80")
Ref_HLT_PFJet110 = HLT_PFJet.Get("Ref_HLT_PFJet110")
Ref_HLT_PFJet140 = HLT_PFJet.Get("Ref_HLT_PFJet140")
Ref_HLT_PFJet200 = HLT_PFJet.Get("Ref_HLT_PFJet200")
Ref_HLT_PFJet260 = HLT_PFJet.Get("Ref_HLT_PFJet260")
Ref_HLT_PFJet320 = HLT_PFJet.Get("Ref_HLT_PFJet320")
Ref_HLT_PFJet400 = HLT_PFJet.Get("Ref_HLT_PFJet400")
Ref_HLT_PFJet450 = HLT_PFJet.Get("Ref_HLT_PFJet450")
Ref_HLT_PFJet500 = HLT_PFJet.Get("Ref_HLT_PFJet500")
Ref_HLT_PFJet550 = HLT_PFJet.Get("Ref_HLT_PFJet550")

RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet60.pdf",HLT_PFJet60,Ref_HLT_PFJet40,"HLT_PFJet60/HLT_PFJet40","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>60")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet80.pdf",HLT_PFJet80,Ref_HLT_PFJet60,"HLT_PFJet80/HLT_PFJet60","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>80")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet80.pdf",HLT_PFJet80,Ref_HLT_PFJet60,"HLT_PFJet80/HLT_PFJet60","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>80")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet110.pdf",HLT_PFJet110,Ref_HLT_PFJet80,"HLT_PFJet110/HLT_PFJet80","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>110")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet140.pdf",HLT_PFJet140,Ref_HLT_PFJet110,"HLT_PFJet140/HLT_PFJet110","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>140")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet200.pdf",HLT_PFJet200,Ref_HLT_PFJet140,"HLT_PFJet200/HLT_PFJet140","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>200")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet260.pdf",HLT_PFJet260,Ref_HLT_PFJet200,"HLT_PFJet260/HLT_PFJet200","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>260")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet320.pdf",HLT_PFJet320,Ref_HLT_PFJet260,"HLT_PFJet320/HLT_PFJet260","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>320")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet400.pdf",HLT_PFJet400,Ref_HLT_PFJet320,"HLT_PFJet400/HLT_PFJet320","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>400")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet450.pdf",HLT_PFJet450,Ref_HLT_PFJet400,"HLT_PFJet450/HLT_PFJet400","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>450")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet500.pdf",HLT_PFJet500,Ref_HLT_PFJet450,"HLT_PFJet500/HLT_PFJet450","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>500")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet550.pdf",HLT_PFJet550,Ref_HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>550")


HLT_PFHT180 = HLT_PFHTJet.Get("HLT_PFHT180")
HLT_PFHT250 = HLT_PFHTJet.Get("HLT_PFHT250")
HLT_PFHT350 = HLT_PFHTJet.Get("HLT_PFHT350")
HLT_PFHT370 = HLT_PFHTJet.Get("HLT_PFHT370")
HLT_PFHT430 = HLT_PFHTJet.Get("HLT_PFHT430")
HLT_PFHT510 = HLT_PFHTJet.Get("HLT_PFHT510")
HLT_PFHT590 = HLT_PFHTJet.Get("HLT_PFHT590")
HLT_PFHT680 = HLT_PFHTJet.Get("HLT_PFHT680")
HLT_PFHT780 = HLT_PFHTJet.Get("HLT_PFHT780")
HLT_PFHT890 = HLT_PFHTJet.Get("HLT_PFHT890")
HLT_PFHT1050 = HLT_PFHTJet.Get("HLT_PFHT1050")

Ref_HLT_PFHT180 = HLT_PFHTJet.Get("Ref_HLT_PFHT180")
Ref_HLT_PFHT250 = HLT_PFHTJet.Get("Ref_HLT_PFHT250")
Ref_HLT_PFHT350 = HLT_PFHTJet.Get("Ref_HLT_PFHT350")
Ref_HLT_PFHT370 = HLT_PFHTJet.Get("Ref_HLT_PFHT370")
Ref_HLT_PFHT430 = HLT_PFHTJet.Get("Ref_HLT_PFHT430")
Ref_HLT_PFHT510 = HLT_PFHTJet.Get("Ref_HLT_PFHT510")
Ref_HLT_PFHT590 = HLT_PFHTJet.Get("Ref_HLT_PFHT590")
Ref_HLT_PFHT680 = HLT_PFHTJet.Get("Ref_HLT_PFHT680")
Ref_HLT_PFHT780 = HLT_PFHTJet.Get("Ref_HLT_PFHT780")
Ref_HLT_PFHT890 = HLT_PFHTJet.Get("Ref_HLT_PFHT890")
Ref_HLT_PFHT1050 = HLT_PFHTJet.Get("Ref_HLT_PFHT1050")

RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT250.pdf",HLT_PFHT250,Ref_HLT_PFHT180,"HLT_PFHT250/HLT_PFHT180","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>250")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT350.pdf",HLT_PFHT350,Ref_HLT_PFHT250,"HLT_PFHT350/HLT_PFHT250","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>350")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT370.pdf",HLT_PFHT370,Ref_HLT_PFHT350,"HLT_PFHT370/HLT_PFHT350","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>370")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT430.pdf",HLT_PFHT430,Ref_HLT_PFHT370,"HLT_PFHT430/HLT_PFHT370","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>430")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT510.pdf",HLT_PFHT510,Ref_HLT_PFHT430,"HLT_PFHT510/HLT_PFHT430","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>510")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT590.pdf",HLT_PFHT590,Ref_HLT_PFHT510,"HLT_PFHT590/HLT_PFHT510","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>590")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT680.pdf",HLT_PFHT680,Ref_HLT_PFHT590,"HLT_PFHT680/HLT_PFHT590","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>680")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT780.pdf",HLT_PFHT780,Ref_HLT_PFHT680,"HLT_PFHT780/HLT_PFHT680","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>780")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT890.pdf",HLT_PFHT890,Ref_HLT_PFHT780,"HLT_PFHT890/HLT_PFHT780","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>890")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT1050.pdf",HLT_PFHT1050,Ref_HLT_PFHT890,"HLT_PFHT1050/HLT_PFHT890","M_{jj} [GeV]","Run3 B 2023 Trigger Efficiency p_{t}>1050")
