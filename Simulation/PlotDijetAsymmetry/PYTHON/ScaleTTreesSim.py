import ROOT
import numpy as np

inDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
outDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/Pdf/"
outRootDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"

#load tree data

root50to80 = ROOT.TFile.Open(inDirectory+"50to80_PlotDijetAsymmetry_Run32023_MC.root")
scale50to80 = ((1.679e+07)/(11988000))
print(scale50to80)
root80to120 = ROOT.TFile.Open(inDirectory+"80to120_PlotDijetAsymmetry_Run32023_MC.root")
scale80to120 = ((2.513e+06)/(17979000))
print(scale80to120)
root120to170 = ROOT.TFile.Open(inDirectory+"120to170_PlotDijetAsymmetry_Run32023_MC.root")
scale120to170 = ((4.574e+05)/(17964000))
print(scale120to170)
root170to300 = ROOT.TFile.Open(inDirectory+"170to300_PlotDijetAsymmetry_Run32023_MC.root")
scale170to300 = ((1.162e+05)/(17889000))
print(scale170to300)
root300to470 = ROOT.TFile.Open(inDirectory+"300to470_PlotDijetAsymmetry_Run32023_MC.root")
scale300to470 = ((7.584e+03)/(34626000))
print(scale300to470)
root470to600 = ROOT.TFile.Open(inDirectory+"470to600_PlotDijetAsymmetry_Run32023_MC.root")
scale470to600 = ((6.490e+02)/(16766000))
print(scale470to600)
root600to800 = ROOT.TFile.Open(inDirectory+"600to800_PlotDijetAsymmetry_Run32023_MC.root")
scale600to800 = ((1.809e+02)/(40468000))
print(scale600to800)
root800to1000 = ROOT.TFile.Open(inDirectory+"800to1000_PlotDijetAsymmetry_Run32023_MC.root")
scale800to1000 = ((3.105e+01)/(23908000))
print(scale800to1000)
root1000to1400 = ROOT.TFile.Open(inDirectory+"1000to1400_PlotDijetAsymmetry_Run32023_MC.root")
scale1000to1400 = ((8.829e+00)/(11956000))
print(scale1000to1400)
root1400to1800 = ROOT.TFile.Open(inDirectory+"1400to1800_PlotDijetAsymmetry_Run32023_MC.root")
scale1400to1800 = ((7.952e-01)/(3596000))
print(scale1400to1800)
root1800to2400 = ROOT.TFile.Open(inDirectory+"1800to2400_PlotDijetAsymmetry_Run32023_MC.root")
scale1800to2400 = ((1.147e-01)/(1792000))
print(scale1800to2400)
root2400to3200 = ROOT.TFile.Open(inDirectory+"2400to3200_PlotDijetAsymmetry_Run32023_MC.root")
scale2400to3200 = ((7.619e-03)/(1200000))
print(scale2400to3200)
root3200 = ROOT.TFile.Open(inDirectory+"3200_PlotDijetAsymmetry_Run32023_MC.root")
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
PtAsymmetry50to80 = root50to80.Get("PtAsymmetry")
PtAsymmetry50to80.Scale(scale50to80)
PhiDifference50to80 = root50to80.Get("PhiDifference")
PhiDifference50to80.Scale(scale50to80)
EtaDifference50to80 = root50to80.Get("EtaDifference")
EtaDifference50to80.Scale(scale50to80)
YDifference50to80 = root50to80.Get("YDifference")
YDifference50to80.Scale(scale50to80)
ThetaDifference50to80 = root50to80.Get("ThetaDifference")
ThetaDifference50to80.Scale(scale50to80)

#load and scale 80to120 Simulation
#load and scale jet1 data
PtAsymmetry80to120 = root80to120.Get("PtAsymmetry")
PtAsymmetry80to120.Scale(scale80to120)
PhiDifference80to120 = root80to120.Get("PhiDifference")
PhiDifference80to120.Scale(scale80to120)
EtaDifference80to120 = root80to120.Get("EtaDifference")
EtaDifference80to120.Scale(scale80to120)
YDifference80to120 = root80to120.Get("YDifference")
YDifference80to120.Scale(scale80to120)
ThetaDifference80to120 = root80to120.Get("ThetaDifference")
ThetaDifference80to120.Scale(scale80to120)

#load and scale 120to170 Simulation
#load and scale jet1 data
PtAsymmetry120to170 = root120to170.Get("PtAsymmetry")
PtAsymmetry120to170.Scale(scale120to170)
PhiDifference120to170 = root120to170.Get("PhiDifference")
PhiDifference120to170.Scale(scale120to170)
EtaDifference120to170 = root120to170.Get("EtaDifference")
EtaDifference120to170.Scale(scale120to170)
YDifference120to170 = root120to170.Get("YDifference")
YDifference120to170.Scale(scale120to170)
ThetaDifference120to170 = root120to170.Get("ThetaDifference")
ThetaDifference120to170.Scale(scale120to170)

#load and scale 170to300 Simulation
#load and scale jet1 data
PtAsymmetry170to300 = root170to300.Get("PtAsymmetry")
PtAsymmetry170to300.Scale(scale170to300)
PhiDifference170to300 = root170to300.Get("PhiDifference")
PhiDifference170to300.Scale(scale170to300)
EtaDifference170to300 = root170to300.Get("EtaDifference")
EtaDifference170to300.Scale(scale170to300)
YDifference170to300 = root170to300.Get("YDifference")
YDifference170to300.Scale(scale170to300)
ThetaDifference170to300 = root170to300.Get("ThetaDifference")
ThetaDifference170to300.Scale(scale170to300)

#load and scale 300to470 Simulation
#load and scale jet1 data
PtAsymmetry300to470 = root300to470.Get("PtAsymmetry")
PtAsymmetry300to470.Scale(scale300to470)
PhiDifference300to470 = root300to470.Get("PhiDifference")
PhiDifference300to470.Scale(scale300to470)
EtaDifference300to470 = root300to470.Get("EtaDifference")
EtaDifference300to470.Scale(scale300to470)
YDifference300to470 = root300to470.Get("YDifference")
YDifference300to470.Scale(scale300to470)
ThetaDifference300to470 = root300to470.Get("ThetaDifference")
ThetaDifference300to470.Scale(scale300to470)

#load and scale 470to600 Simulation
#load and scale jet1 data
PtAsymmetry470to600 = root470to600.Get("PtAsymmetry")
PtAsymmetry470to600.Scale(scale470to600)
PhiDifference470to600 = root470to600.Get("PhiDifference")
PhiDifference470to600.Scale(scale470to600)
EtaDifference470to600 = root470to600.Get("EtaDifference")
EtaDifference470to600.Scale(scale470to600)
YDifference470to600 = root470to600.Get("YDifference")
YDifference470to600.Scale(scale470to600)
ThetaDifference470to600 = root470to600.Get("ThetaDifference")
ThetaDifference470to600.Scale(scale470to600)

#load and scale 600to800 Simulation
#load and scale jet1 data
PtAsymmetry600to800 = root600to800.Get("PtAsymmetry")
PtAsymmetry600to800.Scale(scale600to800)
PhiDifference600to800 = root600to800.Get("PhiDifference")
PhiDifference600to800.Scale(scale600to800)
EtaDifference600to800 = root600to800.Get("EtaDifference")
EtaDifference600to800.Scale(scale600to800)
YDifference600to800 = root600to800.Get("YDifference")
YDifference600to800.Scale(scale600to800)
ThetaDifference600to800 = root600to800.Get("ThetaDifference")
ThetaDifference600to800.Scale(scale600to800)

#load and scale 800to1000 Simulation
#load and scale jet1 data
PtAsymmetry800to1000 = root800to1000.Get("PtAsymmetry")
PtAsymmetry800to1000.Scale(scale800to1000)
PhiDifference800to1000 = root800to1000.Get("PhiDifference")
PhiDifference800to1000.Scale(scale800to1000)
EtaDifference800to1000 = root800to1000.Get("EtaDifference")
EtaDifference800to1000.Scale(scale800to1000)
YDifference800to1000 = root800to1000.Get("YDifference")
YDifference800to1000.Scale(scale800to1000)
ThetaDifference800to1000 = root800to1000.Get("ThetaDifference")
ThetaDifference800to1000.Scale(scale800to1000)

#load and scale 1000to1400 Simulation
#load and scale jet1 data
PtAsymmetry1000to1400 = root1000to1400.Get("PtAsymmetry")
PtAsymmetry1000to1400.Scale(scale1000to1400)
PhiDifference1000to1400 = root1000to1400.Get("PhiDifference")
PhiDifference1000to1400.Scale(scale1000to1400)
EtaDifference1000to1400 = root1000to1400.Get("EtaDifference")
EtaDifference1000to1400.Scale(scale1000to1400)
YDifference1000to1400 = root1000to1400.Get("YDifference")
YDifference1000to1400.Scale(scale1000to1400)
ThetaDifference1000to1400 = root1000to1400.Get("ThetaDifference")
ThetaDifference1000to1400.Scale(scale1000to1400)

#load and scale 1400to1800 Simulation
#load and scale jet1 data
PtAsymmetry1400to1800 = root1400to1800.Get("PtAsymmetry")
PtAsymmetry1400to1800.Scale(scale1400to1800)
PhiDifference1400to1800 = root1400to1800.Get("PhiDifference")
PhiDifference1400to1800.Scale(scale1400to1800)
EtaDifference1400to1800 = root1400to1800.Get("EtaDifference")
EtaDifference1400to1800.Scale(scale1400to1800)
YDifference1400to1800 = root1400to1800.Get("YDifference")
YDifference1400to1800.Scale(scale1400to1800)
ThetaDifference1400to1800 = root1400to1800.Get("ThetaDifference")
ThetaDifference1400to1800.Scale(scale1400to1800)

#load and scale 1800to2400 Simulation
#load and scale jet1 data
PtAsymmetry1800to2400 = root1800to2400.Get("PtAsymmetry")
PtAsymmetry1800to2400.Scale(scale1800to2400)
PhiDifference1800to2400 = root1800to2400.Get("PhiDifference")
PhiDifference1800to2400.Scale(scale1800to2400)
EtaDifference1800to2400 = root1800to2400.Get("EtaDifference")
EtaDifference1800to2400.Scale(scale1800to2400)
YDifference1800to2400 = root1800to2400.Get("YDifference")
YDifference1800to2400.Scale(scale1800to2400)
ThetaDifference1800to2400 = root1800to2400.Get("ThetaDifference")
ThetaDifference1800to2400.Scale(scale1800to2400)

#load and scale 2400to3200 Simulation
#load and scale jet1 data
PtAsymmetry2400to3200 = root2400to3200.Get("PtAsymmetry")
PtAsymmetry2400to3200.Scale(scale2400to3200)
PhiDifference2400to3200 = root2400to3200.Get("PhiDifference")
PhiDifference2400to3200.Scale(scale2400to3200)
EtaDifference2400to3200 = root2400to3200.Get("EtaDifference")
EtaDifference2400to3200.Scale(scale2400to3200)
YDifference2400to3200 = root2400to3200.Get("YDifference")
YDifference2400to3200.Scale(scale2400to3200)
ThetaDifference2400to3200 = root2400to3200.Get("ThetaDifference")
ThetaDifference2400to3200.Scale(scale2400to3200)

#load and scale 3200 Simulation
#load and scale jet1 data
PtAsymmetry3200 = root3200.Get("PtAsymmetry")
PtAsymmetry3200.Scale(scale3200)
PhiDifference3200 = root3200.Get("PhiDifference")
PhiDifference3200.Scale(scale3200)
EtaDifference3200 = root3200.Get("EtaDifference")
EtaDifference3200.Scale(scale3200)
YDifference3200 = root3200.Get("YDifference")
YDifference3200.Scale(scale3200)
ThetaDifference3200 = root3200.Get("ThetaDifference")
ThetaDifference3200.Scale(scale3200)

#add hists together
#add PtAsymmetry hists together
canvas = ROOT.TCanvas("PtAsymmetry_canvas")
canvas.cd()

PtAsymmetrysim_hist = ROOT.TH1D("PtAsymmetrysim_hist","PtAsymmetrysim_hist",PtAsymmetry3200.GetNbinsX(),PtAsymmetry3200.GetXaxis().GetXmin(),PtAsymmetry3200.GetXaxis().GetXmax())
PtAsymmetrysim_hist.Sumw2()

PtAsymmetrysim_hist.Add(PtAsymmetry50to80)
PtAsymmetrysim_hist.Add(PtAsymmetry80to120)
PtAsymmetrysim_hist.Add(PtAsymmetry120to170)
PtAsymmetrysim_hist.Add(PtAsymmetry170to300)
PtAsymmetrysim_hist.Add(PtAsymmetry300to470)
PtAsymmetrysim_hist.Add(PtAsymmetry470to600)
PtAsymmetrysim_hist.Add(PtAsymmetry600to800)
PtAsymmetrysim_hist.Add(PtAsymmetry800to1000)
PtAsymmetrysim_hist.Add(PtAsymmetry1000to1400)
PtAsymmetrysim_hist.Add(PtAsymmetry1400to1800)
PtAsymmetrysim_hist.Add(PtAsymmetry1800to2400)
PtAsymmetrysim_hist.Add(PtAsymmetry2400to3200)
PtAsymmetrysim_hist.Add(PtAsymmetry3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PtAsymmetrysim_hist,"(Pt1-Pt2)/(Pt1+Pt2)","p")
legend.SetTextSize(0.03)

PtAsymmetrysim_hist.SetStats(0)
PtAsymmetrysim_hist.SetLineColor(ROOT.kBlack)
PtAsymmetrysim_hist.SetMarkerColor(ROOT.kBlack)
PtAsymmetrysim_hist.SetLineWidth(2)
PtAsymmetrysim_hist.SetMarkerStyle(4)
PtAsymmetrysim_hist.GetYaxis().SetTitle("#sigma [pb]")
PtAsymmetrysim_hist.GetXaxis().SetTitle("(Pt1-Pt2)/(Pt1+Pt2)")
PtAsymmetrysim_hist.SetTitle("Dijet Asymmetry for Run 2023 Simulation")
PtAsymmetrysim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add PhiDifference hists together
canvas = ROOT.TCanvas("PhiDifference_canvas")
canvas.cd()

PhiDifferencesim_hist = ROOT.TH1D("PhiDifferencesim_hist","PhiDifferencesim_hist",PhiDifference3200.GetNbinsX(),PhiDifference3200.GetXaxis().GetXmin(),PhiDifference3200.GetXaxis().GetXmax())
PhiDifferencesim_hist.Sumw2()

PhiDifferencesim_hist.Add(PhiDifference50to80)
PhiDifferencesim_hist.Add(PhiDifference80to120)
PhiDifferencesim_hist.Add(PhiDifference120to170)
PhiDifferencesim_hist.Add(PhiDifference170to300)
PhiDifferencesim_hist.Add(PhiDifference300to470)
PhiDifferencesim_hist.Add(PhiDifference470to600)
PhiDifferencesim_hist.Add(PhiDifference600to800)
PhiDifferencesim_hist.Add(PhiDifference800to1000)
PhiDifferencesim_hist.Add(PhiDifference1000to1400)
PhiDifferencesim_hist.Add(PhiDifference1400to1800)
PhiDifferencesim_hist.Add(PhiDifference1800to2400)
PhiDifferencesim_hist.Add(PhiDifference2400to3200)
PhiDifferencesim_hist.Add(PhiDifference3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(PhiDifferencesim_hist,"Phi1-Phi2","p")
legend.SetTextSize(0.03)

PhiDifferencesim_hist.SetStats(0)
PhiDifferencesim_hist.SetLineColor(ROOT.kBlack)
PhiDifferencesim_hist.SetMarkerColor(ROOT.kBlack)
PhiDifferencesim_hist.SetLineWidth(2)
PhiDifferencesim_hist.SetMarkerStyle(4)
PhiDifferencesim_hist.GetYaxis().SetTitle("#sigma [pb]")
PhiDifferencesim_hist.GetXaxis().SetTitle("Degree")
PhiDifferencesim_hist.SetTitle("Phi Difference for Run 2023 Simulation")
PhiDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_PhiDifferences_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add EtaDifference hists together
canvas = ROOT.TCanvas("EtaDifference_canvas")
canvas.cd()

EtaDifferencesim_hist = ROOT.TH1D("EtaDifferencesim_hist","EtaDifferencesim_hist",EtaDifference3200.GetNbinsX(),EtaDifference3200.GetXaxis().GetXmin(),EtaDifference3200.GetXaxis().GetXmax())
EtaDifferencesim_hist.Sumw2()

EtaDifferencesim_hist.Add(EtaDifference50to80)
EtaDifferencesim_hist.Add(EtaDifference80to120)
EtaDifferencesim_hist.Add(EtaDifference120to170)
EtaDifferencesim_hist.Add(EtaDifference170to300)
EtaDifferencesim_hist.Add(EtaDifference300to470)
EtaDifferencesim_hist.Add(EtaDifference470to600)
EtaDifferencesim_hist.Add(EtaDifference600to800)
EtaDifferencesim_hist.Add(EtaDifference800to1000)
EtaDifferencesim_hist.Add(EtaDifference1000to1400)
EtaDifferencesim_hist.Add(EtaDifference1400to1800)
EtaDifferencesim_hist.Add(EtaDifference1800to2400)
EtaDifferencesim_hist.Add(EtaDifference2400to3200)
EtaDifferencesim_hist.Add(EtaDifference3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(EtaDifferencesim_hist,"Eta1-Eta2","p")
legend.SetTextSize(0.03)

EtaDifferencesim_hist.SetStats(0)
EtaDifferencesim_hist.SetLineColor(ROOT.kBlack)
EtaDifferencesim_hist.SetMarkerColor(ROOT.kBlack)
EtaDifferencesim_hist.SetLineWidth(2)
EtaDifferencesim_hist.SetMarkerStyle(4)
EtaDifferencesim_hist.GetYaxis().SetTitle("#sigma [pb]")
EtaDifferencesim_hist.GetXaxis().SetTitle("Eta")
EtaDifferencesim_hist.SetTitle("Eta Difference for Run 2023 Simulation")
EtaDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_EtaDifferences_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add YDifference hists together
canvas = ROOT.TCanvas("YDifference_canvas")
canvas.cd()

YDifferencesim_hist = ROOT.TH1D("YDifferencesim_hist","YDifferencesim_hist",YDifference3200.GetNbinsX(),YDifference3200.GetXaxis().GetXmin(),YDifference3200.GetXaxis().GetXmax())
YDifferencesim_hist.Sumw2()

YDifferencesim_hist.Add(YDifference50to80)
YDifferencesim_hist.Add(YDifference80to120)
YDifferencesim_hist.Add(YDifference120to170)
YDifferencesim_hist.Add(YDifference170to300)
YDifferencesim_hist.Add(YDifference300to470)
YDifferencesim_hist.Add(YDifference470to600)
YDifferencesim_hist.Add(YDifference600to800)
YDifferencesim_hist.Add(YDifference800to1000)
YDifferencesim_hist.Add(YDifference1000to1400)
YDifferencesim_hist.Add(YDifference1400to1800)
YDifferencesim_hist.Add(YDifference1800to2400)
YDifferencesim_hist.Add(YDifference2400to3200)
YDifferencesim_hist.Add(YDifference3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(YDifferencesim_hist,"Y1-Y2","p")
legend.SetTextSize(0.03)

YDifferencesim_hist.SetStats(0)
YDifferencesim_hist.SetLineColor(ROOT.kBlack)
YDifferencesim_hist.SetMarkerColor(ROOT.kBlack)
YDifferencesim_hist.SetLineWidth(2)
YDifferencesim_hist.SetMarkerStyle(4)
YDifferencesim_hist.GetYaxis().SetTitle("#sigma [pb]")
YDifferencesim_hist.GetXaxis().SetTitle("Y")
YDifferencesim_hist.SetTitle("Y Difference for Run 2023 Simulation")
YDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_YDifferences_Run2023_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add ThetaDifference hists together
canvas = ROOT.TCanvas("ThetaDifference_canvas")
canvas.cd()

ThetaDifferencesim_hist = ROOT.TH1D("ThetaDifferencesim_hist","ThetaDifferencesim_hist",ThetaDifference3200.GetNbinsX(),ThetaDifference3200.GetXaxis().GetXmin(),ThetaDifference3200.GetXaxis().GetXmax())
ThetaDifferencesim_hist.Sumw2()

ThetaDifferencesim_hist.Add(ThetaDifference50to80)
ThetaDifferencesim_hist.Add(ThetaDifference80to120)
ThetaDifferencesim_hist.Add(ThetaDifference120to170)
ThetaDifferencesim_hist.Add(ThetaDifference170to300)
ThetaDifferencesim_hist.Add(ThetaDifference300to470)
ThetaDifferencesim_hist.Add(ThetaDifference470to600)
ThetaDifferencesim_hist.Add(ThetaDifference600to800)
ThetaDifferencesim_hist.Add(ThetaDifference800to1000)
ThetaDifferencesim_hist.Add(ThetaDifference1000to1400)
ThetaDifferencesim_hist.Add(ThetaDifference1400to1800)
ThetaDifferencesim_hist.Add(ThetaDifference1800to2400)
ThetaDifferencesim_hist.Add(ThetaDifference2400to3200)
ThetaDifferencesim_hist.Add(ThetaDifference3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(ThetaDifferencesim_hist,"Theta1-Theta2","p")
legend.SetTextSize(0.03)

ThetaDifferencesim_hist.SetStats(0)
ThetaDifferencesim_hist.SetLineColor(ROOT.kBlack)
ThetaDifferencesim_hist.SetMarkerColor(ROOT.kBlack)
ThetaDifferencesim_hist.SetLineWidth(2)
ThetaDifferencesim_hist.SetMarkerStyle(4)
ThetaDifferencesim_hist.GetYaxis().SetTitle("#sigma [pb]")
ThetaDifferencesim_hist.GetXaxis().SetTitle("Degree")
ThetaDifferencesim_hist.SetTitle("Theta Difference for Run 2023 Simulation")
ThetaDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_ThetaDifferences_Run2023_Simulation_Scaled.pdf")
canvas.Clear()




#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023_MC.root","RECREATE")
PtAsymmetrysim_hist.Write()
PhiDifferencesim_hist.Write()
EtaDifferencesim_hist.Write()
YDifferencesim_hist.Write()
ThetaDifferencesim_hist.Write()
outHistFile.Close()
