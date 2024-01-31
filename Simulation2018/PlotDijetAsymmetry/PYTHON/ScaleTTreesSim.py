import ROOT
import numpy as np

inDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
outDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/PDF/"
outRootDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"

#load tree data
root200to300 = ROOT.TFile.Open(inDirectory+"200to300_PlotDijetAsymmetry_Run22018_MC.root")
scale200to300 = (1710000./56298746)
print(scale200to300)
root300to500 = ROOT.TFile.Open(inDirectory+"300to500_PlotDijetAsymmetry_Run22018_MC.root")
scale300to500 = (347500./60991701)
print(scale300to500)
root500to700 = ROOT.TFile.Open(inDirectory+"500to700_PlotDijetAsymmetry_Run22018_MC.root")
scale500to700 = (30363.051/48640047)
print(scale500to700)
root700to1000 = ROOT.TFile.Open(inDirectory+"700to1000_PlotDijetAsymmetry_Run22018_MC.root")
scale700to1000 = (6428.869/47925782)
print(scale700to1000)
root1000to1500 = ROOT.TFile.Open(inDirectory+"1000to1500_PlotDijetAsymmetry_Run22018_MC.root")
scale1000to1500 = (1122.659/14244456)
print(scale1000to1500)
root1500to2000 = ROOT.TFile.Open(inDirectory+"1500to2000_PlotDijetAsymmetry_Run22018_MC.root")
scale1500to2000 = (108.163/10751607)
print(scale1500to2000)
root2000toInf = ROOT.TFile.Open(inDirectory+"2000toInf_PlotDijetAsymmetry_Run22018_MC.root")
scale2000toInf = (22.008/5278880)
print(scale2000toInf)
"""
QCD_PT-200to300_TuneCP5_13p6TeV_pythia8 1.679e+07 11988000
QCD_PT-300to500_TuneCP5_13p6TeV_pythia8 2.513e+06 17979000
QCD_PT-500to700_TuneCP5_13p6TeV_pythia8 4.574e+05 17964000
QCD_PT-700to1000_TuneCP5_13p6TeV_pythia8 1.162e+05 17889000
QCD_PT-1000to1500_TuneCP5_13p6TeV_pythia8 7.584e+03 34626000
QCD_PT-1500to2000_TuneCP5_13p6TeV_pythia8 6.490e+02 16766000
QCD_PT-2000toInf_TuneCP5_13p6TeV_pythia8 1.809e+02 40468000
QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8 3.105e+01 23908000
QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8 8.829e+00 11956000
QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8 7.952e-01 3596000
QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8 1.147e-01 1792000
QCD_PT-2400to2000toInf_TuneCP5_13p6TeV_pythia8 7.619e-03 1200000
QCD_PT-2000toInf_TuneCP5_13p6TeV_pythia8 2.331e-04 478000
"""

#load and scale 200to300 Simulation
#load and scale jet1 data
PtAsymmetry200to300 = root200to300.Get("PtAsymmetry")
PtAsymmetry200to300.Scale(scale200to300)
PhiDifference200to300 = root200to300.Get("PhiDifference")
PhiDifference200to300.Scale(scale200to300)
EtaDifference200to300 = root200to300.Get("EtaDifference")
EtaDifference200to300.Scale(scale200to300)
YDifference200to300 = root200to300.Get("YDifference")
YDifference200to300.Scale(scale200to300)
ThetaDifference200to300 = root200to300.Get("ThetaDifference")
ThetaDifference200to300.Scale(scale200to300)

#load and scale 300to500 Simulation
#load and scale jet1 data
PtAsymmetry300to500 = root300to500.Get("PtAsymmetry")
PtAsymmetry300to500.Scale(scale300to500)
PhiDifference300to500 = root300to500.Get("PhiDifference")
PhiDifference300to500.Scale(scale300to500)
EtaDifference300to500 = root300to500.Get("EtaDifference")
EtaDifference300to500.Scale(scale300to500)
YDifference300to500 = root300to500.Get("YDifference")
YDifference300to500.Scale(scale300to500)
ThetaDifference300to500 = root300to500.Get("ThetaDifference")
ThetaDifference300to500.Scale(scale300to500)

#load and scale 500to700 Simulation
#load and scale jet1 data
PtAsymmetry500to700 = root500to700.Get("PtAsymmetry")
PtAsymmetry500to700.Scale(scale500to700)
PhiDifference500to700 = root500to700.Get("PhiDifference")
PhiDifference500to700.Scale(scale500to700)
EtaDifference500to700 = root500to700.Get("EtaDifference")
EtaDifference500to700.Scale(scale500to700)
YDifference500to700 = root500to700.Get("YDifference")
YDifference500to700.Scale(scale500to700)
ThetaDifference500to700 = root500to700.Get("ThetaDifference")
ThetaDifference500to700.Scale(scale500to700)

#load and scale 700to1000 Simulation
#load and scale jet1 data
PtAsymmetry700to1000 = root700to1000.Get("PtAsymmetry")
PtAsymmetry700to1000.Scale(scale700to1000)
PhiDifference700to1000 = root700to1000.Get("PhiDifference")
PhiDifference700to1000.Scale(scale700to1000)
EtaDifference700to1000 = root700to1000.Get("EtaDifference")
EtaDifference700to1000.Scale(scale700to1000)
YDifference700to1000 = root700to1000.Get("YDifference")
YDifference700to1000.Scale(scale700to1000)
ThetaDifference700to1000 = root700to1000.Get("ThetaDifference")
ThetaDifference700to1000.Scale(scale700to1000)

#load and scale 1000to1500 Simulation
#load and scale jet1 data
PtAsymmetry1000to1500 = root1000to1500.Get("PtAsymmetry")
PtAsymmetry1000to1500.Scale(scale1000to1500)
PhiDifference1000to1500 = root1000to1500.Get("PhiDifference")
PhiDifference1000to1500.Scale(scale1000to1500)
EtaDifference1000to1500 = root1000to1500.Get("EtaDifference")
EtaDifference1000to1500.Scale(scale1000to1500)
YDifference1000to1500 = root1000to1500.Get("YDifference")
YDifference1000to1500.Scale(scale1000to1500)
ThetaDifference1000to1500 = root1000to1500.Get("ThetaDifference")
ThetaDifference1000to1500.Scale(scale1000to1500)

#load and scale 1500to2000 Simulation
#load and scale jet1 data
PtAsymmetry1500to2000 = root1500to2000.Get("PtAsymmetry")
PtAsymmetry1500to2000.Scale(scale1500to2000)
PhiDifference1500to2000 = root1500to2000.Get("PhiDifference")
PhiDifference1500to2000.Scale(scale1500to2000)
EtaDifference1500to2000 = root1500to2000.Get("EtaDifference")
EtaDifference1500to2000.Scale(scale1500to2000)
YDifference1500to2000 = root1500to2000.Get("YDifference")
YDifference1500to2000.Scale(scale1500to2000)
ThetaDifference1500to2000 = root1500to2000.Get("ThetaDifference")
ThetaDifference1500to2000.Scale(scale1500to2000)

#load and scale 2000toInf Simulation
#load and scale jet1 data
PtAsymmetry2000toInf = root2000toInf.Get("PtAsymmetry")
PtAsymmetry2000toInf.Scale(scale2000toInf)
PhiDifference2000toInf = root2000toInf.Get("PhiDifference")
PhiDifference2000toInf.Scale(scale2000toInf)
EtaDifference2000toInf = root2000toInf.Get("EtaDifference")
EtaDifference2000toInf.Scale(scale2000toInf)
YDifference2000toInf = root2000toInf.Get("YDifference")
YDifference2000toInf.Scale(scale2000toInf)
ThetaDifference2000toInf = root2000toInf.Get("ThetaDifference")
ThetaDifference2000toInf.Scale(scale2000toInf)

#add hists together
#add PtAsymmetry hists together
canvas = ROOT.TCanvas("PtAsymmetry_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PtAsymmetrysim_hist = ROOT.TH1D("PtAsymmetrysim_hist","PtAsymmetrysim_hist",PtAsymmetry2000toInf.GetNbinsX(),PtAsymmetry2000toInf.GetXaxis().GetXmin(),PtAsymmetry2000toInf.GetXaxis().GetXmax())
PtAsymmetrysim_hist.Sumw2()

PtAsymmetrysim_hist.Add(PtAsymmetry200to300)
PtAsymmetrysim_hist.Add(PtAsymmetry300to500)
PtAsymmetrysim_hist.Add(PtAsymmetry500to700)
PtAsymmetrysim_hist.Add(PtAsymmetry700to1000)
PtAsymmetrysim_hist.Add(PtAsymmetry1000to1500)
PtAsymmetrysim_hist.Add(PtAsymmetry1500to2000)
PtAsymmetrysim_hist.Add(PtAsymmetry2000toInf)

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
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
PtAsymmetrysim_hist.SetTitle("Dijet Asymmetry for Run2 2018 Simulation")
#Set font size
legend.SetTextSize(0.045)
PtAsymmetrysim_hist.SetMarkerSize(3)
PtAsymmetrysim_hist.SetLineWidth(2)
PtAsymmetrysim_hist.GetYaxis().SetLabelSize(0.045)
PtAsymmetrysim_hist.GetYaxis().SetTitleSize(0.05)
PtAsymmetrysim_hist.GetXaxis().SetLabelSize(0.045)
PtAsymmetrysim_hist.GetXaxis().SetTitleSize(0.05)
#PtAsymmetrysim_hist.GetYaxis().SetLabelOffset(0.01)
#PtAsymmetrysim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PtAsymmetrysim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_DijetAsymmetry_Run22018_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add PhiDifference hists together
canvas = ROOT.TCanvas("PhiDifference_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

PhiDifferencesim_hist = ROOT.TH1D("PhiDifferencesim_hist","PhiDifferencesim_hist",PhiDifference2000toInf.GetNbinsX(),PhiDifference2000toInf.GetXaxis().GetXmin(),PhiDifference2000toInf.GetXaxis().GetXmax())
PhiDifferencesim_hist.Sumw2()

PhiDifferencesim_hist.Add(PhiDifference200to300)
PhiDifferencesim_hist.Add(PhiDifference300to500)
PhiDifferencesim_hist.Add(PhiDifference500to700)
PhiDifferencesim_hist.Add(PhiDifference700to1000)
PhiDifferencesim_hist.Add(PhiDifference1000to1500)
PhiDifferencesim_hist.Add(PhiDifference1500to2000)
PhiDifferencesim_hist.Add(PhiDifference2000toInf)
PhiDifferencesim_hist.Add(PhiDifference2000toInf)

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
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
PhiDifferencesim_hist.SetTitle("Phi Difference for Run2 2018 Simulation")
#Set font size
legend.SetTextSize(0.045)
PhiDifferencesim_hist.SetMarkerSize(3)
PhiDifferencesim_hist.SetLineWidth(2)
PhiDifferencesim_hist.GetYaxis().SetLabelSize(0.045)
PhiDifferencesim_hist.GetYaxis().SetTitleSize(0.05)
PhiDifferencesim_hist.GetXaxis().SetLabelSize(0.045)
PhiDifferencesim_hist.GetXaxis().SetTitleSize(0.05)
#PhiDifferencesim_hist.GetYaxis().SetLabelOffset(0.01)
#PhiDifferencesim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
PhiDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_PhiDifferences_Run22018_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add EtaDifference hists together
canvas = ROOT.TCanvas("EtaDifference_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

EtaDifferencesim_hist = ROOT.TH1D("EtaDifferencesim_hist","EtaDifferencesim_hist",EtaDifference2000toInf.GetNbinsX(),EtaDifference2000toInf.GetXaxis().GetXmin(),EtaDifference2000toInf.GetXaxis().GetXmax())
EtaDifferencesim_hist.Sumw2()

EtaDifferencesim_hist.Add(EtaDifference200to300)
EtaDifferencesim_hist.Add(EtaDifference300to500)
EtaDifferencesim_hist.Add(EtaDifference500to700)
EtaDifferencesim_hist.Add(EtaDifference700to1000)
EtaDifferencesim_hist.Add(EtaDifference1000to1500)
EtaDifferencesim_hist.Add(EtaDifference1500to2000)
EtaDifferencesim_hist.Add(EtaDifference2000toInf)
EtaDifferencesim_hist.Add(EtaDifference2000toInf)

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
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
EtaDifferencesim_hist.SetTitle("Eta Difference for Run2 2018 Simulation")
#Set font size
legend.SetTextSize(0.045)
EtaDifferencesim_hist.SetMarkerSize(3)
EtaDifferencesim_hist.SetLineWidth(2)
EtaDifferencesim_hist.GetYaxis().SetLabelSize(0.045)
EtaDifferencesim_hist.GetYaxis().SetTitleSize(0.05)
EtaDifferencesim_hist.GetXaxis().SetLabelSize(0.045)
EtaDifferencesim_hist.GetXaxis().SetTitleSize(0.05)
#EtaDifferencesim_hist.GetYaxis().SetLabelOffset(0.01)
#EtaDifferencesim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
EtaDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_EtaDifferences_Run22018_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add YDifference hists together
canvas = ROOT.TCanvas("YDifference_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

YDifferencesim_hist = ROOT.TH1D("YDifferencesim_hist","YDifferencesim_hist",YDifference2000toInf.GetNbinsX(),YDifference2000toInf.GetXaxis().GetXmin(),YDifference2000toInf.GetXaxis().GetXmax())
YDifferencesim_hist.Sumw2()

YDifferencesim_hist.Add(YDifference200to300)
YDifferencesim_hist.Add(YDifference300to500)
YDifferencesim_hist.Add(YDifference500to700)
YDifferencesim_hist.Add(YDifference700to1000)
YDifferencesim_hist.Add(YDifference1000to1500)
YDifferencesim_hist.Add(YDifference1500to2000)
YDifferencesim_hist.Add(YDifference2000toInf)
YDifferencesim_hist.Add(YDifference2000toInf)

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
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
YDifferencesim_hist.SetTitle("Y Difference for Run2 2018 Simulation")
YDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_YDifferences_Run22018_Simulation_Scaled.pdf")
canvas.Clear()

#add hists together
#add ThetaDifference hists together
canvas = ROOT.TCanvas("ThetaDifference_canvas")
canvas.SetCanvasSize(1600,1100)
canvas.cd()

ThetaDifferencesim_hist = ROOT.TH1D("ThetaDifferencesim_hist","ThetaDifferencesim_hist",ThetaDifference2000toInf.GetNbinsX(),ThetaDifference2000toInf.GetXaxis().GetXmin(),ThetaDifference2000toInf.GetXaxis().GetXmax())
ThetaDifferencesim_hist.Sumw2()

ThetaDifferencesim_hist.Add(ThetaDifference200to300)
ThetaDifferencesim_hist.Add(ThetaDifference300to500)
ThetaDifferencesim_hist.Add(ThetaDifference500to700)
ThetaDifferencesim_hist.Add(ThetaDifference700to1000)
ThetaDifferencesim_hist.Add(ThetaDifference1000to1500)
ThetaDifferencesim_hist.Add(ThetaDifference1500to2000)
ThetaDifferencesim_hist.Add(ThetaDifference2000toInf)
ThetaDifferencesim_hist.Add(ThetaDifference2000toInf)

legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
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
ThetaDifferencesim_hist.SetTitle("Theta Difference for Run2 2018 Simulation")
#Set font size
legend.SetTextSize(0.045)
ThetaDifferencesim_hist.SetMarkerSize(3)
ThetaDifferencesim_hist.SetLineWidth(2)
ThetaDifferencesim_hist.GetYaxis().SetLabelSize(0.045)
ThetaDifferencesim_hist.GetYaxis().SetTitleSize(0.05)
ThetaDifferencesim_hist.GetXaxis().SetLabelSize(0.045)
ThetaDifferencesim_hist.GetXaxis().SetTitleSize(0.05)
#ThetaDifferencesim_hist.GetYaxis().SetLabelOffset(0.01)
#ThetaDifferencesim_hist.GetXaxis().SetLabelOffset(0.01)
canvas.SetBottomMargin(0.15)
canvas.SetTopMargin(0.1)
canvas.SetRightMargin(0.05)
canvas.SetLeftMargin(0.15)
ThetaDifferencesim_hist.Draw("AP")
legend.Draw("same")
canvas.Print(outDirectory+"Plot_ThetaDifferences_Run22018_Simulation_Scaled.pdf")
canvas.Clear()




#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_Plot_DijetAsymmetry_WithScale_Run22018_MC.root","RECREATE")
PtAsymmetrysim_hist.Write()
PhiDifferencesim_hist.Write()
EtaDifferencesim_hist.Write()
YDifferencesim_hist.Write()
ThetaDifferencesim_hist.Write()
outHistFile.Close()
