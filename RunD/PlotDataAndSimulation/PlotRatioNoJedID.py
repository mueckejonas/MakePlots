import ROOT
import numpy as np

#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,simulation,logyScale,yAxisTitle,xAxisTitle,title,undertitle):
    canvas_pads = ROOT.TCanvas("canvas_pads", "Double ratio")
    canvas_pads.SetCanvasSize(1600,1100)
    pad_top = ROOT.TPad("top_pad", "Top pad", 0, 0.3, 1, 1)
    if logyScale:
        pad_top.SetLogy(True)
    pad_top.SetBottomMargin(0)
    pad_top.Draw()
    pad_bottom = ROOT.TPad("bottom_pad", "Bottom pad", 0, 0.05, 1, 0.3)
    pad_bottom.SetBottomMargin(0.4)
    pad_bottom.SetTopMargin(0)
    pad_bottom.Draw()

    data.Scale(1./1206)

    datagraph = ROOT.TGraphAsymmErrors(data)
    for i in range(0,int(data.GetNbinsX())):
	    datagraph.SetPointEXhigh(i,0.0)
	    datagraph.SetPointEXlow(i,0.0)

    legend = ROOT.TLegend(0.6,0.7,0.85,0.85)
    legend.SetLineWidth(0)
    legend.AddEntry(datagraph,"Data","p")
    legend.AddEntry(simulation,"Simulation")

    line = ROOT.TLine(datagraph.GetXaxis().GetXmin(),1,datagraph.GetXaxis().GetXmax(),1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)

    #create and draw to upper plot
    pad_top.cd()
    datagraph.SetStats(0)
    datagraph.SetLineColor(ROOT.kBlack)
    datagraph.SetLineWidth(2)
    datagraph.SetMarkerColor(ROOT.kBlack)
    datagraph.SetMarkerStyle(4)
    simulation.SetStats(0)
    simulation.SetLineColor(ROOT.kRed)
    simulation.SetLineWidth(2)
    simulation.SetTitle(title+undertitle)
    simulation.GetYaxis().SetTitle(yAxisTitle)
    simulation.GetXaxis().SetTitleSize(0)
    simulation.GetXaxis().SetLabelSize(0)
    datagraph.SetTitle("")
    #simulation.Scale(data.Integral()/simulation.Integral())
    #Set font size
    legend.SetTextSize(0.06)
    datagraph.SetMarkerSize(3)
    datagraph.SetLineWidth(2)
    simulation.GetYaxis().SetLabelSize(0.06)
    simulation.GetYaxis().SetTitleSize(0.08)
    simulation.GetYaxis().SetTitleOffset(0.5)
    #data1graph.GetYaxis().SetLabelOffset(0.01)
    #data1graph.GetXaxis().SetLabelOffset(0.01)
    canvas_pads.SetBottomMargin(0.3)
    canvas_pads.SetTopMargin(0.1)
    canvas_pads.SetRightMargin(0.05)
    canvas_pads.SetLeftMargin(0.3)
    simulation.Draw("h")
    datagraph.Draw("P same")
    legend.Draw("same")
    #create and draw to bottom plot
    pad_bottom.cd()
    ratioDataSim = data.Clone()
    ratioDataSim.Divide(simulation)
    ratioDataSimgraph = ROOT.TGraphAsymmErrors(ratioDataSim)
    for i in range(0,int(data.GetNbinsX())):
	    ratioDataSimgraph.SetPointEXhigh(i,0.0)
	    ratioDataSimgraph.SetPointEXlow(i,0.0)
    ratioDataSimgraph.SetLineColor(ROOT.kBlack)
    ratioDataSimgraph.SetLineWidth(2)
    ratioDataSimgraph.SetTitle("")
    ratioDataSimgraph.GetYaxis().SetTitle("Data/Simulation")
    ratioDataSimgraph.GetYaxis().SetTitleOffset(0.3)
    ratioDataSimgraph.GetYaxis().SetNdivisions (207)
    ratioDataSimgraph.GetXaxis().SetTitle(xAxisTitle)
    ratioDataSimgraph.GetYaxis().SetRangeUser(0.5,1.5)
    ratioDataSimgraph.SetLineColor(ROOT.kRed)
    ratioDataSimgraph.GetYaxis().SetLabelSize(0.14)
    ratioDataSimgraph.GetYaxis().SetTitleSize(0.16)
    ratioDataSimgraph.GetXaxis().SetLabelSize(0.14)
    ratioDataSimgraph.GetXaxis().SetTitleSize(0.16)
    ratioDataSimgraph.SetMarkerSize(5)
    ratioDataSimgraph.SetLineWidth(2)
    ratioDataSimgraph.Draw("AP")
    line.Draw("same")
    #draw whole plot
    canvas_pads.Draw()
    canvas_pads.Print(outFileName)



#define directories
InDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/RootD/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/RunD/Pdf/"
dataInFileName = InDirectory+"PlotDijetSelection_Run2023D.root"
simInFileName = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_PlotSimulation_WithScale_Run32023_MC.root"
pdfnames = "PlotData(NoJedID)AndSimulation(JedID)_RunD32023_"

#Get data Jets and Kinematics
dataHistFile = ROOT.TFile.Open(dataInFileName,"READ")
dataJet1 = dataHistFile.Get("Jet1")
dataJet2 = dataHistFile.Get("Jet2")
dataJet3 = dataHistFile.Get("Jet3")
dataKinematics = dataHistFile.Get("Kinematics")

#Get Sim Jets and Kinematics
simHistFile = ROOT.TFile.Open(simInFileName,"READ")
simJet1 = simHistFile.Get("Jet1")
simJet2 = simHistFile.Get("Jet2")
simJet3 = simHistFile.Get("Jet3")
simKinematics = simHistFile.Get("Kinematics")

#define variables to compare and plot as array
JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create data and simulation ratio plots pdfs
for i in range(0,14):
    #get data
    data1 = dataJet1.Get("data_"+JetNameArray[i]+"1")
    data2 = dataJet2.Get("data_"+JetNameArray[i]+"2")
    data3 = dataJet3.Get("data_"+JetNameArray[i]+"3")

    #get simulation
    sim1 = simJet1.Get(JetNameArray[i]+"1sim_hist")
    sim2 = simJet2.Get(JetNameArray[i]+"2sim_hist")
    sim3 = simJet3.Get(JetNameArray[i]+"3sim_hist")

    #create and save pdf files
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"1.pdf",data1,sim1,True,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet1")
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"2.pdf",data2,sim2,True,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet2")
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"3.pdf",data3,sim3,True,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet3")
    else:
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"1.pdf",data1,sim1,False,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet1")
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"2.pdf",data2,sim2,False,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet2")
        RootHisttoPdf(outDirectory+pdfnames+JetNameArray[i]+"3.pdf",data3,sim3,False,"#sigma [pb]",XaxisArray[i],"Run3 D 2023",JetNameArray[i]+" Jet3")


#create yboost pdf
datayboost = dataKinematics.Get("data_yboost")
simyboost = simKinematics.Get("yboostsim_hist")
RootHisttoPdf(outDirectory+pdfnames+"yboostDataandSim.pdf",datayboost,simyboost,False,"#sigma [pb]","Yboost","Run3 D 2023","Yboost")
#create chi pdf
datachi = dataKinematics.Get("data_chi")
simchi = simKinematics.Get("chisim_hist")
RootHisttoPdf(outDirectory+pdfnames+"chiDataandSim.pdf",datachi,simchi,False,"#sigma [pb]","Chi","Run3 D 2023","Chi")
#create mjj pdf
datamjj = dataKinematics.Get("data_mjj")
simmjj = simKinematics.Get("mjjsim_hist")
RootHisttoPdf(outDirectory+pdfnames+"mjjDataandSim.pdf",datamjj,simmjj,True,"#sigma [pb]","Mjj [GeV]","Run3 D 2023","Mjj")
