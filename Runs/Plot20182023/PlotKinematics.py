import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,sim2018,sim2023,yAxisTitle,xAxisTitle,title,setlogy=False):
    canvas = ROOT.TCanvas("canvas")
    canvas.SetCanvasSize(1600,1100)
    if setlogy:
        canvas.SetLogy(True)
    canvas.cd()

    legend = ROOT.TLegend(0.4,0.7,0.65,0.85)
    legend.SetFillStyle(4000)
    legend.SetLineWidth(0)
    legend.AddEntry(sim2018,title+" Run2 MC 2018","l")
    legend.AddEntry(sim2023,title+" Run3 MC 2023","l")

    sim2018.SetStats(0)
    sim2018.SetLineColor(ROOT.kBlack)
    sim2018.SetMarkerColor(ROOT.kBlack)
    sim2018.GetYaxis().SetTitle(yAxisTitle)
    sim2018.GetXaxis().SetTitle(xAxisTitle)
    sim2018.SetTitle("")
    sim2018.SetLineWidth(2)

    sim2023.SetStats(0)
    sim2023.SetLineColor(ROOT.kRed)
    sim2023.SetMarkerColor(ROOT.kRed)
    sim2023.SetLineWidth(2)
    sim2023.SetTitle("")

    #Set font size
    legend.SetTextSize(0.06)
    sim2018.GetYaxis().SetLabelSize(0.05)
    sim2018.GetYaxis().SetTitleSize(0.06)
    sim2018.GetXaxis().SetLabelSize(0.05)
    sim2018.GetXaxis().SetTitleSize(0.06)
    sim2018.GetXaxis().SetNdivisions (207)
    sim2018.GetYaxis().SetLabelOffset(0.01)
    sim2018.GetXaxis().SetLabelOffset(0.01)
    canvas.SetBottomMargin(0.15)
    canvas.SetTopMargin(0.05)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.15)

    sim2018.Draw()
    sim2023.Draw("same")
    legend.Draw("same")

    canvas.Draw()
    canvas.Print(outFileName)


#define directories
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Runs/Pdf/"

#load MC 2023 Data
#define directory
inDirectory2023 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/"
rootFile2023 = ROOT.TFile.Open(inDirectory2023+"_PlotSimulation_WithScale_Run32023_MC.root","READ")

#load MC 2018 Data
#define directory
inDirectory2018 = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2018/RootS2018/"
rootFile2018 = ROOT.TFile.Open(inDirectory2018+"_PlotSimulation_WithScale_Run22018_MC.root","READ")



#create Jet1 pdfs
#load Jet1
Jet12018 = rootFile2018.Get("Jet1")
Jet12023 = rootFile2023.Get("Jet1")
#Plot pt Jet1 hist
ptJet12018 = Jet12018.Get("pt1sim_hist")
ptJet22023 = Jet12023.Get("pt1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_pt_Jet1_2018and2023.pdf",ptJet12018,ptJet22023,"#sigma [pb]","P_{t1} [GeV]","P_{t1}",True)
#Plot y Jet1 hist
yJet12018 = Jet12018.Get("y1sim_hist")
yJet22023 = Jet12023.Get("y1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_y_Jet1_2018and2023.pdf",yJet12018,yJet22023,"#sigma [pb]","Y_{1}","Y_{1}")
#Plot eta Jet1 hist
etaJet12018 = Jet12018.Get("eta1sim_hist")
etaJet22023 = Jet12023.Get("eta1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_eta_Jet1_2018and2023.pdf",etaJet12018,etaJet22023,"#sigma [pb]","#eta_{1}","#eta_{1}")
#Plot phi Jet1 hist
phiJet12018 = Jet12018.Get("phi1sim_hist")
phiJet22023 = Jet12023.Get("phi1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_phi_Jet1_2018and2023.pdf",phiJet12018,phiJet22023,"#sigma [pb]","#phi_{1}","#phi_{1}")
#Plot mass Jet1 hist
massJet12018 = Jet12018.Get("mass1sim_hist")
massJet22023 = Jet12023.Get("mass1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_mass_Jet1_2018and2023.pdf",massJet12018,massJet22023,"#sigma [pb]","mass_{1} [GeV]","mass_{1}")
#Plot jec Jet1 hist
jecJet12018 = Jet12018.Get("jec1sim_hist")
jecJet22023 = Jet12023.Get("jec1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_jec_Jet1_2018and2023.pdf",jecJet12018,jecJet22023,"#sigma [pb]","jec_{1}","jec_{1}")
#Plot muf Jet1 hist
mufJet12018 = Jet12018.Get("muf1sim_hist")
mufJet22023 = Jet12023.Get("muf1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_muf_Jet1_2018and2023.pdf",mufJet12018,mufJet22023,"#sigma [pb]","muf_{1}","muf_{1}")
#Plot nhf Jet1 hist
nhfJet12018 = Jet12018.Get("nhf1sim_hist")
nhfJet22023 = Jet12023.Get("nhf1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nhf_Jet1_2018and2023.pdf",nhfJet12018,nhfJet22023,"#sigma [pb]","nhf_{1}","nhf_{1}")
#Plot chf Jet1 hist
chfJet12018 = Jet12018.Get("chf1sim_hist")
chfJet22023 = Jet12023.Get("chf1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_chf_Jet1_2018and2023.pdf",chfJet12018,chfJet22023,"#sigma [pb]","chf_{1}","chf_{1}")
#Plot nemf Jet1 hist
nemfJet12018 = Jet12018.Get("nemf1sim_hist")
nemfJet22023 = Jet12023.Get("nemf1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nemf_Jet1_2018and2023.pdf",nemfJet12018,nemfJet22023,"#sigma [pb]","nemf_{1}","nemf_{1}")
#Plot cemf Jet1 hist
cemfJet12018 = Jet12018.Get("cemf1sim_hist")
cemfJet22023 = Jet12023.Get("cemf1sim_hist")
RootHisttoPdf(outDirectory+"_Plot_cemf_Jet1_2018and2023.pdf",cemfJet12018,cemfJet22023,"#sigma [pb]","cemf_{1}","cemf_{1}")

#create Jet2 pdfs
#load Jet2
Jet22018 = rootFile2018.Get("Jet2")
Jet22023 = rootFile2023.Get("Jet2")
#Plot pt Jet2 hist
ptJet22018 = Jet22018.Get("pt2sim_hist")
ptJet22023 = Jet22023.Get("pt2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_pt_Jet2_2018and2023.pdf",ptJet22018,ptJet22023,"#sigma [pb]","P_{t2} [GeV]","P_{t2}",True)
#Plot y Jet2 hist
yJet22018 = Jet22018.Get("y2sim_hist")
yJet22023 = Jet22023.Get("y2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_y_Jet2_2018and2023.pdf",yJet22018,yJet22023,"#sigma [pb]","Y_{2}","Y_{2}")
#Plot eta Jet2 hist
etaJet22018 = Jet22018.Get("eta2sim_hist")
etaJet22023 = Jet22023.Get("eta2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_eta_Jet2_2018and2023.pdf",etaJet22018,etaJet22023,"#sigma [pb]","#eta_{2}","#eta_{2}")
#Plot phi Jet2 hist
phiJet22018 = Jet22018.Get("phi2sim_hist")
phiJet22023 = Jet22023.Get("phi2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_phi_Jet2_2018and2023.pdf",phiJet22018,phiJet22023,"#sigma [pb]","#phi_{2}","#phi_{2}")
#Plot mass Jet2 hist
massJet22018 = Jet22018.Get("mass2sim_hist")
massJet22023 = Jet22023.Get("mass2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_mass_Jet2_2018and2023.pdf",massJet22018,massJet22023,"#sigma [pb]","mass_{2} [GeV]","mass_{2}")
#Plot jec Jet2 hist
jecJet22018 = Jet22018.Get("jec2sim_hist")
jecJet22023 = Jet22023.Get("jec2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_jec_Jet2_2018and2023.pdf",jecJet22018,jecJet22023,"#sigma [pb]","jec_{2}","jec_{2}")
#Plot muf Jet2 hist
mufJet22018 = Jet22018.Get("muf2sim_hist")
mufJet22023 = Jet22023.Get("muf2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_muf_Jet2_2018and2023.pdf",mufJet22018,mufJet22023,"#sigma [pb]","muf_{2}","muf_{2}")
#Plot nhf Jet2 hist
nhfJet22018 = Jet22018.Get("nhf2sim_hist")
nhfJet22023 = Jet22023.Get("nhf2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nhf_Jet2_2018and2023.pdf",nhfJet22018,nhfJet22023,"#sigma [pb]","nhf_{2}","nhf_{2}")
#Plot chf Jet2 hist
chfJet22018 = Jet22018.Get("chf2sim_hist")
chfJet22023 = Jet22023.Get("chf2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_chf_Jet2_2018and2023.pdf",chfJet22018,chfJet22023,"#sigma [pb]","chf_{2}","chf_{2}")
#Plot nemf Jet2 hist
nemfJet22018 = Jet22018.Get("nemf2sim_hist")
nemfJet22023 = Jet22023.Get("nemf2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nemf_Jet2_2018and2023.pdf",nemfJet22018,nemfJet22023,"#sigma [pb]","nemf_{2}","nemf_{2}")
#Plot cemf Jet2 hist
cemfJet22018 = Jet22018.Get("cemf2sim_hist")
cemfJet22023 = Jet22023.Get("cemf2sim_hist")
RootHisttoPdf(outDirectory+"_Plot_cemf_Jet2_2018and2023.pdf",cemfJet22018,cemfJet22023,"#sigma [pb]","cemf_{2}","cemf_{2}")

#create Jet3 pdfs
#load Jet3
Jet32018 = rootFile2018.Get("Jet3")
Jet32023 = rootFile2023.Get("Jet3")
#Plot pt Jet3 hist
ptJet32018 = Jet32018.Get("pt3sim_hist")
ptJet32023 = Jet32023.Get("pt3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_pt_Jet3_2018and2023.pdf",ptJet32018,ptJet32023,"#sigma [pb]","P_{t3} [GeV]","P_{t3}",True)
#Plot y Jet3 hist
yJet32018 = Jet32018.Get("y3sim_hist")
yJet32023 = Jet32023.Get("y3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_y_Jet3_2018and2023.pdf",yJet32018,yJet32023,"#sigma [pb]","Y_{3}","Y_{3}")
#Plot eta Jet3 hist
etaJet32018 = Jet32018.Get("eta3sim_hist")
etaJet32023 = Jet32023.Get("eta3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_eta_Jet3_2018and2023.pdf",etaJet32018,etaJet32023,"#sigma [pb]","#eta_{3}","#eta_{3}")
#Plot phi Jet3 hist
phiJet32018 = Jet32018.Get("phi3sim_hist")
phiJet32023 = Jet32023.Get("phi3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_phi_Jet3_2018and2023.pdf",phiJet32018,phiJet32023,"#sigma [pb]","#phi_{3}","#phi_{3}")
#Plot mass Jet3 hist
massJet32018 = Jet32018.Get("mass3sim_hist")
massJet32023 = Jet32023.Get("mass3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_mass_Jet3_2018and2023.pdf",massJet32018,massJet32023,"#sigma [pb]","mass_{3} [GeV]","mass_{3}")
#Plot jec Jet3 hist
jecJet32018 = Jet32018.Get("jec3sim_hist")
jecJet32023 = Jet32023.Get("jec3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_jec_Jet3_2018and2023.pdf",jecJet32018,jecJet32023,"#sigma [pb]","jec_{3}","jec_{3}")
#Plot muf Jet3 hist
mufJet32018 = Jet32018.Get("muf3sim_hist")
mufJet32023 = Jet32023.Get("muf3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_muf_Jet3_2018and2023.pdf",mufJet32018,mufJet32023,"#sigma [pb]","muf_{3}","muf_{3}")
#Plot nhf Jet3 hist
nhfJet32018 = Jet32018.Get("nhf3sim_hist")
nhfJet32023 = Jet32023.Get("nhf3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nhf_Jet3_2018and2023.pdf",nhfJet32018,nhfJet32023,"#sigma [pb]","nhf_{3}","nhf_{3}")
#Plot chf Jet3 hist
chfJet32018 = Jet32018.Get("chf3sim_hist")
chfJet32023 = Jet32023.Get("chf3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_chf_Jet3_2018and2023.pdf",chfJet32018,chfJet32023,"#sigma [pb]","chf_{3}","chf_{3}")
#Plot nemf Jet3 hist
nemfJet32018 = Jet32018.Get("nemf3sim_hist")
nemfJet32023 = Jet32023.Get("nemf3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_nemf_Jet3_2018and2023.pdf",nemfJet32018,nemfJet32023,"#sigma [pb]","nemf_{3}","nemf_{3}")
#Plot cemf Jet3 hist
cemfJet32018 = Jet32018.Get("cemf3sim_hist")
cemfJet32023 = Jet32023.Get("cemf3sim_hist")
RootHisttoPdf(outDirectory+"_Plot_cemf_Jet3_2018and2023.pdf",cemfJet32018,cemfJet32023,"#sigma [pb]","cemf_{3}","cemf_{3}")

#Plot Kinematics
#load kinematics
Kinematics2018 = rootFile2018.Get("Kinematics")
Kinematics2023 = rootFile2023.Get("Kinematics")
#Plot Mjj hist
mjjJet32018 = Kinematics2018.Get("mjjsim_hist")
mjjJet22023 = Kinematics2023.Get("mjjsim_hist")
RootHisttoPdf(outDirectory+"_Plot_mjj_2018and2023.pdf",mjjJet32018,mjjJet22023,"#sigma [pb]","M_{jj} [GeV]","M_{jj}")
#Plot chi hist
chiJet32018 = Kinematics2018.Get("chisim_hist")
chiJet22023 = Kinematics2023.Get("chisim_hist")
RootHisttoPdf(outDirectory+"_Plot_chi_2018and2023.pdf",chiJet32018,chiJet22023,"#sigma [pb]","#chi_{dijet}","#chi_{dijet}")
#Plot yboost hist
yboostJet32018 = Kinematics2018.Get("yboostsim_hist")
yboostJet22023 = Kinematics2023.Get("yboostsim_hist")
RootHisttoPdf(outDirectory+"_Plot_yboost_2018and2023.pdf",yboostJet32018,yboostJet22023,"#sigma [pb]","Y_{boost}","Y_{boost}")
