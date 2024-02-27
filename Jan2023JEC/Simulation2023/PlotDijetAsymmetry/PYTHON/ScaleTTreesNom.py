import ROOT
import numpy as np

inDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"
outDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/Pdf/"
outRootDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"

#load tree data

root50to80 = ROOT.TFile.Open(inDirectory+"50to80_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale50to80 = ((1.679e+07)/(11988000))
print(scale50to80)
root80to120 = ROOT.TFile.Open(inDirectory+"80to120_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale80to120 = ((2.513e+06)/(17979000))
print(scale80to120)
root120to170 = ROOT.TFile.Open(inDirectory+"120to170_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale120to170 = ((4.574e+05)/(17964000))
print(scale120to170)
root170to300 = ROOT.TFile.Open(inDirectory+"170to300_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale170to300 = ((1.162e+05)/(17889000))
print(scale170to300)
root300to470 = ROOT.TFile.Open(inDirectory+"300to470_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale300to470 = ((7.584e+03)/(34626000))
print(scale300to470)
root470to600 = ROOT.TFile.Open(inDirectory+"470to600_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale470to600 = ((6.490e+02)/(16766000))
print(scale470to600)
root600to800 = ROOT.TFile.Open(inDirectory+"600to800_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale600to800 = ((1.809e+02)/(40468000))
print(scale600to800)
root800to1000 = ROOT.TFile.Open(inDirectory+"800to1000_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale800to1000 = ((3.105e+01)/(23908000))
print(scale800to1000)
root1000to1400 = ROOT.TFile.Open(inDirectory+"1000to1400_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale1000to1400 = ((8.829e+00)/(11956000))
print(scale1000to1400)
root1400to1800 = ROOT.TFile.Open(inDirectory+"1400to1800_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale1400to1800 = ((7.952e-01)/(3596000))
print(scale1400to1800)
root1800to2400 = ROOT.TFile.Open(inDirectory+"1800to2400_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale1800to2400 = ((1.147e-01)/(1792000))
print(scale1800to2400)
root2400to3200 = ROOT.TFile.Open(inDirectory+"2400to3200_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale2400to3200 = ((7.619e-03)/(1200000))
print(scale2400to3200)
root3200 = ROOT.TFile.Open(inDirectory+"3200_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root")
scale3200 = ((2.331e-04)/(478000))
print(scale3200)
"""
QCD_PT-50to80_TuneCP5_13p6TeV_pythia8 1.679e+07 11988000
QCD_PT-80to120_TuneCP5_13p6TeV_pythia8 2.513e+06 17979000
QCD_PT-120to170_TuneCP5_13p6TeV_pythia8 4.574e+05 17964000
QCD_PT-170to300_TuneCP5_13p6TeV_pythia8 1.162e+05 17889000
QCD_PT-300to470_TuneCP5_13p6TeV_pythia8 7.584e+03 34626000
QCD_PT-470to600_TuneCP5_13p6TeV_pythia8 6.490e+02 16766000
QCD_PT-600to800_TuneCP5_13p6TeV_pythia8 1.809e+02 40468000
QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8 3.105e+01 23908000
QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8 8.829e+00 11956000
QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8 7.952e-01 3596000
QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8 1.147e-01 1792000
QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8 7.619e-03 1200000
QCD_PT-3200_TuneCP5_13p6TeV_pythia8 2.331e-04 478000
"""

#load and scale 50to80 Simulation
#load and scale jet1 data
PtAsymmetryNom50to80 = root50to80.Get("PtAsymmetryNom")
PtAsymmetryNom50to80.Scale(scale50to80)
PhiDifferenceNom50to80 = root50to80.Get("PhiDifferenceNom")
PhiDifferenceNom50to80.Scale(scale50to80)
EtaDifferenceNom50to80 = root50to80.Get("EtaDifferenceNom")
EtaDifferenceNom50to80.Scale(scale50to80)
YDifferenceNom50to80 = root50to80.Get("YDifferenceNom")
YDifferenceNom50to80.Scale(scale50to80)
ThetaDifferenceNom50to80 = root50to80.Get("ThetaDifferenceNom")
ThetaDifferenceNom50to80.Scale(scale50to80)

#load and scale 80to120 Simulation
#load and scale jet1 data
PtAsymmetryNom80to120 = root80to120.Get("PtAsymmetryNom")
PtAsymmetryNom80to120.Scale(scale80to120)
PhiDifferenceNom80to120 = root80to120.Get("PhiDifferenceNom")
PhiDifferenceNom80to120.Scale(scale80to120)
EtaDifferenceNom80to120 = root80to120.Get("EtaDifferenceNom")
EtaDifferenceNom80to120.Scale(scale80to120)
YDifferenceNom80to120 = root80to120.Get("YDifferenceNom")
YDifferenceNom80to120.Scale(scale80to120)
ThetaDifferenceNom80to120 = root80to120.Get("ThetaDifferenceNom")
ThetaDifferenceNom80to120.Scale(scale80to120)

#load and scale 120to170 Simulation
#load and scale jet1 data
PtAsymmetryNom120to170 = root120to170.Get("PtAsymmetryNom")
PtAsymmetryNom120to170.Scale(scale120to170)
PhiDifferenceNom120to170 = root120to170.Get("PhiDifferenceNom")
PhiDifferenceNom120to170.Scale(scale120to170)
EtaDifferenceNom120to170 = root120to170.Get("EtaDifferenceNom")
EtaDifferenceNom120to170.Scale(scale120to170)
YDifferenceNom120to170 = root120to170.Get("YDifferenceNom")
YDifferenceNom120to170.Scale(scale120to170)
ThetaDifferenceNom120to170 = root120to170.Get("ThetaDifferenceNom")
ThetaDifferenceNom120to170.Scale(scale120to170)

#load and scale 170to300 Simulation
#load and scale jet1 data
PtAsymmetryNom170to300 = root170to300.Get("PtAsymmetryNom")
PtAsymmetryNom170to300.Scale(scale170to300)
PhiDifferenceNom170to300 = root170to300.Get("PhiDifferenceNom")
PhiDifferenceNom170to300.Scale(scale170to300)
EtaDifferenceNom170to300 = root170to300.Get("EtaDifferenceNom")
EtaDifferenceNom170to300.Scale(scale170to300)
YDifferenceNom170to300 = root170to300.Get("YDifferenceNom")
YDifferenceNom170to300.Scale(scale170to300)
ThetaDifferenceNom170to300 = root170to300.Get("ThetaDifferenceNom")
ThetaDifferenceNom170to300.Scale(scale170to300)

#load and scale 300to470 Simulation
#load and scale jet1 data
PtAsymmetryNom300to470 = root300to470.Get("PtAsymmetryNom")
PtAsymmetryNom300to470.Scale(scale300to470)
PhiDifferenceNom300to470 = root300to470.Get("PhiDifferenceNom")
PhiDifferenceNom300to470.Scale(scale300to470)
EtaDifferenceNom300to470 = root300to470.Get("EtaDifferenceNom")
EtaDifferenceNom300to470.Scale(scale300to470)
YDifferenceNom300to470 = root300to470.Get("YDifferenceNom")
YDifferenceNom300to470.Scale(scale300to470)
ThetaDifferenceNom300to470 = root300to470.Get("ThetaDifferenceNom")
ThetaDifferenceNom300to470.Scale(scale300to470)

#load and scale 470to600 Simulation
#load and scale jet1 data
PtAsymmetryNom470to600 = root470to600.Get("PtAsymmetryNom")
PtAsymmetryNom470to600.Scale(scale470to600)
PhiDifferenceNom470to600 = root470to600.Get("PhiDifferenceNom")
PhiDifferenceNom470to600.Scale(scale470to600)
EtaDifferenceNom470to600 = root470to600.Get("EtaDifferenceNom")
EtaDifferenceNom470to600.Scale(scale470to600)
YDifferenceNom470to600 = root470to600.Get("YDifferenceNom")
YDifferenceNom470to600.Scale(scale470to600)
ThetaDifferenceNom470to600 = root470to600.Get("ThetaDifferenceNom")
ThetaDifferenceNom470to600.Scale(scale470to600)

#load and scale 600to800 Simulation
#load and scale jet1 data
PtAsymmetryNom600to800 = root600to800.Get("PtAsymmetryNom")
PtAsymmetryNom600to800.Scale(scale600to800)
PhiDifferenceNom600to800 = root600to800.Get("PhiDifferenceNom")
PhiDifferenceNom600to800.Scale(scale600to800)
EtaDifferenceNom600to800 = root600to800.Get("EtaDifferenceNom")
EtaDifferenceNom600to800.Scale(scale600to800)
YDifferenceNom600to800 = root600to800.Get("YDifferenceNom")
YDifferenceNom600to800.Scale(scale600to800)
ThetaDifferenceNom600to800 = root600to800.Get("ThetaDifferenceNom")
ThetaDifferenceNom600to800.Scale(scale600to800)

#load and scale 800to1000 Simulation
#load and scale jet1 data
PtAsymmetryNom800to1000 = root800to1000.Get("PtAsymmetryNom")
PtAsymmetryNom800to1000.Scale(scale800to1000)
PhiDifferenceNom800to1000 = root800to1000.Get("PhiDifferenceNom")
PhiDifferenceNom800to1000.Scale(scale800to1000)
EtaDifferenceNom800to1000 = root800to1000.Get("EtaDifferenceNom")
EtaDifferenceNom800to1000.Scale(scale800to1000)
YDifferenceNom800to1000 = root800to1000.Get("YDifferenceNom")
YDifferenceNom800to1000.Scale(scale800to1000)
ThetaDifferenceNom800to1000 = root800to1000.Get("ThetaDifferenceNom")
ThetaDifferenceNom800to1000.Scale(scale800to1000)

#load and scale 1000to1400 Simulation
#load and scale jet1 data
PtAsymmetryNom1000to1400 = root1000to1400.Get("PtAsymmetryNom")
PtAsymmetryNom1000to1400.Scale(scale1000to1400)
PhiDifferenceNom1000to1400 = root1000to1400.Get("PhiDifferenceNom")
PhiDifferenceNom1000to1400.Scale(scale1000to1400)
EtaDifferenceNom1000to1400 = root1000to1400.Get("EtaDifferenceNom")
EtaDifferenceNom1000to1400.Scale(scale1000to1400)
YDifferenceNom1000to1400 = root1000to1400.Get("YDifferenceNom")
YDifferenceNom1000to1400.Scale(scale1000to1400)
ThetaDifferenceNom1000to1400 = root1000to1400.Get("ThetaDifferenceNom")
ThetaDifferenceNom1000to1400.Scale(scale1000to1400)

#load and scale 1400to1800 Simulation
#load and scale jet1 data
PtAsymmetryNom1400to1800 = root1400to1800.Get("PtAsymmetryNom")
PtAsymmetryNom1400to1800.Scale(scale1400to1800)
PhiDifferenceNom1400to1800 = root1400to1800.Get("PhiDifferenceNom")
PhiDifferenceNom1400to1800.Scale(scale1400to1800)
EtaDifferenceNom1400to1800 = root1400to1800.Get("EtaDifferenceNom")
EtaDifferenceNom1400to1800.Scale(scale1400to1800)
YDifferenceNom1400to1800 = root1400to1800.Get("YDifferenceNom")
YDifferenceNom1400to1800.Scale(scale1400to1800)
ThetaDifferenceNom1400to1800 = root1400to1800.Get("ThetaDifferenceNom")
ThetaDifferenceNom1400to1800.Scale(scale1400to1800)

#load and scale 1800to2400 Simulation
#load and scale jet1 data
PtAsymmetryNom1800to2400 = root1800to2400.Get("PtAsymmetryNom")
PtAsymmetryNom1800to2400.Scale(scale1800to2400)
PhiDifferenceNom1800to2400 = root1800to2400.Get("PhiDifferenceNom")
PhiDifferenceNom1800to2400.Scale(scale1800to2400)
EtaDifferenceNom1800to2400 = root1800to2400.Get("EtaDifferenceNom")
EtaDifferenceNom1800to2400.Scale(scale1800to2400)
YDifferenceNom1800to2400 = root1800to2400.Get("YDifferenceNom")
YDifferenceNom1800to2400.Scale(scale1800to2400)
ThetaDifferenceNom1800to2400 = root1800to2400.Get("ThetaDifferenceNom")
ThetaDifferenceNom1800to2400.Scale(scale1800to2400)

#load and scale 2400to3200 Simulation
#load and scale jet1 data
PtAsymmetryNom2400to3200 = root2400to3200.Get("PtAsymmetryNom")
PtAsymmetryNom2400to3200.Scale(scale2400to3200)
PhiDifferenceNom2400to3200 = root2400to3200.Get("PhiDifferenceNom")
PhiDifferenceNom2400to3200.Scale(scale2400to3200)
EtaDifferenceNom2400to3200 = root2400to3200.Get("EtaDifferenceNom")
EtaDifferenceNom2400to3200.Scale(scale2400to3200)
YDifferenceNom2400to3200 = root2400to3200.Get("YDifferenceNom")
YDifferenceNom2400to3200.Scale(scale2400to3200)
ThetaDifferenceNom2400to3200 = root2400to3200.Get("ThetaDifferenceNom")
ThetaDifferenceNom2400to3200.Scale(scale2400to3200)

#load and scale 3200 Simulation
#load and scale jet1 data
PtAsymmetryNom3200 = root3200.Get("PtAsymmetryNom")
PtAsymmetryNom3200.Scale(scale3200)
PhiDifferenceNom3200 = root3200.Get("PhiDifferenceNom")
PhiDifferenceNom3200.Scale(scale3200)
EtaDifferenceNom3200 = root3200.Get("EtaDifferenceNom")
EtaDifferenceNom3200.Scale(scale3200)
YDifferenceNom3200 = root3200.Get("YDifferenceNom")
YDifferenceNom3200.Scale(scale3200)
ThetaDifferenceNom3200 = root3200.Get("ThetaDifferenceNom")
ThetaDifferenceNom3200.Scale(scale3200)

#add hists together
#add PtAsymmetryNom hists together
canvas = ROOT.TCanvas("PtAsymmetryNom_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PtAsymmetryNomsim_hist = ROOT.TH1D("PtAsymmetryNomsim_hist","PtAsymmetryNomsim_hist",PtAsymmetryNom3200.GetNbinsX(),PtAsymmetryNom3200.GetXaxis().GetXmin(),PtAsymmetryNom3200.GetXaxis().GetXmax())
PtAsymmetryNomsim_hist.Sumw2()

PtAsymmetryNomsim_hist.Add(PtAsymmetryNom50to80)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom80to120)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom120to170)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom170to300)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom300to470)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom470to600)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom600to800)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom800to1000)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom1000to1400)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom1400to1800)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom1800to2400)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom2400to3200)
PtAsymmetryNomsim_hist.Add(PtAsymmetryNom3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PtAsymmetryNomsim_hist,"(Pt1-Pt2)/(Pt1+Pt2)","p")
legend.SetTextSize(0.03)

PtAsymmetryNomsim_hist.SetStats(0)
PtAsymmetryNomsim_hist.SetLineColor(ROOT.kBlack)
PtAsymmetryNomsim_hist.SetMarkerColor(ROOT.kBlack)
PtAsymmetryNomsim_hist.SetLineWidth(2)
PtAsymmetryNomsim_hist.SetMarkerStyle(4)
PtAsymmetryNomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
PtAsymmetryNomsim_hist.GetXaxis().SetTitle("(Pt1-Pt2)/(Pt1+Pt2)")
PtAsymmetryNomsim_hist.SetTitle("Dijet Asymmetry for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
PtAsymmetryNomsim_hist.SetMarkerSize(3)
PtAsymmetryNomsim_hist.SetLineWidth(2)
PtAsymmetryNomsim_hist.GetYaxis().SetLabelSize(0.045)
PtAsymmetryNomsim_hist.GetYaxis().SetTitleSize(0.05)
PtAsymmetryNomsim_hist.GetXaxis().SetLabelSize(0.045)
PtAsymmetryNomsim_hist.GetXaxis().SetTitleSize(0.05)
#PtAsymmetryNomsim_hist.GetYaxis().SetLabelOffset(0.01)
#PtAsymmetryNomsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PtAsymmetryNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add PhiDifferenceNom hists together
canvas = ROOT.TCanvas("PhiDifferenceNom_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PhiDifferenceNomsim_hist = ROOT.TH1D("PhiDifferenceNomsim_hist","PhiDifferenceNomsim_hist",PhiDifferenceNom3200.GetNbinsX(),PhiDifferenceNom3200.GetXaxis().GetXmin(),PhiDifferenceNom3200.GetXaxis().GetXmax())
PhiDifferenceNomsim_hist.Sumw2()

PhiDifferenceNomsim_hist.Add(PhiDifferenceNom50to80)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom80to120)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom120to170)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom170to300)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom300to470)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom470to600)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom600to800)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom800to1000)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom1000to1400)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom1400to1800)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom1800to2400)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom2400to3200)
PhiDifferenceNomsim_hist.Add(PhiDifferenceNom3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PhiDifferenceNomsim_hist,"Phi1-Phi2","p")
legend.SetTextSize(0.03)

PhiDifferenceNomsim_hist.SetStats(0)
PhiDifferenceNomsim_hist.SetLineColor(ROOT.kBlack)
PhiDifferenceNomsim_hist.SetMarkerColor(ROOT.kBlack)
PhiDifferenceNomsim_hist.SetLineWidth(2)
PhiDifferenceNomsim_hist.SetMarkerStyle(4)
PhiDifferenceNomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
PhiDifferenceNomsim_hist.GetXaxis().SetTitle("Degree")
PhiDifferenceNomsim_hist.SetTitle("Phi Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
PhiDifferenceNomsim_hist.SetMarkerSize(3)
PhiDifferenceNomsim_hist.SetLineWidth(2)
PhiDifferenceNomsim_hist.GetYaxis().SetLabelSize(0.045)
PhiDifferenceNomsim_hist.GetYaxis().SetTitleSize(0.05)
PhiDifferenceNomsim_hist.GetXaxis().SetLabelSize(0.045)
PhiDifferenceNomsim_hist.GetXaxis().SetTitleSize(0.05)
#PhiDifferenceNomsim_hist.GetYaxis().SetLabelOffset(0.01)
#PhiDifferenceNomsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PhiDifferenceNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_PhiDifferenceNoms_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add EtaDifferenceNom hists together
canvas = ROOT.TCanvas("EtaDifferenceNom_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

EtaDifferenceNomsim_hist = ROOT.TH1D("EtaDifferenceNomsim_hist","EtaDifferenceNomsim_hist",EtaDifferenceNom3200.GetNbinsX(),EtaDifferenceNom3200.GetXaxis().GetXmin(),EtaDifferenceNom3200.GetXaxis().GetXmax())
EtaDifferenceNomsim_hist.Sumw2()

EtaDifferenceNomsim_hist.Add(EtaDifferenceNom50to80)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom80to120)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom120to170)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom170to300)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom300to470)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom470to600)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom600to800)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom800to1000)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom1000to1400)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom1400to1800)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom1800to2400)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom2400to3200)
EtaDifferenceNomsim_hist.Add(EtaDifferenceNom3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(EtaDifferenceNomsim_hist,"Eta1-Eta2","p")
legend.SetTextSize(0.03)

EtaDifferenceNomsim_hist.SetStats(0)
EtaDifferenceNomsim_hist.SetLineColor(ROOT.kBlack)
EtaDifferenceNomsim_hist.SetMarkerColor(ROOT.kBlack)
EtaDifferenceNomsim_hist.SetLineWidth(2)
EtaDifferenceNomsim_hist.SetMarkerStyle(4)
EtaDifferenceNomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
EtaDifferenceNomsim_hist.GetXaxis().SetTitle("Eta")
EtaDifferenceNomsim_hist.SetTitle("Eta Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
EtaDifferenceNomsim_hist.SetMarkerSize(3)
EtaDifferenceNomsim_hist.SetLineWidth(2)
EtaDifferenceNomsim_hist.GetYaxis().SetLabelSize(0.045)
EtaDifferenceNomsim_hist.GetYaxis().SetTitleSize(0.05)
EtaDifferenceNomsim_hist.GetXaxis().SetLabelSize(0.045)
EtaDifferenceNomsim_hist.GetXaxis().SetTitleSize(0.05)
#EtaDifferenceNomsim_hist.GetYaxis().SetLabelOffset(0.01)
#EtaDifferenceNomsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
EtaDifferenceNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_EtaDifferenceNoms_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add YDifferenceNom hists together
canvas = ROOT.TCanvas("YDifferenceNom_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

YDifferenceNomsim_hist = ROOT.TH1D("YDifferenceNomsim_hist","YDifferenceNomsim_hist",YDifferenceNom3200.GetNbinsX(),YDifferenceNom3200.GetXaxis().GetXmin(),YDifferenceNom3200.GetXaxis().GetXmax())
YDifferenceNomsim_hist.Sumw2()

YDifferenceNomsim_hist.Add(YDifferenceNom50to80)
YDifferenceNomsim_hist.Add(YDifferenceNom80to120)
YDifferenceNomsim_hist.Add(YDifferenceNom120to170)
YDifferenceNomsim_hist.Add(YDifferenceNom170to300)
YDifferenceNomsim_hist.Add(YDifferenceNom300to470)
YDifferenceNomsim_hist.Add(YDifferenceNom470to600)
YDifferenceNomsim_hist.Add(YDifferenceNom600to800)
YDifferenceNomsim_hist.Add(YDifferenceNom800to1000)
YDifferenceNomsim_hist.Add(YDifferenceNom1000to1400)
YDifferenceNomsim_hist.Add(YDifferenceNom1400to1800)
YDifferenceNomsim_hist.Add(YDifferenceNom1800to2400)
YDifferenceNomsim_hist.Add(YDifferenceNom2400to3200)
YDifferenceNomsim_hist.Add(YDifferenceNom3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(YDifferenceNomsim_hist,"Y1-Y2","p")
legend.SetTextSize(0.03)

YDifferenceNomsim_hist.SetStats(0)
YDifferenceNomsim_hist.SetLineColor(ROOT.kBlack)
YDifferenceNomsim_hist.SetMarkerColor(ROOT.kBlack)
YDifferenceNomsim_hist.SetLineWidth(2)
YDifferenceNomsim_hist.SetMarkerStyle(4)
YDifferenceNomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
YDifferenceNomsim_hist.GetXaxis().SetTitle("Y")
YDifferenceNomsim_hist.SetTitle("Y Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
YDifferenceNomsim_hist.SetMarkerSize(3)
YDifferenceNomsim_hist.SetLineWidth(2)
YDifferenceNomsim_hist.GetYaxis().SetLabelSize(0.045)
YDifferenceNomsim_hist.GetYaxis().SetTitleSize(0.05)
YDifferenceNomsim_hist.GetXaxis().SetLabelSize(0.045)
YDifferenceNomsim_hist.GetXaxis().SetTitleSize(0.05)
#YDifferenceNomsim_hist.GetYaxis().SetLabelOffset(0.01)
#YDifferenceNomsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
YDifferenceNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_YDifferenceNoms_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add ThetaDifferenceNom hists together
canvas = ROOT.TCanvas("ThetaDifferenceNom_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

ThetaDifferenceNomsim_hist = ROOT.TH1D("ThetaDifferenceNomsim_hist","ThetaDifferenceNomsim_hist",ThetaDifferenceNom3200.GetNbinsX(),ThetaDifferenceNom3200.GetXaxis().GetXmin(),ThetaDifferenceNom3200.GetXaxis().GetXmax())
ThetaDifferenceNomsim_hist.Sumw2()

ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom50to80)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom80to120)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom120to170)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom170to300)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom300to470)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom470to600)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom600to800)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom800to1000)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom1000to1400)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom1400to1800)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom1800to2400)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom2400to3200)
ThetaDifferenceNomsim_hist.Add(ThetaDifferenceNom3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(ThetaDifferenceNomsim_hist,"Theta1-Theta2","p")
legend.SetTextSize(0.03)

ThetaDifferenceNomsim_hist.SetStats(0)
ThetaDifferenceNomsim_hist.SetLineColor(ROOT.kBlack)
ThetaDifferenceNomsim_hist.SetMarkerColor(ROOT.kBlack)
ThetaDifferenceNomsim_hist.SetLineWidth(2)
ThetaDifferenceNomsim_hist.SetMarkerStyle(4)
ThetaDifferenceNomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
ThetaDifferenceNomsim_hist.GetXaxis().SetTitle("Degree")
ThetaDifferenceNomsim_hist.SetTitle("Theta Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
ThetaDifferenceNomsim_hist.SetMarkerSize(3)
ThetaDifferenceNomsim_hist.SetLineWidth(2)
ThetaDifferenceNomsim_hist.GetYaxis().SetLabelSize(0.045)
ThetaDifferenceNomsim_hist.GetYaxis().SetTitleSize(0.05)
ThetaDifferenceNomsim_hist.GetXaxis().SetLabelSize(0.045)
ThetaDifferenceNomsim_hist.GetXaxis().SetTitleSize(0.05)
#ThetaDifferenceNomsim_hist.GetYaxis().SetLabelOffset(0.01)
#ThetaDifferenceNomsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
ThetaDifferenceNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_ThetaDifferenceNoms_Run2023_Simulation_Scaled.pdf")
canvas.Clear()




#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023-15Jan2023_MC.root","RECREATE")
PtAsymmetryNomsim_hist.Write()
PhiDifferenceNomsim_hist.Write()
EtaDifferenceNomsim_hist.Write()
YDifferenceNomsim_hist.Write()
ThetaDifferenceNomsim_hist.Write()
outHistFile.Close()
