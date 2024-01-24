import ROOT
import numpy as np

inDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
outDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/PDF/"
outRootDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
pdfnames = "PlotSimulation_Run22018_Gen_All_"

"""
("UL18_QCDmadgraph-HT200to300",1710000./56298746, "MG+Py QCD (UL18)"),
   	("UL18_QCDmadgraph-HT300to500",347500./60991701, ""),
   	("UL18_QCDmadgraph-HT500to700",30363.051/48640047, ""),
   	("UL18_QCDmadgraph-HT700to1000",6428.869/47925782, ""),
   	("UL18_QCDmadgraph-HT1000to1500",1122.659/14244456, ""),
   	("UL18_QCDmadgraph-HT1500to2000",108.163/10751607, ""),
   	("UL18_QCDmadgraph-HT2000toInf",22.008/5278880, ""),
"""

#load tree data

root200to300 = ROOT.TFile.Open(inDirectory+"200to300_PlotSimulation_Run22018_Gen.root")
scale200to300 = (1710000./56298746)
print(scale200to300)
root300to500 = ROOT.TFile.Open(inDirectory+"300to500_PlotSimulation_Run22018_Gen.root")
scale300to500 = (347500./60991701)
print(scale300to500)
root500to700 = ROOT.TFile.Open(inDirectory+"500to700_PlotSimulation_Run22018_Gen.root")
scale500to700 = (30363.051/48640047)
print(scale500to700)
root700to1000 = ROOT.TFile.Open(inDirectory+"700to1000_PlotSimulation_Run22018_Gen.root")
scale700to1000 = (6428.869/47925782)
print(scale700to1000)
root1000to1500 = ROOT.TFile.Open(inDirectory+"1000to1500_PlotSimulation_Run22018_Gen.root")
scale1000to1500 = (1122.659/14244456)
print(scale1000to1500)
root1500to2000 = ROOT.TFile.Open(inDirectory+"1500to2000_PlotSimulation_Run22018_Gen.root")
scale1500to2000 = (108.163/10751607)
print(scale1500to2000)
root2000toInf = ROOT.TFile.Open(inDirectory+"2000toInf_PlotSimulation_Run22018_Gen.root")
scale2000toInf = (22.008/5278880)
print(scale2000toInf)

#load and scale 200to300 Simulation
#load and scale jet1 data
Jet1200to300 = root200to300.Get("Jet1")
pt1_200to300 = Jet1200to300.Get("Genpt1")
pt1_200to300.Scale(scale200to300)
y1_200to300 = Jet1200to300.Get("Geny1")
y1_200to300.Scale(scale200to300)
eta1_200to300 = Jet1200to300.Get("Geneta1")
eta1_200to300.Scale(scale200to300)
phi1_200to300 = Jet1200to300.Get("Genphi1")
phi1_200to300.Scale(scale200to300)
mass1_200to300 = Jet1200to300.Get("Genmass1")
mass1_200to300.Scale(scale200to300)

#load and sclae jet2 data
Jet2200to300 = root200to300.Get("Jet2")
pt2_200to300 = Jet2200to300.Get("Genpt2")
pt2_200to300.Scale(scale200to300)
y2_200to300 = Jet2200to300.Get("Geny2")
y2_200to300.Scale(scale200to300)
eta2_200to300 = Jet2200to300.Get("Geneta2")
eta2_200to300.Scale(scale200to300)
phi2_200to300 = Jet2200to300.Get("Genphi2")
phi2_200to300.Scale(scale200to300)
mass2_200to300 = Jet2200to300.Get("Genmass2")
mass2_200to300.Scale(scale200to300)

#load and sclae jet3 data
Jet3200to300 = root200to300.Get("Jet3")
pt3_200to300 = Jet3200to300.Get("Genpt3")
pt3_200to300.Scale(scale200to300)
y3_200to300 = Jet3200to300.Get("Geny3")
y3_200to300.Scale(scale200to300)
eta3_200to300 = Jet3200to300.Get("Geneta3")
eta3_200to300.Scale(scale200to300)
phi3_200to300 = Jet3200to300.Get("Genphi3")
phi3_200to300.Scale(scale200to300)
mass3_200to300 = Jet3200to300.Get("Genmass3")
mass3_200to300.Scale(scale200to300)

#load and scale jet kinematics
kinematics200to300 = root200to300.Get("Kinematics")
mjj_200to300 = kinematics200to300.Get("Genmjj")
mjj_200to300.Scale(scale200to300)
yboost_200to300 = kinematics200to300.Get("Genyboost")
yboost_200to300.Scale(scale200to300)
chi_200to300 = kinematics200to300.Get("Genchi")
chi_200to300.Scale(scale200to300)

#load and scale 300to500 Genulation
#load and scale jet1 data
Jet1300to500 = root300to500.Get("Jet1")
pt1_300to500 = Jet1300to500.Get("Genpt1")
pt1_300to500.Scale(scale300to500)
y1_300to500 = Jet1300to500.Get("Geny1")
y1_300to500.Scale(scale300to500)
eta1_300to500 = Jet1300to500.Get("Geneta1")
eta1_300to500.Scale(scale300to500)
phi1_300to500 = Jet1300to500.Get("Genphi1")
phi1_300to500.Scale(scale300to500)
mass1_300to500 = Jet1300to500.Get("Genmass1")
mass1_300to500.Scale(scale300to500)

#load and sclae jet2 data
Jet2300to500 = root300to500.Get("Jet2")
pt2_300to500 = Jet2300to500.Get("Genpt2")
pt2_300to500.Scale(scale300to500)
y2_300to500 = Jet2300to500.Get("Geny2")
y2_300to500.Scale(scale300to500)
eta2_300to500 = Jet2300to500.Get("Geneta2")
eta2_300to500.Scale(scale300to500)
phi2_300to500 = Jet2300to500.Get("Genphi2")
phi2_300to500.Scale(scale300to500)
mass2_300to500 = Jet2300to500.Get("Genmass2")
mass2_300to500.Scale(scale300to500)

#load and sclae jet3 data
Jet3300to500 = root300to500.Get("Jet3")
pt3_300to500 = Jet3300to500.Get("Genpt3")
pt3_300to500.Scale(scale300to500)
y3_300to500 = Jet3300to500.Get("Geny3")
y3_300to500.Scale(scale300to500)
eta3_300to500 = Jet3300to500.Get("Geneta3")
eta3_300to500.Scale(scale300to500)
phi3_300to500 = Jet3300to500.Get("Genphi3")
phi3_300to500.Scale(scale300to500)
mass3_300to500 = Jet3300to500.Get("Genmass3")
mass3_300to500.Scale(scale300to500)

#load and scale jet kinematics
kinematics300to500 = root300to500.Get("Kinematics")
mjj_300to500 = kinematics300to500.Get("Genmjj")
mjj_300to500.Scale(scale300to500)
yboost_300to500 = kinematics300to500.Get("Genyboost")
yboost_300to500.Scale(scale300to500)
chi_300to500 = kinematics300to500.Get("Genchi")
chi_300to500.Scale(scale300to500)

#load and scale 500to700 Genulation
#load and scale jet1 data
Jet1500to700 = root500to700.Get("Jet1")
pt1_500to700 = Jet1500to700.Get("Genpt1")
pt1_500to700.Scale(scale500to700)
y1_500to700 = Jet1500to700.Get("Geny1")
y1_500to700.Scale(scale500to700)
eta1_500to700 = Jet1500to700.Get("Geneta1")
eta1_500to700.Scale(scale500to700)
phi1_500to700 = Jet1500to700.Get("Genphi1")
phi1_500to700.Scale(scale500to700)
mass1_500to700 = Jet1500to700.Get("Genmass1")
mass1_500to700.Scale(scale500to700)

#load and sclae jet2 data
Jet2500to700 = root500to700.Get("Jet2")
pt2_500to700 = Jet2500to700.Get("Genpt2")
pt2_500to700.Scale(scale500to700)
y2_500to700 = Jet2500to700.Get("Geny2")
y2_500to700.Scale(scale500to700)
eta2_500to700 = Jet2500to700.Get("Geneta2")
eta2_500to700.Scale(scale500to700)
phi2_500to700 = Jet2500to700.Get("Genphi2")
phi2_500to700.Scale(scale500to700)
mass2_500to700 = Jet2500to700.Get("Genmass2")
mass2_500to700.Scale(scale500to700)


#load and sclae jet3 data
Jet3500to700 = root500to700.Get("Jet3")
pt3_500to700 = Jet3500to700.Get("Genpt3")
pt3_500to700.Scale(scale500to700)
y3_500to700 = Jet3500to700.Get("Geny3")
y3_500to700.Scale(scale500to700)
eta3_500to700 = Jet3500to700.Get("Geneta3")
eta3_500to700.Scale(scale500to700)
phi3_500to700 = Jet3500to700.Get("Genphi3")
phi3_500to700.Scale(scale500to700)
mass3_500to700 = Jet3500to700.Get("Genmass3")
mass3_500to700.Scale(scale500to700)

#load and scale jet kinematics
kinematics500to700 = root500to700.Get("Kinematics")
mjj_500to700 = kinematics500to700.Get("Genmjj")
mjj_500to700.Scale(scale500to700)
yboost_500to700 = kinematics500to700.Get("Genyboost")
yboost_500to700.Scale(scale500to700)
chi_500to700 = kinematics500to700.Get("Genchi")
chi_500to700.Scale(scale500to700)

#load and scale 700to1000 Genulation
#load and scale jet1 data
Jet1700to1000 = root700to1000.Get("Jet1")
pt1_700to1000 = Jet1700to1000.Get("Genpt1")
pt1_700to1000.Scale(scale700to1000)
y1_700to1000 = Jet1700to1000.Get("Geny1")
y1_700to1000.Scale(scale700to1000)
eta1_700to1000 = Jet1700to1000.Get("Geneta1")
eta1_700to1000.Scale(scale700to1000)
phi1_700to1000 = Jet1700to1000.Get("Genphi1")
phi1_700to1000.Scale(scale700to1000)
mass1_700to1000 = Jet1700to1000.Get("Genmass1")
mass1_700to1000.Scale(scale700to1000)

#load and sclae jet2 data
Jet2700to1000 = root700to1000.Get("Jet2")
pt2_700to1000 = Jet2700to1000.Get("Genpt2")
pt2_700to1000.Scale(scale700to1000)
y2_700to1000 = Jet2700to1000.Get("Geny2")
y2_700to1000.Scale(scale700to1000)
eta2_700to1000 = Jet2700to1000.Get("Geneta2")
eta2_700to1000.Scale(scale700to1000)
phi2_700to1000 = Jet2700to1000.Get("Genphi2")
phi2_700to1000.Scale(scale700to1000)
mass2_700to1000 = Jet2700to1000.Get("Genmass2")
mass2_700to1000.Scale(scale700to1000)

#load and sclae jet3 data
Jet3700to1000 = root700to1000.Get("Jet3")
pt3_700to1000 = Jet3700to1000.Get("Genpt3")
pt3_700to1000.Scale(scale700to1000)
y3_700to1000 = Jet3700to1000.Get("Geny3")
y3_700to1000.Scale(scale700to1000)
eta3_700to1000 = Jet3700to1000.Get("Geneta3")
eta3_700to1000.Scale(scale700to1000)
phi3_700to1000 = Jet3700to1000.Get("Genphi3")
phi3_700to1000.Scale(scale700to1000)
mass3_700to1000 = Jet3700to1000.Get("Genmass3")
mass3_700to1000.Scale(scale700to1000)

#load and scale jet kinematics
kinematics700to1000 = root700to1000.Get("Kinematics")
mjj_700to1000 = kinematics700to1000.Get("Genmjj")
mjj_700to1000.Scale(scale700to1000)
yboost_700to1000 = kinematics700to1000.Get("Genyboost")
yboost_700to1000.Scale(scale700to1000)
chi_700to1000 = kinematics700to1000.Get("Genchi")
chi_700to1000.Scale(scale700to1000)

#load and scale 1000to1500 Genulation
#load and scale jet1 data
Jet11000to1500 = root1000to1500.Get("Jet1")
pt1_1000to1500 = Jet11000to1500.Get("Genpt1")
pt1_1000to1500.Scale(scale1000to1500)
y1_1000to1500 = Jet11000to1500.Get("Geny1")
y1_1000to1500.Scale(scale1000to1500)
eta1_1000to1500 = Jet11000to1500.Get("Geneta1")
eta1_1000to1500.Scale(scale1000to1500)
phi1_1000to1500 = Jet11000to1500.Get("Genphi1")
phi1_1000to1500.Scale(scale1000to1500)
mass1_1000to1500 = Jet11000to1500.Get("Genmass1")
mass1_1000to1500.Scale(scale1000to1500)

#load and sclae jet2 data
Jet21000to1500 = root1000to1500.Get("Jet2")
pt2_1000to1500 = Jet21000to1500.Get("Genpt2")
pt2_1000to1500.Scale(scale1000to1500)
y2_1000to1500 = Jet21000to1500.Get("Geny2")
y2_1000to1500.Scale(scale1000to1500)
eta2_1000to1500 = Jet21000to1500.Get("Geneta2")
eta2_1000to1500.Scale(scale1000to1500)
phi2_1000to1500 = Jet21000to1500.Get("Genphi2")
phi2_1000to1500.Scale(scale1000to1500)
mass2_1000to1500 = Jet21000to1500.Get("Genmass2")
mass2_1000to1500.Scale(scale1000to1500)

#load and sclae jet3 data
Jet31000to1500 = root1000to1500.Get("Jet3")
pt3_1000to1500 = Jet31000to1500.Get("Genpt3")
pt3_1000to1500.Scale(scale1000to1500)
y3_1000to1500 = Jet31000to1500.Get("Geny3")
y3_1000to1500.Scale(scale1000to1500)
eta3_1000to1500 = Jet31000to1500.Get("Geneta3")
eta3_1000to1500.Scale(scale1000to1500)
phi3_1000to1500 = Jet31000to1500.Get("Genphi3")
phi3_1000to1500.Scale(scale1000to1500)
mass3_1000to1500 = Jet31000to1500.Get("Genmass3")
mass3_1000to1500.Scale(scale1000to1500)

#load and scale jet kinematics
kinematics1000to1500 = root1000to1500.Get("Kinematics")
mjj_1000to1500 = kinematics1000to1500.Get("Genmjj")
mjj_1000to1500.Scale(scale1000to1500)
yboost_1000to1500 = kinematics1000to1500.Get("Genyboost")
yboost_1000to1500.Scale(scale1000to1500)
chi_1000to1500 = kinematics1000to1500.Get("Genchi")
chi_1000to1500.Scale(scale1000to1500)

#load and scale 1500to2000 Genulation
#load and scale jet1 data
Jet11500to2000 = root1500to2000.Get("Jet1")
pt1_1500to2000 = Jet11500to2000.Get("Genpt1")
pt1_1500to2000.Scale(scale1500to2000)
y1_1500to2000 = Jet11500to2000.Get("Geny1")
y1_1500to2000.Scale(scale1500to2000)
eta1_1500to2000 = Jet11500to2000.Get("Geneta1")
eta1_1500to2000.Scale(scale1500to2000)
phi1_1500to2000 = Jet11500to2000.Get("Genphi1")
phi1_1500to2000.Scale(scale1500to2000)
mass1_1500to2000 = Jet11500to2000.Get("Genmass1")
mass1_1500to2000.Scale(scale1500to2000)

#load and sclae jet2 data
Jet21500to2000 = root1500to2000.Get("Jet2")
pt2_1500to2000 = Jet21500to2000.Get("Genpt2")
pt2_1500to2000.Scale(scale1500to2000)
y2_1500to2000 = Jet21500to2000.Get("Geny2")
y2_1500to2000.Scale(scale1500to2000)
eta2_1500to2000 = Jet21500to2000.Get("Geneta2")
eta2_1500to2000.Scale(scale1500to2000)
phi2_1500to2000 = Jet21500to2000.Get("Genphi2")
phi2_1500to2000.Scale(scale1500to2000)
mass2_1500to2000 = Jet21500to2000.Get("Genmass2")
mass2_1500to2000.Scale(scale1500to2000)

#load and sclae jet3 data
Jet31500to2000 = root1500to2000.Get("Jet3")
pt3_1500to2000 = Jet31500to2000.Get("Genpt3")
pt3_1500to2000.Scale(scale1500to2000)
y3_1500to2000 = Jet31500to2000.Get("Geny3")
y3_1500to2000.Scale(scale1500to2000)
eta3_1500to2000 = Jet31500to2000.Get("Geneta3")
eta3_1500to2000.Scale(scale1500to2000)
phi3_1500to2000 = Jet31500to2000.Get("Genphi3")
phi3_1500to2000.Scale(scale1500to2000)
mass3_1500to2000 = Jet31500to2000.Get("Genmass3")
mass3_1500to2000.Scale(scale1500to2000)

#load and scale jet kinematics
kinematics1500to2000 = root1500to2000.Get("Kinematics")
mjj_1500to2000 = kinematics1500to2000.Get("Genmjj")
mjj_1500to2000.Scale(scale1500to2000)
yboost_1500to2000 = kinematics1500to2000.Get("Genyboost")
yboost_1500to2000.Scale(scale1500to2000)
chi_1500to2000 = kinematics1500to2000.Get("Genchi")
chi_1500to2000.Scale(scale1500to2000)

#load and scale 2000toInf Genulation
#load and scale jet1 data
Jet12000toInf = root2000toInf.Get("Jet1")
pt1_2000toInf = Jet12000toInf.Get("Genpt1")
pt1_2000toInf.Scale(scale2000toInf)
y1_2000toInf = Jet12000toInf.Get("Geny1")
y1_2000toInf.Scale(scale2000toInf)
eta1_2000toInf = Jet12000toInf.Get("Geneta1")
eta1_2000toInf.Scale(scale2000toInf)
phi1_2000toInf = Jet12000toInf.Get("Genphi1")
phi1_2000toInf.Scale(scale2000toInf)
mass1_2000toInf = Jet12000toInf.Get("Genmass1")
mass1_2000toInf.Scale(scale2000toInf)

#load and sclae jet2 data
Jet22000toInf = root2000toInf.Get("Jet2")
pt2_2000toInf = Jet22000toInf.Get("Genpt2")
pt2_2000toInf.Scale(scale2000toInf)
y2_2000toInf = Jet22000toInf.Get("Geny2")
y2_2000toInf.Scale(scale2000toInf)
eta2_2000toInf = Jet22000toInf.Get("Geneta2")
eta2_2000toInf.Scale(scale2000toInf)
phi2_2000toInf = Jet22000toInf.Get("Genphi2")
phi2_2000toInf.Scale(scale2000toInf)
mass2_2000toInf = Jet22000toInf.Get("Genmass2")
mass2_2000toInf.Scale(scale2000toInf)

#load and sclae jet3 data
Jet32000toInf = root2000toInf.Get("Jet3")
pt3_2000toInf = Jet32000toInf.Get("Genpt3")
pt3_2000toInf.Scale(scale2000toInf)
y3_2000toInf = Jet32000toInf.Get("Geny3")
y3_2000toInf.Scale(scale2000toInf)
eta3_2000toInf = Jet32000toInf.Get("Geneta3")
eta3_2000toInf.Scale(scale2000toInf)
phi3_2000toInf = Jet32000toInf.Get("Genphi3")
phi3_2000toInf.Scale(scale2000toInf)
mass3_2000toInf = Jet32000toInf.Get("Genmass3")
mass3_2000toInf.Scale(scale2000toInf)

#load and scale jet kinematics
kinematics2000toInf = root2000toInf.Get("Kinematics")
mjj_2000toInf = kinematics2000toInf.Get("Genmjj")
mjj_2000toInf.Scale(scale2000toInf)
yboost_2000toInf = kinematics2000toInf.Get("Genyboost")
yboost_2000toInf.Scale(scale2000toInf)
chi_2000toInf = kinematics2000toInf.Get("Genchi")
chi_2000toInf.Scale(scale2000toInf)

#add hists together
#add jet1 hists together
#add pt1 hists together
canvas = ROOT.TCanvas("pt1canvas")
canvas.SetLogy(True)
canvas.cd()

pt1gen_hist = ROOT.TH1D("pt1gen_hist","pt1gen_hist",pt1_2000toInf.GetNbinsX(),pt1_2000toInf.GetXaxis().GetXmin(),pt1_2000toInf.GetXaxis().GetXmax())
pt1gen_hist.Sumw2()

pt1gen_hist.Add(pt1_200to300)
pt1gen_hist.Add(pt1_300to500)
pt1gen_hist.Add(pt1_500to700)
pt1gen_hist.Add(pt1_700to1000)
pt1gen_hist.Add(pt1_1000to1500)
pt1gen_hist.Add(pt1_1500to2000)
pt1gen_hist.Add(pt1_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt1gen_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt1gen_hist.GetYaxis().SetTitle("#sigma [pb]")
pt1gen_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt1gen_hist.SetLineColor(ROOT.kBlack)
pt1gen_hist.SetStats(0)
pt1gen_hist.SetLineWidth(2)
pt1gen_hist.SetTitle("")
pt1gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt1 Simulation")
canvas.Print(outDirectory+pdfnames+"pt1simulation.pdf")
canvas.Clear()
#add hists together
#add y1 hists together
canvas = ROOT.TCanvas("y1canvas")
canvas.cd()

y1gen_hist = ROOT.TH1D("y1gen_hist","y1gen_hist",y1_2000toInf.GetNbinsX(),y1_2000toInf.GetXaxis().GetXmin(),y1_2000toInf.GetXaxis().GetXmax())
y1gen_hist.Sumw2()

y1gen_hist.Add(y1_200to300)
y1gen_hist.Add(y1_300to500)
y1gen_hist.Add(y1_500to700)
y1gen_hist.Add(y1_700to1000)
y1gen_hist.Add(y1_1000to1500)
y1gen_hist.Add(y1_1500to2000)
y1gen_hist.Add(y1_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(y1gen_hist,"Simulated y1")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

y1gen_hist.GetYaxis().SetTitle("#sigma [pb]")
y1gen_hist.GetXaxis().SetTitle("y1")

y1gen_hist.SetLineColor(ROOT.kBlack)
y1gen_hist.SetStats(0)
y1gen_hist.SetLineWidth(2)
y1gen_hist.SetTitle("")
y1gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"y1 Simualtion")
canvas.Print(outDirectory+pdfnames+"y1simulation.pdf")
canvas.Clear()
#add hists together
#add eta1 hists together
canvas = ROOT.TCanvas("eta1canvas")
canvas.cd()

eta1gen_hist = ROOT.TH1D("eta1gen_hist","eta1gen_hist",eta1_2000toInf.GetNbinsX(),eta1_2000toInf.GetXaxis().GetXmin(),eta1_2000toInf.GetXaxis().GetXmax())
eta1gen_hist.Sumw2()

eta1gen_hist.Add(eta1_200to300)
eta1gen_hist.Add(eta1_300to500)
eta1gen_hist.Add(eta1_500to700)
eta1gen_hist.Add(eta1_700to1000)
eta1gen_hist.Add(eta1_1000to1500)
eta1gen_hist.Add(eta1_1500to2000)
eta1gen_hist.Add(eta1_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(eta1gen_hist,"Simulated eta1")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

eta1gen_hist.GetYaxis().SetTitle("#sigma [pb]")
eta1gen_hist.GetXaxis().SetTitle("eta1")

eta1gen_hist.SetLineColor(ROOT.kBlack)
eta1gen_hist.SetStats(0)
eta1gen_hist.SetLineWidth(2)
eta1gen_hist.SetTitle("")
eta1gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"eta1 Simualtion")
canvas.Print(outDirectory+pdfnames+"eta1simulation.pdf")
canvas.Clear()
#add hists together
#add phi1 hists together
canvas = ROOT.TCanvas("phi1canvas")
canvas.cd()

phi1gen_hist = ROOT.TH1D("phi1gen_hist","phi1gen_hist",phi1_2000toInf.GetNbinsX(),phi1_2000toInf.GetXaxis().GetXmin(),phi1_2000toInf.GetXaxis().GetXmax())
phi1gen_hist.Sumw2()

phi1gen_hist.Add(phi1_200to300)
phi1gen_hist.Add(phi1_300to500)
phi1gen_hist.Add(phi1_500to700)
phi1gen_hist.Add(phi1_700to1000)
phi1gen_hist.Add(phi1_1000to1500)
phi1gen_hist.Add(phi1_1500to2000)
phi1gen_hist.Add(phi1_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(phi1gen_hist,"Simulated phi1")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

phi1gen_hist.GetYaxis().SetTitle("#sigma [pb]")
phi1gen_hist.GetXaxis().SetTitle("phi1")

phi1gen_hist.SetLineColor(ROOT.kBlack)
phi1gen_hist.SetStats(0)
phi1gen_hist.SetLineWidth(2)
phi1gen_hist.SetTitle("")
phi1gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"phi1 Simualtion")
canvas.Print(outDirectory+pdfnames+"phi1simulation.pdf")
canvas.Clear()
#add hists together
#add mass1 hists together
canvas = ROOT.TCanvas("mass1canvas")
canvas.SetLogy(True)
canvas.cd()

mass1gen_hist = ROOT.TH1D("mass1gen_hist","mass1gen_hist",mass1_2000toInf.GetNbinsX(),mass1_2000toInf.GetXaxis().GetXmin(),mass1_2000toInf.GetXaxis().GetXmax())
mass1gen_hist.Sumw2()

mass1gen_hist.Add(mass1_200to300)
mass1gen_hist.Add(mass1_300to500)
mass1gen_hist.Add(mass1_500to700)
mass1gen_hist.Add(mass1_700to1000)
mass1gen_hist.Add(mass1_1000to1500)
mass1gen_hist.Add(mass1_1500to2000)
mass1gen_hist.Add(mass1_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mass1gen_hist,"Simulated mass1")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mass1gen_hist.GetYaxis().SetTitle("#sigma [pb]")
mass1gen_hist.GetXaxis().SetTitle("mass1 [GeV]")

mass1gen_hist.SetLineColor(ROOT.kBlack)
mass1gen_hist.SetStats(0)
mass1gen_hist.SetLineWidth(2)
mass1gen_hist.SetTitle("")
mass1gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"mass1 Simualtion")
canvas.Print(outDirectory+pdfnames+"mass1simulation.pdf")
canvas.Clear()

#add jet2 hists together
#add pt2 hists together
canvas = ROOT.TCanvas("pt2canvas")
canvas.SetLogy(True)
canvas.cd()

pt2gen_hist = ROOT.TH1D("pt2gen_hist","pt2gen_hist",pt2_2000toInf.GetNbinsX(),pt2_2000toInf.GetXaxis().GetXmin(),pt2_2000toInf.GetXaxis().GetXmax())
pt2gen_hist.Sumw2()

pt2gen_hist.Add(pt2_200to300)
pt2gen_hist.Add(pt2_300to500)
pt2gen_hist.Add(pt2_500to700)
pt2gen_hist.Add(pt2_700to1000)
pt2gen_hist.Add(pt2_1000to1500)
pt2gen_hist.Add(pt2_1500to2000)
pt2gen_hist.Add(pt2_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt2gen_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt2gen_hist.GetYaxis().SetTitle("#sigma [pb]")
pt2gen_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt2gen_hist.SetLineColor(ROOT.kBlack)
pt2gen_hist.SetStats(0)
pt2gen_hist.SetLineWidth(2)
pt2gen_hist.SetTitle("")
pt2gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"pt2 Simulation")
canvas.Print(outDirectory+pdfnames+"pt2simulation.pdf")
canvas.Clear()
#add hists together
#add y2 hists together
canvas = ROOT.TCanvas("y2canvas")
canvas.cd()

y2gen_hist = ROOT.TH1D("y2gen_hist","y2gen_hist",y2_2000toInf.GetNbinsX(),y2_2000toInf.GetXaxis().GetXmin(),y2_2000toInf.GetXaxis().GetXmax())
y2gen_hist.Sumw2()

y2gen_hist.Add(y2_200to300)
y2gen_hist.Add(y2_300to500)
y2gen_hist.Add(y2_500to700)
y2gen_hist.Add(y2_700to1000)
y2gen_hist.Add(y2_1000to1500)
y2gen_hist.Add(y2_1500to2000)
y2gen_hist.Add(y2_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(y2gen_hist,"Simulated y2")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

y2gen_hist.GetYaxis().SetTitle("#sigma [pb]")
y2gen_hist.GetXaxis().SetTitle("y2")

y2gen_hist.SetLineColor(ROOT.kBlack)
y2gen_hist.SetStats(0)
y2gen_hist.SetLineWidth(2)
y2gen_hist.SetTitle("")
y2gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"y2 Simualtion")
canvas.Print(outDirectory+pdfnames+"y2simulation.pdf")
canvas.Clear()
#add hists together
#add eta2 hists together
canvas = ROOT.TCanvas("eta2canvas")
canvas.cd()

eta2gen_hist = ROOT.TH1D("eta2gen_hist","eta2gen_hist",eta2_2000toInf.GetNbinsX(),eta2_2000toInf.GetXaxis().GetXmin(),eta2_2000toInf.GetXaxis().GetXmax())
eta2gen_hist.Sumw2()

eta2gen_hist.Add(eta2_200to300)
eta2gen_hist.Add(eta2_300to500)
eta2gen_hist.Add(eta2_500to700)
eta2gen_hist.Add(eta2_700to1000)
eta2gen_hist.Add(eta2_1000to1500)
eta2gen_hist.Add(eta2_1500to2000)
eta2gen_hist.Add(eta2_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(eta2gen_hist,"Simulated eta2")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

eta2gen_hist.GetYaxis().SetTitle("#sigma [pb]")
eta2gen_hist.GetXaxis().SetTitle("eta2")

eta2gen_hist.SetLineColor(ROOT.kBlack)
eta2gen_hist.SetStats(0)
eta2gen_hist.SetLineWidth(2)
eta2gen_hist.SetTitle("")
eta2gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"eta2 Simualtion")
canvas.Print(outDirectory+pdfnames+"eta2simulation.pdf")
canvas.Clear()
#add hists together
#add phi2 hists together
canvas = ROOT.TCanvas("phi2canvas")
canvas.cd()

phi2gen_hist = ROOT.TH1D("phi2gen_hist","phi2gen_hist",phi2_2000toInf.GetNbinsX(),phi2_2000toInf.GetXaxis().GetXmin(),phi2_2000toInf.GetXaxis().GetXmax())
phi2gen_hist.Sumw2()

phi2gen_hist.Add(phi2_200to300)
phi2gen_hist.Add(phi2_300to500)
phi2gen_hist.Add(phi2_500to700)
phi2gen_hist.Add(phi2_700to1000)
phi2gen_hist.Add(phi2_1000to1500)
phi2gen_hist.Add(phi2_1500to2000)
phi2gen_hist.Add(phi2_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(phi2gen_hist,"Simulated phi2")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

phi2gen_hist.GetYaxis().SetTitle("#sigma [pb]")
phi2gen_hist.GetXaxis().SetTitle("phi2")

phi2gen_hist.SetLineColor(ROOT.kBlack)
phi2gen_hist.SetStats(0)
phi2gen_hist.SetLineWidth(2)
phi2gen_hist.SetTitle("")
phi2gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"phi2 Simualtion")
canvas.Print(outDirectory+pdfnames+"phi2simulation.pdf")
canvas.Clear()
#add hists together
#add mass2 hists together
canvas = ROOT.TCanvas("mass2canvas")
canvas.SetLogy(True)
canvas.cd()

mass2gen_hist = ROOT.TH1D("mass2gen_hist","mass2gen_hist",mass2_2000toInf.GetNbinsX(),mass2_2000toInf.GetXaxis().GetXmin(),mass2_2000toInf.GetXaxis().GetXmax())
mass2gen_hist.Sumw2()

mass2gen_hist.Add(mass2_200to300)
mass2gen_hist.Add(mass2_300to500)
mass2gen_hist.Add(mass2_500to700)
mass2gen_hist.Add(mass2_700to1000)
mass2gen_hist.Add(mass2_1000to1500)
mass2gen_hist.Add(mass2_1500to2000)
mass2gen_hist.Add(mass2_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mass2gen_hist,"Simulated mass2")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mass2gen_hist.GetYaxis().SetTitle("#sigma [pb]")
mass2gen_hist.GetXaxis().SetTitle("mass2 [GeV]")

mass2gen_hist.SetLineColor(ROOT.kBlack)
mass2gen_hist.SetStats(0)
mass2gen_hist.SetLineWidth(2)
mass2gen_hist.SetTitle("")
mass2gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"mass2 Simualtion")
canvas.Print(outDirectory+pdfnames+"mass2simulation.pdf")
canvas.Clear()


#add jet3 hists together
#add pt3 hists together
canvas = ROOT.TCanvas("pt3canvas")
canvas.SetLogy(True)
canvas.cd()

pt3gen_hist = ROOT.TH1D("pt3gen_hist","pt3gen_hist",pt3_2000toInf.GetNbinsX(),pt3_2000toInf.GetXaxis().GetXmin(),pt3_2000toInf.GetXaxis().GetXmax())
pt3gen_hist.Sumw2()

pt3gen_hist.Add(pt3_200to300)
pt3gen_hist.Add(pt3_300to500)
pt3gen_hist.Add(pt3_500to700)
pt3gen_hist.Add(pt3_700to1000)
pt3gen_hist.Add(pt3_1000to1500)
pt3gen_hist.Add(pt3_1500to2000)
pt3gen_hist.Add(pt3_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt3gen_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt3gen_hist.GetYaxis().SetTitle("#sigma [pb]")
pt3gen_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt3gen_hist.SetLineColor(ROOT.kBlack)
pt3gen_hist.SetStats(0)
pt3gen_hist.SetLineWidth(2)
pt3gen_hist.SetTitle("")
pt3gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"pt3 Simulation")
canvas.Print(outDirectory+pdfnames+"pt3simulation.pdf")
canvas.Clear()
#add hists together
#add y3 hists together
canvas = ROOT.TCanvas("y3canvas")
canvas.cd()

y3gen_hist = ROOT.TH1D("y3gen_hist","y3gen_hist",y3_2000toInf.GetNbinsX(),y3_2000toInf.GetXaxis().GetXmin(),y3_2000toInf.GetXaxis().GetXmax())
y3gen_hist.Sumw2()

y3gen_hist.Add(y3_200to300)
y3gen_hist.Add(y3_300to500)
y3gen_hist.Add(y3_500to700)
y3gen_hist.Add(y3_700to1000)
y3gen_hist.Add(y3_1000to1500)
y3gen_hist.Add(y3_1500to2000)
y3gen_hist.Add(y3_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(y3gen_hist,"Simulated y3")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

y3gen_hist.GetYaxis().SetTitle("#sigma [pb]")
y3gen_hist.GetXaxis().SetTitle("y3")

y3gen_hist.SetLineColor(ROOT.kBlack)
y3gen_hist.SetStats(0)
y3gen_hist.SetLineWidth(2)
y3gen_hist.SetTitle("")
y3gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"y3 Simualtion")
canvas.Print(outDirectory+pdfnames+"y3simulation.pdf")
canvas.Clear()
#add hists together
#add eta3 hists together
canvas = ROOT.TCanvas("eta3canvas")
canvas.cd()

eta3gen_hist = ROOT.TH1D("eta3gen_hist","eta3gen_hist",eta3_2000toInf.GetNbinsX(),eta3_2000toInf.GetXaxis().GetXmin(),eta3_2000toInf.GetXaxis().GetXmax())
eta3gen_hist.Sumw2()

eta3gen_hist.Add(eta3_200to300)
eta3gen_hist.Add(eta3_300to500)
eta3gen_hist.Add(eta3_500to700)
eta3gen_hist.Add(eta3_700to1000)
eta3gen_hist.Add(eta3_1000to1500)
eta3gen_hist.Add(eta3_1500to2000)
eta3gen_hist.Add(eta3_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(eta3gen_hist,"Simulated eta3")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

eta3gen_hist.GetYaxis().SetTitle("#sigma [pb]")
eta3gen_hist.GetXaxis().SetTitle("eta3")

eta3gen_hist.SetLineColor(ROOT.kBlack)
eta3gen_hist.SetStats(0)
eta3gen_hist.SetLineWidth(2)
eta3gen_hist.SetTitle("")
eta3gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"eta3 Simualtion")
canvas.Print(outDirectory+pdfnames+"eta3simulation.pdf")
canvas.Clear()
#add hists together
#add phi3 hists together
canvas = ROOT.TCanvas("phi3canvas")
canvas.cd()

phi3gen_hist = ROOT.TH1D("phi3gen_hist","phi3gen_hist",phi3_2000toInf.GetNbinsX(),phi3_2000toInf.GetXaxis().GetXmin(),phi3_2000toInf.GetXaxis().GetXmax())
phi3gen_hist.Sumw2()

phi3gen_hist.Add(phi3_200to300)
phi3gen_hist.Add(phi3_300to500)
phi3gen_hist.Add(phi3_500to700)
phi3gen_hist.Add(phi3_700to1000)
phi3gen_hist.Add(phi3_1000to1500)
phi3gen_hist.Add(phi3_1500to2000)
phi3gen_hist.Add(phi3_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(phi3gen_hist,"Simulated phi3")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

phi3gen_hist.GetYaxis().SetTitle("#sigma [pb]")
phi3gen_hist.GetXaxis().SetTitle("phi3")

phi3gen_hist.SetLineColor(ROOT.kBlack)
phi3gen_hist.SetStats(0)
phi3gen_hist.SetLineWidth(2)
phi3gen_hist.SetTitle("")
phi3gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"phi3 Simualtion")
canvas.Print(outDirectory+pdfnames+"phi3simulation.pdf")
canvas.Clear()
#add hists together
#add mass3 hists together
canvas = ROOT.TCanvas("mass3canvas")
canvas.SetLogy(True)
canvas.cd()

mass3gen_hist = ROOT.TH1D("mass3gen_hist","mass3gen_hist",mass3_2000toInf.GetNbinsX(),mass3_2000toInf.GetXaxis().GetXmin(),mass3_2000toInf.GetXaxis().GetXmax())
mass3gen_hist.Sumw2()

mass3gen_hist.Add(mass3_200to300)
mass3gen_hist.Add(mass3_300to500)
mass3gen_hist.Add(mass3_500to700)
mass3gen_hist.Add(mass3_700to1000)
mass3gen_hist.Add(mass3_1000to1500)
mass3gen_hist.Add(mass3_1500to2000)
mass3gen_hist.Add(mass3_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mass3gen_hist,"Simulated mass3")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mass3gen_hist.GetYaxis().SetTitle("#sigma [pb]")
mass3gen_hist.GetXaxis().SetTitle("mass3 [GeV]")

mass3gen_hist.SetLineColor(ROOT.kBlack)
mass3gen_hist.SetStats(0)
mass3gen_hist.SetLineWidth(2)
mass3gen_hist.SetTitle("")
mass3gen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"mass3 Simualtion")
canvas.Print(outDirectory+pdfnames+"mass3simulation.pdf")
canvas.Clear()

#add and plot kinematics together
#add mjj hists together
canvas = ROOT.TCanvas("mjjcanvas")
canvas.SetLogy(True)
canvas.cd()

mjjgen_hist = ROOT.TH1D("mjjgen_hist","mjjgen_hist",mjj_2000toInf.GetNbinsX(),mjj_2000toInf.GetXaxis().GetXmin(),mjj_2000toInf.GetXaxis().GetXmax())
mjjgen_hist.Sumw2()

mjjgen_hist.Add(mjj_200to300)
mjjgen_hist.Add(mjj_300to500)
mjjgen_hist.Add(mjj_500to700)
mjjgen_hist.Add(mjj_700to1000)
mjjgen_hist.Add(mjj_1000to1500)
mjjgen_hist.Add(mjj_1500to2000)
mjjgen_hist.Add(mjj_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mjjgen_hist,"Simulated mjj")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mjjgen_hist.GetYaxis().SetTitle("#sigma [pb]")
mjjgen_hist.GetXaxis().SetTitle("mjj [GeV]")

mjjgen_hist.SetLineColor(ROOT.kBlack)
mjjgen_hist.SetStats(0)
mjjgen_hist.SetLineWidth(2)
mjjgen_hist.SetTitle("")
mjjgen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"mjj Simualtion")
canvas.Print(outDirectory+pdfnames+"mjjsimulation.pdf")
canvas.Clear()

#add and plot kinematics together
#add chi hists together
canvas = ROOT.TCanvas("chicanvas")
canvas.cd()

chigen_hist = ROOT.TH1D("chigen_hist","chigen_hist",chi_2000toInf.GetNbinsX(),chi_2000toInf.GetXaxis().GetXmin(),chi_2000toInf.GetXaxis().GetXmax())
chigen_hist.Sumw2()

chigen_hist.Add(chi_200to300)
chigen_hist.Add(chi_300to500)
chigen_hist.Add(chi_500to700)
chigen_hist.Add(chi_700to1000)
chigen_hist.Add(chi_1000to1500)
chigen_hist.Add(chi_1500to2000)
chigen_hist.Add(chi_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(chigen_hist,"Simulated chi")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

chigen_hist.GetYaxis().SetTitle("#sigma [pb]")
chigen_hist.GetXaxis().SetTitle("chi")

chigen_hist.SetLineColor(ROOT.kBlack)
chigen_hist.SetStats(0)
chigen_hist.SetLineWidth(2)
chigen_hist.SetTitle("")
chigen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"chi Simualtion")
canvas.Print(outDirectory+pdfnames+"chisimulation.pdf")
canvas.Clear()

#add and plot kinematics together
#add yboost hists together
canvas = ROOT.TCanvas("yboostcanvas")
canvas.cd()

yboostgen_hist = ROOT.TH1D("yboostgen_hist","yboostgen_hist",yboost_2000toInf.GetNbinsX(),yboost_2000toInf.GetXaxis().GetXmin(),yboost_2000toInf.GetXaxis().GetXmax())
yboostgen_hist.Sumw2()

yboostgen_hist.Add(yboost_200to300)
yboostgen_hist.Add(yboost_300to500)
yboostgen_hist.Add(yboost_500to700)
yboostgen_hist.Add(yboost_700to1000)
yboostgen_hist.Add(yboost_1000to1500)
yboostgen_hist.Add(yboost_1500to2000)
yboostgen_hist.Add(yboost_2000toInf)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(yboostgen_hist,"Simulated yboost")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

yboostgen_hist.GetYaxis().SetTitle("#sigma [pb]")
yboostgen_hist.GetXaxis().SetTitle("yboost")

yboostgen_hist.SetLineColor(ROOT.kBlack)
yboostgen_hist.SetStats(0)
yboostgen_hist.SetLineWidth(2)
yboostgen_hist.SetTitle("")
yboostgen_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"yboost Simualtion")
canvas.Print(outDirectory+pdfnames+"yboostsimulation.pdf")
canvas.Clear()

#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_PlotSimulation_WithScale_Run22018_MC.root","RECREATE")
#Write simJet1 to Root
outHistFile.mkdir("Jet1")
outHistFile.cd("Jet1")
pt1gen_hist.Write()
y1gen_hist.Write()
eta1gen_hist.Write()
phi1gen_hist.Write()
mass1gen_hist.Write()
#Write simJet2 to Root
outHistFile.mkdir("Jet2")
outHistFile.cd("Jet2")
pt2gen_hist.Write()
y2gen_hist.Write()
eta2gen_hist.Write()
phi2gen_hist.Write()
mass2gen_hist.Write()
#Write simJet3 to Root
outHistFile.mkdir("Jet3")
outHistFile.cd("Jet3")
pt3gen_hist.Write()
y3gen_hist.Write()
eta3gen_hist.Write()
phi3gen_hist.Write()
mass3gen_hist.Write()
#Write simjet quantities to Root
outHistFile.mkdir("Kinematics")
outHistFile.cd("Kinematics")
mjjgen_hist.Write()
yboostgen_hist.Write()
chigen_hist.Write()
outHistFile.Close()
