import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,data2,yAxisTitle,xAxisTitle,title,undertitle):
    Efficiency = ROOT.TGraphAsymmErrors(int(data1.GetNbinsX()))
    Efficiency.BayesDivide(data1,data2)

    canvas = ROOT.TCanvas("canvas")

    for i in range(0,int(data1.GetNbinsX())):
	    Efficiency.SetPointEXhigh(i,0.0)
	    Efficiency.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    Efficiency.SetStats(0)
    Efficiency.SetLineColor(ROOT.kBlack)
    Efficiency.SetLineWidth(1)
    Efficiency.GetYaxis().SetTitle(yAxisTitle)
    Efficiency.GetXaxis().SetTitle(xAxisTitle)
    Efficiency.GetXaxis().SetRangeUser(data1.GetXaxis().GetXmin(),data1.GetXaxis().GetXmax())
    Efficiency.SetTitle(title+undertitle)
    Efficiency.SetMarkerStyle(4)
    legend.AddEntry(Efficiency,yAxisTitle,"p")
    legend.SetLineWidth(0)
    Efficiency.Draw("AP")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/Pdf/"
pdfnames = "PlotTriggerEfficientcy_Run2023C_"
inFileName = inDirectory+"PlotTriggerEfficientcy_Run2023C.root"
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

RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet60.pdf",HLT_PFJet60,Ref_HLT_PFJet40,"HLT_PFJet60/HLT_PFJet40","Mjj [GeV]","Run2023C","Trigger Efficiency pt>60")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet80.pdf",HLT_PFJet80,Ref_HLT_PFJet60,"HLT_PFJet80/HLT_PFJet60","Mjj [GeV]","Run2023C","Trigger Efficiency pt>80")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFJet80.pdf",HLT_PFJet80,Ref_HLT_PFJet60,"HLT_PFJet80/HLT_PFJet60","Mjj [GeV]","Run2023C","Trigger Efficiency pt>80")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet110.pdf",HLT_PFJet110,Ref_HLT_PFJet80,"HLT_PFJet110/HLT_PFJet80","Mjj [GeV]","Run2023C","Trigger Efficiency pt>110")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet140.pdf",HLT_PFJet140,Ref_HLT_PFJet110,"HLT_PFJet140/HLT_PFJet110","Mjj [GeV]","Run2023C","Trigger Efficiency pt>140")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet200.pdf",HLT_PFJet200,Ref_HLT_PFJet140,"HLT_PFJet200/HLT_PFJet140","Mjj [GeV]","Run2023C","Trigger Efficiency pt>200")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet260.pdf",HLT_PFJet260,Ref_HLT_PFJet200,"HLT_PFJet260/HLT_PFJet200","Mjj [GeV]","Run2023C","Trigger Efficiency pt>260")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet320.pdf",HLT_PFJet320,Ref_HLT_PFJet260,"HLT_PFJet320/HLT_PFJet260","Mjj [GeV]","Run2023C","Trigger Efficiency pt>320")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet400.pdf",HLT_PFJet400,Ref_HLT_PFJet320,"HLT_PFJet400/HLT_PFJet320","Mjj [GeV]","Run2023C","Trigger Efficiency pt>400")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet450.pdf",HLT_PFJet450,Ref_HLT_PFJet400,"HLT_PFJet450/HLT_PFJet400","Mjj [GeV]","Run2023C","Trigger Efficiency pt>450")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet500.pdf",HLT_PFJet500,Ref_HLT_PFJet450,"HLT_PFJet500/HLT_PFJet450","Mjj [GeV]","Run2023C","Trigger Efficiency pt>500")
RootHisttoPdf(outDirectory+"PlottriggerEfficiency_HLT_PFJet550.pdf",HLT_PFJet550,Ref_HLT_PFJet500,"HLT_PFJet550/HLT_PFJet500","Mjj [GeV]","Run2023C","Trigger Efficiency pt>550")


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

RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT250.pdf",HLT_PFHT250,Ref_HLT_PFHT180,"HLT_PFHT250/HLT_PFHT180","Mjj [GeV]","Run2023C","Trigger Efficiency pt>250")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT350.pdf",HLT_PFHT350,Ref_HLT_PFHT250,"HLT_PFHT350/HLT_PFHT250","Mjj [GeV]","Run2023C","Trigger Efficiency pt>350")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT370.pdf",HLT_PFHT370,Ref_HLT_PFHT350,"HLT_PFHT370/HLT_PFHT350","Mjj [GeV]","Run2023C","Trigger Efficiency pt>370")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT430.pdf",HLT_PFHT430,Ref_HLT_PFHT370,"HLT_PFHT430/HLT_PFHT370","Mjj [GeV]","Run2023C","Trigger Efficiency pt>430")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT510.pdf",HLT_PFHT510,Ref_HLT_PFHT430,"HLT_PFHT510/HLT_PFHT430","Mjj [GeV]","Run2023C","Trigger Efficiency pt>510")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT590.pdf",HLT_PFHT590,Ref_HLT_PFHT510,"HLT_PFHT590/HLT_PFHT510","Mjj [GeV]","Run2023C","Trigger Efficiency pt>590")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT680.pdf",HLT_PFHT680,Ref_HLT_PFHT590,"HLT_PFHT680/HLT_PFHT590","Mjj [GeV]","Run2023C","Trigger Efficiency pt>680")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT780.pdf",HLT_PFHT780,Ref_HLT_PFHT680,"HLT_PFHT780/HLT_PFHT680","Mjj [GeV]","Run2023C","Trigger Efficiency pt>780")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT890.pdf",HLT_PFHT890,Ref_HLT_PFHT780,"HLT_PFHT890/HLT_PFHT780","Mjj [GeV]","Run2023C","Trigger Efficiency pt>890")
RootHisttoPdf(outDirectory+"PlotTriggerEfficiency_HLT_PFHT1050.pdf",HLT_PFHT1050,Ref_HLT_PFHT890,"HLT_PFHT1050/HLT_PFHT890","Mjj [GeV]","Run2023C","Trigger Efficiency pt>1050")
