int JetResolutionDiffEtas()
{

    //define folders of Root Tree File and where to write Hist Files
    char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile3[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile4[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile5[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile6[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile7[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile8[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile9[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile10[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile11[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile12[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile13[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-3200_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char outNameJet1[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet1_Run2023_Sim.root";
    char outNameJet2[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet2_Run2023_Sim.root";
    char outNameJet3[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet3_Run2023_Sim.root";


    TChain tree("Events");   // name of the tree is the argument
    tree.Add(rootFile1);
    tree.Add(rootFile2);
    tree.Add(rootFile3);
    tree.Add(rootFile4);
    tree.Add(rootFile5);
    tree.Add(rootFile6);
    tree.Add(rootFile7);
    tree.Add(rootFile8);
    tree.Add(rootFile9);
    tree.Add(rootFile10);
    tree.Add(rootFile11);
    tree.Add(rootFile12);
    tree.Add(rootFile13);

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float y1Num[eventNum];
    float eta1Num[eventNum];
    float phi1Num[eventNum];
    float mass1Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree.SetBranchAddress("jetAK4_y1",&y1Num);
    tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
    tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
    tree.SetBranchAddress("jetAK4_mass1",&mass1Num);

    //variables of genJet
    float genpt1Num[eventNum];
    float geny1Num[eventNum];
    float geneta1Num[eventNum];
    float genphi1Num[eventNum];
    float genmass1Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt1",&genpt1Num);
    tree.SetBranchAddress("genJetAK4_y1",&geny1Num);
    tree.SetBranchAddress("genJetAK4_eta1",&geneta1Num);
    tree.SetBranchAddress("genJetAK4_phi1",&genphi1Num);
    tree.SetBranchAddress("genJetAK4_mass1",&genmass1Num);

    TH1D Eta0to1p3ResponseJet150to80("Eta0to1p3ResponseJet150to80","Eta0to1p3ResponseJet150to80",40,-0.4,0.4);
    Eta0to1p3ResponseJet150to80.Sumw2();
    TH1D Eta0to1p3ResponseJet180to120("Eta0to1p3ResponseJet180to120","Eta0to1p3ResponseJet180to120",40,-0.4,0.4);
    Eta0to1p3ResponseJet180to120.Sumw2();
    TH1D Eta0to1p3ResponseJet1120to170("Eta0to1p3ResponseJet1120to170","Eta0to1p3ResponseJet1120to170",40,-0.4,0.4);
    Eta0to1p3ResponseJet1120to170.Sumw2();
    TH1D Eta0to1p3ResponseJet1170to300("Eta0to1p3ResponseJet1170to300","Eta0to1p3ResponseJet1170to300",40,-0.4,0.4);
    Eta0to1p3ResponseJet1170to300.Sumw2();
    TH1D Eta0to1p3ResponseJet1300to470("Eta0to1p3ResponseJet1300to470","Eta0to1p3ResponseJet1300to470",40,-0.4,0.4);
    Eta0to1p3ResponseJet1300to470.Sumw2();
    TH1D Eta0to1p3ResponseJet1470to600("Eta0to1p3ResponseJet1470to600","Eta0to1p3ResponseJet1470to600",40,-0.4,0.4);
    Eta0to1p3ResponseJet1470to600.Sumw2();
    TH1D Eta0to1p3ResponseJet1600to800("Eta0to1p3ResponseJet1600to800","Eta0to1p3ResponseJet1600to800",40,-0.4,0.4);
    Eta0to1p3ResponseJet1600to800.Sumw2();
    TH1D Eta0to1p3ResponseJet1800to1000("Eta0to1p3ResponseJet1800to1000","Eta0to1p3ResponseJet1800to1000",40,-0.4,0.4);
    Eta0to1p3ResponseJet1800to1000.Sumw2();
    TH1D Eta0to1p3ResponseJet11000to1400("Eta0to1p3ResponseJet11000to1400","Eta0to1p3ResponseJet11000to1400",40,-0.4,0.4);
    Eta0to1p3ResponseJet11000to1400.Sumw2();
    TH1D Eta0to1p3ResponseJet11400to1800("Eta0to1p3ResponseJet11400to1800","Eta0to1p3ResponseJet11400to1800",40,-0.4,0.4);
    Eta0to1p3ResponseJet11400to1800.Sumw2();
    TH1D Eta0to1p3ResponseJet11800to2400("Eta0to1p3ResponseJet11800to2400","Eta0to1p3ResponseJet11800to2400",40,-0.4,0.4);
    Eta0to1p3ResponseJet11800to2400.Sumw2();
    TH1D Eta0to1p3ResponseJet12400to3200("Eta0to1p3ResponseJet12400to3200","Eta0to1p3ResponseJet12400to3200",40,-0.4,0.4);
    Eta0to1p3ResponseJet12400to3200.Sumw2();
    TH1D Eta0to1p3ResponseJet13200("Eta0to1p3ResponseJet13200","Eta0to1p3ResponseJet13200",40,-0.4,0.4);
    Eta0to1p3ResponseJet13200.Sumw2();

    TH1D Eta1p3to2p5ResponseJet150to80("Eta1p3to2p5ResponseJet150to80","Eta1p3to2p5ResponseJet150to80",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet150to80.Sumw2();
    TH1D Eta1p3to2p5ResponseJet180to120("Eta1p3to2p5ResponseJet180to120","Eta1p3to2p5ResponseJet180to120",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet180to120.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1120to170("Eta1p3to2p5ResponseJet1120to170","Eta1p3to2p5ResponseJet1120to170",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1120to170.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1170to300("Eta1p3to2p5ResponseJet1170to300","Eta1p3to2p5ResponseJet1170to300",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1170to300.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1300to470("Eta1p3to2p5ResponseJet1300to470","Eta1p3to2p5ResponseJet1300to470",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1300to470.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1470to600("Eta1p3to2p5ResponseJet1470to600","Eta1p3to2p5ResponseJet1470to600",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1470to600.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1600to800("Eta1p3to2p5ResponseJet1600to800","Eta1p3to2p5ResponseJet1600to800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1600to800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet1800to1000("Eta1p3to2p5ResponseJet1800to1000","Eta1p3to2p5ResponseJet1800to1000",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet1800to1000.Sumw2();
    TH1D Eta1p3to2p5ResponseJet11000to1400("Eta1p3to2p5ResponseJet11000to1400","Eta1p3to2p5ResponseJet11000to1400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet11000to1400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet11400to1800("Eta1p3to2p5ResponseJet11400to1800","Eta1p3to2p5ResponseJet11400to1800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet11400to1800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet11800to2400("Eta1p3to2p5ResponseJet11800to2400","Eta1p3to2p5ResponseJet11800to2400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet11800to2400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet12400to3200("Eta1p3to2p5ResponseJet12400to3200","Eta1p3to2p5ResponseJet12400to3200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet12400to3200.Sumw2();
    TH1D Eta1p3to2p5ResponseJet13200("Eta1p3to2p5ResponseJet13200","Eta1p3to2p5ResponseJet13200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet13200.Sumw2();

    TH1D Eta2p5to3ResponseJet150to80("Eta2p5to3ResponseJet150to80","Eta2p5to3ResponseJet150to80",40,-0.4,0.4);
    Eta2p5to3ResponseJet150to80.Sumw2();
    TH1D Eta2p5to3ResponseJet180to120("Eta2p5to3ResponseJet180to120","Eta2p5to3ResponseJet180to120",40,-0.4,0.4);
    Eta2p5to3ResponseJet180to120.Sumw2();
    TH1D Eta2p5to3ResponseJet1120to170("Eta2p5to3ResponseJet1120to170","Eta2p5to3ResponseJet1120to170",40,-0.4,0.4);
    Eta2p5to3ResponseJet1120to170.Sumw2();
    TH1D Eta2p5to3ResponseJet1170to300("Eta2p5to3ResponseJet1170to300","Eta2p5to3ResponseJet1170to300",40,-0.4,0.4);
    Eta2p5to3ResponseJet1170to300.Sumw2();
    TH1D Eta2p5to3ResponseJet1300to470("Eta2p5to3ResponseJet1300to470","Eta2p5to3ResponseJet1300to470",40,-0.4,0.4);
    Eta2p5to3ResponseJet1300to470.Sumw2();
    TH1D Eta2p5to3ResponseJet1470to600("Eta2p5to3ResponseJet1470to600","Eta2p5to3ResponseJet1470to600",40,-0.4,0.4);
    Eta2p5to3ResponseJet1470to600.Sumw2();
    TH1D Eta2p5to3ResponseJet1600to800("Eta2p5to3ResponseJet1600to800","Eta2p5to3ResponseJet1600to800",40,-0.4,0.4);
    Eta2p5to3ResponseJet1600to800.Sumw2();
    TH1D Eta2p5to3ResponseJet1800to1000("Eta2p5to3ResponseJet1800to1000","Eta2p5to3ResponseJet1800to1000",40,-0.4,0.4);
    Eta2p5to3ResponseJet1800to1000.Sumw2();
    TH1D Eta2p5to3ResponseJet11000to1400("Eta2p5to3ResponseJet11000to1400","Eta2p5to3ResponseJet11000to1400",40,-0.4,0.4);
    Eta2p5to3ResponseJet11000to1400.Sumw2();
    TH1D Eta2p5to3ResponseJet11400to1800("Eta2p5to3ResponseJet11400to1800","Eta2p5to3ResponseJet11400to1800",40,-0.4,0.4);
    Eta2p5to3ResponseJet11400to1800.Sumw2();
    TH1D Eta2p5to3ResponseJet11800to2400("Eta2p5to3ResponseJet11800to2400","Eta2p5to3ResponseJet11800to2400",40,-0.4,0.4);
    Eta2p5to3ResponseJet11800to2400.Sumw2();
    TH1D Eta2p5to3ResponseJet12400to3200("Eta2p5to3ResponseJet12400to3200","Eta2p5to3ResponseJet12400to3200",40,-0.4,0.4);
    Eta2p5to3ResponseJet12400to3200.Sumw2();
    TH1D Eta2p5to3ResponseJet13200("Eta2p5to3ResponseJet13200","Eta2p5to3ResponseJet13200",40,-0.4,0.4);
    Eta2p5to3ResponseJet13200.Sumw2();

    TH1D Eta3to5ResponseJet150to80("Eta3to5ResponseJet150to80","Eta3to5ResponseJet150to80",40,-0.4,0.4);
    Eta3to5ResponseJet150to80.Sumw2();
    TH1D Eta3to5ResponseJet180to120("Eta3to5ResponseJet180to120","Eta3to5ResponseJet180to120",40,-0.4,0.4);
    Eta3to5ResponseJet180to120.Sumw2();
    TH1D Eta3to5ResponseJet1120to170("Eta3to5ResponseJet1120to170","Eta3to5ResponseJet1120to170",40,-0.4,0.4);
    Eta3to5ResponseJet1120to170.Sumw2();
    TH1D Eta3to5ResponseJet1170to300("Eta3to5ResponseJet1170to300","Eta3to5ResponseJet1170to300",40,-0.4,0.4);
    Eta3to5ResponseJet1170to300.Sumw2();
    TH1D Eta3to5ResponseJet1300to470("Eta3to5ResponseJet1300to470","Eta3to5ResponseJet1300to470",40,-0.4,0.4);
    Eta3to5ResponseJet1300to470.Sumw2();
    TH1D Eta3to5ResponseJet1470to600("Eta3to5ResponseJet1470to600","Eta3to5ResponseJet1470to600",40,-0.4,0.4);
    Eta3to5ResponseJet1470to600.Sumw2();
    TH1D Eta3to5ResponseJet1600to800("Eta3to5ResponseJet1600to800","Eta3to5ResponseJet1600to800",40,-0.4,0.4);
    Eta3to5ResponseJet1600to800.Sumw2();
    TH1D Eta3to5ResponseJet1800to1000("Eta3to5ResponseJet1800to1000","Eta3to5ResponseJet1800to1000",40,-0.4,0.4);
    Eta3to5ResponseJet1800to1000.Sumw2();
    TH1D Eta3to5ResponseJet11000to1400("Eta3to5ResponseJet11000to1400","Eta3to5ResponseJet11000to1400",40,-0.4,0.4);
    Eta3to5ResponseJet11000to1400.Sumw2();
    TH1D Eta3to5ResponseJet11400to1800("Eta3to5ResponseJet11400to1800","Eta3to5ResponseJet11400to1800",40,-0.4,0.4);
    Eta3to5ResponseJet11400to1800.Sumw2();
    TH1D Eta3to5ResponseJet11800to2400("Eta3to5ResponseJet11800to2400","Eta3to5ResponseJet11800to2400",40,-0.4,0.4);
    Eta3to5ResponseJet11800to2400.Sumw2();
    TH1D Eta3to5ResponseJet12400to3200("Eta3to5ResponseJet12400to3200","Eta3to5ResponseJet12400to3200",40,-0.4,0.4);
    Eta3to5ResponseJet12400to3200.Sumw2();
    TH1D Eta3to5ResponseJet13200("Eta3to5ResponseJet13200","Eta3to5ResponseJet13200",40,-0.4,0.4);
    Eta3to5ResponseJet13200.Sumw2();

    //variables of Jet2
    float pt2Num[eventNum];
    float y2Num[eventNum];
    float eta2Num[eventNum];
    float phi2Num[eventNum];
    float mass2Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree.SetBranchAddress("jetAK4_y2",&y2Num);
    tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
    tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
    tree.SetBranchAddress("jetAK4_mass2",&mass2Num);

    //variables of genJet
    float genpt2Num[eventNum];
    float geny2Num[eventNum];
    float geneta2Num[eventNum];
    float genphi2Num[eventNum];
    float genmass2Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt2",&genpt2Num);
    tree.SetBranchAddress("genJetAK4_y2",&geny2Num);
    tree.SetBranchAddress("genJetAK4_eta2",&geneta2Num);
    tree.SetBranchAddress("genJetAK4_phi2",&genphi2Num);
    tree.SetBranchAddress("genJetAK4_mass2",&genmass2Num);

    TH1D Eta0to1p3ResponseJet250to80("Eta0to1p3ResponseJet250to80","Eta0to1p3ResponseJet250to80",40,-0.4,0.4);
    Eta0to1p3ResponseJet250to80.Sumw2();
    TH1D Eta0to1p3ResponseJet280to120("Eta0to1p3ResponseJet280to120","Eta0to1p3ResponseJet280to120",40,-0.4,0.4);
    Eta0to1p3ResponseJet280to120.Sumw2();
    TH1D Eta0to1p3ResponseJet2120to170("Eta0to1p3ResponseJet2120to170","Eta0to1p3ResponseJet2120to170",40,-0.4,0.4);
    Eta0to1p3ResponseJet2120to170.Sumw2();
    TH1D Eta0to1p3ResponseJet2170to300("Eta0to1p3ResponseJet2170to300","Eta0to1p3ResponseJet2170to300",40,-0.4,0.4);
    Eta0to1p3ResponseJet2170to300.Sumw2();
    TH1D Eta0to1p3ResponseJet2300to470("Eta0to1p3ResponseJet2300to470","Eta0to1p3ResponseJet2300to470",40,-0.4,0.4);
    Eta0to1p3ResponseJet2300to470.Sumw2();
    TH1D Eta0to1p3ResponseJet2470to600("Eta0to1p3ResponseJet2470to600","Eta0to1p3ResponseJet2470to600",40,-0.4,0.4);
    Eta0to1p3ResponseJet2470to600.Sumw2();
    TH1D Eta0to1p3ResponseJet2600to800("Eta0to1p3ResponseJet2600to800","Eta0to1p3ResponseJet2600to800",40,-0.4,0.4);
    Eta0to1p3ResponseJet2600to800.Sumw2();
    TH1D Eta0to1p3ResponseJet2800to1000("Eta0to1p3ResponseJet2800to1000","Eta0to1p3ResponseJet2800to1000",40,-0.4,0.4);
    Eta0to1p3ResponseJet2800to1000.Sumw2();
    TH1D Eta0to1p3ResponseJet21000to1400("Eta0to1p3ResponseJet21000to1400","Eta0to1p3ResponseJet21000to1400",40,-0.4,0.4);
    Eta0to1p3ResponseJet21000to1400.Sumw2();
    TH1D Eta0to1p3ResponseJet21400to1800("Eta0to1p3ResponseJet21400to1800","Eta0to1p3ResponseJet21400to1800",40,-0.4,0.4);
    Eta0to1p3ResponseJet21400to1800.Sumw2();
    TH1D Eta0to1p3ResponseJet21800to2400("Eta0to1p3ResponseJet21800to2400","Eta0to1p3ResponseJet21800to2400",40,-0.4,0.4);
    Eta0to1p3ResponseJet21800to2400.Sumw2();
    TH1D Eta0to1p3ResponseJet22400to3200("Eta0to1p3ResponseJet22400to3200","Eta0to1p3ResponseJet22400to3200",40,-0.4,0.4);
    Eta0to1p3ResponseJet22400to3200.Sumw2();
    TH1D Eta0to1p3ResponseJet23200("Eta0to1p3ResponseJet23200","Eta0to1p3ResponseJet23200",40,-0.4,0.4);
    Eta0to1p3ResponseJet23200.Sumw2();

    TH1D Eta1p3to2p5ResponseJet250to80("Eta1p3to2p5ResponseJet250to80","Eta1p3to2p5ResponseJet250to80",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet250to80.Sumw2();
    TH1D Eta1p3to2p5ResponseJet280to120("Eta1p3to2p5ResponseJet280to120","Eta1p3to2p5ResponseJet280to120",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet280to120.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2120to170("Eta1p3to2p5ResponseJet2120to170","Eta1p3to2p5ResponseJet2120to170",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2120to170.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2170to300("Eta1p3to2p5ResponseJet2170to300","Eta1p3to2p5ResponseJet2170to300",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2170to300.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2300to470("Eta1p3to2p5ResponseJet2300to470","Eta1p3to2p5ResponseJet2300to470",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2300to470.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2470to600("Eta1p3to2p5ResponseJet2470to600","Eta1p3to2p5ResponseJet2470to600",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2470to600.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2600to800("Eta1p3to2p5ResponseJet2600to800","Eta1p3to2p5ResponseJet2600to800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2600to800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet2800to1000("Eta1p3to2p5ResponseJet2800to1000","Eta1p3to2p5ResponseJet2800to1000",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet2800to1000.Sumw2();
    TH1D Eta1p3to2p5ResponseJet21000to1400("Eta1p3to2p5ResponseJet21000to1400","Eta1p3to2p5ResponseJet21000to1400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet21000to1400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet21400to1800("Eta1p3to2p5ResponseJet21400to1800","Eta1p3to2p5ResponseJet21400to1800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet21400to1800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet21800to2400("Eta1p3to2p5ResponseJet21800to2400","Eta1p3to2p5ResponseJet21800to2400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet21800to2400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet22400to3200("Eta1p3to2p5ResponseJet22400to3200","Eta1p3to2p5ResponseJet22400to3200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet22400to3200.Sumw2();
    TH1D Eta1p3to2p5ResponseJet23200("Eta1p3to2p5ResponseJet23200","Eta1p3to2p5ResponseJet23200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet23200.Sumw2();

    TH1D Eta2p5to3ResponseJet250to80("Eta2p5to3ResponseJet250to80","Eta2p5to3ResponseJet250to80",40,-0.4,0.4);
    Eta2p5to3ResponseJet250to80.Sumw2();
    TH1D Eta2p5to3ResponseJet280to120("Eta2p5to3ResponseJet280to120","Eta2p5to3ResponseJet280to120",40,-0.4,0.4);
    Eta2p5to3ResponseJet280to120.Sumw2();
    TH1D Eta2p5to3ResponseJet2120to170("Eta2p5to3ResponseJet2120to170","Eta2p5to3ResponseJet2120to170",40,-0.4,0.4);
    Eta2p5to3ResponseJet2120to170.Sumw2();
    TH1D Eta2p5to3ResponseJet2170to300("Eta2p5to3ResponseJet2170to300","Eta2p5to3ResponseJet2170to300",40,-0.4,0.4);
    Eta2p5to3ResponseJet2170to300.Sumw2();
    TH1D Eta2p5to3ResponseJet2300to470("Eta2p5to3ResponseJet2300to470","Eta2p5to3ResponseJet2300to470",40,-0.4,0.4);
    Eta2p5to3ResponseJet2300to470.Sumw2();
    TH1D Eta2p5to3ResponseJet2470to600("Eta2p5to3ResponseJet2470to600","Eta2p5to3ResponseJet2470to600",40,-0.4,0.4);
    Eta2p5to3ResponseJet2470to600.Sumw2();
    TH1D Eta2p5to3ResponseJet2600to800("Eta2p5to3ResponseJet2600to800","Eta2p5to3ResponseJet2600to800",40,-0.4,0.4);
    Eta2p5to3ResponseJet2600to800.Sumw2();
    TH1D Eta2p5to3ResponseJet2800to1000("Eta2p5to3ResponseJet2800to1000","Eta2p5to3ResponseJet2800to1000",40,-0.4,0.4);
    Eta2p5to3ResponseJet2800to1000.Sumw2();
    TH1D Eta2p5to3ResponseJet21000to1400("Eta2p5to3ResponseJet21000to1400","Eta2p5to3ResponseJet21000to1400",40,-0.4,0.4);
    Eta2p5to3ResponseJet21000to1400.Sumw2();
    TH1D Eta2p5to3ResponseJet21400to1800("Eta2p5to3ResponseJet21400to1800","Eta2p5to3ResponseJet21400to1800",40,-0.4,0.4);
    Eta2p5to3ResponseJet21400to1800.Sumw2();
    TH1D Eta2p5to3ResponseJet21800to2400("Eta2p5to3ResponseJet21800to2400","Eta2p5to3ResponseJet21800to2400",40,-0.4,0.4);
    Eta2p5to3ResponseJet21800to2400.Sumw2();
    TH1D Eta2p5to3ResponseJet22400to3200("Eta2p5to3ResponseJet22400to3200","Eta2p5to3ResponseJet22400to3200",40,-0.4,0.4);
    Eta2p5to3ResponseJet22400to3200.Sumw2();
    TH1D Eta2p5to3ResponseJet23200("Eta2p5to3ResponseJet23200","Eta2p5to3ResponseJet23200",40,-0.4,0.4);
    Eta2p5to3ResponseJet23200.Sumw2();

    TH1D Eta3to5ResponseJet250to80("Eta3to5ResponseJet250to80","Eta3to5ResponseJet250to80",40,-0.4,0.4);
    Eta3to5ResponseJet250to80.Sumw2();
    TH1D Eta3to5ResponseJet280to120("Eta3to5ResponseJet280to120","Eta3to5ResponseJet280to120",40,-0.4,0.4);
    Eta3to5ResponseJet280to120.Sumw2();
    TH1D Eta3to5ResponseJet2120to170("Eta3to5ResponseJet2120to170","Eta3to5ResponseJet2120to170",40,-0.4,0.4);
    Eta3to5ResponseJet2120to170.Sumw2();
    TH1D Eta3to5ResponseJet2170to300("Eta3to5ResponseJet2170to300","Eta3to5ResponseJet2170to300",40,-0.4,0.4);
    Eta3to5ResponseJet2170to300.Sumw2();
    TH1D Eta3to5ResponseJet2300to470("Eta3to5ResponseJet2300to470","Eta3to5ResponseJet2300to470",40,-0.4,0.4);
    Eta3to5ResponseJet2300to470.Sumw2();
    TH1D Eta3to5ResponseJet2470to600("Eta3to5ResponseJet2470to600","Eta3to5ResponseJet2470to600",40,-0.4,0.4);
    Eta3to5ResponseJet2470to600.Sumw2();
    TH1D Eta3to5ResponseJet2600to800("Eta3to5ResponseJet2600to800","Eta3to5ResponseJet2600to800",40,-0.4,0.4);
    Eta3to5ResponseJet2600to800.Sumw2();
    TH1D Eta3to5ResponseJet2800to1000("Eta3to5ResponseJet2800to1000","Eta3to5ResponseJet2800to1000",40,-0.4,0.4);
    Eta3to5ResponseJet2800to1000.Sumw2();
    TH1D Eta3to5ResponseJet21000to1400("Eta3to5ResponseJet21000to1400","Eta3to5ResponseJet21000to1400",40,-0.4,0.4);
    Eta3to5ResponseJet21000to1400.Sumw2();
    TH1D Eta3to5ResponseJet21400to1800("Eta3to5ResponseJet21400to1800","Eta3to5ResponseJet21400to1800",40,-0.4,0.4);
    Eta3to5ResponseJet21400to1800.Sumw2();
    TH1D Eta3to5ResponseJet21800to2400("Eta3to5ResponseJet21800to2400","Eta3to5ResponseJet21800to2400",40,-0.4,0.4);
    Eta3to5ResponseJet21800to2400.Sumw2();
    TH1D Eta3to5ResponseJet22400to3200("Eta3to5ResponseJet22400to3200","Eta3to5ResponseJet22400to3200",40,-0.4,0.4);
    Eta3to5ResponseJet22400to3200.Sumw2();
    TH1D Eta3to5ResponseJet23200("Eta3to5ResponseJet23200","Eta3to5ResponseJet23200",40,-0.4,0.4);
    Eta3to5ResponseJet23200.Sumw2();

    //variables of Jet3
    float pt3Num[eventNum];
    float y3Num[eventNum];
    float eta3Num[eventNum];
    float phi3Num[eventNum];
    float mass3Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
    tree.SetBranchAddress("jetAK4_y3",&y3Num);
    tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
    tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
    tree.SetBranchAddress("jetAK4_mass3",&mass3Num);

    //variables of genJet
    float genpt3Num[eventNum];
    float geny3Num[eventNum];
    float geneta3Num[eventNum];
    float genphi3Num[eventNum];
    float genmass3Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt3",&genpt3Num);
    tree.SetBranchAddress("genJetAK4_y3",&geny3Num);
    tree.SetBranchAddress("genJetAK4_eta3",&geneta3Num);
    tree.SetBranchAddress("genJetAK4_phi3",&genphi3Num);
    tree.SetBranchAddress("genJetAK4_mass3",&genmass3Num);

    TH1D Eta0to1p3ResponseJet350to80("Eta0to1p3ResponseJet350to80","Eta0to1p3ResponseJet350to80",40,-0.4,0.4);
    Eta0to1p3ResponseJet350to80.Sumw2();
    TH1D Eta0to1p3ResponseJet380to120("Eta0to1p3ResponseJet380to120","Eta0to1p3ResponseJet380to120",40,-0.4,0.4);
    Eta0to1p3ResponseJet380to120.Sumw2();
    TH1D Eta0to1p3ResponseJet3120to170("Eta0to1p3ResponseJet3120to170","Eta0to1p3ResponseJet3120to170",40,-0.4,0.4);
    Eta0to1p3ResponseJet3120to170.Sumw2();
    TH1D Eta0to1p3ResponseJet3170to300("Eta0to1p3ResponseJet3170to300","Eta0to1p3ResponseJet3170to300",40,-0.4,0.4);
    Eta0to1p3ResponseJet3170to300.Sumw2();
    TH1D Eta0to1p3ResponseJet3300to470("Eta0to1p3ResponseJet3300to470","Eta0to1p3ResponseJet3300to470",40,-0.4,0.4);
    Eta0to1p3ResponseJet3300to470.Sumw2();
    TH1D Eta0to1p3ResponseJet3470to600("Eta0to1p3ResponseJet3470to600","Eta0to1p3ResponseJet3470to600",40,-0.4,0.4);
    Eta0to1p3ResponseJet3470to600.Sumw2();
    TH1D Eta0to1p3ResponseJet3600to800("Eta0to1p3ResponseJet3600to800","Eta0to1p3ResponseJet3600to800",40,-0.4,0.4);
    Eta0to1p3ResponseJet3600to800.Sumw2();
    TH1D Eta0to1p3ResponseJet3800to1000("Eta0to1p3ResponseJet3800to1000","Eta0to1p3ResponseJet3800to1000",40,-0.4,0.4);
    Eta0to1p3ResponseJet3800to1000.Sumw2();
    TH1D Eta0to1p3ResponseJet31000to1400("Eta0to1p3ResponseJet31000to1400","Eta0to1p3ResponseJet31000to1400",40,-0.4,0.4);
    Eta0to1p3ResponseJet31000to1400.Sumw2();
    TH1D Eta0to1p3ResponseJet31400to1800("Eta0to1p3ResponseJet31400to1800","Eta0to1p3ResponseJet31400to1800",40,-0.4,0.4);
    Eta0to1p3ResponseJet31400to1800.Sumw2();
    TH1D Eta0to1p3ResponseJet31800to2400("Eta0to1p3ResponseJet31800to2400","Eta0to1p3ResponseJet31800to2400",40,-0.4,0.4);
    Eta0to1p3ResponseJet31800to2400.Sumw2();
    TH1D Eta0to1p3ResponseJet32400to3200("Eta0to1p3ResponseJet32400to3200","Eta0to1p3ResponseJet32400to3200",40,-0.4,0.4);
    Eta0to1p3ResponseJet32400to3200.Sumw2();
    TH1D Eta0to1p3ResponseJet33200("Eta0to1p3ResponseJet33200","Eta0to1p3ResponseJet33200",40,-0.4,0.4);
    Eta0to1p3ResponseJet33200.Sumw2();

    TH1D Eta1p3to2p5ResponseJet350to80("Eta1p3to2p5ResponseJet350to80","Eta1p3to2p5ResponseJet350to80",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet350to80.Sumw2();
    TH1D Eta1p3to2p5ResponseJet380to120("Eta1p3to2p5ResponseJet380to120","Eta1p3to2p5ResponseJet380to120",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet380to120.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3120to170("Eta1p3to2p5ResponseJet3120to170","Eta1p3to2p5ResponseJet3120to170",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3120to170.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3170to300("Eta1p3to2p5ResponseJet3170to300","Eta1p3to2p5ResponseJet3170to300",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3170to300.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3300to470("Eta1p3to2p5ResponseJet3300to470","Eta1p3to2p5ResponseJet3300to470",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3300to470.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3470to600("Eta1p3to2p5ResponseJet3470to600","Eta1p3to2p5ResponseJet3470to600",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3470to600.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3600to800("Eta1p3to2p5ResponseJet3600to800","Eta1p3to2p5ResponseJet3600to800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3600to800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet3800to1000("Eta1p3to2p5ResponseJet3800to1000","Eta1p3to2p5ResponseJet3800to1000",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet3800to1000.Sumw2();
    TH1D Eta1p3to2p5ResponseJet31000to1400("Eta1p3to2p5ResponseJet31000to1400","Eta1p3to2p5ResponseJet31000to1400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet31000to1400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet31400to1800("Eta1p3to2p5ResponseJet31400to1800","Eta1p3to2p5ResponseJet31400to1800",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet31400to1800.Sumw2();
    TH1D Eta1p3to2p5ResponseJet31800to2400("Eta1p3to2p5ResponseJet31800to2400","Eta1p3to2p5ResponseJet31800to2400",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet31800to2400.Sumw2();
    TH1D Eta1p3to2p5ResponseJet32400to3200("Eta1p3to2p5ResponseJet32400to3200","Eta1p3to2p5ResponseJet32400to3200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet32400to3200.Sumw2();
    TH1D Eta1p3to2p5ResponseJet33200("Eta1p3to2p5ResponseJet33200","Eta1p3to2p5ResponseJet33200",40,-0.4,0.4);
    Eta1p3to2p5ResponseJet33200.Sumw2();

    TH1D Eta2p5to3ResponseJet350to80("Eta2p5to3ResponseJet350to80","Eta2p5to3ResponseJet350to80",40,-0.4,0.4);
    Eta2p5to3ResponseJet350to80.Sumw2();
    TH1D Eta2p5to3ResponseJet380to120("Eta2p5to3ResponseJet380to120","Eta2p5to3ResponseJet380to120",40,-0.4,0.4);
    Eta2p5to3ResponseJet380to120.Sumw2();
    TH1D Eta2p5to3ResponseJet3120to170("Eta2p5to3ResponseJet3120to170","Eta2p5to3ResponseJet3120to170",40,-0.4,0.4);
    Eta2p5to3ResponseJet3120to170.Sumw2();
    TH1D Eta2p5to3ResponseJet3170to300("Eta2p5to3ResponseJet3170to300","Eta2p5to3ResponseJet3170to300",40,-0.4,0.4);
    Eta2p5to3ResponseJet3170to300.Sumw2();
    TH1D Eta2p5to3ResponseJet3300to470("Eta2p5to3ResponseJet3300to470","Eta2p5to3ResponseJet3300to470",40,-0.4,0.4);
    Eta2p5to3ResponseJet3300to470.Sumw2();
    TH1D Eta2p5to3ResponseJet3470to600("Eta2p5to3ResponseJet3470to600","Eta2p5to3ResponseJet3470to600",40,-0.4,0.4);
    Eta2p5to3ResponseJet3470to600.Sumw2();
    TH1D Eta2p5to3ResponseJet3600to800("Eta2p5to3ResponseJet3600to800","Eta2p5to3ResponseJet3600to800",40,-0.4,0.4);
    Eta2p5to3ResponseJet3600to800.Sumw2();
    TH1D Eta2p5to3ResponseJet3800to1000("Eta2p5to3ResponseJet3800to1000","Eta2p5to3ResponseJet3800to1000",40,-0.4,0.4);
    Eta2p5to3ResponseJet3800to1000.Sumw2();
    TH1D Eta2p5to3ResponseJet31000to1400("Eta2p5to3ResponseJet31000to1400","Eta2p5to3ResponseJet31000to1400",40,-0.4,0.4);
    Eta2p5to3ResponseJet31000to1400.Sumw2();
    TH1D Eta2p5to3ResponseJet31400to1800("Eta2p5to3ResponseJet31400to1800","Eta2p5to3ResponseJet31400to1800",40,-0.4,0.4);
    Eta2p5to3ResponseJet31400to1800.Sumw2();
    TH1D Eta2p5to3ResponseJet31800to2400("Eta2p5to3ResponseJet31800to2400","Eta2p5to3ResponseJet31800to2400",40,-0.4,0.4);
    Eta2p5to3ResponseJet31800to2400.Sumw2();
    TH1D Eta2p5to3ResponseJet32400to3200("Eta2p5to3ResponseJet32400to3200","Eta2p5to3ResponseJet32400to3200",40,-0.4,0.4);
    Eta2p5to3ResponseJet32400to3200.Sumw2();
    TH1D Eta2p5to3ResponseJet33200("Eta2p5to3ResponseJet33200","Eta2p5to3ResponseJet33200",40,-0.4,0.4);
    Eta2p5to3ResponseJet33200.Sumw2();

    TH1D Eta3to5ResponseJet350to80("Eta3to5ResponseJet350to80","Eta3to5ResponseJet350to80",40,-0.4,0.4);
    Eta3to5ResponseJet350to80.Sumw2();
    TH1D Eta3to5ResponseJet380to120("Eta3to5ResponseJet380to120","Eta3to5ResponseJet380to120",40,-0.4,0.4);
    Eta3to5ResponseJet380to120.Sumw2();
    TH1D Eta3to5ResponseJet3120to170("Eta3to5ResponseJet3120to170","Eta3to5ResponseJet3120to170",40,-0.4,0.4);
    Eta3to5ResponseJet3120to170.Sumw2();
    TH1D Eta3to5ResponseJet3170to300("Eta3to5ResponseJet3170to300","Eta3to5ResponseJet3170to300",40,-0.4,0.4);
    Eta3to5ResponseJet3170to300.Sumw2();
    TH1D Eta3to5ResponseJet3300to470("Eta3to5ResponseJet3300to470","Eta3to5ResponseJet3300to470",40,-0.4,0.4);
    Eta3to5ResponseJet3300to470.Sumw2();
    TH1D Eta3to5ResponseJet3470to600("Eta3to5ResponseJet3470to600","Eta3to5ResponseJet3470to600",40,-0.4,0.4);
    Eta3to5ResponseJet3470to600.Sumw2();
    TH1D Eta3to5ResponseJet3600to800("Eta3to5ResponseJet3600to800","Eta3to5ResponseJet3600to800",40,-0.4,0.4);
    Eta3to5ResponseJet3600to800.Sumw2();
    TH1D Eta3to5ResponseJet3800to1000("Eta3to5ResponseJet3800to1000","Eta3to5ResponseJet3800to1000",40,-0.4,0.4);
    Eta3to5ResponseJet3800to1000.Sumw2();
    TH1D Eta3to5ResponseJet31000to1400("Eta3to5ResponseJet31000to1400","Eta3to5ResponseJet31000to1400",40,-0.4,0.4);
    Eta3to5ResponseJet31000to1400.Sumw2();
    TH1D Eta3to5ResponseJet31400to1800("Eta3to5ResponseJet31400to1800","Eta3to5ResponseJet31400to1800",40,-0.4,0.4);
    Eta3to5ResponseJet31400to1800.Sumw2();
    TH1D Eta3to5ResponseJet31800to2400("Eta3to5ResponseJet31800to2400","Eta3to5ResponseJet31800to2400",40,-0.4,0.4);
    Eta3to5ResponseJet31800to2400.Sumw2();
    TH1D Eta3to5ResponseJet32400to3200("Eta3to5ResponseJet32400to3200","Eta3to5ResponseJet32400to3200",40,-0.4,0.4);
    Eta3to5ResponseJet32400to3200.Sumw2();
    TH1D Eta3to5ResponseJet33200("Eta3to5ResponseJet33200","Eta3to5ResponseJet33200",40,-0.4,0.4);
    Eta3to5ResponseJet33200.Sumw2();

    TH1D ResponseJet150to80("ResponseJet150to80","ResponseJet150to80",40,-0.4,0.4);
    ResponseJet150to80.Sumw2();
    TH1D ResponseJet180to120("ResponseJet180to120","ResponseJet180to120",40,-0.4,0.4);
    ResponseJet180to120.Sumw2();
    TH1D ResponseJet1120to170("ResponseJet1120to170","ResponseJet1120to170",40,-0.4,0.4);
    ResponseJet1120to170.Sumw2();
    TH1D ResponseJet1170to300("ResponseJet1170to300","ResponseJet1170to300",40,-0.4,0.4);
    ResponseJet1170to300.Sumw2();
    TH1D ResponseJet1300to470("ResponseJet1300to470","ResponseJet1300to470",40,-0.4,0.4);
    ResponseJet1300to470.Sumw2();
    TH1D ResponseJet1470to600("ResponseJet1470to600","ResponseJet1470to600",40,-0.4,0.4);
    ResponseJet1470to600.Sumw2();
    TH1D ResponseJet1600to800("ResponseJet1600to800","ResponseJet1600to800",40,-0.4,0.4);
    ResponseJet1600to800.Sumw2();
    TH1D ResponseJet1800to1000("ResponseJet1800to1000","ResponseJet1800to1000",40,-0.4,0.4);
    ResponseJet1800to1000.Sumw2();
    TH1D ResponseJet11000to1400("ResponseJet11000to1400","ResponseJet11000to1400",40,-0.4,0.4);
    ResponseJet11000to1400.Sumw2();
    TH1D ResponseJet11400to1800("ResponseJet11400to1800","ResponseJet11400to1800",40,-0.4,0.4);
    ResponseJet11400to1800.Sumw2();
    TH1D ResponseJet11800to2400("ResponseJet11800to2400","ResponseJet11800to2400",40,-0.4,0.4);
    ResponseJet11800to2400.Sumw2();
    TH1D ResponseJet12400to3200("ResponseJet12400to3200","ResponseJet12400to3200",40,-0.4,0.4);
    ResponseJet12400to3200.Sumw2();
    TH1D ResponseJet13200("ResponseJet13200","ResponseJet13200",40,-0.4,0.4);
    ResponseJet13200.Sumw2();

    TH1D ResponseJet250to80("ResponseJet250to80","ResponseJet250to80",40,-0.4,0.4);
    ResponseJet250to80.Sumw2();
    TH1D ResponseJet280to120("ResponseJet280to120","ResponseJet280to120",40,-0.4,0.4);
    ResponseJet280to120.Sumw2();
    TH1D ResponseJet2120to170("ResponseJet2120to170","ResponseJet2120to170",40,-0.4,0.4);
    ResponseJet2120to170.Sumw2();
    TH1D ResponseJet2170to300("ResponseJet2170to300","ResponseJet2170to300",40,-0.4,0.4);
    ResponseJet2170to300.Sumw2();
    TH1D ResponseJet2300to470("ResponseJet2300to470","ResponseJet2300to470",40,-0.4,0.4);
    ResponseJet2300to470.Sumw2();
    TH1D ResponseJet2470to600("ResponseJet2470to600","ResponseJet2470to600",40,-0.4,0.4);
    ResponseJet2470to600.Sumw2();
    TH1D ResponseJet2600to800("ResponseJet2600to800","ResponseJet2600to800",40,-0.4,0.4);
    ResponseJet2600to800.Sumw2();
    TH1D ResponseJet2800to1000("ResponseJet2800to1000","ResponseJet2800to1000",40,-0.4,0.4);
    ResponseJet2800to1000.Sumw2();
    TH1D ResponseJet21000to1400("ResponseJet21000to1400","ResponseJet21000to1400",40,-0.4,0.4);
    ResponseJet21000to1400.Sumw2();
    TH1D ResponseJet21400to1800("ResponseJet21400to1800","ResponseJet21400to1800",40,-0.4,0.4);
    ResponseJet21400to1800.Sumw2();
    TH1D ResponseJet21800to2400("ResponseJet21800to2400","ResponseJet21800to2400",40,-0.4,0.4);
    ResponseJet21800to2400.Sumw2();
    TH1D ResponseJet22400to3200("ResponseJet22400to3200","ResponseJet22400to3200",40,-0.4,0.4);
    ResponseJet22400to3200.Sumw2();
    TH1D ResponseJet23200("ResponseJet23200","ResponseJet23200",40,-0.4,0.4);
    ResponseJet23200.Sumw2();

    TH1D ResponseJet350to80("ResponseJet350to80","ResponseJet350to80",40,-0.4,0.4);
    ResponseJet350to80.Sumw2();
    TH1D ResponseJet380to120("ResponseJet380to120","ResponseJet380to120",40,-0.4,0.4);
    ResponseJet380to120.Sumw2();
    TH1D ResponseJet3120to170("ResponseJet3120to170","ResponseJet3120to170",40,-0.4,0.4);
    ResponseJet3120to170.Sumw2();
    TH1D ResponseJet3170to300("ResponseJet3170to300","ResponseJet3170to300",40,-0.4,0.4);
    ResponseJet3170to300.Sumw2();
    TH1D ResponseJet3300to470("ResponseJet3300to470","ResponseJet3300to470",40,-0.4,0.4);
    ResponseJet3300to470.Sumw2();
    TH1D ResponseJet3470to600("ResponseJet3470to600","ResponseJet3470to600",40,-0.4,0.4);
    ResponseJet3470to600.Sumw2();
    TH1D ResponseJet3600to800("ResponseJet3600to800","ResponseJet3600to800",40,-0.4,0.4);
    ResponseJet3600to800.Sumw2();
    TH1D ResponseJet3800to1000("ResponseJet3800to1000","ResponseJet3800to1000",40,-0.4,0.4);
    ResponseJet3800to1000.Sumw2();
    TH1D ResponseJet31000to1400("ResponseJet31000to1400","ResponseJet31000to1400",40,-0.4,0.4);
    ResponseJet31000to1400.Sumw2();
    TH1D ResponseJet31400to1800("ResponseJet31400to1800","ResponseJet31400to1800",40,-0.4,0.4);
    ResponseJet31400to1800.Sumw2();
    TH1D ResponseJet31800to2400("ResponseJet31800to2400","ResponseJet31800to2400",40,-0.4,0.4);
    ResponseJet31800to2400.Sumw2();
    TH1D ResponseJet32400to3200("ResponseJet32400to3200","ResponseJet32400to3200",40,-0.4,0.4);
    ResponseJet32400to3200.Sumw2();
    TH1D ResponseJet33200("ResponseJet33200","ResponseJet33200",40,-0.4,0.4);
    ResponseJet33200.Sumw2();

    float numberEntries = tree.GetEntries();

    float pi = 3.141

    std::cout << tree.GetEntries() << std::endl;
    //Fill the Hists with Root Tree Sim and Genjets
    //GetEntries();
    for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
    {
      tree.GetEntry(entry);

      if(entry % 100000 == 0)
      {
        std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
      }

      //For Jet1
      //calculate R
      float deltaPhi1 = TMath::Abs(phi1Num[0]-genphi1Num[0]);
      float deltaEta1 = eta1Num[0] - geneta1Num[0];
      if(deltaPhi1 > TMath::Pi()){
        deltaPhi1 = TMath::TwoPi() - deltaPhi1;
      }

      float R_ValueJet1 = TMath::Sqrt(deltaEta1*deltaEta1 + deltaPhi1*deltaPhi1);

      if(entry % 100000 == 0)
      {
        std::cout << to_string(R_ValueJet1) << "R_ValueJet1" << std::endl;
      }


      if(R_ValueJet1 < 0.2){

        //calculate response
        double ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        ResponseJet150to80.Fill(ResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        ResponseJet180to120.Fill(ResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        ResponseJet1120to170.Fill(ResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        ResponseJet1170to300.Fill(ResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        ResponseJet1300to470.Fill(ResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        ResponseJet1470to600.Fill(ResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        ResponseJet1600to800.Fill(ResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        ResponseJet1800to1000.Fill(ResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        ResponseJet11000to1400.Fill(ResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        ResponseJet11400to1800.Fill(ResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        ResponseJet11800to2400.Fill(ResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        ResponseJet12400to3200.Fill(ResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        ResponseJet13200.Fill(ResponseJet1);
        }

        if(abs(geneta1Num[0]) < 1.3 ){
            //calculate response
        double Eta0to1p3ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        Eta0to1p3ResponseJet150to80.Fill(Eta0to1p3ResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        Eta0to1p3ResponseJet180to120.Fill(Eta0to1p3ResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        Eta0to1p3ResponseJet1120to170.Fill(Eta0to1p3ResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        Eta0to1p3ResponseJet1170to300.Fill(Eta0to1p3ResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        Eta0to1p3ResponseJet1300to470.Fill(Eta0to1p3ResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        Eta0to1p3ResponseJet1470to600.Fill(Eta0to1p3ResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        Eta0to1p3ResponseJet1600to800.Fill(Eta0to1p3ResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        Eta0to1p3ResponseJet1800to1000.Fill(Eta0to1p3ResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        Eta0to1p3ResponseJet11000to1400.Fill(Eta0to1p3ResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        Eta0to1p3ResponseJet11400to1800.Fill(Eta0to1p3ResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        Eta0to1p3ResponseJet11800to2400.Fill(Eta0to1p3ResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        Eta0to1p3ResponseJet12400to3200.Fill(Eta0to1p3ResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        Eta0to1p3ResponseJet13200.Fill(Eta0to1p3ResponseJet1);
        }
        }
        if(abs(geneta1Num[0])  >= 1.3 && abs(geneta1Num[0]) < 2.5){
            //calculate response
        double Eta1p3to2p5ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        Eta1p3to2p5ResponseJet150to80.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        Eta1p3to2p5ResponseJet180to120.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        Eta1p3to2p5ResponseJet1120to170.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        Eta1p3to2p5ResponseJet1170to300.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        Eta1p3to2p5ResponseJet1300to470.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        Eta1p3to2p5ResponseJet1470to600.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        Eta1p3to2p5ResponseJet1600to800.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        Eta1p3to2p5ResponseJet1800to1000.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        Eta1p3to2p5ResponseJet11000to1400.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        Eta1p3to2p5ResponseJet11400to1800.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        Eta1p3to2p5ResponseJet11800to2400.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        Eta1p3to2p5ResponseJet12400to3200.Fill(Eta1p3to2p5ResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        Eta1p3to2p5ResponseJet13200.Fill(Eta1p3to2p5ResponseJet1);
        }
        }
        if(abs(geneta1Num[0])  >= 2.5 && abs(geneta1Num[0]) < 3.0){
            //calculate response
        double Eta2p5to3ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        Eta2p5to3ResponseJet150to80.Fill(Eta2p5to3ResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        Eta2p5to3ResponseJet180to120.Fill(Eta2p5to3ResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        Eta2p5to3ResponseJet1120to170.Fill(Eta2p5to3ResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        Eta2p5to3ResponseJet1170to300.Fill(Eta2p5to3ResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        Eta2p5to3ResponseJet1300to470.Fill(Eta2p5to3ResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        Eta2p5to3ResponseJet1470to600.Fill(Eta2p5to3ResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        Eta2p5to3ResponseJet1600to800.Fill(Eta2p5to3ResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        Eta2p5to3ResponseJet1800to1000.Fill(Eta2p5to3ResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        Eta2p5to3ResponseJet11000to1400.Fill(Eta2p5to3ResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        Eta2p5to3ResponseJet11400to1800.Fill(Eta2p5to3ResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        Eta2p5to3ResponseJet11800to2400.Fill(Eta2p5to3ResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        Eta2p5to3ResponseJet12400to3200.Fill(Eta2p5to3ResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        Eta2p5to3ResponseJet13200.Fill(Eta2p5to3ResponseJet1);
        }
        }
        if(abs(geneta1Num[0])  >= 3.0 && abs(geneta1Num[0]) < 5.0){
            //calculate response
        double Eta3to5ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        Eta3to5ResponseJet150to80.Fill(Eta3to5ResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        Eta3to5ResponseJet180to120.Fill(Eta3to5ResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        Eta3to5ResponseJet1120to170.Fill(Eta3to5ResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        Eta3to5ResponseJet1170to300.Fill(Eta3to5ResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        Eta3to5ResponseJet1300to470.Fill(Eta3to5ResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        Eta3to5ResponseJet1470to600.Fill(Eta3to5ResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        Eta3to5ResponseJet1600to800.Fill(Eta3to5ResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        Eta3to5ResponseJet1800to1000.Fill(Eta3to5ResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        Eta3to5ResponseJet11000to1400.Fill(Eta3to5ResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        Eta3to5ResponseJet11400to1800.Fill(Eta3to5ResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        Eta3to5ResponseJet11800to2400.Fill(Eta3to5ResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        Eta3to5ResponseJet12400to3200.Fill(Eta3to5ResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        Eta3to5ResponseJet13200.Fill(Eta3to5ResponseJet1);
        }
        }
      }

      //For Jet2
      //calculate R
      double R_ValueJet2 = sqrt(pow(phi2Num[0]-genphi2Num[0],2)*pow(eta2Num[0]-geneta2Num[0],2));

      if(entry % 100000 == 0)
      {
        std::cout << to_string(R_ValueJet2) << "R_ValueJet2" << std::endl;
        std::cout << to_string(genpt2Num[0]) << "pt2Num[0]" << std::endl;
        std::cout << to_string(geneta2Num[0]) << "geneta2Num[0]" << std::endl;
        std::cout << to_string(phi2Num[0]) << "phi2Num[0]" << std::endl;
        std::cout << to_string(genphi2Num[0]) << "genphi2Num[0]" << std::endl;
        std::cout << to_string(eta2Num[0]) << "eta2Num[0]" << std::endl;
        std::cout << to_string(geneta2Num[0]) << "geneta2Num[0]" << std::endl;
      }

      if(R_ValueJet2 < 0.2){

        //calculate response
        double ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        ResponseJet250to80.Fill(ResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        ResponseJet280to120.Fill(ResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        ResponseJet2120to170.Fill(ResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        ResponseJet2170to300.Fill(ResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        ResponseJet2300to470.Fill(ResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        ResponseJet2470to600.Fill(ResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        ResponseJet2600to800.Fill(ResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        ResponseJet2800to1000.Fill(ResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        ResponseJet21000to1400.Fill(ResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        ResponseJet21400to1800.Fill(ResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        ResponseJet21800to2400.Fill(ResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        ResponseJet22400to3200.Fill(ResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        ResponseJet23200.Fill(ResponseJet2);
        }

        if(abs(geneta2Num[0]) < 1.3 ){
            //calculate response
        double Eta0to1p3ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        Eta0to1p3ResponseJet250to80.Fill(Eta0to1p3ResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        Eta0to1p3ResponseJet280to120.Fill(Eta0to1p3ResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        Eta0to1p3ResponseJet2120to170.Fill(Eta0to1p3ResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        Eta0to1p3ResponseJet2170to300.Fill(Eta0to1p3ResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        Eta0to1p3ResponseJet2300to470.Fill(Eta0to1p3ResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        Eta0to1p3ResponseJet2470to600.Fill(Eta0to1p3ResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        Eta0to1p3ResponseJet2600to800.Fill(Eta0to1p3ResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        Eta0to1p3ResponseJet2800to1000.Fill(Eta0to1p3ResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        Eta0to1p3ResponseJet21000to1400.Fill(Eta0to1p3ResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        Eta0to1p3ResponseJet21400to1800.Fill(Eta0to1p3ResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        Eta0to1p3ResponseJet21800to2400.Fill(Eta0to1p3ResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        Eta0to1p3ResponseJet22400to3200.Fill(Eta0to1p3ResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        Eta0to1p3ResponseJet23200.Fill(Eta0to1p3ResponseJet2);
        }
        }
        if(abs(geneta2Num[0])  >= 1.3 && abs(geneta2Num[0]) < 2.5){
            //calculate response
        double Eta1p3to2p5ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        Eta1p3to2p5ResponseJet250to80.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        Eta1p3to2p5ResponseJet280to120.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        Eta1p3to2p5ResponseJet2120to170.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        Eta1p3to2p5ResponseJet2170to300.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        Eta1p3to2p5ResponseJet2300to470.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        Eta1p3to2p5ResponseJet2470to600.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        Eta1p3to2p5ResponseJet2600to800.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        Eta1p3to2p5ResponseJet2800to1000.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        Eta1p3to2p5ResponseJet21000to1400.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        Eta1p3to2p5ResponseJet21400to1800.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        Eta1p3to2p5ResponseJet21800to2400.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        Eta1p3to2p5ResponseJet22400to3200.Fill(Eta1p3to2p5ResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        Eta1p3to2p5ResponseJet23200.Fill(Eta1p3to2p5ResponseJet2);
        }
        }
        if(abs(geneta2Num[0])  >= 2.5 && abs(geneta2Num[0]) < 3.0){
            //calculate response
        double Eta2p5to3ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        Eta2p5to3ResponseJet250to80.Fill(Eta2p5to3ResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        Eta2p5to3ResponseJet280to120.Fill(Eta2p5to3ResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        Eta2p5to3ResponseJet2120to170.Fill(Eta2p5to3ResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        Eta2p5to3ResponseJet2170to300.Fill(Eta2p5to3ResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        Eta2p5to3ResponseJet2300to470.Fill(Eta2p5to3ResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        Eta2p5to3ResponseJet2470to600.Fill(Eta2p5to3ResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        Eta2p5to3ResponseJet2600to800.Fill(Eta2p5to3ResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        Eta2p5to3ResponseJet2800to1000.Fill(Eta2p5to3ResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        Eta2p5to3ResponseJet21000to1400.Fill(Eta2p5to3ResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        Eta2p5to3ResponseJet21400to1800.Fill(Eta2p5to3ResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        Eta2p5to3ResponseJet21800to2400.Fill(Eta2p5to3ResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        Eta2p5to3ResponseJet22400to3200.Fill(Eta2p5to3ResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        Eta2p5to3ResponseJet23200.Fill(Eta2p5to3ResponseJet2);
        }
        }
        if(abs(geneta2Num[0])  >= 3.0 && abs(geneta2Num[0]) < 5.0){
            //calculate response
        double Eta3to5ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        Eta3to5ResponseJet250to80.Fill(Eta3to5ResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        Eta3to5ResponseJet280to120.Fill(Eta3to5ResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        Eta3to5ResponseJet2120to170.Fill(Eta3to5ResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        Eta3to5ResponseJet2170to300.Fill(Eta3to5ResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        Eta3to5ResponseJet2300to470.Fill(Eta3to5ResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        Eta3to5ResponseJet2470to600.Fill(Eta3to5ResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        Eta3to5ResponseJet2600to800.Fill(Eta3to5ResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        Eta3to5ResponseJet2800to1000.Fill(Eta3to5ResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        Eta3to5ResponseJet21000to1400.Fill(Eta3to5ResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        Eta3to5ResponseJet21400to1800.Fill(Eta3to5ResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        Eta3to5ResponseJet21800to2400.Fill(Eta3to5ResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        Eta3to5ResponseJet22400to3200.Fill(Eta3to5ResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        Eta3to5ResponseJet23200.Fill(Eta3to5ResponseJet2);
        }
        }
      }

      //For Jet3
      //calculate R
      double R_ValueJet3 = sqrt(pow(phi3Num[0]-genphi3Num[0],2)*pow(eta3Num[0]-geneta3Num[0],2));

      if(entry % 100000 == 0)
      {
        std::cout << to_string(R_ValueJet3) << "R_ValueJet3" << std::endl;
        std::cout << to_string(genpt3Num[0]) << "pt3Num[0]" << std::endl;
        std::cout << to_string(geneta3Num[0]) << "geneta3Num[0]" << std::endl;
        std::cout << to_string(phi3Num[0]) << "phi3Num[0]" << std::endl;
        std::cout << to_string(genphi3Num[0]) << "genphi3Num[0]" << std::endl;
        std::cout << to_string(eta3Num[0]) << "eta3Num[0]" << std::endl;
        std::cout << to_string(geneta3Num[0]) << "geneta3Num[0]" << std::endl;
      }

      if(R_ValueJet3 < 0.2){

        //calculate response
        double ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        ResponseJet350to80.Fill(ResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        ResponseJet380to120.Fill(ResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        ResponseJet3120to170.Fill(ResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        ResponseJet3170to300.Fill(ResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        ResponseJet3300to470.Fill(ResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        ResponseJet3470to600.Fill(ResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        ResponseJet3600to800.Fill(ResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        ResponseJet3800to1000.Fill(ResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        ResponseJet31000to1400.Fill(ResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        ResponseJet31400to1800.Fill(ResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        ResponseJet31800to2400.Fill(ResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        ResponseJet32400to3200.Fill(ResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        ResponseJet33200.Fill(ResponseJet3);
        }

        if(abs(geneta3Num[0]) < 1.3 ){
            //calculate response
        double Eta0to1p3ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        Eta0to1p3ResponseJet350to80.Fill(Eta0to1p3ResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        Eta0to1p3ResponseJet380to120.Fill(Eta0to1p3ResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        Eta0to1p3ResponseJet3120to170.Fill(Eta0to1p3ResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        Eta0to1p3ResponseJet3170to300.Fill(Eta0to1p3ResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        Eta0to1p3ResponseJet3300to470.Fill(Eta0to1p3ResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        Eta0to1p3ResponseJet3470to600.Fill(Eta0to1p3ResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        Eta0to1p3ResponseJet3600to800.Fill(Eta0to1p3ResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        Eta0to1p3ResponseJet3800to1000.Fill(Eta0to1p3ResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        Eta0to1p3ResponseJet31000to1400.Fill(Eta0to1p3ResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        Eta0to1p3ResponseJet31400to1800.Fill(Eta0to1p3ResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        Eta0to1p3ResponseJet31800to2400.Fill(Eta0to1p3ResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        Eta0to1p3ResponseJet32400to3200.Fill(Eta0to1p3ResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        Eta0to1p3ResponseJet33200.Fill(Eta0to1p3ResponseJet3);
        }
        }
        if(abs(geneta3Num[0])  >= 1.3 && abs(geneta3Num[0]) < 2.5){
            //calculate response
        double Eta1p3to2p5ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        Eta1p3to2p5ResponseJet350to80.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        Eta1p3to2p5ResponseJet380to120.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        Eta1p3to2p5ResponseJet3120to170.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        Eta1p3to2p5ResponseJet3170to300.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        Eta1p3to2p5ResponseJet3300to470.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        Eta1p3to2p5ResponseJet3470to600.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        Eta1p3to2p5ResponseJet3600to800.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        Eta1p3to2p5ResponseJet3800to1000.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        Eta1p3to2p5ResponseJet31000to1400.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        Eta1p3to2p5ResponseJet31400to1800.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        Eta1p3to2p5ResponseJet31800to2400.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        Eta1p3to2p5ResponseJet32400to3200.Fill(Eta1p3to2p5ResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        Eta1p3to2p5ResponseJet33200.Fill(Eta1p3to2p5ResponseJet3);
        }
        }
        if(abs(geneta3Num[0])  >= 2.5 && abs(geneta3Num[0]) < 3.0){
            //calculate response
        double Eta2p5to3ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        Eta2p5to3ResponseJet350to80.Fill(Eta2p5to3ResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        Eta2p5to3ResponseJet380to120.Fill(Eta2p5to3ResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        Eta2p5to3ResponseJet3120to170.Fill(Eta2p5to3ResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        Eta2p5to3ResponseJet3170to300.Fill(Eta2p5to3ResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        Eta2p5to3ResponseJet3300to470.Fill(Eta2p5to3ResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        Eta2p5to3ResponseJet3470to600.Fill(Eta2p5to3ResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        Eta2p5to3ResponseJet3600to800.Fill(Eta2p5to3ResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        Eta2p5to3ResponseJet3800to1000.Fill(Eta2p5to3ResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        Eta2p5to3ResponseJet31000to1400.Fill(Eta2p5to3ResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        Eta2p5to3ResponseJet31400to1800.Fill(Eta2p5to3ResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        Eta2p5to3ResponseJet31800to2400.Fill(Eta2p5to3ResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        Eta2p5to3ResponseJet32400to3200.Fill(Eta2p5to3ResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        Eta2p5to3ResponseJet33200.Fill(Eta2p5to3ResponseJet3);
        }
        }
        if(abs(geneta3Num[0])  >= 3.0 && abs(geneta3Num[0]) < 5.0){
            //calculate response
        double Eta3to5ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        Eta3to5ResponseJet350to80.Fill(Eta3to5ResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        Eta3to5ResponseJet380to120.Fill(Eta3to5ResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        Eta3to5ResponseJet3120to170.Fill(Eta3to5ResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        Eta3to5ResponseJet3170to300.Fill(Eta3to5ResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        Eta3to5ResponseJet3300to470.Fill(Eta3to5ResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        Eta3to5ResponseJet3470to600.Fill(Eta3to5ResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        Eta3to5ResponseJet3600to800.Fill(Eta3to5ResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        Eta3to5ResponseJet3800to1000.Fill(Eta3to5ResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        Eta3to5ResponseJet31000to1400.Fill(Eta3to5ResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        Eta3to5ResponseJet31400to1800.Fill(Eta3to5ResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        Eta3to5ResponseJet31800to2400.Fill(Eta3to5ResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        Eta3to5ResponseJet32400to3200.Fill(Eta3to5ResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        Eta3to5ResponseJet33200.Fill(Eta3to5ResponseJet3);
        }
        }
      }

    }

    //Neccesary so files dont get lost
    Eta1p3to2p5ResponseJet150to80.SetDirectory(0);
    Eta1p3to2p5ResponseJet180to120.SetDirectory(0);
    Eta1p3to2p5ResponseJet1120to170.SetDirectory(0);
    Eta1p3to2p5ResponseJet1170to300.SetDirectory(0);
    Eta1p3to2p5ResponseJet1300to470.SetDirectory(0);
    Eta1p3to2p5ResponseJet1470to600.SetDirectory(0);
    Eta1p3to2p5ResponseJet1600to800.SetDirectory(0);
    Eta1p3to2p5ResponseJet1800to1000.SetDirectory(0);
    Eta1p3to2p5ResponseJet11000to1400.SetDirectory(0);
    Eta1p3to2p5ResponseJet11400to1800.SetDirectory(0);
    Eta1p3to2p5ResponseJet11800to2400.SetDirectory(0);
    Eta1p3to2p5ResponseJet12400to3200.SetDirectory(0);
    Eta1p3to2p5ResponseJet13200.SetDirectory(0);
    Eta1p3to2p5ResponseJet250to80.SetDirectory(0);
    Eta1p3to2p5ResponseJet280to120.SetDirectory(0);
    Eta1p3to2p5ResponseJet2120to170.SetDirectory(0);
    Eta1p3to2p5ResponseJet2170to300.SetDirectory(0);
    Eta1p3to2p5ResponseJet2300to470.SetDirectory(0);
    Eta1p3to2p5ResponseJet2470to600.SetDirectory(0);
    Eta1p3to2p5ResponseJet2600to800.SetDirectory(0);
    Eta1p3to2p5ResponseJet2800to1000.SetDirectory(0);
    Eta1p3to2p5ResponseJet21000to1400.SetDirectory(0);
    Eta1p3to2p5ResponseJet21400to1800.SetDirectory(0);
    Eta1p3to2p5ResponseJet21800to2400.SetDirectory(0);
    Eta1p3to2p5ResponseJet22400to3200.SetDirectory(0);
    Eta1p3to2p5ResponseJet23200.SetDirectory(0);
    Eta1p3to2p5ResponseJet350to80.SetDirectory(0);
    Eta1p3to2p5ResponseJet380to120.SetDirectory(0);
    Eta1p3to2p5ResponseJet3120to170.SetDirectory(0);
    Eta1p3to2p5ResponseJet3170to300.SetDirectory(0);
    Eta1p3to2p5ResponseJet3300to470.SetDirectory(0);
    Eta1p3to2p5ResponseJet3470to600.SetDirectory(0);
    Eta1p3to2p5ResponseJet3600to800.SetDirectory(0);
    Eta1p3to2p5ResponseJet3800to1000.SetDirectory(0);
    Eta1p3to2p5ResponseJet31000to1400.SetDirectory(0);
    Eta1p3to2p5ResponseJet31400to1800.SetDirectory(0);
    Eta1p3to2p5ResponseJet31800to2400.SetDirectory(0);
    Eta1p3to2p5ResponseJet32400to3200.SetDirectory(0);
    Eta1p3to2p5ResponseJet33200.SetDirectory(0);
    Eta0to1p3ResponseJet150to80.SetDirectory(0);
    Eta0to1p3ResponseJet180to120.SetDirectory(0);
    Eta0to1p3ResponseJet1120to170.SetDirectory(0);
    Eta0to1p3ResponseJet1170to300.SetDirectory(0);
    Eta0to1p3ResponseJet1300to470.SetDirectory(0);
    Eta0to1p3ResponseJet1470to600.SetDirectory(0);
    Eta0to1p3ResponseJet1600to800.SetDirectory(0);
    Eta0to1p3ResponseJet1800to1000.SetDirectory(0);
    Eta0to1p3ResponseJet11000to1400.SetDirectory(0);
    Eta0to1p3ResponseJet11400to1800.SetDirectory(0);
    Eta0to1p3ResponseJet11800to2400.SetDirectory(0);
    Eta0to1p3ResponseJet12400to3200.SetDirectory(0);
    Eta0to1p3ResponseJet13200.SetDirectory(0);
    Eta0to1p3ResponseJet250to80.SetDirectory(0);
    Eta0to1p3ResponseJet280to120.SetDirectory(0);
    Eta0to1p3ResponseJet2120to170.SetDirectory(0);
    Eta0to1p3ResponseJet2170to300.SetDirectory(0);
    Eta0to1p3ResponseJet2300to470.SetDirectory(0);
    Eta0to1p3ResponseJet2470to600.SetDirectory(0);
    Eta0to1p3ResponseJet2600to800.SetDirectory(0);
    Eta0to1p3ResponseJet2800to1000.SetDirectory(0);
    Eta0to1p3ResponseJet21000to1400.SetDirectory(0);
    Eta0to1p3ResponseJet21400to1800.SetDirectory(0);
    Eta0to1p3ResponseJet21800to2400.SetDirectory(0);
    Eta0to1p3ResponseJet22400to3200.SetDirectory(0);
    Eta0to1p3ResponseJet23200.SetDirectory(0);
    Eta0to1p3ResponseJet350to80.SetDirectory(0);
    Eta0to1p3ResponseJet380to120.SetDirectory(0);
    Eta0to1p3ResponseJet3120to170.SetDirectory(0);
    Eta0to1p3ResponseJet3170to300.SetDirectory(0);
    Eta0to1p3ResponseJet3300to470.SetDirectory(0);
    Eta0to1p3ResponseJet3470to600.SetDirectory(0);
    Eta0to1p3ResponseJet3600to800.SetDirectory(0);
    Eta0to1p3ResponseJet3800to1000.SetDirectory(0);
    Eta0to1p3ResponseJet31000to1400.SetDirectory(0);
    Eta0to1p3ResponseJet31400to1800.SetDirectory(0);
    Eta0to1p3ResponseJet31800to2400.SetDirectory(0);
    Eta0to1p3ResponseJet32400to3200.SetDirectory(0);
    Eta0to1p3ResponseJet33200.SetDirectory(0);
    ResponseJet150to80.SetDirectory(0);
    ResponseJet180to120.SetDirectory(0);
    ResponseJet1120to170.SetDirectory(0);
    ResponseJet1170to300.SetDirectory(0);
    ResponseJet1300to470.SetDirectory(0);
    ResponseJet1470to600.SetDirectory(0);
    ResponseJet1600to800.SetDirectory(0);
    ResponseJet1800to1000.SetDirectory(0);
    ResponseJet11000to1400.SetDirectory(0);
    ResponseJet11400to1800.SetDirectory(0);
    ResponseJet11800to2400.SetDirectory(0);
    ResponseJet12400to3200.SetDirectory(0);
    ResponseJet13200.SetDirectory(0);
    ResponseJet250to80.SetDirectory(0);
    ResponseJet280to120.SetDirectory(0);
    ResponseJet2120to170.SetDirectory(0);
    ResponseJet2170to300.SetDirectory(0);
    ResponseJet2300to470.SetDirectory(0);
    ResponseJet2470to600.SetDirectory(0);
    ResponseJet2600to800.SetDirectory(0);
    ResponseJet2800to1000.SetDirectory(0);
    ResponseJet21000to1400.SetDirectory(0);
    ResponseJet21400to1800.SetDirectory(0);
    ResponseJet21800to2400.SetDirectory(0);
    ResponseJet22400to3200.SetDirectory(0);
    ResponseJet23200.SetDirectory(0);
    ResponseJet350to80.SetDirectory(0);
    ResponseJet380to120.SetDirectory(0);
    ResponseJet3120to170.SetDirectory(0);
    ResponseJet3170to300.SetDirectory(0);
    ResponseJet3300to470.SetDirectory(0);
    ResponseJet3470to600.SetDirectory(0);
    ResponseJet3600to800.SetDirectory(0);
    ResponseJet3800to1000.SetDirectory(0);
    ResponseJet31000to1400.SetDirectory(0);
    ResponseJet31400to1800.SetDirectory(0);
    ResponseJet31800to2400.SetDirectory(0);
    ResponseJet32400to3200.SetDirectory(0);
    ResponseJet33200.SetDirectory(0);
    Eta2p5to3ResponseJet150to80.SetDirectory(0);
    Eta2p5to3ResponseJet180to120.SetDirectory(0);
    Eta2p5to3ResponseJet1120to170.SetDirectory(0);
    Eta2p5to3ResponseJet1170to300.SetDirectory(0);
    Eta2p5to3ResponseJet1300to470.SetDirectory(0);
    Eta2p5to3ResponseJet1470to600.SetDirectory(0);
    Eta2p5to3ResponseJet1600to800.SetDirectory(0);
    Eta2p5to3ResponseJet1800to1000.SetDirectory(0);
    Eta2p5to3ResponseJet11000to1400.SetDirectory(0);
    Eta2p5to3ResponseJet11400to1800.SetDirectory(0);
    Eta2p5to3ResponseJet11800to2400.SetDirectory(0);
    Eta2p5to3ResponseJet12400to3200.SetDirectory(0);
    Eta2p5to3ResponseJet13200.SetDirectory(0);
    Eta2p5to3ResponseJet250to80.SetDirectory(0);
    Eta2p5to3ResponseJet280to120.SetDirectory(0);
    Eta2p5to3ResponseJet2120to170.SetDirectory(0);
    Eta2p5to3ResponseJet2170to300.SetDirectory(0);
    Eta2p5to3ResponseJet2300to470.SetDirectory(0);
    Eta2p5to3ResponseJet2470to600.SetDirectory(0);
    Eta2p5to3ResponseJet2600to800.SetDirectory(0);
    Eta2p5to3ResponseJet2800to1000.SetDirectory(0);
    Eta2p5to3ResponseJet21000to1400.SetDirectory(0);
    Eta2p5to3ResponseJet21400to1800.SetDirectory(0);
    Eta2p5to3ResponseJet21800to2400.SetDirectory(0);
    Eta2p5to3ResponseJet22400to3200.SetDirectory(0);
    Eta2p5to3ResponseJet23200.SetDirectory(0);
    Eta2p5to3ResponseJet350to80.SetDirectory(0);
    Eta2p5to3ResponseJet380to120.SetDirectory(0);
    Eta2p5to3ResponseJet3120to170.SetDirectory(0);
    Eta2p5to3ResponseJet3170to300.SetDirectory(0);
    Eta2p5to3ResponseJet3300to470.SetDirectory(0);
    Eta2p5to3ResponseJet3470to600.SetDirectory(0);
    Eta2p5to3ResponseJet3600to800.SetDirectory(0);
    Eta2p5to3ResponseJet3800to1000.SetDirectory(0);
    Eta2p5to3ResponseJet31000to1400.SetDirectory(0);
    Eta2p5to3ResponseJet31400to1800.SetDirectory(0);
    Eta2p5to3ResponseJet31800to2400.SetDirectory(0);
    Eta2p5to3ResponseJet32400to3200.SetDirectory(0);
    Eta3to5ResponseJet150to80.SetDirectory(0);
    Eta3to5ResponseJet180to120.SetDirectory(0);
    Eta3to5ResponseJet1120to170.SetDirectory(0);
    Eta3to5ResponseJet1170to300.SetDirectory(0);
    Eta3to5ResponseJet1300to470.SetDirectory(0);
    Eta3to5ResponseJet1470to600.SetDirectory(0);
    Eta3to5ResponseJet1600to800.SetDirectory(0);
    Eta3to5ResponseJet1800to1000.SetDirectory(0);
    Eta3to5ResponseJet11000to1400.SetDirectory(0);
    Eta3to5ResponseJet11400to1800.SetDirectory(0);
    Eta3to5ResponseJet11800to2400.SetDirectory(0);
    Eta3to5ResponseJet12400to3200.SetDirectory(0);
    Eta3to5ResponseJet13200.SetDirectory(0);
    Eta3to5ResponseJet250to80.SetDirectory(0);
    Eta3to5ResponseJet280to120.SetDirectory(0);
    Eta3to5ResponseJet2120to170.SetDirectory(0);
    Eta3to5ResponseJet2170to300.SetDirectory(0);
    Eta3to5ResponseJet2300to470.SetDirectory(0);
    Eta3to5ResponseJet2470to600.SetDirectory(0);
    Eta3to5ResponseJet2600to800.SetDirectory(0);
    Eta3to5ResponseJet2800to1000.SetDirectory(0);
    Eta3to5ResponseJet21000to1400.SetDirectory(0);
    Eta3to5ResponseJet21400to1800.SetDirectory(0);
    Eta3to5ResponseJet21800to2400.SetDirectory(0);
    Eta3to5ResponseJet22400to3200.SetDirectory(0);
    Eta3to5ResponseJet23200.SetDirectory(0);
    Eta3to5ResponseJet350to80.SetDirectory(0);
    Eta3to5ResponseJet380to120.SetDirectory(0);
    Eta3to5ResponseJet3120to170.SetDirectory(0);
    Eta3to5ResponseJet3170to300.SetDirectory(0);
    Eta3to5ResponseJet3300to470.SetDirectory(0);
    Eta3to5ResponseJet3470to600.SetDirectory(0);
    Eta3to5ResponseJet3600to800.SetDirectory(0);
    Eta3to5ResponseJet3800to1000.SetDirectory(0);
    Eta3to5ResponseJet31000to1400.SetDirectory(0);
    Eta3to5ResponseJet31400to1800.SetDirectory(0);
    Eta3to5ResponseJet31800to2400.SetDirectory(0);
    Eta3to5ResponseJet32400to3200.SetDirectory(0);


    TFile* outHistFile1 = TFile::Open(outNameJet1,"RECREATE");
    ResponseJet150to80.Write();
    ResponseJet180to120.Write();
    ResponseJet1120to170.Write();
    ResponseJet1170to300.Write();
    ResponseJet1300to470.Write();
    ResponseJet1470to600.Write();
    ResponseJet1600to800.Write();
    ResponseJet1800to1000.Write();
    ResponseJet11000to1400.Write();
    ResponseJet11400to1800.Write();
    ResponseJet11800to2400.Write();
    ResponseJet12400to3200.Write();
    ResponseJet13200.Write();
    Eta0to1p3ResponseJet150to80.Write();
    Eta0to1p3ResponseJet180to120.Write();
    Eta0to1p3ResponseJet1120to170.Write();
    Eta0to1p3ResponseJet1170to300.Write();
    Eta0to1p3ResponseJet1300to470.Write();
    Eta0to1p3ResponseJet1470to600.Write();
    Eta0to1p3ResponseJet1600to800.Write();
    Eta0to1p3ResponseJet1800to1000.Write();
    Eta0to1p3ResponseJet11000to1400.Write();
    Eta0to1p3ResponseJet11400to1800.Write();
    Eta0to1p3ResponseJet11800to2400.Write();
    Eta0to1p3ResponseJet12400to3200.Write();
    Eta0to1p3ResponseJet13200.Write();
    Eta1p3to2p5ResponseJet150to80.Write();
    Eta1p3to2p5ResponseJet180to120.Write();
    Eta1p3to2p5ResponseJet1120to170.Write();
    Eta1p3to2p5ResponseJet1170to300.Write();
    Eta1p3to2p5ResponseJet1300to470.Write();
    Eta1p3to2p5ResponseJet1470to600.Write();
    Eta1p3to2p5ResponseJet1600to800.Write();
    Eta1p3to2p5ResponseJet1800to1000.Write();
    Eta1p3to2p5ResponseJet11000to1400.Write();
    Eta1p3to2p5ResponseJet11400to1800.Write();
    Eta1p3to2p5ResponseJet11800to2400.Write();
    Eta1p3to2p5ResponseJet12400to3200.Write();
    Eta1p3to2p5ResponseJet13200.Write();
    Eta2p5to3ResponseJet150to80.Write();
    Eta2p5to3ResponseJet180to120.Write();
    Eta2p5to3ResponseJet1120to170.Write();
    Eta2p5to3ResponseJet1170to300.Write();
    Eta2p5to3ResponseJet1300to470.Write();
    Eta2p5to3ResponseJet1470to600.Write();
    Eta2p5to3ResponseJet1600to800.Write();
    Eta2p5to3ResponseJet1800to1000.Write();
    Eta2p5to3ResponseJet11000to1400.Write();
    Eta2p5to3ResponseJet11400to1800.Write();
    Eta2p5to3ResponseJet11800to2400.Write();
    Eta2p5to3ResponseJet12400to3200.Write();
    Eta2p5to3ResponseJet13200.Write();
    Eta3to5ResponseJet150to80.Write();
    Eta3to5ResponseJet180to120.Write();
    Eta3to5ResponseJet1120to170.Write();
    Eta3to5ResponseJet1170to300.Write();
    Eta3to5ResponseJet1300to470.Write();
    Eta3to5ResponseJet1470to600.Write();
    Eta3to5ResponseJet1600to800.Write();
    Eta3to5ResponseJet1800to1000.Write();
    Eta3to5ResponseJet11000to1400.Write();
    Eta3to5ResponseJet11400to1800.Write();
    Eta3to5ResponseJet11800to2400.Write();
    Eta3to5ResponseJet12400to3200.Write();
    Eta3to5ResponseJet13200.Write();
    outHistFile1->Close();

    TFile* outHistFile2 = TFile::Open(outNameJet2,"RECREATE");
    ResponseJet250to80.Write();
    ResponseJet280to120.Write();
    ResponseJet2120to170.Write();
    ResponseJet2170to300.Write();
    ResponseJet2300to470.Write();
    ResponseJet2470to600.Write();
    ResponseJet2600to800.Write();
    ResponseJet2800to1000.Write();
    ResponseJet21000to1400.Write();
    ResponseJet21400to1800.Write();
    ResponseJet21800to2400.Write();
    ResponseJet22400to3200.Write();
    ResponseJet23200.Write();
    Eta0to1p3ResponseJet250to80.Write();
    Eta0to1p3ResponseJet280to120.Write();
    Eta0to1p3ResponseJet2120to170.Write();
    Eta0to1p3ResponseJet2170to300.Write();
    Eta0to1p3ResponseJet2300to470.Write();
    Eta0to1p3ResponseJet2470to600.Write();
    Eta0to1p3ResponseJet2600to800.Write();
    Eta0to1p3ResponseJet2800to1000.Write();
    Eta0to1p3ResponseJet21000to1400.Write();
    Eta0to1p3ResponseJet21400to1800.Write();
    Eta0to1p3ResponseJet21800to2400.Write();
    Eta0to1p3ResponseJet22400to3200.Write();
    Eta0to1p3ResponseJet23200.Write();
    Eta1p3to2p5ResponseJet250to80.Write();
    Eta1p3to2p5ResponseJet280to120.Write();
    Eta1p3to2p5ResponseJet2120to170.Write();
    Eta1p3to2p5ResponseJet2170to300.Write();
    Eta1p3to2p5ResponseJet2300to470.Write();
    Eta1p3to2p5ResponseJet2470to600.Write();
    Eta1p3to2p5ResponseJet2600to800.Write();
    Eta1p3to2p5ResponseJet2800to1000.Write();
    Eta1p3to2p5ResponseJet21000to1400.Write();
    Eta1p3to2p5ResponseJet21400to1800.Write();
    Eta1p3to2p5ResponseJet21800to2400.Write();
    Eta1p3to2p5ResponseJet22400to3200.Write();
    Eta1p3to2p5ResponseJet23200.Write();
    Eta2p5to3ResponseJet250to80.Write();
    Eta2p5to3ResponseJet280to120.Write();
    Eta2p5to3ResponseJet2120to170.Write();
    Eta2p5to3ResponseJet2170to300.Write();
    Eta2p5to3ResponseJet2300to470.Write();
    Eta2p5to3ResponseJet2470to600.Write();
    Eta2p5to3ResponseJet2600to800.Write();
    Eta2p5to3ResponseJet2800to1000.Write();
    Eta2p5to3ResponseJet21000to1400.Write();
    Eta2p5to3ResponseJet21400to1800.Write();
    Eta2p5to3ResponseJet21800to2400.Write();
    Eta2p5to3ResponseJet22400to3200.Write();
    Eta2p5to3ResponseJet23200.Write();
    Eta3to5ResponseJet250to80.Write();
    Eta3to5ResponseJet280to120.Write();
    Eta3to5ResponseJet2120to170.Write();
    Eta3to5ResponseJet2170to300.Write();
    Eta3to5ResponseJet2300to470.Write();
    Eta3to5ResponseJet2470to600.Write();
    Eta3to5ResponseJet2600to800.Write();
    Eta3to5ResponseJet2800to1000.Write();
    Eta3to5ResponseJet21000to1400.Write();
    Eta3to5ResponseJet21400to1800.Write();
    Eta3to5ResponseJet21800to2400.Write();
    Eta3to5ResponseJet22400to3200.Write();
    Eta3to5ResponseJet23200.Write();
    outHistFile2->Close();

    TFile* outHistFile3 = TFile::Open(outNameJet3,"RECREATE");
    ResponseJet350to80.Write();
    ResponseJet380to120.Write();
    ResponseJet3120to170.Write();
    ResponseJet3170to300.Write();
    ResponseJet3300to470.Write();
    ResponseJet3470to600.Write();
    ResponseJet3600to800.Write();
    ResponseJet3800to1000.Write();
    ResponseJet31000to1400.Write();
    ResponseJet31400to1800.Write();
    ResponseJet31800to2400.Write();
    ResponseJet32400to3200.Write();
    ResponseJet33200.Write();
    Eta0to1p3ResponseJet350to80.Write();
    Eta0to1p3ResponseJet380to120.Write();
    Eta0to1p3ResponseJet3120to170.Write();
    Eta0to1p3ResponseJet3170to300.Write();
    Eta0to1p3ResponseJet3300to470.Write();
    Eta0to1p3ResponseJet3470to600.Write();
    Eta0to1p3ResponseJet3600to800.Write();
    Eta0to1p3ResponseJet3800to1000.Write();
    Eta0to1p3ResponseJet31000to1400.Write();
    Eta0to1p3ResponseJet31400to1800.Write();
    Eta0to1p3ResponseJet31800to2400.Write();
    Eta0to1p3ResponseJet32400to3200.Write();
    Eta0to1p3ResponseJet33200.Write();
    Eta1p3to2p5ResponseJet350to80.Write();
    Eta1p3to2p5ResponseJet380to120.Write();
    Eta1p3to2p5ResponseJet3120to170.Write();
    Eta1p3to2p5ResponseJet3170to300.Write();
    Eta1p3to2p5ResponseJet3300to470.Write();
    Eta1p3to2p5ResponseJet3470to600.Write();
    Eta1p3to2p5ResponseJet3600to800.Write();
    Eta1p3to2p5ResponseJet3800to1000.Write();
    Eta1p3to2p5ResponseJet31000to1400.Write();
    Eta1p3to2p5ResponseJet31400to1800.Write();
    Eta1p3to2p5ResponseJet31800to2400.Write();
    Eta1p3to2p5ResponseJet32400to3200.Write();
    Eta1p3to2p5ResponseJet33200.Write();
    Eta2p5to3ResponseJet350to80.Write();
    Eta2p5to3ResponseJet380to120.Write();
    Eta2p5to3ResponseJet3120to170.Write();
    Eta2p5to3ResponseJet3170to300.Write();
    Eta2p5to3ResponseJet3300to470.Write();
    Eta2p5to3ResponseJet3470to600.Write();
    Eta2p5to3ResponseJet3600to800.Write();
    Eta2p5to3ResponseJet3800to1000.Write();
    Eta2p5to3ResponseJet31000to1400.Write();
    Eta2p5to3ResponseJet31400to1800.Write();
    Eta2p5to3ResponseJet31800to2400.Write();
    Eta2p5to3ResponseJet32400to3200.Write();
    Eta2p5to3ResponseJet33200.Write();
    Eta3to5ResponseJet350to80.Write();
    Eta3to5ResponseJet380to120.Write();
    Eta3to5ResponseJet3120to170.Write();
    Eta3to5ResponseJet3170to300.Write();
    Eta3to5ResponseJet3300to470.Write();
    Eta3to5ResponseJet3470to600.Write();
    Eta3to5ResponseJet3600to800.Write();
    Eta3to5ResponseJet3800to1000.Write();
    Eta3to5ResponseJet31000to1400.Write();
    Eta3to5ResponseJet31400to1800.Write();
    Eta3to5ResponseJet31800to2400.Write();
    Eta3to5ResponseJet32400to3200.Write();
    Eta3to5ResponseJet33200.Write();
    outHistFile3->Close();

  return 0;
}
