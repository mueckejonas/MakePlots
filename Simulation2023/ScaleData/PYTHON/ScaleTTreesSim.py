import ROOT
import numpy as np

inDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"
outDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/Pdf/"
outRootDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim2023/RootS2023/"
pdfnames = "PlotSimulation_Run32023-15Jan2023_MC_All_"

#load tree data

root50to80 = ROOT.TFile.Open(inDirectory+"50to80_PlotSimulation_Run32023-15Jan2023_MC.root")
scale50to80 = ((1.679e+07)/(11988000))
print(scale50to80)
root80to120 = ROOT.TFile.Open(inDirectory+"80to120_PlotSimulation_Run32023-15Jan2023_MC.root")
scale80to120 = ((2.513e+06)/(17979000))
print(scale80to120)
root120to170 = ROOT.TFile.Open(inDirectory+"120to170_PlotSimulation_Run32023-15Jan2023_MC.root")
scale120to170 = ((4.574e+05)/(17964000))
print(scale120to170)
root170to300 = ROOT.TFile.Open(inDirectory+"170to300_PlotSimulation_Run32023-15Jan2023_MC.root")
scale170to300 = ((1.162e+05)/(17889000))
print(scale170to300)
root300to470 = ROOT.TFile.Open(inDirectory+"300to470_PlotSimulation_Run32023-15Jan2023_MC.root")
scale300to470 = ((7.584e+03)/(34626000))
print(scale300to470)
root470to600 = ROOT.TFile.Open(inDirectory+"470to600_PlotSimulation_Run32023-15Jan2023_MC.root")
scale470to600 = ((6.490e+02)/(16766000))
print(scale470to600)
root600to800 = ROOT.TFile.Open(inDirectory+"600to800_PlotSimulation_Run32023-15Jan2023_MC.root")
scale600to800 = ((1.809e+02)/(40468000))
print(scale600to800)
root800to1000 = ROOT.TFile.Open(inDirectory+"800to1000_PlotSimulation_Run32023-15Jan2023_MC.root")
scale800to1000 = ((3.105e+01)/(23908000))
print(scale800to1000)
root1000to1400 = ROOT.TFile.Open(inDirectory+"1000to1400_PlotSimulation_Run32023-15Jan2023_MC.root")
scale1000to1400 = ((8.829e+00)/(11956000))
print(scale1000to1400)
root1400to1800 = ROOT.TFile.Open(inDirectory+"1400to1800_PlotSimulation_Run32023-15Jan2023_MC.root")
scale1400to1800 = ((7.952e-01)/(3596000))
print(scale1400to1800)
root1800to2400 = ROOT.TFile.Open(inDirectory+"1800to2400_PlotSimulation_Run32023-15Jan2023_MC.root")
scale1800to2400 = ((1.147e-01)/(1792000))
print(scale1800to2400)
root2400to3200 = ROOT.TFile.Open(inDirectory+"2400to3200_PlotSimulation_Run32023-15Jan2023_MC.root")
scale2400to3200 = ((7.619e-03)/(1200000))
print(scale2400to3200)
root3200 = ROOT.TFile.Open(inDirectory+"3200_PlotSimulation_Run32023-15Jan2023_MC.root")
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
pt1_50to80 = root50to80.Get("Simpt1")
pt1_50to80.Scale(scale50to80)
pt1raw_50to80 = root50to80.Get("Simpt1raw")
pt1raw_50to80.Scale(scale50to80)
pt1nom_50to80 = root50to80.Get("Simpt1nom")
pt1nom_50to80.Scale(scale50to80)
#load and sclae jet2 data
pt2_50to80 = root50to80.Get("Simpt2")
pt2_50to80.Scale(scale50to80)
pt2raw_50to80 = root50to80.Get("Simpt2raw")
pt2raw_50to80.Scale(scale50to80)
pt2nom_50to80 = root50to80.Get("Simpt2nom")
pt2nom_50to80.Scale(scale50to80)
#load and sclae jet3 data
pt3_50to80 = root50to80.Get("Simpt3")
pt3_50to80.Scale(scale50to80)
pt3raw_50to80 = root50to80.Get("Simpt3raw")
pt3raw_50to80.Scale(scale50to80)
pt3nom_50to80 = root50to80.Get("Simpt3nom")
pt3nom_50to80.Scale(scale50to80)
#load and scale jet kinematics
mjj_50to80 = root50to80.Get("Simmjj")
mjj_50to80.Scale(scale50to80)
mjjraw_50to80 = root50to80.Get("Simmjjraw")
mjjraw_50to80.Scale(scale50to80)
mjjnom_50to80 = root50to80.Get("Simmjjnom")
mjjnom_50to80.Scale(scale50to80)

#load and scale 80to120 Simulation
#load and scale jet1 data
pt1_80to120 = root80to120.Get("Simpt1")
pt1_80to120.Scale(scale80to120)
pt1raw_80to120 = root80to120.Get("Simpt1raw")
pt1raw_80to120.Scale(scale80to120)
pt1nom_80to120 = root80to120.Get("Simpt1nom")
pt1nom_80to120.Scale(scale80to120)
#load and sclae jet2 data
pt2_80to120 = root80to120.Get("Simpt2")
pt2_80to120.Scale(scale80to120)
pt2raw_80to120 = root80to120.Get("Simpt2raw")
pt2raw_80to120.Scale(scale80to120)
pt2nom_80to120 = root80to120.Get("Simpt2nom")
pt2nom_80to120.Scale(scale80to120)
#load and sclae jet3 data
pt3_80to120 = root80to120.Get("Simpt3")
pt3_80to120.Scale(scale80to120)
pt3raw_80to120 = root80to120.Get("Simpt3raw")
pt3raw_80to120.Scale(scale80to120)
pt3nom_80to120 = root80to120.Get("Simpt3nom")
pt3nom_80to120.Scale(scale80to120)
#load and scale jet kinematics
mjj_80to120 = root80to120.Get("Simmjj")
mjj_80to120.Scale(scale80to120)
mjjraw_80to120 = root80to120.Get("Simmjjraw")
mjjraw_80to120.Scale(scale80to120)
mjjnom_80to120 = root80to120.Get("Simmjjnom")
mjjnom_80to120.Scale(scale80to120)

#load and scale 120to170 Simulation
#load and scale jet1 data
pt1_120to170 = root120to170.Get("Simpt1")
pt1_120to170.Scale(scale120to170)
pt1raw_120to170 = root120to170.Get("Simpt1raw")
pt1raw_120to170.Scale(scale120to170)
pt1nom_120to170 = root120to170.Get("Simpt1nom")
pt1nom_120to170.Scale(scale120to170)
#load and sclae jet2 data
pt2_120to170 = root120to170.Get("Simpt2")
pt2_120to170.Scale(scale120to170)
pt2raw_120to170 = root120to170.Get("Simpt2raw")
pt2raw_120to170.Scale(scale120to170)
pt2nom_120to170 = root120to170.Get("Simpt2nom")
pt2nom_120to170.Scale(scale120to170)
#load and sclae jet3 data
pt3_120to170 = root120to170.Get("Simpt3")
pt3_120to170.Scale(scale120to170)
pt3raw_120to170 = root120to170.Get("Simpt3raw")
pt3raw_120to170.Scale(scale120to170)
pt3nom_120to170 = root120to170.Get("Simpt3nom")
pt3nom_120to170.Scale(scale120to170)
#load and scale jet kinematics
mjj_120to170 = root120to170.Get("Simmjj")
mjj_120to170.Scale(scale120to170)
mjjraw_120to170 = root120to170.Get("Simmjjraw")
mjjraw_120to170.Scale(scale120to170)
mjjnom_120to170 = root120to170.Get("Simmjjnom")
mjjnom_120to170.Scale(scale120to170)

#load and scale 170to300 Simulation
#load and scale jet1 data
pt1_170to300 = root170to300.Get("Simpt1")
pt1_170to300.Scale(scale170to300)
pt1raw_170to300 = root170to300.Get("Simpt1raw")
pt1raw_170to300.Scale(scale170to300)
pt1nom_170to300 = root170to300.Get("Simpt1nom")
pt1nom_170to300.Scale(scale170to300)
#load and sclae jet2 data
pt2_170to300 = root170to300.Get("Simpt2")
pt2_170to300.Scale(scale170to300)
pt2raw_170to300 = root170to300.Get("Simpt2raw")
pt2raw_170to300.Scale(scale170to300)
pt2nom_170to300 = root170to300.Get("Simpt2nom")
pt2nom_170to300.Scale(scale170to300)
#load and sclae jet3 data
pt3_170to300 = root170to300.Get("Simpt3")
pt3_170to300.Scale(scale170to300)
pt3raw_170to300 = root170to300.Get("Simpt3raw")
pt3raw_170to300.Scale(scale170to300)
pt3nom_170to300 = root170to300.Get("Simpt3nom")
pt3nom_170to300.Scale(scale170to300)
#load and scale jet kinematics
mjj_170to300 = root170to300.Get("Simmjj")
mjj_170to300.Scale(scale170to300)
mjjraw_170to300 = root170to300.Get("Simmjjraw")
mjjraw_170to300.Scale(scale170to300)
mjjnom_170to300 = root170to300.Get("Simmjjnom")
mjjnom_170to300.Scale(scale170to300)

#load and scale 300to470 Simulation
#load and scale jet1 data
pt1_300to470 = root300to470.Get("Simpt1")
pt1_300to470.Scale(scale300to470)
pt1raw_300to470 = root300to470.Get("Simpt1raw")
pt1raw_300to470.Scale(scale300to470)
pt1nom_300to470 = root300to470.Get("Simpt1nom")
pt1nom_300to470.Scale(scale300to470)
#load and sclae jet2 data
pt2_300to470 = root300to470.Get("Simpt2")
pt2_300to470.Scale(scale300to470)
pt2raw_300to470 = root300to470.Get("Simpt2raw")
pt2raw_300to470.Scale(scale300to470)
pt2nom_300to470 = root300to470.Get("Simpt2nom")
pt2nom_300to470.Scale(scale300to470)
#load and sclae jet3 data
pt3_300to470 = root300to470.Get("Simpt3")
pt3_300to470.Scale(scale300to470)
pt3raw_300to470 = root300to470.Get("Simpt3raw")
pt3raw_300to470.Scale(scale300to470)
pt3nom_300to470 = root300to470.Get("Simpt3nom")
pt3nom_300to470.Scale(scale300to470)
#load and scale jet kinematics
mjj_300to470 = root300to470.Get("Simmjj")
mjj_300to470.Scale(scale300to470)
mjjraw_300to470 = root300to470.Get("Simmjjraw")
mjjraw_300to470.Scale(scale300to470)
mjjnom_300to470 = root300to470.Get("Simmjjnom")
mjjnom_300to470.Scale(scale300to470)

#load and scale 470to600 Simulation
#load and scale jet1 data
pt1_470to600 = root470to600.Get("Simpt1")
pt1_470to600.Scale(scale470to600)
pt1raw_470to600 = root470to600.Get("Simpt1raw")
pt1raw_470to600.Scale(scale470to600)
pt1nom_470to600 = root470to600.Get("Simpt1nom")
pt1nom_470to600.Scale(scale470to600)
#load and sclae jet2 data
pt2_470to600 = root470to600.Get("Simpt2")
pt2_470to600.Scale(scale470to600)
pt2raw_470to600 = root470to600.Get("Simpt2raw")
pt2raw_470to600.Scale(scale470to600)
pt2nom_470to600 = root470to600.Get("Simpt2nom")
pt2nom_470to600.Scale(scale470to600)
#load and sclae jet3 data
pt3_470to600 = root470to600.Get("Simpt3")
pt3_470to600.Scale(scale470to600)
pt3raw_470to600 = root470to600.Get("Simpt3raw")
pt3raw_470to600.Scale(scale470to600)
pt3nom_470to600 = root470to600.Get("Simpt3nom")
pt3nom_470to600.Scale(scale470to600)
#load and scale jet kinematics
mjj_470to600 = root470to600.Get("Simmjj")
mjj_470to600.Scale(scale470to600)
mjjraw_470to600 = root470to600.Get("Simmjjraw")
mjjraw_470to600.Scale(scale470to600)
mjjnom_470to600 = root470to600.Get("Simmjjnom")
mjjnom_470to600.Scale(scale470to600)

#load and scale 600to800 Simulation
#load and scale jet1 data
pt1_600to800 = root600to800.Get("Simpt1")
pt1_600to800.Scale(scale600to800)
pt1raw_600to800 = root600to800.Get("Simpt1raw")
pt1raw_600to800.Scale(scale600to800)
pt1nom_600to800 = root600to800.Get("Simpt1nom")
pt1nom_600to800.Scale(scale600to800)
#load and sclae jet2 data
pt2_600to800 = root600to800.Get("Simpt2")
pt2_600to800.Scale(scale600to800)
pt2raw_600to800 = root600to800.Get("Simpt2raw")
pt2raw_600to800.Scale(scale600to800)
pt2nom_600to800 = root600to800.Get("Simpt2nom")
pt2nom_600to800.Scale(scale600to800)
#load and sclae jet3 data
pt3_600to800 = root600to800.Get("Simpt3")
pt3_600to800.Scale(scale600to800)
pt3raw_600to800 = root600to800.Get("Simpt3raw")
pt3raw_600to800.Scale(scale600to800)
pt3nom_600to800 = root600to800.Get("Simpt3nom")
pt3nom_600to800.Scale(scale600to800)
#load and scale jet kinematics
mjj_600to800 = root600to800.Get("Simmjj")
mjj_600to800.Scale(scale600to800)
mjjraw_600to800 = root600to800.Get("Simmjjraw")
mjjraw_600to800.Scale(scale600to800)
mjjnom_600to800 = root600to800.Get("Simmjjnom")
mjjnom_600to800.Scale(scale600to800)

#load and scale 800to1000 Simulation
#load and scale jet1 data
pt1_800to1000 = root800to1000.Get("Simpt1")
pt1_800to1000.Scale(scale800to1000)
pt1raw_800to1000 = root800to1000.Get("Simpt1raw")
pt1raw_800to1000.Scale(scale800to1000)
pt1nom_800to1000 = root800to1000.Get("Simpt1nom")
pt1nom_800to1000.Scale(scale800to1000)
#load and sclae jet2 data
pt2_800to1000 = root800to1000.Get("Simpt2")
pt2_800to1000.Scale(scale800to1000)
pt2raw_800to1000 = root800to1000.Get("Simpt2raw")
pt2raw_800to1000.Scale(scale800to1000)
pt2nom_800to1000 = root800to1000.Get("Simpt2nom")
pt2nom_800to1000.Scale(scale800to1000)
#load and sclae jet3 data
pt3_800to1000 = root800to1000.Get("Simpt3")
pt3_800to1000.Scale(scale800to1000)
pt3raw_800to1000 = root800to1000.Get("Simpt3raw")
pt3raw_800to1000.Scale(scale800to1000)
pt3nom_800to1000 = root800to1000.Get("Simpt3nom")
pt3nom_800to1000.Scale(scale800to1000)
#load and scale jet kinematics
mjj_800to1000 = root800to1000.Get("Simmjj")
mjj_800to1000.Scale(scale800to1000)
mjjraw_800to1000 = root800to1000.Get("Simmjjraw")
mjjraw_800to1000.Scale(scale800to1000)
mjjnom_800to1000 = root800to1000.Get("Simmjjnom")
mjjnom_800to1000.Scale(scale800to1000)

#load and scale 1000to1400 Simulation
#load and scale jet1 data
pt1_1000to1400 = root1000to1400.Get("Simpt1")
pt1_1000to1400.Scale(scale1000to1400)
pt1raw_1000to1400 = root1000to1400.Get("Simpt1raw")
pt1raw_1000to1400.Scale(scale1000to1400)
pt1nom_1000to1400 = root1000to1400.Get("Simpt1nom")
pt1nom_1000to1400.Scale(scale1000to1400)
#load and sclae jet2 data
pt2_1000to1400 = root1000to1400.Get("Simpt2")
pt2_1000to1400.Scale(scale1000to1400)
pt2raw_1000to1400 = root1000to1400.Get("Simpt2raw")
pt2raw_1000to1400.Scale(scale1000to1400)
pt2nom_1000to1400 = root1000to1400.Get("Simpt2nom")
pt2nom_1000to1400.Scale(scale1000to1400)
#load and sclae jet3 data
pt3_1000to1400 = root1000to1400.Get("Simpt3")
pt3_1000to1400.Scale(scale1000to1400)
pt3raw_1000to1400 = root1000to1400.Get("Simpt3raw")
pt3raw_1000to1400.Scale(scale1000to1400)
pt3nom_1000to1400 = root1000to1400.Get("Simpt3nom")
pt3nom_1000to1400.Scale(scale1000to1400)
#load and scale jet kinematics
mjj_1000to1400 = root1000to1400.Get("Simmjj")
mjj_1000to1400.Scale(scale1000to1400)
mjjraw_1000to1400 = root1000to1400.Get("Simmjjraw")
mjjraw_1000to1400.Scale(scale1000to1400)
mjjnom_1000to1400 = root1000to1400.Get("Simmjjnom")
mjjnom_1000to1400.Scale(scale1000to1400)

#load and scale 1400to1800 Simulation
#load and scale jet1 data
pt1_1400to1800 = root1400to1800.Get("Simpt1")
pt1_1400to1800.Scale(scale1400to1800)
pt1raw_1400to1800 = root1400to1800.Get("Simpt1raw")
pt1raw_1400to1800.Scale(scale1400to1800)
pt1nom_1400to1800 = root1400to1800.Get("Simpt1nom")
pt1nom_1400to1800.Scale(scale1400to1800)
#load and sclae jet2 data
pt2_1400to1800 = root1400to1800.Get("Simpt2")
pt2_1400to1800.Scale(scale1400to1800)
pt2raw_1400to1800 = root1400to1800.Get("Simpt2raw")
pt2raw_1400to1800.Scale(scale1400to1800)
pt2nom_1400to1800 = root1400to1800.Get("Simpt2nom")
pt2nom_1400to1800.Scale(scale1400to1800)
#load and sclae jet3 data
pt3_1400to1800 = root1400to1800.Get("Simpt3")
pt3_1400to1800.Scale(scale1400to1800)
pt3raw_1400to1800 = root1400to1800.Get("Simpt3raw")
pt3raw_1400to1800.Scale(scale1400to1800)
pt3nom_1400to1800 = root1400to1800.Get("Simpt3nom")
pt3nom_1400to1800.Scale(scale1400to1800)
#load and scale jet kinematics
mjj_1400to1800 = root1400to1800.Get("Simmjj")
mjj_1400to1800.Scale(scale1400to1800)
mjjraw_1400to1800 = root1400to1800.Get("Simmjjraw")
mjjraw_1400to1800.Scale(scale1400to1800)
mjjnom_1400to1800 = root1400to1800.Get("Simmjjnom")
mjjnom_1400to1800.Scale(scale1400to1800)

#load and scale 1800to2400 Simulation
#load and scale jet1 data
pt1_1800to2400 = root1800to2400.Get("Simpt1")
pt1_1800to2400.Scale(scale1800to2400)
pt1raw_1800to2400 = root1800to2400.Get("Simpt1raw")
pt1raw_1800to2400.Scale(scale1800to2400)
pt1nom_1800to2400 = root1800to2400.Get("Simpt1nom")
pt1nom_1800to2400.Scale(scale1800to2400)
#load and sclae jet2 data
pt2_1800to2400 = root1800to2400.Get("Simpt2")
pt2_1800to2400.Scale(scale1800to2400)
pt2raw_1800to2400 = root1800to2400.Get("Simpt2raw")
pt2raw_1800to2400.Scale(scale1800to2400)
pt2nom_1800to2400 = root1800to2400.Get("Simpt2nom")
pt2nom_1800to2400.Scale(scale1800to2400)
#load and sclae jet3 data
pt3_1800to2400 = root1800to2400.Get("Simpt3")
pt3_1800to2400.Scale(scale1800to2400)
pt3raw_1800to2400 = root1800to2400.Get("Simpt3raw")
pt3raw_1800to2400.Scale(scale1800to2400)
pt3nom_1800to2400 = root1800to2400.Get("Simpt3nom")
pt3nom_1800to2400.Scale(scale1800to2400)
#load and scale jet kinematics
mjj_1800to2400 = root1800to2400.Get("Simmjj")
mjj_1800to2400.Scale(scale1800to2400)
mjjraw_1800to2400 = root1800to2400.Get("Simmjjraw")
mjjraw_1800to2400.Scale(scale1800to2400)
mjjnom_1800to2400 = root1800to2400.Get("Simmjjnom")
mjjnom_1800to2400.Scale(scale1800to2400)

#load and scale 2400to3200 Simulation
#load and scale jet1 data
pt1_2400to3200 = root2400to3200.Get("Simpt1")
pt1_2400to3200.Scale(scale2400to3200)
pt1raw_2400to3200 = root2400to3200.Get("Simpt1raw")
pt1raw_2400to3200.Scale(scale2400to3200)
pt1nom_2400to3200 = root2400to3200.Get("Simpt1nom")
pt1nom_2400to3200.Scale(scale2400to3200)
#load and sclae jet2 data
pt2_2400to3200 = root2400to3200.Get("Simpt2")
pt2_2400to3200.Scale(scale2400to3200)
pt2raw_2400to3200 = root2400to3200.Get("Simpt2raw")
pt2raw_2400to3200.Scale(scale2400to3200)
pt2nom_2400to3200 = root2400to3200.Get("Simpt2nom")
pt2nom_2400to3200.Scale(scale2400to3200)
#load and sclae jet3 data
pt3_2400to3200 = root2400to3200.Get("Simpt3")
pt3_2400to3200.Scale(scale2400to3200)
pt3raw_2400to3200 = root2400to3200.Get("Simpt3raw")
pt3raw_2400to3200.Scale(scale2400to3200)
pt3nom_2400to3200 = root2400to3200.Get("Simpt3nom")
pt3nom_2400to3200.Scale(scale2400to3200)
#load and scale jet kinematics
mjj_2400to3200 = root2400to3200.Get("Simmjj")
mjj_2400to3200.Scale(scale2400to3200)
mjjraw_2400to3200 = root2400to3200.Get("Simmjjraw")
mjjraw_2400to3200.Scale(scale2400to3200)
mjjnom_2400to3200 = root2400to3200.Get("Simmjjnom")
mjjnom_2400to3200.Scale(scale2400to3200)

#load and scale 3200 Simulation
#load and scale jet1 data
pt1_3200 = root3200.Get("Simpt1")
pt1_3200.Scale(scale3200)
pt1raw_3200 = root3200.Get("Simpt1raw")
pt1raw_3200.Scale(scale3200)
pt1nom_3200 = root3200.Get("Simpt1nom")
pt1nom_3200.Scale(scale3200)
#load and sclae jet2 data
pt2_3200 = root3200.Get("Simpt2")
pt2_3200.Scale(scale3200)
pt2raw_3200 = root3200.Get("Simpt2raw")
pt2raw_3200.Scale(scale3200)
pt2nom_3200 = root3200.Get("Simpt2nom")
pt2nom_3200.Scale(scale3200)
#load and sclae jet3 data
pt3_3200 = root3200.Get("Simpt3")
pt3_3200.Scale(scale3200)
pt3raw_3200 = root3200.Get("Simpt3raw")
pt3raw_3200.Scale(scale3200)
pt3nom_3200 = root3200.Get("Simpt3nom")
pt3nom_3200.Scale(scale3200)
#load and scale jet kinematics
mjj_3200 = root3200.Get("Simmjj")
mjj_3200.Scale(scale3200)
mjjraw_3200 = root3200.Get("Simmjjraw")
mjjraw_3200.Scale(scale3200)
mjjnom_3200 = root3200.Get("Simmjjnom")
mjjnom_3200.Scale(scale3200)
#add hists together
#add jet1 hists together
#add pt1 hists together
canvas = ROOT.TCanvas("pt1canvas")
canvas.SetLogy(True)
canvas.cd()

pt1sim_hist = ROOT.TH1D("pt1sim_hist","pt1sim_hist",pt1_3200.GetNbinsX(),pt1_3200.GetXaxis().GetXmin(),pt1_3200.GetXaxis().GetXmax())
pt1sim_hist.Sumw2()

pt1sim_hist.Add(pt1_50to80)
pt1sim_hist.Add(pt1_80to120)
pt1sim_hist.Add(pt1_120to170)
pt1sim_hist.Add(pt1_170to300)
pt1sim_hist.Add(pt1_300to470)
pt1sim_hist.Add(pt1_470to600)
pt1sim_hist.Add(pt1_600to800)
pt1sim_hist.Add(pt1_800to1000)
pt1sim_hist.Add(pt1_1000to1400)
pt1sim_hist.Add(pt1_1400to1800)
pt1sim_hist.Add(pt1_1800to2400)
pt1sim_hist.Add(pt1_2400to3200)
pt1sim_hist.Add(pt1_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt1sim_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt1sim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt1sim_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt1sim_hist.SetLineColor(ROOT.kBlack)
pt1sim_hist.SetStats(0)
pt1sim_hist.SetLineWidth(2)
pt1sim_hist.SetTitle("")
pt1sim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt1 Simulation")
canvas.Print(outDirectory+pdfnames+"pt1simulation.pdf")
canvas.Clear()

#add pt1raw hists together
canvas = ROOT.TCanvas("pt1rawcanvas")
canvas.SetLogy(True)
canvas.cd()

pt1rawsim_hist = ROOT.TH1D("pt1rawsim_hist","pt1rawsim_hist",pt1raw_3200.GetNbinsX(),pt1raw_3200.GetXaxis().GetXmin(),pt1raw_3200.GetXaxis().GetXmax())
pt1rawsim_hist.Sumw2()

pt1rawsim_hist.Add(pt1raw_50to80)
pt1rawsim_hist.Add(pt1raw_80to120)
pt1rawsim_hist.Add(pt1raw_120to170)
pt1rawsim_hist.Add(pt1raw_170to300)
pt1rawsim_hist.Add(pt1raw_300to470)
pt1rawsim_hist.Add(pt1raw_470to600)
pt1rawsim_hist.Add(pt1raw_600to800)
pt1rawsim_hist.Add(pt1raw_800to1000)
pt1rawsim_hist.Add(pt1raw_1000to1400)
pt1rawsim_hist.Add(pt1raw_1400to1800)
pt1rawsim_hist.Add(pt1raw_1800to2400)
pt1rawsim_hist.Add(pt1raw_2400to3200)
pt1rawsim_hist.Add(pt1raw_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt1rawsim_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt1rawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt1rawsim_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt1rawsim_hist.SetLineColor(ROOT.kBlack)
pt1rawsim_hist.SetStats(0)
pt1rawsim_hist.SetLineWidth(2)
pt1rawsim_hist.SetTitle("")
pt1rawsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt1 Raw Simulation")
canvas.Print(outDirectory+pdfnames+"pt1rawsimulation.pdf")
canvas.Clear()

#add pt1nom hists together
canvas = ROOT.TCanvas("pt1nomcanvas")
canvas.SetLogy(True)
canvas.cd()

pt1nomsim_hist = ROOT.TH1D("pt1nomsim_hist","pt1nomsim_hist",pt1nom_3200.GetNbinsX(),pt1nom_3200.GetXaxis().GetXmin(),pt1nom_3200.GetXaxis().GetXmax())
pt1nomsim_hist.Sumw2()

pt1nomsim_hist.Add(pt1nom_50to80)
pt1nomsim_hist.Add(pt1nom_80to120)
pt1nomsim_hist.Add(pt1nom_120to170)
pt1nomsim_hist.Add(pt1nom_170to300)
pt1nomsim_hist.Add(pt1nom_300to470)
pt1nomsim_hist.Add(pt1nom_470to600)
pt1nomsim_hist.Add(pt1nom_600to800)
pt1nomsim_hist.Add(pt1nom_800to1000)
pt1nomsim_hist.Add(pt1nom_1000to1400)
pt1nomsim_hist.Add(pt1nom_1400to1800)
pt1nomsim_hist.Add(pt1nom_1800to2400)
pt1nomsim_hist.Add(pt1nom_2400to3200)
pt1nomsim_hist.Add(pt1nom_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt1nomsim_hist,"Simulated Pt_{1}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt1nomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt1nomsim_hist.GetXaxis().SetTitle("Pt_{1} [GeV]")

pt1nomsim_hist.SetLineColor(ROOT.kBlack)
pt1nomsim_hist.SetStats(0)
pt1nomsim_hist.SetLineWidth(2)
pt1nomsim_hist.SetTitle("")
pt1nomsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt1 Nom Simulation")
canvas.Print(outDirectory+pdfnames+"pt1nomsimulation.pdf")
canvas.Clear()

#add jet2 hists together
#add pt2 hists together
canvas = ROOT.TCanvas("pt2canvas")
canvas.SetLogy(True)
canvas.cd()

pt2sim_hist = ROOT.TH1D("pt2sim_hist","pt2sim_hist",pt2_3200.GetNbinsX(),pt2_3200.GetXaxis().GetXmin(),pt2_3200.GetXaxis().GetXmax())
pt2sim_hist.Sumw2()

pt2sim_hist.Add(pt2_50to80)
pt2sim_hist.Add(pt2_80to120)
pt2sim_hist.Add(pt2_120to170)
pt2sim_hist.Add(pt2_170to300)
pt2sim_hist.Add(pt2_300to470)
pt2sim_hist.Add(pt2_470to600)
pt2sim_hist.Add(pt2_600to800)
pt2sim_hist.Add(pt2_800to1000)
pt2sim_hist.Add(pt2_1000to1400)
pt2sim_hist.Add(pt2_1400to1800)
pt2sim_hist.Add(pt2_1800to2400)
pt2sim_hist.Add(pt2_2400to3200)
pt2sim_hist.Add(pt2_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt2sim_hist,"Simulated Pt_{2}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt2sim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt2sim_hist.GetXaxis().SetTitle("Pt_{2} [GeV]")

pt2sim_hist.SetLineColor(ROOT.kBlack)
pt2sim_hist.SetStats(0)
pt2sim_hist.SetLineWidth(2)
pt2sim_hist.SetTitle("")
pt2sim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt2 Simulation")
canvas.Print(outDirectory+pdfnames+"pt2simulation.pdf")
canvas.Clear()

#add pt2raw hists together
canvas = ROOT.TCanvas("pt2rawcanvas")
canvas.SetLogy(True)
canvas.cd()

pt2rawsim_hist = ROOT.TH1D("pt2rawsim_hist","pt2rawsim_hist",pt2raw_3200.GetNbinsX(),pt2raw_3200.GetXaxis().GetXmin(),pt2raw_3200.GetXaxis().GetXmax())
pt2rawsim_hist.Sumw2()

pt2rawsim_hist.Add(pt2raw_50to80)
pt2rawsim_hist.Add(pt2raw_80to120)
pt2rawsim_hist.Add(pt2raw_120to170)
pt2rawsim_hist.Add(pt2raw_170to300)
pt2rawsim_hist.Add(pt2raw_300to470)
pt2rawsim_hist.Add(pt2raw_470to600)
pt2rawsim_hist.Add(pt2raw_600to800)
pt2rawsim_hist.Add(pt2raw_800to1000)
pt2rawsim_hist.Add(pt2raw_1000to1400)
pt2rawsim_hist.Add(pt2raw_1400to1800)
pt2rawsim_hist.Add(pt2raw_1800to2400)
pt2rawsim_hist.Add(pt2raw_2400to3200)
pt2rawsim_hist.Add(pt2raw_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt2rawsim_hist,"Simulated Pt_{2}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt2rawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt2rawsim_hist.GetXaxis().SetTitle("Pt_{2} [GeV]")

pt2rawsim_hist.SetLineColor(ROOT.kBlack)
pt2rawsim_hist.SetStats(0)
pt2rawsim_hist.SetLineWidth(2)
pt2rawsim_hist.SetTitle("")
pt2rawsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt2 Raw Simulation")
canvas.Print(outDirectory+pdfnames+"pt2rawsimulation.pdf")
canvas.Clear()

#add pt2nom hists together
canvas = ROOT.TCanvas("pt2nomcanvas")
canvas.SetLogy(True)
canvas.cd()

pt2nomsim_hist = ROOT.TH1D("pt2nomsim_hist","pt2nomsim_hist",pt2nom_3200.GetNbinsX(),pt2nom_3200.GetXaxis().GetXmin(),pt2nom_3200.GetXaxis().GetXmax())
pt2nomsim_hist.Sumw2()

pt2nomsim_hist.Add(pt2nom_50to80)
pt2nomsim_hist.Add(pt2nom_80to120)
pt2nomsim_hist.Add(pt2nom_120to170)
pt2nomsim_hist.Add(pt2nom_170to300)
pt2nomsim_hist.Add(pt2nom_300to470)
pt2nomsim_hist.Add(pt2nom_470to600)
pt2nomsim_hist.Add(pt2nom_600to800)
pt2nomsim_hist.Add(pt2nom_800to1000)
pt2nomsim_hist.Add(pt2nom_1000to1400)
pt2nomsim_hist.Add(pt2nom_1400to1800)
pt2nomsim_hist.Add(pt2nom_1800to2400)
pt2nomsim_hist.Add(pt2nom_2400to3200)
pt2nomsim_hist.Add(pt2nom_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt2nomsim_hist,"Simulated Pt_{2}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt2nomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt2nomsim_hist.GetXaxis().SetTitle("Pt_{2} [GeV]")

pt2nomsim_hist.SetLineColor(ROOT.kBlack)
pt2nomsim_hist.SetStats(0)
pt2nomsim_hist.SetLineWidth(2)
pt2nomsim_hist.SetTitle("")
pt2nomsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt2 Nom Simulation")
canvas.Print(outDirectory+pdfnames+"pt2nomsimulation.pdf")
canvas.Clear()

#add jet3 hists together
#add pt3 hists together
canvas = ROOT.TCanvas("pt3canvas")
canvas.SetLogy(True)
canvas.cd()

pt3sim_hist = ROOT.TH1D("pt3sim_hist","pt3sim_hist",pt3_3200.GetNbinsX(),pt3_3200.GetXaxis().GetXmin(),pt3_3200.GetXaxis().GetXmax())
pt3sim_hist.Sumw2()

pt3sim_hist.Add(pt3_50to80)
pt3sim_hist.Add(pt3_80to120)
pt3sim_hist.Add(pt3_120to170)
pt3sim_hist.Add(pt3_170to300)
pt3sim_hist.Add(pt3_300to470)
pt3sim_hist.Add(pt3_470to600)
pt3sim_hist.Add(pt3_600to800)
pt3sim_hist.Add(pt3_800to1000)
pt3sim_hist.Add(pt3_1000to1400)
pt3sim_hist.Add(pt3_1400to1800)
pt3sim_hist.Add(pt3_1800to2400)
pt3sim_hist.Add(pt3_2400to3200)
pt3sim_hist.Add(pt3_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt3sim_hist,"Simulated Pt_{3}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt3sim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt3sim_hist.GetXaxis().SetTitle("Pt_{3} [GeV]")

pt3sim_hist.SetLineColor(ROOT.kBlack)
pt3sim_hist.SetStats(0)
pt3sim_hist.SetLineWidth(2)
pt3sim_hist.SetTitle("")
pt3sim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt3 Simulation")
canvas.Print(outDirectory+pdfnames+"pt3simulation.pdf")
canvas.Clear()

#add pt3raw hists together
canvas = ROOT.TCanvas("pt3rawcanvas")
canvas.SetLogy(True)
canvas.cd()

pt3rawsim_hist = ROOT.TH1D("pt3rawsim_hist","pt3rawsim_hist",pt3raw_3200.GetNbinsX(),pt3raw_3200.GetXaxis().GetXmin(),pt3raw_3200.GetXaxis().GetXmax())
pt3rawsim_hist.Sumw2()

pt3rawsim_hist.Add(pt3raw_50to80)
pt3rawsim_hist.Add(pt3raw_80to120)
pt3rawsim_hist.Add(pt3raw_120to170)
pt3rawsim_hist.Add(pt3raw_170to300)
pt3rawsim_hist.Add(pt3raw_300to470)
pt3rawsim_hist.Add(pt3raw_470to600)
pt3rawsim_hist.Add(pt3raw_600to800)
pt3rawsim_hist.Add(pt3raw_800to1000)
pt3rawsim_hist.Add(pt3raw_1000to1400)
pt3rawsim_hist.Add(pt3raw_1400to1800)
pt3rawsim_hist.Add(pt3raw_1800to2400)
pt3rawsim_hist.Add(pt3raw_2400to3200)
pt3rawsim_hist.Add(pt3raw_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt3rawsim_hist,"Simulated Pt_{3}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt3rawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt3rawsim_hist.GetXaxis().SetTitle("Pt_{3} [GeV]")

pt3rawsim_hist.SetLineColor(ROOT.kBlack)
pt3rawsim_hist.SetStats(0)
pt3rawsim_hist.SetLineWidth(2)
pt3rawsim_hist.SetTitle("")
pt3rawsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt3 Raw Simulation")
canvas.Print(outDirectory+pdfnames+"pt3rawsimulation.pdf")
canvas.Clear()

#add pt3nom hists together
canvas = ROOT.TCanvas("pt3nomcanvas")
canvas.SetLogy(True)
canvas.cd()

pt3nomsim_hist = ROOT.TH1D("pt3nomsim_hist","pt3nomsim_hist",pt3nom_3200.GetNbinsX(),pt3nom_3200.GetXaxis().GetXmin(),pt3nom_3200.GetXaxis().GetXmax())
pt3nomsim_hist.Sumw2()

pt3nomsim_hist.Add(pt3nom_50to80)
pt3nomsim_hist.Add(pt3nom_80to120)
pt3nomsim_hist.Add(pt3nom_120to170)
pt3nomsim_hist.Add(pt3nom_170to300)
pt3nomsim_hist.Add(pt3nom_300to470)
pt3nomsim_hist.Add(pt3nom_470to600)
pt3nomsim_hist.Add(pt3nom_600to800)
pt3nomsim_hist.Add(pt3nom_800to1000)
pt3nomsim_hist.Add(pt3nom_1000to1400)
pt3nomsim_hist.Add(pt3nom_1400to1800)
pt3nomsim_hist.Add(pt3nom_1800to2400)
pt3nomsim_hist.Add(pt3nom_2400to3200)
pt3nomsim_hist.Add(pt3nom_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(pt3nomsim_hist,"Simulated Pt_{3}")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

pt3nomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
pt3nomsim_hist.GetXaxis().SetTitle("Pt_{3} [GeV]")

pt3nomsim_hist.SetLineColor(ROOT.kBlack)
pt3nomsim_hist.SetStats(0)
pt3nomsim_hist.SetLineWidth(2)
pt3nomsim_hist.SetTitle("")
pt3nomsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Pt3 Nom Simulation")
canvas.Print(outDirectory+pdfnames+"pt3nomsimulation.pdf")
canvas.Clear()

#Plot Mjj hists
#add mjj hists together
canvas = ROOT.TCanvas("mjjcanvas")
canvas.SetLogy(True)
canvas.cd()

mjjsim_hist = ROOT.TH1D("mjjsim_hist","mjjsim_hist",mjj_3200.GetNbinsX(),mjj_3200.GetXaxis().GetXmin(),mjj_3200.GetXaxis().GetXmax())
mjjsim_hist.Sumw2()

mjjsim_hist.Add(mjj_50to80)
mjjsim_hist.Add(mjj_80to120)
mjjsim_hist.Add(mjj_120to170)
mjjsim_hist.Add(mjj_170to300)
mjjsim_hist.Add(mjj_300to470)
mjjsim_hist.Add(mjj_470to600)
mjjsim_hist.Add(mjj_600to800)
mjjsim_hist.Add(mjj_800to1000)
mjjsim_hist.Add(mjj_1000to1400)
mjjsim_hist.Add(mjj_1400to1800)
mjjsim_hist.Add(mjj_1800to2400)
mjjsim_hist.Add(mjj_2400to3200)
mjjsim_hist.Add(mjj_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mjjsim_hist,"Simulated Mjj")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mjjsim_hist.GetYaxis().SetTitle("#sigma [pb]")
mjjsim_hist.GetXaxis().SetTitle("Mjj [GeV]")

mjjsim_hist.SetLineColor(ROOT.kBlack)
mjjsim_hist.SetStats(0)
mjjsim_hist.SetLineWidth(2)
mjjsim_hist.SetTitle("")
mjjsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Mjj Simulation")
canvas.Print(outDirectory+pdfnames+"mjjsimulation.pdf")
canvas.Clear()

#add mjjraw hists together
canvas = ROOT.TCanvas("mjjrawcanvas")
canvas.SetLogy(True)
canvas.cd()

mjjrawsim_hist = ROOT.TH1D("mjjrawsim_hist","mjjrawsim_hist",mjjraw_3200.GetNbinsX(),mjjraw_3200.GetXaxis().GetXmin(),mjjraw_3200.GetXaxis().GetXmax())
mjjrawsim_hist.Sumw2()

mjjrawsim_hist.Add(mjjraw_50to80)
mjjrawsim_hist.Add(mjjraw_80to120)
mjjrawsim_hist.Add(mjjraw_120to170)
mjjrawsim_hist.Add(mjjraw_170to300)
mjjrawsim_hist.Add(mjjraw_300to470)
mjjrawsim_hist.Add(mjjraw_470to600)
mjjrawsim_hist.Add(mjjraw_600to800)
mjjrawsim_hist.Add(mjjraw_800to1000)
mjjrawsim_hist.Add(mjjraw_1000to1400)
mjjrawsim_hist.Add(mjjraw_1400to1800)
mjjrawsim_hist.Add(mjjraw_1800to2400)
mjjrawsim_hist.Add(mjjraw_2400to3200)
mjjrawsim_hist.Add(mjjraw_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mjjrawsim_hist,"Simulated Mjjraw")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mjjrawsim_hist.GetYaxis().SetTitle("#sigma [pb]")
mjjrawsim_hist.GetXaxis().SetTitle("Mjjraw [GeV]")

mjjrawsim_hist.SetLineColor(ROOT.kBlack)
mjjrawsim_hist.SetStats(0)
mjjrawsim_hist.SetLineWidth(2)
mjjrawsim_hist.SetTitle("")
mjjrawsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Mjj Raw Simulation")
canvas.Print(outDirectory+pdfnames+"mjjrawsimulation.pdf")
canvas.Clear()

#add mjjnom hists together
canvas = ROOT.TCanvas("mjjnomcanvas")
canvas.SetLogy(True)
canvas.cd()

mjjnomsim_hist = ROOT.TH1D("mjjnomsim_hist","mjjnomsim_hist",mjjnom_3200.GetNbinsX(),mjjnom_3200.GetXaxis().GetXmin(),mjjnom_3200.GetXaxis().GetXmax())
mjjnomsim_hist.Sumw2()

mjjnomsim_hist.Add(mjjnom_50to80)
mjjnomsim_hist.Add(mjjnom_80to120)
mjjnomsim_hist.Add(mjjnom_120to170)
mjjnomsim_hist.Add(mjjnom_170to300)
mjjnomsim_hist.Add(mjjnom_300to470)
mjjnomsim_hist.Add(mjjnom_470to600)
mjjnomsim_hist.Add(mjjnom_600to800)
mjjnomsim_hist.Add(mjjnom_800to1000)
mjjnomsim_hist.Add(mjjnom_1000to1400)
mjjnomsim_hist.Add(mjjnom_1400to1800)
mjjnomsim_hist.Add(mjjnom_1800to2400)
mjjnomsim_hist.Add(mjjnom_2400to3200)
mjjnomsim_hist.Add(mjjnom_3200)

legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
legend.SetLineWidth(0)
legend.AddEntry(mjjnomsim_hist,"Simulated Mjjnom")
legend.SetTextSize(0.03)

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)

mjjnomsim_hist.GetYaxis().SetTitle("#sigma [pb]")
mjjnomsim_hist.GetXaxis().SetTitle("Mjjnom [GeV]")

mjjnomsim_hist.SetLineColor(ROOT.kBlack)
mjjnomsim_hist.SetStats(0)
mjjnomsim_hist.SetLineWidth(2)
mjjnomsim_hist.SetTitle("")
mjjnomsim_hist.Draw("pe")
legend.Draw("same")
latex.DrawText(0.7,0.8,"Mjj Nom Simulation")
canvas.Print(outDirectory+pdfnames+"mjjnomsimulation.pdf")
canvas.Clear()

#create and save root file with all added hists
outHistFile = ROOT.TFile.Open(outRootDirectory+"_PlotSimulation_WithScale_Run32023_MC.root","RECREATE")
pt1sim_hist.Write()
pt1rawsim_hist.Write()
pt1nomsim_hist.Write()
pt2sim_hist.Write()
pt2rawsim_hist.Write()
pt2nomsim_hist.Write()
pt3sim_hist.Write()
pt3rawsim_hist.Write()
pt3nomsim_hist.Write()
mjjsim_hist.Write()
mjjrawsim_hist.Write()
mjjnomsim_hist.Write()
outHistFile.Close()
