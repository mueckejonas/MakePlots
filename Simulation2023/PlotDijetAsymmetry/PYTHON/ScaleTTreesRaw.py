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
PtAsymmetryRaw50to80 = root50to80.Get("PtAsymmetryRaw")
PtAsymmetryRaw50to80.Scale(scale50to80)
PhiDifferenceRaw50to80 = root50to80.Get("PhiDifferenceRaw")
PhiDifferenceRaw50to80.Scale(scale50to80)
EtaDifferenceRaw50to80 = root50to80.Get("EtaDifferenceRaw")
EtaDifferenceRaw50to80.Scale(scale50to80)
YDifferenceRaw50to80 = root50to80.Get("YDifferenceRaw")
YDifferenceRaw50to80.Scale(scale50to80)
ThetaDifferenceRaw50to80 = root50to80.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw50to80.Scale(scale50to80)

#load and scale 80to120 Simulation
#load and scale jet1 data
PtAsymmetryRaw80to120 = root80to120.Get("PtAsymmetryRaw")
PtAsymmetryRaw80to120.Scale(scale80to120)
PhiDifferenceRaw80to120 = root80to120.Get("PhiDifferenceRaw")
PhiDifferenceRaw80to120.Scale(scale80to120)
EtaDifferenceRaw80to120 = root80to120.Get("EtaDifferenceRaw")
EtaDifferenceRaw80to120.Scale(scale80to120)
YDifferenceRaw80to120 = root80to120.Get("YDifferenceRaw")
YDifferenceRaw80to120.Scale(scale80to120)
ThetaDifferenceRaw80to120 = root80to120.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw80to120.Scale(scale80to120)

#load and scale 120to170 Simulation
#load and scale jet1 data
PtAsymmetryRaw120to170 = root120to170.Get("PtAsymmetryRaw")
PtAsymmetryRaw120to170.Scale(scale120to170)
PhiDifferenceRaw120to170 = root120to170.Get("PhiDifferenceRaw")
PhiDifferenceRaw120to170.Scale(scale120to170)
EtaDifferenceRaw120to170 = root120to170.Get("EtaDifferenceRaw")
EtaDifferenceRaw120to170.Scale(scale120to170)
YDifferenceRaw120to170 = root120to170.Get("YDifferenceRaw")
YDifferenceRaw120to170.Scale(scale120to170)
ThetaDifferenceRaw120to170 = root120to170.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw120to170.Scale(scale120to170)

#load and scale 170to300 Simulation
#load and scale jet1 data
PtAsymmetryRaw170to300 = root170to300.Get("PtAsymmetryRaw")
PtAsymmetryRaw170to300.Scale(scale170to300)
PhiDifferenceRaw170to300 = root170to300.Get("PhiDifferenceRaw")
PhiDifferenceRaw170to300.Scale(scale170to300)
EtaDifferenceRaw170to300 = root170to300.Get("EtaDifferenceRaw")
EtaDifferenceRaw170to300.Scale(scale170to300)
YDifferenceRaw170to300 = root170to300.Get("YDifferenceRaw")
YDifferenceRaw170to300.Scale(scale170to300)
ThetaDifferenceRaw170to300 = root170to300.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw170to300.Scale(scale170to300)

#load and scale 300to470 Simulation
#load and scale jet1 data
PtAsymmetryRaw300to470 = root300to470.Get("PtAsymmetryRaw")
PtAsymmetryRaw300to470.Scale(scale300to470)
PhiDifferenceRaw300to470 = root300to470.Get("PhiDifferenceRaw")
PhiDifferenceRaw300to470.Scale(scale300to470)
EtaDifferenceRaw300to470 = root300to470.Get("EtaDifferenceRaw")
EtaDifferenceRaw300to470.Scale(scale300to470)
YDifferenceRaw300to470 = root300to470.Get("YDifferenceRaw")
YDifferenceRaw300to470.Scale(scale300to470)
ThetaDifferenceRaw300to470 = root300to470.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw300to470.Scale(scale300to470)

#load and scale 470to600 Simulation
#load and scale jet1 data
PtAsymmetryRaw470to600 = root470to600.Get("PtAsymmetryRaw")
PtAsymmetryRaw470to600.Scale(scale470to600)
PhiDifferenceRaw470to600 = root470to600.Get("PhiDifferenceRaw")
PhiDifferenceRaw470to600.Scale(scale470to600)
EtaDifferenceRaw470to600 = root470to600.Get("EtaDifferenceRaw")
EtaDifferenceRaw470to600.Scale(scale470to600)
YDifferenceRaw470to600 = root470to600.Get("YDifferenceRaw")
YDifferenceRaw470to600.Scale(scale470to600)
ThetaDifferenceRaw470to600 = root470to600.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw470to600.Scale(scale470to600)

#load and scale 600to800 Simulation
#load and scale jet1 data
PtAsymmetryRaw600to800 = root600to800.Get("PtAsymmetryRaw")
PtAsymmetryRaw600to800.Scale(scale600to800)
PhiDifferenceRaw600to800 = root600to800.Get("PhiDifferenceRaw")
PhiDifferenceRaw600to800.Scale(scale600to800)
EtaDifferenceRaw600to800 = root600to800.Get("EtaDifferenceRaw")
EtaDifferenceRaw600to800.Scale(scale600to800)
YDifferenceRaw600to800 = root600to800.Get("YDifferenceRaw")
YDifferenceRaw600to800.Scale(scale600to800)
ThetaDifferenceRaw600to800 = root600to800.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw600to800.Scale(scale600to800)

#load and scale 800to1000 Simulation
#load and scale jet1 data
PtAsymmetryRaw800to1000 = root800to1000.Get("PtAsymmetryRaw")
PtAsymmetryRaw800to1000.Scale(scale800to1000)
PhiDifferenceRaw800to1000 = root800to1000.Get("PhiDifferenceRaw")
PhiDifferenceRaw800to1000.Scale(scale800to1000)
EtaDifferenceRaw800to1000 = root800to1000.Get("EtaDifferenceRaw")
EtaDifferenceRaw800to1000.Scale(scale800to1000)
YDifferenceRaw800to1000 = root800to1000.Get("YDifferenceRaw")
YDifferenceRaw800to1000.Scale(scale800to1000)
ThetaDifferenceRaw800to1000 = root800to1000.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw800to1000.Scale(scale800to1000)

#load and scale 1000to1400 Simulation
#load and scale jet1 data
PtAsymmetryRaw1000to1400 = root1000to1400.Get("PtAsymmetryRaw")
PtAsymmetryRaw1000to1400.Scale(scale1000to1400)
PhiDifferenceRaw1000to1400 = root1000to1400.Get("PhiDifferenceRaw")
PhiDifferenceRaw1000to1400.Scale(scale1000to1400)
EtaDifferenceRaw1000to1400 = root1000to1400.Get("EtaDifferenceRaw")
EtaDifferenceRaw1000to1400.Scale(scale1000to1400)
YDifferenceRaw1000to1400 = root1000to1400.Get("YDifferenceRaw")
YDifferenceRaw1000to1400.Scale(scale1000to1400)
ThetaDifferenceRaw1000to1400 = root1000to1400.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw1000to1400.Scale(scale1000to1400)

#load and scale 1400to1800 Simulation
#load and scale jet1 data
PtAsymmetryRaw1400to1800 = root1400to1800.Get("PtAsymmetryRaw")
PtAsymmetryRaw1400to1800.Scale(scale1400to1800)
PhiDifferenceRaw1400to1800 = root1400to1800.Get("PhiDifferenceRaw")
PhiDifferenceRaw1400to1800.Scale(scale1400to1800)
EtaDifferenceRaw1400to1800 = root1400to1800.Get("EtaDifferenceRaw")
EtaDifferenceRaw1400to1800.Scale(scale1400to1800)
YDifferenceRaw1400to1800 = root1400to1800.Get("YDifferenceRaw")
YDifferenceRaw1400to1800.Scale(scale1400to1800)
ThetaDifferenceRaw1400to1800 = root1400to1800.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw1400to1800.Scale(scale1400to1800)

#load and scale 1800to2400 Simulation
#load and scale jet1 data
PtAsymmetryRaw1800to2400 = root1800to2400.Get("PtAsymmetryRaw")
PtAsymmetryRaw1800to2400.Scale(scale1800to2400)
PhiDifferenceRaw1800to2400 = root1800to2400.Get("PhiDifferenceRaw")
PhiDifferenceRaw1800to2400.Scale(scale1800to2400)
EtaDifferenceRaw1800to2400 = root1800to2400.Get("EtaDifferenceRaw")
EtaDifferenceRaw1800to2400.Scale(scale1800to2400)
YDifferenceRaw1800to2400 = root1800to2400.Get("YDifferenceRaw")
YDifferenceRaw1800to2400.Scale(scale1800to2400)
ThetaDifferenceRaw1800to2400 = root1800to2400.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw1800to2400.Scale(scale1800to2400)

#load and scale 2400to3200 Simulation
#load and scale jet1 data
PtAsymmetryRaw2400to3200 = root2400to3200.Get("PtAsymmetryRaw")
PtAsymmetryRaw2400to3200.Scale(scale2400to3200)
PhiDifferenceRaw2400to3200 = root2400to3200.Get("PhiDifferenceRaw")
PhiDifferenceRaw2400to3200.Scale(scale2400to3200)
EtaDifferenceRaw2400to3200 = root2400to3200.Get("EtaDifferenceRaw")
EtaDifferenceRaw2400to3200.Scale(scale2400to3200)
YDifferenceRaw2400to3200 = root2400to3200.Get("YDifferenceRaw")
YDifferenceRaw2400to3200.Scale(scale2400to3200)
ThetaDifferenceRaw2400to3200 = root2400to3200.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw2400to3200.Scale(scale2400to3200)

#load and scale 3200 Simulation
#load and scale jet1 data
PtAsymmetryRaw3200 = root3200.Get("PtAsymmetryRaw")
PtAsymmetryRaw3200.Scale(scale3200)
PhiDifferenceRaw3200 = root3200.Get("PhiDifferenceRaw")
PhiDifferenceRaw3200.Scale(scale3200)
EtaDifferenceRaw3200 = root3200.Get("EtaDifferenceRaw")
EtaDifferenceRaw3200.Scale(scale3200)
YDifferenceRaw3200 = root3200.Get("YDifferenceRaw")
YDifferenceRaw3200.Scale(scale3200)
ThetaDifferenceRaw3200 = root3200.Get("ThetaDifferenceRaw")
ThetaDifferenceRaw3200.Scale(scale3200)

#add hists together
#add PtAsymmetryRaw hists together
canvas = ROOT.TCanvas("PtAsymmetryRaw_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PtAsymmetryRawsim_hist = ROOT.TH1D("PtAsymmetryRawsim_hist","PtAsymmetryRawsim_hist",PtAsymmetryRaw3200.GetNbinsX(),PtAsymmetryRaw3200.GetXaxis().GetXmin(),PtAsymmetryRaw3200.GetXaxis().GetXmax())
PtAsymmetryRawsim_hist.Sumw2()

PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw50to80)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw80to120)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw120to170)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw170to300)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw300to470)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw470to600)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw600to800)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw800to1000)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw1000to1400)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw1400to1800)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw1800to2400)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw2400to3200)
PtAsymmetryRawsim_hist.Add(PtAsymmetryRaw3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PtAsymmetryRawsim_hist,"(Pt1-Pt2)/(Pt1+Pt2)","p")
legend.SetTextSize(0.03)

PtAsymmetryRawsim_hist.SetStats(0)
PtAsymmetryRawsim_hist.SetLineColor(ROOT.kBlack)
PtAsymmetryRawsim_hist.SetMarkerColor(ROOT.kBlack)
PtAsymmetryRawsim_hist.SetLineWidth(2)
PtAsymmetryRawsim_hist.SetMarkerStyle(4)
PtAsymmetryRawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
PtAsymmetryRawsim_hist.GetXaxis().SetTitle("(Pt1-Pt2)/(Pt1+Pt2)")
PtAsymmetryRawsim_hist.SetTitle("Dijet Asymmetry for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
PtAsymmetryRawsim_hist.SetMarkerSize(3)
PtAsymmetryRawsim_hist.SetLineWidth(2)
PtAsymmetryRawsim_hist.GetYaxis().SetLabelSize(0.045)
PtAsymmetryRawsim_hist.GetYaxis().SetTitleSize(0.05)
PtAsymmetryRawsim_hist.GetXaxis().SetLabelSize(0.045)
PtAsymmetryRawsim_hist.GetXaxis().SetTitleSize(0.05)
#PtAsymmetryRawsim_hist.GetYaxis().SetLabelOffset(0.01)
#PtAsymmetryRawsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PtAsymmetryRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add PhiDifferenceRaw hists together
canvas = ROOT.TCanvas("PhiDifferenceRaw_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PhiDifferenceRawsim_hist = ROOT.TH1D("PhiDifferenceRawsim_hist","PhiDifferenceRawsim_hist",PhiDifferenceRaw3200.GetNbinsX(),PhiDifferenceRaw3200.GetXaxis().GetXmin(),PhiDifferenceRaw3200.GetXaxis().GetXmax())
PhiDifferenceRawsim_hist.Sumw2()

PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw50to80)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw80to120)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw120to170)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw170to300)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw300to470)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw470to600)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw600to800)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw800to1000)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw1000to1400)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw1400to1800)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw1800to2400)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw2400to3200)
PhiDifferenceRawsim_hist.Add(PhiDifferenceRaw3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PhiDifferenceRawsim_hist,"Phi1-Phi2","p")
legend.SetTextSize(0.03)

PhiDifferenceRawsim_hist.SetStats(0)
PhiDifferenceRawsim_hist.SetLineColor(ROOT.kBlack)
PhiDifferenceRawsim_hist.SetMarkerColor(ROOT.kBlack)
PhiDifferenceRawsim_hist.SetLineWidth(2)
PhiDifferenceRawsim_hist.SetMarkerStyle(4)
PhiDifferenceRawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
PhiDifferenceRawsim_hist.GetXaxis().SetTitle("Degree")
PhiDifferenceRawsim_hist.SetTitle("Phi Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
PhiDifferenceRawsim_hist.SetMarkerSize(3)
PhiDifferenceRawsim_hist.SetLineWidth(2)
PhiDifferenceRawsim_hist.GetYaxis().SetLabelSize(0.045)
PhiDifferenceRawsim_hist.GetYaxis().SetTitleSize(0.05)
PhiDifferenceRawsim_hist.GetXaxis().SetLabelSize(0.045)
PhiDifferenceRawsim_hist.GetXaxis().SetTitleSize(0.05)
#PhiDifferenceRawsim_hist.GetYaxis().SetLabelOffset(0.01)
#PhiDifferenceRawsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PhiDifferenceRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_PhiDifferenceRaws_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add EtaDifferenceRaw hists together
canvas = ROOT.TCanvas("EtaDifferenceRaw_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

EtaDifferenceRawsim_hist = ROOT.TH1D("EtaDifferenceRawsim_hist","EtaDifferenceRawsim_hist",EtaDifferenceRaw3200.GetNbinsX(),EtaDifferenceRaw3200.GetXaxis().GetXmin(),EtaDifferenceRaw3200.GetXaxis().GetXmax())
EtaDifferenceRawsim_hist.Sumw2()

EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw50to80)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw80to120)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw120to170)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw170to300)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw300to470)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw470to600)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw600to800)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw800to1000)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw1000to1400)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw1400to1800)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw1800to2400)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw2400to3200)
EtaDifferenceRawsim_hist.Add(EtaDifferenceRaw3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(EtaDifferenceRawsim_hist,"Eta1-Eta2","p")
legend.SetTextSize(0.03)

EtaDifferenceRawsim_hist.SetStats(0)
EtaDifferenceRawsim_hist.SetLineColor(ROOT.kBlack)
EtaDifferenceRawsim_hist.SetMarkerColor(ROOT.kBlack)
EtaDifferenceRawsim_hist.SetLineWidth(2)
EtaDifferenceRawsim_hist.SetMarkerStyle(4)
EtaDifferenceRawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
EtaDifferenceRawsim_hist.GetXaxis().SetTitle("Eta")
EtaDifferenceRawsim_hist.SetTitle("Eta Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
EtaDifferenceRawsim_hist.SetMarkerSize(3)
EtaDifferenceRawsim_hist.SetLineWidth(2)
EtaDifferenceRawsim_hist.GetYaxis().SetLabelSize(0.045)
EtaDifferenceRawsim_hist.GetYaxis().SetTitleSize(0.05)
EtaDifferenceRawsim_hist.GetXaxis().SetLabelSize(0.045)
EtaDifferenceRawsim_hist.GetXaxis().SetTitleSize(0.05)
#EtaDifferenceRawsim_hist.GetYaxis().SetLabelOffset(0.01)
#EtaDifferenceRawsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
EtaDifferenceRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_EtaDifferenceRaws_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add YDifferenceRaw hists together
canvas = ROOT.TCanvas("YDifferenceRaw_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

YDifferenceRawsim_hist = ROOT.TH1D("YDifferenceRawsim_hist","YDifferenceRawsim_hist",YDifferenceRaw3200.GetNbinsX(),YDifferenceRaw3200.GetXaxis().GetXmin(),YDifferenceRaw3200.GetXaxis().GetXmax())
YDifferenceRawsim_hist.Sumw2()

YDifferenceRawsim_hist.Add(YDifferenceRaw50to80)
YDifferenceRawsim_hist.Add(YDifferenceRaw80to120)
YDifferenceRawsim_hist.Add(YDifferenceRaw120to170)
YDifferenceRawsim_hist.Add(YDifferenceRaw170to300)
YDifferenceRawsim_hist.Add(YDifferenceRaw300to470)
YDifferenceRawsim_hist.Add(YDifferenceRaw470to600)
YDifferenceRawsim_hist.Add(YDifferenceRaw600to800)
YDifferenceRawsim_hist.Add(YDifferenceRaw800to1000)
YDifferenceRawsim_hist.Add(YDifferenceRaw1000to1400)
YDifferenceRawsim_hist.Add(YDifferenceRaw1400to1800)
YDifferenceRawsim_hist.Add(YDifferenceRaw1800to2400)
YDifferenceRawsim_hist.Add(YDifferenceRaw2400to3200)
YDifferenceRawsim_hist.Add(YDifferenceRaw3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(YDifferenceRawsim_hist,"Y1-Y2","p")
legend.SetTextSize(0.03)

YDifferenceRawsim_hist.SetStats(0)
YDifferenceRawsim_hist.SetLineColor(ROOT.kBlack)
YDifferenceRawsim_hist.SetMarkerColor(ROOT.kBlack)
YDifferenceRawsim_hist.SetLineWidth(2)
YDifferenceRawsim_hist.SetMarkerStyle(4)
YDifferenceRawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
YDifferenceRawsim_hist.GetXaxis().SetTitle("Y")
YDifferenceRawsim_hist.SetTitle("Y Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
YDifferenceRawsim_hist.SetMarkerSize(3)
YDifferenceRawsim_hist.SetLineWidth(2)
YDifferenceRawsim_hist.GetYaxis().SetLabelSize(0.045)
YDifferenceRawsim_hist.GetYaxis().SetTitleSize(0.05)
YDifferenceRawsim_hist.GetXaxis().SetLabelSize(0.045)
YDifferenceRawsim_hist.GetXaxis().SetTitleSize(0.05)
#YDifferenceRawsim_hist.GetYaxis().SetLabelOffset(0.01)
#YDifferenceRawsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
YDifferenceRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_YDifferenceRaws_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add ThetaDifferenceRaw hists together
canvas = ROOT.TCanvas("ThetaDifferenceRaw_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

ThetaDifferenceRawsim_hist = ROOT.TH1D("ThetaDifferenceRawsim_hist","ThetaDifferenceRawsim_hist",ThetaDifferenceRaw3200.GetNbinsX(),ThetaDifferenceRaw3200.GetXaxis().GetXmin(),ThetaDifferenceRaw3200.GetXaxis().GetXmax())
ThetaDifferenceRawsim_hist.Sumw2()

ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw50to80)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw80to120)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw120to170)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw170to300)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw300to470)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw470to600)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw600to800)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw800to1000)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw1000to1400)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw1400to1800)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw1800to2400)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw2400to3200)
ThetaDifferenceRawsim_hist.Add(ThetaDifferenceRaw3200)

legend = ROOT.TLegend(0.6,0.8,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(ThetaDifferenceRawsim_hist,"Theta1-Theta2","p")
legend.SetTextSize(0.03)

ThetaDifferenceRawsim_hist.SetStats(0)
ThetaDifferenceRawsim_hist.SetLineColor(ROOT.kBlack)
ThetaDifferenceRawsim_hist.SetMarkerColor(ROOT.kBlack)
ThetaDifferenceRawsim_hist.SetLineWidth(2)
ThetaDifferenceRawsim_hist.SetMarkerStyle(4)
ThetaDifferenceRawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
ThetaDifferenceRawsim_hist.GetXaxis().SetTitle("Degree")
ThetaDifferenceRawsim_hist.SetTitle("Theta Difference for Run 2023 Simulation")
#Set font size
legend.SetTextSize(0.045)
ThetaDifferenceRawsim_hist.SetMarkerSize(3)
ThetaDifferenceRawsim_hist.SetLineWidth(2)
ThetaDifferenceRawsim_hist.GetYaxis().SetLabelSize(0.045)
ThetaDifferenceRawsim_hist.GetYaxis().SetTitleSize(0.05)
ThetaDifferenceRawsim_hist.GetXaxis().SetLabelSize(0.045)
ThetaDifferenceRawsim_hist.GetXaxis().SetTitleSize(0.05)
#ThetaDifferenceRawsim_hist.GetYaxis().SetLabelOffset(0.01)
#ThetaDifferenceRawsim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
ThetaDifferenceRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_ThetaDifferenceRaws_Run2023_Simulation_Scaled.pdf")
canvas.Clear()




#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023-15Jan2023_MC.root","RECREATE")
PtAsymmetryRawsim_hist.Write()
PhiDifferenceRawsim_hist.Write()
EtaDifferenceRawsim_hist.Write()
YDifferenceRawsim_hist.Write()
ThetaDifferenceRawsim_hist.Write()
outHistFile.Close()
