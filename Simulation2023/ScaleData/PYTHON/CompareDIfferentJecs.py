import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,normal,raw,nom,yAxisTitle,xAxisTitle,title):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    canvas.SetBottomMargin(0.18)
    canvas.SetTopMargin(0.05)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)

    legend = ROOT.TLegend(0.4,0.6,0.65,0.85)
    legend.SetFillStyle(4000)
    legend.SetTextSize(0.045)
    legend.SetLineWidth(0)

    normalgraph = ROOT.TGraphAsymmErrors(normal)
    for i in range(0,int(normal.GetNbinsX())):
        normalgraph.SetPointEXhigh(i,0.0)
        normalgraph.SetPointEXlow(i,0.0)

    rawgraph = ROOT.TGraphAsymmErrors(raw)
    for i in range(0,int(raw.GetNbinsX())):
        rawgraph.SetPointEXhigh(i,0.0)
        rawgraph.SetPointEXlow(i,0.0)

    nomgraph = ROOT.TGraphAsymmErrors(nom)
    for i in range(0,int(nom.GetNbinsX())):
        nomgraph.SetPointEXhigh(i,0.0)
        nomgraph.SetPointEXlow(i,0.0)

    #draw sim
    normalgraph.SetStats(0)
    normalgraph.SetLineColor(ROOT.kBlack)
    normalgraph.SetLineWidth(2)
    normalgraph.SetTitle("")
    normalgraph.SetMarkerColor(ROOT.kBlack)
    normalgraph.SetMarkerStyle(4)
    normalgraph.SetMarkerSize(3)
    rawgraph.SetStats(0)
    rawgraph.SetLineColor(ROOT.kBlue)
    rawgraph.SetLineWidth(2)
    rawgraph.SetTitle("")
    rawgraph.SetMarkerColor(ROOT.kBlue)
    rawgraph.SetMarkerStyle(4)
    rawgraph.SetMarkerSize(3)
    nomgraph.SetStats(0)
    nomgraph.SetLineColor(ROOT.kGreen)
    nomgraph.SetLineWidth(2)
    nomgraph.SetTitle("")
    nomgraph.SetMarkerColor(ROOT.kGreen)
    nomgraph.SetMarkerStyle(4)
    nomgraph.SetMarkerSize(3)

    normalgraph.GetYaxis().SetTitle(yAxisTitle)
    normalgraph.GetXaxis().SetTitleSize(0.06)
    normalgraph.GetXaxis().SetTitle(xAxisTitle)
    normalgraph.GetXaxis().SetLabelSize(0.06)
    normalgraph.GetXaxis().SetNdivisions(207)
    normalgraph.GetYaxis().SetLabelSize(0.06)
    normalgraph.GetYaxis().SetTitleSize(0.08)
    normalgraph.GetYaxis().SetTitleOffset(0.8)

    legend.AddEntry(normalgraph,title+" old JEC","p")
    legend.AddEntry(rawgraph,title+" no JEC","p")
    legend.AddEntry(nomgraph,title+" new JEC","p")

    normalgraph.Draw("AP")
    rawgraph.Draw("P same")
    nomgraph.Draw("P same")
    legend.Draw("same")
    canvas.Print(outFileName)

#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/Pdf/"

#load Asymmetry hists
#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"
rootFile = ROOT.TFile.Open(inDirectory+"_PlotSimulation_WithScale_Run32023_MC_OldJEC.root","READ")
rootFileNom = ROOT.TFile.Open(inDirectory+"_PlotSimulation_WithScale_Run32023_MC_NewJEC.root","READ")
rootFileRaw = ROOT.TFile.Open(inDirectory+"_PlotSimulation_WithScale_Run32023_MC_NoJEC.root","READ")

#load pt Jet1
pt1sim_hist = rootFile.Get("pt1sim_hist")
pt1rawsim_hist = rootFileRaw.Get("pt1rawsim_hist")
pt1nomsim_hist = rootFileNom.Get("pt1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt1.pdf",pt1sim_hist,pt1rawsim_hist,pt1nomsim_hist,"#sigma [pb]","p_{T1}","p_{T1}")
#load y Jet1
y1sim_hist = rootFile.Get("y1sim_hist")
y1rawsim_hist = rootFileRaw.Get("y1rawsim_hist")
y1nomsim_hist = rootFileNom.Get("y1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_y1.pdf",y1sim_hist,y1rawsim_hist,y1nomsim_hist,"#sigma [pb]","y_{1}","y_{1}")
#load eta Jet1
eta1sim_hist = rootFile.Get("eta1sim_hist")
eta1rawsim_hist = rootFileRaw.Get("eta1rawsim_hist")
eta1nomsim_hist = rootFileNom.Get("eta1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_eta1.pdf",eta1sim_hist,eta1rawsim_hist,eta1nomsim_hist,"#sigma [pb]","#eta_{1}","#eta_{1}")
#load phi Jet1
phi1sim_hist = rootFile.Get("phi1sim_hist")
phi1rawsim_hist = rootFileRaw.Get("phi1rawsim_hist")
phi1nomsim_hist = rootFileNom.Get("phi1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_phi1.pdf",phi1sim_hist,phi1rawsim_hist,phi1nomsim_hist,"#sigma [pb]","#phi_{1}","#phi_{1}")
#load mass Jet1
mass1sim_hist = rootFile.Get("mass1sim_hist")
mass1rawsim_hist = rootFileRaw.Get("mass1rawsim_hist")
mass1nomsim_hist = rootFileNom.Get("mass1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_mass1.pdf",mass1sim_hist,mass1rawsim_hist,mass1nomsim_hist,"#sigma [pb]","mass_{1}","mass_{1}")
#load jec Jet1
jec1sim_hist = rootFile.Get("jec1sim_hist")
jec1rawsim_hist = rootFileRaw.Get("jec1rawsim_hist")
jec1nomsim_hist = rootFileNom.Get("jec1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_jec1.pdf",jec1sim_hist,jec1rawsim_hist,jec1nomsim_hist,"#sigma [pb]","jec_{1}","jec_{1}")
#load muf Jet1
muf1sim_hist = rootFile.Get("muf1sim_hist")
muf1rawsim_hist = rootFileRaw.Get("muf1rawsim_hist")
muf1nomsim_hist = rootFileNom.Get("muf1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_muf1.pdf",muf1sim_hist,muf1rawsim_hist,muf1nomsim_hist,"#sigma [pb]","muf_{1}","muf_{1}")
#load nhf Jet1
nhf1sim_hist = rootFile.Get("nhf1sim_hist")
nhf1rawsim_hist = rootFileRaw.Get("nhf1rawsim_hist")
nhf1nomsim_hist = rootFileNom.Get("nhf1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nhf1.pdf",nhf1sim_hist,nhf1rawsim_hist,nhf1nomsim_hist,"#sigma [pb]","nhf_{1}","nhf_{1}")
#load chf Jet1
chf1sim_hist = rootFile.Get("chf1sim_hist")
chf1rawsim_hist = rootFileRaw.Get("chf1rawsim_hist")
chf1nomsim_hist = rootFileNom.Get("chf1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_chf1.pdf",chf1sim_hist,chf1rawsim_hist,chf1nomsim_hist,"#sigma [pb]","chf_{1}","chf_{1}")
#load area Jet1
area1sim_hist = rootFile.Get("area1sim_hist")
area1rawsim_hist = rootFileRaw.Get("area1rawsim_hist")
area1nomsim_hist = rootFileNom.Get("area1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_area1.pdf",area1sim_hist,area1rawsim_hist,area1nomsim_hist,"#sigma [pb]","area_{1}","area_{1}")
#load nemf Jet1
nemf1sim_hist = rootFile.Get("nemf1sim_hist")
nemf1rawsim_hist = rootFileRaw.Get("nemf1rawsim_hist")
nemf1nomsim_hist = rootFileNom.Get("nemf1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nemf1.pdf",nemf1sim_hist,nemf1rawsim_hist,nemf1nomsim_hist,"#sigma [pb]","nemf_{1}","nemf_{1}")
#load cemf Jet1
cemf1sim_hist = rootFile.Get("cemf1sim_hist")
cemf1rawsim_hist = rootFileRaw.Get("cemf1rawsim_hist")
cemf1nomsim_hist = rootFileNom.Get("cemf1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_cemf1.pdf",cemf1sim_hist,cemf1rawsim_hist,cemf1nomsim_hist,"#sigma [pb]","cemf_{1}","cemf_{1}")
#load btagDeepFlavB Jet1
btagDeepFlavB1sim_hist = rootFile.Get("btagDeepFlavB1sim_hist")
btagDeepFlavB1rawsim_hist = rootFileRaw.Get("btagDeepFlavB1rawsim_hist")
btagDeepFlavB1nomsim_hist = rootFileNom.Get("btagDeepFlavB1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_btagDeepFlavB1.pdf",btagDeepFlavB1sim_hist,btagDeepFlavB1rawsim_hist,btagDeepFlavB1nomsim_hist,"#sigma [pb]","btagDeepFlavB_{1}","btagDeepFlavB_{1}")
#load nConstituents Jet1
nConstituents1sim_hist = rootFile.Get("nConstituents1sim_hist")
nConstituents1rawsim_hist = rootFileRaw.Get("nConstituents1rawsim_hist")
nConstituents1nomsim_hist = rootFileNom.Get("nConstituents1nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nConstituents1.pdf",nConstituents1sim_hist,nConstituents1rawsim_hist,nConstituents1nomsim_hist,"#sigma [pb]","nConstituents_{1}","nConstituents_{1}")

#load pt Jet2
pt2sim_hist = rootFile.Get("pt2sim_hist")
pt2rawsim_hist = rootFileRaw.Get("pt2rawsim_hist")
pt2nomsim_hist = rootFileNom.Get("pt2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt2.pdf",pt2sim_hist,pt2rawsim_hist,pt2nomsim_hist,"#sigma [pb]","p_{T2}","p_{T2}")
#load y Jet2
y2sim_hist = rootFile.Get("y2sim_hist")
y2rawsim_hist = rootFileRaw.Get("y2rawsim_hist")
y2nomsim_hist = rootFileNom.Get("y2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_y2.pdf",y2sim_hist,y2rawsim_hist,y2nomsim_hist,"#sigma [pb]","y_{2}","y_{2}")
#load eta Jet2
eta2sim_hist = rootFile.Get("eta2sim_hist")
eta2rawsim_hist = rootFileRaw.Get("eta2rawsim_hist")
eta2nomsim_hist = rootFileNom.Get("eta2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_eta2.pdf",eta2sim_hist,eta2rawsim_hist,eta2nomsim_hist,"#sigma [pb]","#eta_{2}","#eta_{2}")
#load phi Jet2
phi2sim_hist = rootFile.Get("phi2sim_hist")
phi2rawsim_hist = rootFileRaw.Get("phi2rawsim_hist")
phi2nomsim_hist = rootFileNom.Get("phi2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_phi2.pdf",phi2sim_hist,phi2rawsim_hist,phi2nomsim_hist,"#sigma [pb]","#phi_{2}","#phi_{2}")
#load mass Jet2
mass2sim_hist = rootFile.Get("mass2sim_hist")
mass2rawsim_hist = rootFileRaw.Get("mass2rawsim_hist")
mass2nomsim_hist = rootFileNom.Get("mass2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_mass2.pdf",mass2sim_hist,mass2rawsim_hist,mass2nomsim_hist,"#sigma [pb]","mass_{2}","mass_{2}")
#load jec Jet2
jec2sim_hist = rootFile.Get("jec2sim_hist")
jec2rawsim_hist = rootFileRaw.Get("jec2rawsim_hist")
jec2nomsim_hist = rootFileNom.Get("jec2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_jec2.pdf",jec2sim_hist,jec2rawsim_hist,jec2nomsim_hist,"#sigma [pb]","jec_{2}","jec_{2}")
#load muf Jet2
muf2sim_hist = rootFile.Get("muf2sim_hist")
muf2rawsim_hist = rootFileRaw.Get("muf2rawsim_hist")
muf2nomsim_hist = rootFileNom.Get("muf2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_muf2.pdf",muf2sim_hist,muf2rawsim_hist,muf2nomsim_hist,"#sigma [pb]","muf_{2}","muf_{2}")
#load nhf Jet2
nhf2sim_hist = rootFile.Get("nhf2sim_hist")
nhf2rawsim_hist = rootFileRaw.Get("nhf2rawsim_hist")
nhf2nomsim_hist = rootFileNom.Get("nhf2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nhf2.pdf",nhf2sim_hist,nhf2rawsim_hist,nhf2nomsim_hist,"#sigma [pb]","nhf_{2}","nhf_{2}")
#load chf Jet2
chf2sim_hist = rootFile.Get("chf2sim_hist")
chf2rawsim_hist = rootFileRaw.Get("chf2rawsim_hist")
chf2nomsim_hist = rootFileNom.Get("chf2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_chf2.pdf",chf2sim_hist,chf2rawsim_hist,chf2nomsim_hist,"#sigma [pb]","chf_{2}","chf_{2}")
#load area Jet2
area2sim_hist = rootFile.Get("area2sim_hist")
area2rawsim_hist = rootFileRaw.Get("area2rawsim_hist")
area2nomsim_hist = rootFileNom.Get("area2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_area2.pdf",area2sim_hist,area2rawsim_hist,area2nomsim_hist,"#sigma [pb]","area_{2}","area_{2}")
#load nemf Jet2
nemf2sim_hist = rootFile.Get("nemf2sim_hist")
nemf2rawsim_hist = rootFileRaw.Get("nemf2rawsim_hist")
nemf2nomsim_hist = rootFileNom.Get("nemf2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nemf2.pdf",nemf2sim_hist,nemf2rawsim_hist,nemf2nomsim_hist,"#sigma [pb]","nemf_{2}","nemf_{2}")
#load cemf Jet2
cemf2sim_hist = rootFile.Get("cemf2sim_hist")
cemf2rawsim_hist = rootFileRaw.Get("cemf2rawsim_hist")
cemf2nomsim_hist = rootFileNom.Get("cemf2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_cemf2.pdf",cemf2sim_hist,cemf2rawsim_hist,cemf2nomsim_hist,"#sigma [pb]","cemf_{2}","cemf_{2}")
#load btagDeepFlavB Jet2
btagDeepFlavB2sim_hist = rootFile.Get("btagDeepFlavB2sim_hist")
btagDeepFlavB2rawsim_hist = rootFileRaw.Get("btagDeepFlavB2rawsim_hist")
btagDeepFlavB2nomsim_hist = rootFileNom.Get("btagDeepFlavB2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_btagDeepFlavB2.pdf",btagDeepFlavB2sim_hist,btagDeepFlavB2rawsim_hist,btagDeepFlavB2nomsim_hist,"#sigma [pb]","btagDeepFlavB_{2}","btagDeepFlavB_{2}")
#load nConstituents Jet2
nConstituents2sim_hist = rootFile.Get("nConstituents2sim_hist")
nConstituents2rawsim_hist = rootFileRaw.Get("nConstituents2rawsim_hist")
nConstituents2nomsim_hist = rootFileNom.Get("nConstituents2nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nConstituents2.pdf",nConstituents2sim_hist,nConstituents2rawsim_hist,nConstituents2nomsim_hist,"#sigma [pb]","nConstituents_{2}","nConstituents_{2}")

#load pt Jet3
pt3sim_hist = rootFile.Get("pt3sim_hist")
pt3rawsim_hist = rootFileRaw.Get("pt3rawsim_hist")
pt3nomsim_hist = rootFileNom.Get("pt3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Pt3.pdf",pt3sim_hist,pt3rawsim_hist,pt3nomsim_hist,"#sigma [pb]","p_{T3}","p_{T3}")
#load y Jet3
y3sim_hist = rootFile.Get("y3sim_hist")
y3rawsim_hist = rootFileRaw.Get("y3rawsim_hist")
y3nomsim_hist = rootFileNom.Get("y3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_y3.pdf",y3sim_hist,y3rawsim_hist,y3nomsim_hist,"#sigma [pb]","y_{3}","y_{3}")
#load eta Jet3
eta3sim_hist = rootFile.Get("eta3sim_hist")
eta3rawsim_hist = rootFileRaw.Get("eta3rawsim_hist")
eta3nomsim_hist = rootFileNom.Get("eta3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_eta3.pdf",eta3sim_hist,eta3rawsim_hist,eta3nomsim_hist,"#sigma [pb]","#eta_{3}","#eta_{3}")
#load phi Jet3
phi3sim_hist = rootFile.Get("phi3sim_hist")
phi3rawsim_hist = rootFileRaw.Get("phi3rawsim_hist")
phi3nomsim_hist = rootFileNom.Get("phi3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_phi3.pdf",phi3sim_hist,phi3rawsim_hist,phi3nomsim_hist,"#sigma [pb]","#phi_{3}","#phi_{3}")
#load mass Jet3
mass3sim_hist = rootFile.Get("mass3sim_hist")
mass3rawsim_hist = rootFileRaw.Get("mass3rawsim_hist")
mass3nomsim_hist = rootFileNom.Get("mass3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_mass3.pdf",mass3sim_hist,mass3rawsim_hist,mass3nomsim_hist,"#sigma [pb]","mass_{3}","mass_{3}")
#load jec Jet3
jec3sim_hist = rootFile.Get("jec3sim_hist")
jec3rawsim_hist = rootFileRaw.Get("jec3rawsim_hist")
jec3nomsim_hist = rootFileNom.Get("jec3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_jec3.pdf",jec3sim_hist,jec3rawsim_hist,jec3nomsim_hist,"#sigma [pb]","jec_{3}","jec_{3}")
#load muf Jet3
muf3sim_hist = rootFile.Get("muf3sim_hist")
muf3rawsim_hist = rootFileRaw.Get("muf3rawsim_hist")
muf3nomsim_hist = rootFileNom.Get("muf3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_muf3.pdf",muf3sim_hist,muf3rawsim_hist,muf3nomsim_hist,"#sigma [pb]","muf_{3}","muf_{3}")
#load nhf Jet3
nhf3sim_hist = rootFile.Get("nhf3sim_hist")
nhf3rawsim_hist = rootFileRaw.Get("nhf3rawsim_hist")
nhf3nomsim_hist = rootFileNom.Get("nhf3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nhf3.pdf",nhf3sim_hist,nhf3rawsim_hist,nhf3nomsim_hist,"#sigma [pb]","nhf_{3}","nhf_{3}")
#load chf Jet3
chf3sim_hist = rootFile.Get("chf3sim_hist")
chf3rawsim_hist = rootFileRaw.Get("chf3rawsim_hist")
chf3nomsim_hist = rootFileNom.Get("chf3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_chf3.pdf",chf3sim_hist,chf3rawsim_hist,chf3nomsim_hist,"#sigma [pb]","chf_{3}","chf_{3}")
#load area Jet3
area3sim_hist = rootFile.Get("area3sim_hist")
area3rawsim_hist = rootFileRaw.Get("area3rawsim_hist")
area3nomsim_hist = rootFileNom.Get("area3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_area3.pdf",area3sim_hist,area3rawsim_hist,area3nomsim_hist,"#sigma [pb]","area_{3}","area_{3}")
#load nemf Jet3
nemf3sim_hist = rootFile.Get("nemf3sim_hist")
nemf3rawsim_hist = rootFileRaw.Get("nemf3rawsim_hist")
nemf3nomsim_hist = rootFileNom.Get("nemf3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nemf3.pdf",nemf3sim_hist,nemf3rawsim_hist,nemf3nomsim_hist,"#sigma [pb]","nemf_{3}","nemf_{3}")
#load cemf Jet3
cemf3sim_hist = rootFile.Get("cemf3sim_hist")
cemf3rawsim_hist = rootFileRaw.Get("cemf3rawsim_hist")
cemf3nomsim_hist = rootFileNom.Get("cemf3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_cemf3.pdf",cemf3sim_hist,cemf3rawsim_hist,cemf3nomsim_hist,"#sigma [pb]","cemf_{3}","cemf_{3}")
#load btagDeepFlavB Jet3
btagDeepFlavB3sim_hist = rootFile.Get("btagDeepFlavB3sim_hist")
btagDeepFlavB3rawsim_hist = rootFileRaw.Get("btagDeepFlavB3rawsim_hist")
btagDeepFlavB3nomsim_hist = rootFileNom.Get("btagDeepFlavB3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_btagDeepFlavB3.pdf",btagDeepFlavB3sim_hist,btagDeepFlavB3rawsim_hist,btagDeepFlavB3nomsim_hist,"#sigma [pb]","btagDeepFlavB_{3}","btagDeepFlavB_{3}")
#load nConstituents Jet3
nConstituents3sim_hist = rootFile.Get("nConstituents3sim_hist")
nConstituents3rawsim_hist = rootFileRaw.Get("nConstituents3rawsim_hist")
nConstituents3nomsim_hist = rootFileNom.Get("nConstituents3nomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_nConstituents3.pdf",nConstituents3sim_hist,nConstituents3rawsim_hist,nConstituents3nomsim_hist,"#sigma [pb]","nConstituents_{3}","nConstituents_{3}")

#load Mjj
mjjsim_hist = rootFile.Get("mjjsim_hist")
mjjrawsim_hist = rootFileRaw.Get("mjjrawsim_hist")
mjjnomsim_hist = rootFileNom.Get("mjjnomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_Mjj.pdf",mjjsim_hist,mjjrawsim_hist,mjjnomsim_hist,"#sigma [pb]","M_{jj}","M_{jj}")

#load yboost
yboostsim_hist = rootFile.Get("yboostsim_hist")
yboostrawsim_hist = rootFileRaw.Get("yboostrawsim_hist")
yboostnomsim_hist = rootFileNom.Get("yboostnomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_yboost.pdf",yboostsim_hist,yboostrawsim_hist,yboostnomsim_hist,"#sigma [pb]","Y_{boost}","Y_{boost}")

#load chi
chisim_hist = rootFile.Get("chisim_hist")
chirawsim_hist = rootFileRaw.Get("chirawsim_hist")
chinomsim_hist = rootFileNom.Get("chinomsim_hist")
RootHisttoPdf(outDirectory+"_CompareDifferentJecs_chi.pdf",chisim_hist,chirawsim_hist,chinomsim_hist,"#sigma [pb]","#chi_{dijet}","#chi_{dijet}")
