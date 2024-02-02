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
PtAsymmetry50to80 = root50to80.Get("PtAsymmetry")
PtAsymmetry50to80.Scale(scale50to80)
PtAsymmetryRaw50to80 = root50to80.Get("PtAsymmetryRaw")
PtAsymmetryRaw50to80.Scale(scale50to80)
PtAsymmetryNom50to80 = root50to80.Get("PtAsymmetryNom")
PtAsymmetryNom50to80.Scale(scale50to80)

#load and scale 80to120 Simulation
#load and scale jet1 data
PtAsymmetry80to120 = root80to120.Get("PtAsymmetry")
PtAsymmetry80to120.Scale(scale80to120)
PtAsymmetryRaw80to120 = root80to120.Get("PtAsymmetryRaw")
PtAsymmetryRaw80to120.Scale(scale80to120)
PtAsymmetryNom80to120 = root80to120.Get("PtAsymmetryNom")
PtAsymmetryNom80to120.Scale(scale80to120)

#load and scale 120to170 Simulation
#load and scale jet1 data
PtAsymmetry120to170 = root120to170.Get("PtAsymmetry")
PtAsymmetry120to170.Scale(scale120to170)
PtAsymmetryRaw120to170 = root120to170.Get("PtAsymmetryRaw")
PtAsymmetryRaw120to170.Scale(scale120to170)
PtAsymmetryNom120to170 = root120to170.Get("PtAsymmetryNom")
PtAsymmetryNom120to170.Scale(scale120to170)

#load and scale 170to300 Simulation
#load and scale jet1 data
PtAsymmetry170to300 = root170to300.Get("PtAsymmetry")
PtAsymmetry170to300.Scale(scale170to300)
PtAsymmetryRaw170to300 = root170to300.Get("PtAsymmetryRaw")
PtAsymmetryRaw170to300.Scale(scale170to300)
PtAsymmetryNom170to300 = root170to300.Get("PtAsymmetryNom")
PtAsymmetryNom170to300.Scale(scale170to300)

#load and scale 300to470 Simulation
#load and scale jet1 data
PtAsymmetry300to470 = root300to470.Get("PtAsymmetry")
PtAsymmetry300to470.Scale(scale300to470)
PtAsymmetryRaw300to470 = root300to470.Get("PtAsymmetryRaw")
PtAsymmetryRaw300to470.Scale(scale300to470)
PtAsymmetryNom300to470 = root300to470.Get("PtAsymmetryNom")
PtAsymmetryNom300to470.Scale(scale300to470)

#load and scale 470to600 Simulation
#load and scale jet1 data
PtAsymmetry470to600 = root470to600.Get("PtAsymmetry")
PtAsymmetry470to600.Scale(scale470to600)
PtAsymmetryRaw470to600 = root470to600.Get("PtAsymmetryRaw")
PtAsymmetryRaw470to600.Scale(scale470to600)
PtAsymmetryNom470to600 = root470to600.Get("PtAsymmetryNom")
PtAsymmetryNom470to600.Scale(scale470to600)

#load and scale 600to800 Simulation
#load and scale jet1 data
PtAsymmetry600to800 = root600to800.Get("PtAsymmetry")
PtAsymmetry600to800.Scale(scale600to800)
PtAsymmetryRaw600to800 = root600to800.Get("PtAsymmetryRaw")
PtAsymmetryRaw600to800.Scale(scale600to800)
PtAsymmetryNom600to800 = root600to800.Get("PtAsymmetryNom")
PtAsymmetryNom600to800.Scale(scale600to800)

#load and scale 800to1000 Simulation
#load and scale jet1 data
PtAsymmetry800to1000 = root800to1000.Get("PtAsymmetry")
PtAsymmetry800to1000.Scale(scale800to1000)
PtAsymmetryRaw800to1000 = root800to1000.Get("PtAsymmetryRaw")
PtAsymmetryRaw800to1000.Scale(scale800to1000)
PtAsymmetryNom800to1000 = root800to1000.Get("PtAsymmetryNom")
PtAsymmetryNom800to1000.Scale(scale800to1000)

#load and scale 1000to1400 Simulation
#load and scale jet1 data
PtAsymmetry1000to1400 = root1000to1400.Get("PtAsymmetry")
PtAsymmetry1000to1400.Scale(scale1000to1400)
PtAsymmetryRaw1000to1400 = root1000to1400.Get("PtAsymmetryRaw")
PtAsymmetryRaw1000to1400.Scale(scale1000to1400)
PtAsymmetryNom1000to1400 = root1000to1400.Get("PtAsymmetryNom")
PtAsymmetryNom1000to1400.Scale(scale1000to1400)

#load and scale 1400to1800 Simulation
#load and scale jet1 data
PtAsymmetry1400to1800 = root1400to1800.Get("PtAsymmetry")
PtAsymmetry1400to1800.Scale(scale1400to1800)
PtAsymmetryRaw1400to1800 = root1400to1800.Get("PtAsymmetryRaw")
PtAsymmetryRaw1400to1800.Scale(scale1400to1800)
PtAsymmetryNom1400to1800 = root1400to1800.Get("PtAsymmetryNom")
PtAsymmetryNom1400to1800.Scale(scale1400to1800)

#load and scale 1800to2400 Simulation
#load and scale jet1 data
PtAsymmetry1800to2400 = root1800to2400.Get("PtAsymmetry")
PtAsymmetry1800to2400.Scale(scale1800to2400)
PtAsymmetryRaw1800to2400 = root1800to2400.Get("PtAsymmetryRaw")
PtAsymmetryRaw1800to2400.Scale(scale1800to2400)
PtAsymmetryNom1800to2400 = root1800to2400.Get("PtAsymmetryNom")
PtAsymmetryNom1800to2400.Scale(scale1800to2400)

#load and scale 2400to3200 Simulation
#load and scale jet1 data
PtAsymmetry2400to3200 = root2400to3200.Get("PtAsymmetry")
PtAsymmetry2400to3200.Scale(scale2400to3200)
PtAsymmetryRaw2400to3200 = root2400to3200.Get("PtAsymmetryRaw")
PtAsymmetryRaw2400to3200.Scale(scale2400to3200)
PtAsymmetryNom2400to3200 = root2400to3200.Get("PtAsymmetryNom")
PtAsymmetryNom2400to3200.Scale(scale2400to3200)

#load and scale 3200 Simulation
#load and scale jet1 data
PtAsymmetry3200 = root3200.Get("PtAsymmetry")
PtAsymmetry3200.Scale(scale3200)
PtAsymmetryRaw3200 = root3200.Get("PtAsymmetryRaw")
PtAsymmetryRaw3200.Scale(scale3200)
PtAsymmetryNom3200 = root3200.Get("PtAsymmetryNom")
PtAsymmetryNom3200.Scale(scale3200)

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
PtAsymmetrysim_hist.SetTitle("Dijet Asymmetry for Jan15 2023 Simulation")
PtAsymmetrysim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Run2023-15Jan2023_Simulation_Scaled.pdf")
canvas.Clear()

#add PtAsymmetryRaw hists together
canvas = ROOT.TCanvas("PtAsymmetryRaw_canvas")
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

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
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
PtAsymmetryRawsim_hist.SetTitle("Dijet Asymmetry Raw for Jan15 2023 Simulation")
PtAsymmetryRawsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Raw_Run2023-15Jan2023_Simulation_Scaled.pdf")
canvas.Clear()

#add PtAsymmetryNom hists together
canvas = ROOT.TCanvas("PtAsymmetryNom_canvas")
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

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
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
PtAsymmetryNomsim_hist.SetTitle("Dijet Asymmetry Nom for Jan15 2023 Simulation")
PtAsymmetryNomsim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Nom_Run2023-15Jan2023_Simulation_Scaled.pdf")
canvas.Clear()

#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_Plot_DijetAsymmetry_WithScale_Run32023-15Jan2023_MC.root","RECREATE")
PtAsymmetrysim_hist.Write()
PtAsymmetryNomsim_hist.Write()
PtAsymmetryRawsim_hist.Write()
outHistFile.Close()
