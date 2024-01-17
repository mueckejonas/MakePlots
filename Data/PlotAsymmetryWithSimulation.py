import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,runb,runc,rund,sim,yAxisTitle,xAxisTitle,title):
    canvas_pads = ROOT.TCanvas("canvas_pads", "Double ratio")
    pad_top = ROOT.TPad("top_pad", "Top pad", 0, 0.3, 1, 1)
    pad_top.SetBottomMargin(0)
    pad_top.Draw()
    pad_bottom = ROOT.TPad("bottom_pad", "Bottom pad", 0, 0.05, 1, 0.3)
    pad_bottom.SetBottomMargin(0.25)
    pad_bottom.SetTopMargin(0)
    pad_bottom.Draw()

    runb.Scale(1./1206)
    runc.Scale(1./18600)
    rund.Scale(1./10000)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.SetTextSize(0.03)

    runbgraph = ROOT.TGraphAsymmErrors(runb)
    for i in range(0,int(runb.GetNbinsX())):
	    runbgraph.SetPointEXhigh(i,0.0)
	    runbgraph.SetPointEXlow(i,0.0)

    runcgraph = ROOT.TGraphAsymmErrors(runc)
    for i in range(0,int(runc.GetNbinsX())):
	    runcgraph.SetPointEXhigh(i,0.0)
	    runcgraph.SetPointEXlow(i,0.0)

    rundgraph = ROOT.TGraphAsymmErrors(rund)
    for i in range(0,int(rund.GetNbinsX())):
	    rundgraph.SetPointEXhigh(i,0.0)
	    rundgraph.SetPointEXlow(i,0.0)

    #draw sim
    pad_top.cd()
    runbgraph.SetStats(0)
    runbgraph.SetLineColor(ROOT.kBlack)
    runbgraph.SetLineWidth(2)
    runbgraph.SetTitle("")
    runbgraph.SetMarkerColor(ROOT.kBlack)
    runbgraph.SetMarkerStyle(4)
    runcgraph.SetStats(0)
    runcgraph.SetLineColor(ROOT.kBlue)
    runcgraph.SetLineWidth(2)
    runcgraph.SetTitle("")
    runcgraph.SetMarkerColor(ROOT.kBlue)
    runcgraph.SetMarkerStyle(4)
    rundgraph.SetStats(0)
    rundgraph.SetLineColor(ROOT.kGreen)
    rundgraph.SetLineWidth(2)
    rundgraph.SetTitle("")
    rundgraph.SetMarkerColor(ROOT.kGreen)
    rundgraph.SetMarkerStyle(4)
    sim.SetStats(0)
    sim.SetLineColor(ROOT.kRed)
    sim.SetLineWidth(2)
    sim.SetTitle(title)

    runbgraph.Scale(sim.Integral()/runb.Integral())
    runcgraph.Scale(sim.Integral()/runc.Integral())
    rundgraph.Scale(sim.Integral()/rund.Integral())

    sim.GetYaxis().SetTitle(yAxisTitle)
    sim.GetYaxis().SetTitleSize(0.05)
    #sim.GetXaxis().SetTitle(xAxisTitle)
    #sim.GetXaxis().SetTitleSize(0.05)

    legend.AddEntry(runbgraph,"RunB Data","p")
    legend.AddEntry(runcgraph,"RunC Data","p")
    legend.AddEntry(rundgraph,"RunD Data","p")
    legend.AddEntry(sim,"Simulation")

    sim.Draw("h")
    runbgraph.Draw("P same")
    runcgraph.Draw("P same")
    rundgraph.Draw("P same")
    legend.Draw("same")


    line = ROOT.TLine(runbgraph.GetXaxis().GetXmin(),1,runbgraph.GetXaxis().GetXmax(),1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)

    #draw ratio
    pad_bottom.cd()

    runb.Scale(sim.Integral()/runb.Integral())
    runc.Scale(sim.Integral()/runc.Integral())
    rund.Scale(sim.Integral()/rund.Integral())

    ratiorunbSim = runb.Clone()
    ratiorunbSim.Divide(runb)
    ratiorunbSimgraph = ROOT.TGraphAsymmErrors(ratiorunbSim)
    for i in range(0,int(runb.GetNbinsX())):
	    ratiorunbSimgraph.SetPointEXhigh(i,0.0)
	    ratiorunbSimgraph.SetPointEXlow(i,0.0)

    ratioruncSim = runc.Clone()
    ratioruncSim.Divide(runc)
    ratioruncSimgraph = ROOT.TGraphAsymmErrors(ratioruncSim)
    for i in range(0,int(runc.GetNbinsX())):
	    ratioruncSimgraph.SetPointEXhigh(i,0.0)
	    ratioruncSimgraph.SetPointEXlow(i,0.0)

    ratiorundSim = rund.Clone()
    ratiorundSim.Divide(rund)
    ratiorundSimgraph = ROOT.TGraphAsymmErrors(ratiorundSim)
    for i in range(0,int(rund.GetNbinsX())):
	    ratiorundSimgraph.SetPointEXhigh(i,0.0)
	    ratiorundSimgraph.SetPointEXlow(i,0.0)

    ratiorunbSimgraph.SetLineColor(ROOT.kBlack)
    ratiorunbSimgraph.SetLineWidth(2)
    ratiorunbSimgraph.SetTitle("")
    ratiorunbSimgraph.SetMarkerStyle(4)

    ratioruncSimgraph.SetLineColor(ROOT.kBlue)
    ratioruncSimgraph.SetLineWidth(2)
    ratioruncSimgraph.SetTitle("")
    ratioruncSimgraph.SetMarkerStyle(4)

    ratiorundSimgraph.SetLineColor(ROOT.kGreen)
    ratiorundSimgraph.SetLineWidth(2)
    ratiorundSimgraph.SetTitle("")
    ratiorundSimgraph.SetMarkerStyle(4)

    ratiorunbSimgraph.GetYaxis().SetTitle("Data/Simulation")
    ratiorunbSimgraph.GetYaxis().SetLabelSize(0.1)
    ratiorunbSimgraph.GetYaxis().SetTitleSize(0.15)
    ratiorunbSimgraph.GetXaxis().SetLabelSize(0.12)
    ratiorunbSimgraph.GetXaxis().SetTitleSize(0.12)
    ratiorunbSimgraph.GetYaxis().SetTitleOffset(0.3)
    ratiorunbSimgraph.GetYaxis().SetNdivisions (207)
    ratiorunbSimgraph.GetXaxis().SetTitle(xAxisTitle)
    ratiorunbSimgraph.GetYaxis().SetRangeUser(0.5,1.5)

    ratiorunbSimgraph.Draw("AP")
    ratioruncSimgraph.Draw("P same")
    ratiorundSimgraph.Draw("P same")
    line.Draw("same")


    #draw whole plot
    canvas_pads.Draw()
    canvas_pads.Print(outFileName)

#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Data/"

#load RunB Data
#define directory
inFileNameB = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/RootB/PlotDijetAsymmetry_Run2023B.root"
rootFileB = ROOT.TFile.Open(inFileNameB,"READ")
PtAsymmetryB = rootFileB.Get("PtAsymmetry")
PhiDifferenceB = rootFileB.Get("PhiDifference")
EtaDifferenceB = rootFileB.Get("EtaDifference")
YDifferenceB = rootFileB.Get("YDifference")
ThetaDifferenceB = rootFileB.Get("ThetaDifference")

#load RunC Data
#define directory
inFileNameC = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/PlotDijetAsymmetry_Run2023C.root"
rootFileC = ROOT.TFile.Open(inFileNameC,"READ")
PtAsymmetryC = rootFileC.Get("PtAsymmetry")
PhiDifferenceC = rootFileC.Get("PhiDifference")
EtaDifferenceC = rootFileC.Get("EtaDifference")
YDifferenceC = rootFileC.Get("YDifference")
ThetaDifferenceC = rootFileC.Get("ThetaDifference")

#load RunD Data
#define directory
inFileNameD = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/PlotDijetAsymmetry_Run2023D.root"
rootFileD = ROOT.TFile.Open(inFileNameD,"READ")
PtAsymmetryD = rootFileD.Get("PtAsymmetry")
PhiDifferenceD = rootFileD.Get("PhiDifference")
EtaDifferenceD = rootFileD.Get("EtaDifference")
YDifferenceD = rootFileD.Get("YDifference")
ThetaDifferenceD = rootFileD.Get("ThetaDifference")

#load Simulation
#define directory
inFileNameSim = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_Plot_DijetAsymmetry_WithScale_Run32023_MC.root"
rootFileSim = ROOT.TFile.Open(inFileNameSim,"READ")
PtAsymmetrySim = rootFileSim.Get("PtAsymmetrysim_hist")
PhiDifferenceSim = rootFileSim.Get("PhiDifferencesim_hist")
EtaDifferenceSim = rootFileSim.Get("EtaDifferencesim_hist")
YDifferenceSim = rootFileSim.Get("YDifferencesim_hist")
ThetaDifferenceSim = rootFileSim.Get("ThetaDifferencesim_hist")

#create PtAsymmetry pdf
RootHisttoPdf(outDirectory+"PlotDijetAsymmetry_AllRuns.pdf",PtAsymmetryB,PtAsymmetryC,PtAsymmetryD,PtAsymmetrySim,"#sigma [pb]","(Pt1-Pt2)/(Pt1+Pt2)","Dijet Asymmetry RunB, C and D Run2023")

#create PhiDifference pdf
RootHisttoPdf(outDirectory+"PlotPhiDifference_AllRuns.pdf",PhiDifferenceB,PhiDifferenceC,PhiDifferenceD,PhiDifferenceSim,"#sigma [pb]","Phi1-Phi2","Phi Difference RunB, C and D Run2023")

#create EtaDifference pdf
RootHisttoPdf(outDirectory+"PlotEtaDifference_AllRuns.pdf",EtaDifferenceB,EtaDifferenceC,EtaDifferenceD,EtaDifferenceSim,"#sigma [pb]","Eta1-Eta2","Eta Difference RunB, C and D Run2023")

#create YDifference pdf
RootHisttoPdf(outDirectory+"PlotYDifference_AllRuns.pdf",YDifferenceB,YDifferenceC,YDifferenceD,YDifferenceSim,"#sigma [pb]","Y1-Y2","Y Difference RunB, C and D Run2023")

#create ThetaDifference pdf
RootHisttoPdf(outDirectory+"PlotThetaDifference_AllRuns.pdf",ThetaDifferenceB,ThetaDifferenceC,ThetaDifferenceD,ThetaDifferenceSim,"#sigma [pb]","Theta1-Theta2","Theta Difference RunB, C and D Run2023")
