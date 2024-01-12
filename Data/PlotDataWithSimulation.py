import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,runb,runc,rund,sim,yAxisTitle,xAxisTitle,title,undertitle,setLogy):
    canvas_pads = ROOT.TCanvas("canvas_pads", "Double ratio")
    pad_top = ROOT.TPad("top_pad", "Top pad", 0, 0.3, 1, 1)
    if setLogy:
        pad_top.SetLogy(True)
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
    sim.SetTitle(title+undertitle)

    runb.Scale(sim.Integral()/runb.Integral())
    runc.Scale(sim.Integral()/runc.Integral())
    rund.Scale(sim.Integral()/rund.Integral())

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

    ratiorunbSim = runb.Clone()
    ratiorunbSim.Divide(sim)
    ratiorunbSimgraph = ROOT.TGraphAsymmErrors(ratiorunbSim)
    for i in range(0,int(runb.GetNbinsX())):
	    ratiorunbSimgraph.SetPointEXhigh(i,0.0)
	    ratiorunbSimgraph.SetPointEXlow(i,0.0)

    ratioruncSim = runc.Clone()
    ratioruncSim.Divide(sim)
    ratioruncSimgraph = ROOT.TGraphAsymmErrors(ratioruncSim)
    for i in range(0,int(runc.GetNbinsX())):
	    ratioruncSimgraph.SetPointEXhigh(i,0.0)
	    ratioruncSimgraph.SetPointEXlow(i,0.0)

    ratiorundSim = rund.Clone()
    ratiorundSim.Divide(sim)
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
inFileNameB = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunB/RootB/PlotDijetJetID_Run2023B.root"
#Get Jets and Kinematics
histFileB = ROOT.TFile.Open(inFileNameB,"READ")
Jet1B = histFileB.Get("Jet1")
Jet2B = histFileB.Get("Jet2")
Jet3B = histFileB.Get("Jet3")
KinematicsB = histFileB.Get("Kinematics")

#load RunC Data
#define directory
inFileNameC = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunC/RootC/PlotDijetJetID_Run2023C.root"
#Get Jets and Kinematics
histFileC = ROOT.TFile.Open(inFileNameC,"READ")
Jet1C = histFileC.Get("Jet1")
Jet2C = histFileC.Get("Jet2")
Jet3C = histFileC.Get("Jet3")
KinematicsC = histFileC.Get("Kinematics")

#load RunD Data
#define directory
inFileNameD = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/PlotDijetJetID_Run2023D.root"
#Get Jets and Kinematics
histFileD = ROOT.TFile.Open(inFileNameD,"READ")
Jet1D = histFileD.Get("Jet1")
Jet2D = histFileD.Get("Jet2")
Jet3D = histFileD.Get("Jet3")
KinematicsD = histFileD.Get("Kinematics")

#load Simulation
#define directory
inFileNameS = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_PlotSimulation_WithScale_Run32023_MC.root"
#Get Jets and Kinematics
histFileS = ROOT.TFile.Open(inFileNameS,"READ")
Jet1S = histFileS.Get("Jet1")
Jet2S = histFileS.Get("Jet2")
Jet3S = histFileS.Get("Jet3")
KinematicsS = histFileS.Get("Kinematics")

JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create Jet pdfs
for i in range(0,14):
    #load JetB data
    Jet1_Bdata = Jet1B.Get("data_"+JetNameArray[i]+"1")
    Jet2_Bdata = Jet2B.Get("data_"+JetNameArray[i]+"2")
    Jet3_Bdata = Jet3B.Get("data_"+JetNameArray[i]+"3")
    #load JetC data
    Jet1_Cdata = Jet1C.Get("data_"+JetNameArray[i]+"1")
    Jet2_Cdata = Jet2C.Get("data_"+JetNameArray[i]+"2")
    Jet3_Cdata = Jet3C.Get("data_"+JetNameArray[i]+"3")
    #load JetD data
    Jet1_Ddata = Jet1D.Get("data_"+JetNameArray[i]+"1")
    Jet2_Ddata = Jet2D.Get("data_"+JetNameArray[i]+"2")
    Jet3_Ddata = Jet3D.Get("data_"+JetNameArray[i]+"3")
    #load Simulation
    Jet1_Sim = Jet1S.Get(JetNameArray[i]+"1sim_hist")
    Jet2_Sim = Jet2S.Get(JetNameArray[i]+"2sim_hist")
    Jet3_Sim = Jet3S.Get(JetNameArray[i]+"3sim_hist")

    #plot jet1
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"1.pdf",Jet1_Bdata,Jet1_Cdata,Jet1_Ddata,Jet1_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet1",True)
    else:
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"1.pdf",Jet1_Bdata,Jet1_Cdata,Jet1_Ddata,Jet1_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet1",False)

    #plot jet2
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"2.pdf",Jet2_Bdata,Jet2_Cdata,Jet2_Ddata,Jet2_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet2",True)
    else:
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"2.pdf",Jet2_Bdata,Jet2_Cdata,Jet2_Ddata,Jet1_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet2",False)

    #plot jet3
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"3.pdf",Jet3_Bdata,Jet3_Cdata,Jet3_Ddata,Jet3_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet3",True)
    else:
        RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_"+JetNameArray[i]+"3.pdf",Jet3_Bdata,Jet3_Cdata,Jet3_Ddata,Jet3_Sim,"#sigma [pb]",XaxisArray[i],"Run2023",JetNameArray[i]+" for Jet3",False)


#create yboost pdf
yboostDataB = KinematicsB.Get("data_yboost")
yboostDataC = KinematicsC.Get("data_yboost")
yboostDataD = KinematicsD.Get("data_yboost")
yboostSim = KinematicsS.Get("yboostsim_hist")
RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_yboost.pdf",yboostDataB,yboostDataC,yboostDataD,yboostSim,"#sigma [pb]","YBoost","Run2023","yboost",False)

#create chi pdf
chiDataB = KinematicsB.Get("data_chi")
chiDataC = KinematicsC.Get("data_chi")
chiDataD = KinematicsD.Get("data_chi")
chiSim = KinematicsS.Get("chisim_hist")
RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_chi.pdf",chiDataB,chiDataC,chiDataD,chiSim,"#sigma [pb]","Chi","Run2023","chi",False)

#create mjj pdf
mjjDataB = KinematicsB.Get("data_mjj")
mjjDataC = KinematicsC.Get("data_mjj")
mjjDataD = KinematicsD.Get("data_mjj")
mjjSim = KinematicsS.Get("mjjsim_hist")
RootHisttoPdf(outDirectory+"PlotAllRunsWithSimulation_Normiert_mjj.pdf",mjjDataB,mjjDataC,mjjDataD,mjjSim,"#sigma [pb]","Mjj","Run2023","mjj",True)
