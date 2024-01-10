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
    char outNameJet1[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet1_Run2023C.root";
    char outNameJet2[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet2_Run2023C.root";
    char outNameJet3[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_Jet3_Run2023C.root";


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

    TH1D SmallEtaResponseJet150to80("SmallEtaResponseJet150to80","SmallEtaResponseJet150to80",40,-0.2,0.2);
    SmallEtaResponseJet150to80.Sumw2();
    TH1D SmallEtaResponseJet180to120("SmallEtaResponseJet180to120","SmallEtaResponseJet180to120",40,-0.2,0.2);
    SmallEtaResponseJet180to120.Sumw2();
    TH1D SmallEtaResponseJet1120to170("SmallEtaResponseJet1120to170","SmallEtaResponseJet1120to170",40,-0.2,0.2);
    SmallEtaResponseJet1120to170.Sumw2();
    TH1D SmallEtaResponseJet1170to300("SmallEtaResponseJet1170to300","SmallEtaResponseJet1170to300",40,-0.2,0.2);
    SmallEtaResponseJet1170to300.Sumw2();
    TH1D SmallEtaResponseJet1300to470("SmallEtaResponseJet1300to470","SmallEtaResponseJet1300to470",40,-0.2,0.2);
    SmallEtaResponseJet1300to470.Sumw2();
    TH1D SmallEtaResponseJet1470to600("SmallEtaResponseJet1470to600","SmallEtaResponseJet1470to600",40,-0.2,0.2);
    SmallEtaResponseJet1470to600.Sumw2();
    TH1D SmallEtaResponseJet1600to800("SmallEtaResponseJet1600to800","SmallEtaResponseJet1600to800",40,-0.2,0.2);
    SmallEtaResponseJet1600to800.Sumw2();
    TH1D SmallEtaResponseJet1800to1000("SmallEtaResponseJet1800to1000","SmallEtaResponseJet1800to1000",40,-0.2,0.2);
    SmallEtaResponseJet1800to1000.Sumw2();
    TH1D SmallEtaResponseJet11000to1400("SmallEtaResponseJet11000to1400","SmallEtaResponseJet11000to1400",40,-0.2,0.2);
    SmallEtaResponseJet11000to1400.Sumw2();
    TH1D SmallEtaResponseJet11400to1800("SmallEtaResponseJet11400to1800","SmallEtaResponseJet11400to1800",40,-0.2,0.2);
    SmallEtaResponseJet11400to1800.Sumw2();
    TH1D SmallEtaResponseJet11800to2400("SmallEtaResponseJet11800to2400","SmallEtaResponseJet11800to2400",40,-0.2,0.2);
    SmallEtaResponseJet11800to2400.Sumw2();
    TH1D SmallEtaResponseJet12400to3200("SmallEtaResponseJet12400to3200","SmallEtaResponseJet12400to3200",40,-0.2,0.2);
    SmallEtaResponseJet12400to3200.Sumw2();
    TH1D SmallEtaResponseJet13200("SmallEtaResponseJet13200","SmallEtaResponseJet13200",40,-0.2,0.2);
    SmallEtaResponseJet13200.Sumw2();

    TH1D BigEtaResponseJet150to80("BigEtaResponseJet150to80","BigEtaResponseJet150to80",40,-0.2,0.2);
    BigEtaResponseJet150to80.Sumw2();
    TH1D BigEtaResponseJet180to120("BigEtaResponseJet180to120","BigEtaResponseJet180to120",40,-0.2,0.2);
    BigEtaResponseJet180to120.Sumw2();
    TH1D BigEtaResponseJet1120to170("BigEtaResponseJet1120to170","BigEtaResponseJet1120to170",40,-0.2,0.2);
    BigEtaResponseJet1120to170.Sumw2();
    TH1D BigEtaResponseJet1170to300("BigEtaResponseJet1170to300","BigEtaResponseJet1170to300",40,-0.2,0.2);
    BigEtaResponseJet1170to300.Sumw2();
    TH1D BigEtaResponseJet1300to470("BigEtaResponseJet1300to470","BigEtaResponseJet1300to470",40,-0.2,0.2);
    BigEtaResponseJet1300to470.Sumw2();
    TH1D BigEtaResponseJet1470to600("BigEtaResponseJet1470to600","BigEtaResponseJet1470to600",40,-0.2,0.2);
    BigEtaResponseJet1470to600.Sumw2();
    TH1D BigEtaResponseJet1600to800("BigEtaResponseJet1600to800","BigEtaResponseJet1600to800",40,-0.2,0.2);
    BigEtaResponseJet1600to800.Sumw2();
    TH1D BigEtaResponseJet1800to1000("BigEtaResponseJet1800to1000","BigEtaResponseJet1800to1000",40,-0.2,0.2);
    BigEtaResponseJet1800to1000.Sumw2();
    TH1D BigEtaResponseJet11000to1400("BigEtaResponseJet11000to1400","BigEtaResponseJet11000to1400",40,-0.2,0.2);
    BigEtaResponseJet11000to1400.Sumw2();
    TH1D BigEtaResponseJet11400to1800("BigEtaResponseJet11400to1800","BigEtaResponseJet11400to1800",40,-0.2,0.2);
    BigEtaResponseJet11400to1800.Sumw2();
    TH1D BigEtaResponseJet11800to2400("BigEtaResponseJet11800to2400","BigEtaResponseJet11800to2400",40,-0.2,0.2);
    BigEtaResponseJet11800to2400.Sumw2();
    TH1D BigEtaResponseJet12400to3200("BigEtaResponseJet12400to3200","BigEtaResponseJet12400to3200",40,-0.2,0.2);
    BigEtaResponseJet12400to3200.Sumw2();
    TH1D BigEtaResponseJet13200("BigEtaResponseJet13200","BigEtaResponseJet13200",40,-0.2,0.2);
    BigEtaResponseJet13200.Sumw2();

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

    TH1D SmallEtaResponseJet250to80("SmallEtaResponseJet250to80","SmallEtaResponseJet250to80",40,-0.2,0.2);
    SmallEtaResponseJet250to80.Sumw2();
    TH1D SmallEtaResponseJet280to120("SmallEtaResponseJet280to120","SmallEtaResponseJet280to120",40,-0.2,0.2);
    SmallEtaResponseJet280to120.Sumw2();
    TH1D SmallEtaResponseJet2120to170("SmallEtaResponseJet2120to170","SmallEtaResponseJet2120to170",40,-0.2,0.2);
    SmallEtaResponseJet2120to170.Sumw2();
    TH1D SmallEtaResponseJet2170to300("SmallEtaResponseJet2170to300","SmallEtaResponseJet2170to300",40,-0.2,0.2);
    SmallEtaResponseJet2170to300.Sumw2();
    TH1D SmallEtaResponseJet2300to470("SmallEtaResponseJet2300to470","SmallEtaResponseJet2300to470",40,-0.2,0.2);
    SmallEtaResponseJet2300to470.Sumw2();
    TH1D SmallEtaResponseJet2470to600("SmallEtaResponseJet2470to600","SmallEtaResponseJet2470to600",40,-0.2,0.2);
    SmallEtaResponseJet2470to600.Sumw2();
    TH1D SmallEtaResponseJet2600to800("SmallEtaResponseJet2600to800","SmallEtaResponseJet2600to800",40,-0.2,0.2);
    SmallEtaResponseJet2600to800.Sumw2();
    TH1D SmallEtaResponseJet2800to1000("SmallEtaResponseJet2800to1000","SmallEtaResponseJet2800to1000",40,-0.2,0.2);
    SmallEtaResponseJet2800to1000.Sumw2();
    TH1D SmallEtaResponseJet21000to1400("SmallEtaResponseJet21000to1400","SmallEtaResponseJet21000to1400",40,-0.2,0.2);
    SmallEtaResponseJet21000to1400.Sumw2();
    TH1D SmallEtaResponseJet21400to1800("SmallEtaResponseJet21400to1800","SmallEtaResponseJet21400to1800",40,-0.2,0.2);
    SmallEtaResponseJet21400to1800.Sumw2();
    TH1D SmallEtaResponseJet21800to2400("SmallEtaResponseJet21800to2400","SmallEtaResponseJet21800to2400",40,-0.2,0.2);
    SmallEtaResponseJet21800to2400.Sumw2();
    TH1D SmallEtaResponseJet22400to3200("SmallEtaResponseJet22400to3200","SmallEtaResponseJet22400to3200",40,-0.2,0.2);
    SmallEtaResponseJet22400to3200.Sumw2();
    TH1D SmallEtaResponseJet23200("SmallEtaResponseJet23200","SmallEtaResponseJet23200",40,-0.2,0.2);
    SmallEtaResponseJet23200.Sumw2();

    TH1D BigEtaResponseJet250to80("BigEtaResponseJet250to80","BigEtaResponseJet250to80",40,-0.2,0.2);
    BigEtaResponseJet250to80.Sumw2();
    TH1D BigEtaResponseJet280to120("BigEtaResponseJet280to120","BigEtaResponseJet280to120",40,-0.2,0.2);
    BigEtaResponseJet280to120.Sumw2();
    TH1D BigEtaResponseJet2120to170("BigEtaResponseJet2120to170","BigEtaResponseJet2120to170",40,-0.2,0.2);
    BigEtaResponseJet2120to170.Sumw2();
    TH1D BigEtaResponseJet2170to300("BigEtaResponseJet2170to300","BigEtaResponseJet2170to300",40,-0.2,0.2);
    BigEtaResponseJet2170to300.Sumw2();
    TH1D BigEtaResponseJet2300to470("BigEtaResponseJet2300to470","BigEtaResponseJet2300to470",40,-0.2,0.2);
    BigEtaResponseJet2300to470.Sumw2();
    TH1D BigEtaResponseJet2470to600("BigEtaResponseJet2470to600","BigEtaResponseJet2470to600",40,-0.2,0.2);
    BigEtaResponseJet2470to600.Sumw2();
    TH1D BigEtaResponseJet2600to800("BigEtaResponseJet2600to800","BigEtaResponseJet2600to800",40,-0.2,0.2);
    BigEtaResponseJet2600to800.Sumw2();
    TH1D BigEtaResponseJet2800to1000("BigEtaResponseJet2800to1000","BigEtaResponseJet2800to1000",40,-0.2,0.2);
    BigEtaResponseJet2800to1000.Sumw2();
    TH1D BigEtaResponseJet21000to1400("BigEtaResponseJet21000to1400","BigEtaResponseJet21000to1400",40,-0.2,0.2);
    BigEtaResponseJet21000to1400.Sumw2();
    TH1D BigEtaResponseJet21400to1800("BigEtaResponseJet21400to1800","BigEtaResponseJet21400to1800",40,-0.2,0.2);
    BigEtaResponseJet21400to1800.Sumw2();
    TH1D BigEtaResponseJet21800to2400("BigEtaResponseJet21800to2400","BigEtaResponseJet21800to2400",40,-0.2,0.2);
    BigEtaResponseJet21800to2400.Sumw2();
    TH1D BigEtaResponseJet22400to3200("BigEtaResponseJet22400to3200","BigEtaResponseJet22400to3200",40,-0.2,0.2);
    BigEtaResponseJet22400to3200.Sumw2();
    TH1D BigEtaResponseJet23200("BigEtaResponseJet23200","BigEtaResponseJet23200",40,-0.2,0.2);
    BigEtaResponseJet23200.Sumw2();

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

    TH1D SmallEtaResponseJet350to80("SmallEtaResponseJet350to80","SmallEtaResponseJet350to80",40,-0.2,0.2);
    SmallEtaResponseJet350to80.Sumw2();
    TH1D SmallEtaResponseJet380to120("SmallEtaResponseJet380to120","SmallEtaResponseJet380to120",40,-0.2,0.2);
    SmallEtaResponseJet380to120.Sumw2();
    TH1D SmallEtaResponseJet3120to170("SmallEtaResponseJet3120to170","SmallEtaResponseJet3120to170",40,-0.2,0.2);
    SmallEtaResponseJet3120to170.Sumw2();
    TH1D SmallEtaResponseJet3170to300("SmallEtaResponseJet3170to300","SmallEtaResponseJet3170to300",40,-0.2,0.2);
    SmallEtaResponseJet3170to300.Sumw2();
    TH1D SmallEtaResponseJet3300to470("SmallEtaResponseJet3300to470","SmallEtaResponseJet3300to470",40,-0.2,0.2);
    SmallEtaResponseJet3300to470.Sumw2();
    TH1D SmallEtaResponseJet3470to600("SmallEtaResponseJet3470to600","SmallEtaResponseJet3470to600",40,-0.2,0.2);
    SmallEtaResponseJet3470to600.Sumw2();
    TH1D SmallEtaResponseJet3600to800("SmallEtaResponseJet3600to800","SmallEtaResponseJet3600to800",40,-0.2,0.2);
    SmallEtaResponseJet3600to800.Sumw2();
    TH1D SmallEtaResponseJet3800to1000("SmallEtaResponseJet3800to1000","SmallEtaResponseJet3800to1000",40,-0.2,0.2);
    SmallEtaResponseJet3800to1000.Sumw2();
    TH1D SmallEtaResponseJet31000to1400("SmallEtaResponseJet31000to1400","SmallEtaResponseJet31000to1400",40,-0.2,0.2);
    SmallEtaResponseJet31000to1400.Sumw2();
    TH1D SmallEtaResponseJet31400to1800("SmallEtaResponseJet31400to1800","SmallEtaResponseJet31400to1800",40,-0.2,0.2);
    SmallEtaResponseJet31400to1800.Sumw2();
    TH1D SmallEtaResponseJet31800to2400("SmallEtaResponseJet31800to2400","SmallEtaResponseJet31800to2400",40,-0.2,0.2);
    SmallEtaResponseJet31800to2400.Sumw2();
    TH1D SmallEtaResponseJet32400to3200("SmallEtaResponseJet32400to3200","SmallEtaResponseJet32400to3200",40,-0.2,0.2);
    SmallEtaResponseJet32400to3200.Sumw2();
    TH1D SmallEtaResponseJet33200("SmallEtaResponseJet33200","SmallEtaResponseJet33200",40,-0.2,0.2);
    SmallEtaResponseJet33200.Sumw2();

    TH1D BigEtaResponseJet350to80("BigEtaResponseJet350to80","BigEtaResponseJet350to80",40,-0.2,0.2);
    BigEtaResponseJet350to80.Sumw2();
    TH1D BigEtaResponseJet380to120("BigEtaResponseJet380to120","BigEtaResponseJet380to120",40,-0.2,0.2);
    BigEtaResponseJet380to120.Sumw2();
    TH1D BigEtaResponseJet3120to170("BigEtaResponseJet3120to170","BigEtaResponseJet3120to170",40,-0.2,0.2);
    BigEtaResponseJet3120to170.Sumw2();
    TH1D BigEtaResponseJet3170to300("BigEtaResponseJet3170to300","BigEtaResponseJet3170to300",40,-0.2,0.2);
    BigEtaResponseJet3170to300.Sumw2();
    TH1D BigEtaResponseJet3300to470("BigEtaResponseJet3300to470","BigEtaResponseJet3300to470",40,-0.2,0.2);
    BigEtaResponseJet3300to470.Sumw2();
    TH1D BigEtaResponseJet3470to600("BigEtaResponseJet3470to600","BigEtaResponseJet3470to600",40,-0.2,0.2);
    BigEtaResponseJet3470to600.Sumw2();
    TH1D BigEtaResponseJet3600to800("BigEtaResponseJet3600to800","BigEtaResponseJet3600to800",40,-0.2,0.2);
    BigEtaResponseJet3600to800.Sumw2();
    TH1D BigEtaResponseJet3800to1000("BigEtaResponseJet3800to1000","BigEtaResponseJet3800to1000",40,-0.2,0.2);
    BigEtaResponseJet3800to1000.Sumw2();
    TH1D BigEtaResponseJet31000to1400("BigEtaResponseJet31000to1400","BigEtaResponseJet31000to1400",40,-0.2,0.2);
    BigEtaResponseJet31000to1400.Sumw2();
    TH1D BigEtaResponseJet31400to1800("BigEtaResponseJet31400to1800","BigEtaResponseJet31400to1800",40,-0.2,0.2);
    BigEtaResponseJet31400to1800.Sumw2();
    TH1D BigEtaResponseJet31800to2400("BigEtaResponseJet31800to2400","BigEtaResponseJet31800to2400",40,-0.2,0.2);
    BigEtaResponseJet31800to2400.Sumw2();
    TH1D BigEtaResponseJet32400to3200("BigEtaResponseJet32400to3200","BigEtaResponseJet32400to3200",40,-0.2,0.2);
    BigEtaResponseJet32400to3200.Sumw2();
    TH1D BigEtaResponseJet33200("BigEtaResponseJet33200","BigEtaResponseJet33200",40,-0.2,0.2);
    BigEtaResponseJet33200.Sumw2();

    TH1D ResponseJet150to80("ResponseJet150to80","ResponseJet150to80",40,-0.2,0.2);
    ResponseJet150to80.Sumw2();
    TH1D ResponseJet180to120("ResponseJet180to120","ResponseJet180to120",40,-0.2,0.2);
    ResponseJet180to120.Sumw2();
    TH1D ResponseJet1120to170("ResponseJet1120to170","ResponseJet1120to170",40,-0.2,0.2);
    ResponseJet1120to170.Sumw2();
    TH1D ResponseJet1170to300("ResponseJet1170to300","ResponseJet1170to300",40,-0.2,0.2);
    ResponseJet1170to300.Sumw2();
    TH1D ResponseJet1300to470("ResponseJet1300to470","ResponseJet1300to470",40,-0.2,0.2);
    ResponseJet1300to470.Sumw2();
    TH1D ResponseJet1470to600("ResponseJet1470to600","ResponseJet1470to600",40,-0.2,0.2);
    ResponseJet1470to600.Sumw2();
    TH1D ResponseJet1600to800("ResponseJet1600to800","ResponseJet1600to800",40,-0.2,0.2);
    ResponseJet1600to800.Sumw2();
    TH1D ResponseJet1800to1000("ResponseJet1800to1000","ResponseJet1800to1000",40,-0.2,0.2);
    ResponseJet1800to1000.Sumw2();
    TH1D ResponseJet11000to1400("ResponseJet11000to1400","ResponseJet11000to1400",40,-0.2,0.2);
    ResponseJet11000to1400.Sumw2();
    TH1D ResponseJet11400to1800("ResponseJet11400to1800","ResponseJet11400to1800",40,-0.2,0.2);
    ResponseJet11400to1800.Sumw2();
    TH1D ResponseJet11800to2400("ResponseJet11800to2400","ResponseJet11800to2400",40,-0.2,0.2);
    ResponseJet11800to2400.Sumw2();
    TH1D ResponseJet12400to3200("ResponseJet12400to3200","ResponseJet12400to3200",40,-0.2,0.2);
    ResponseJet12400to3200.Sumw2();
    TH1D ResponseJet13200("ResponseJet13200","ResponseJet13200",40,-0.2,0.2);
    ResponseJet13200.Sumw2();

    TH1D ResponseJet250to80("ResponseJet250to80","ResponseJet250to80",40,-0.2,0.2);
    ResponseJet250to80.Sumw2();
    TH1D ResponseJet280to120("ResponseJet280to120","ResponseJet280to120",40,-0.2,0.2);
    ResponseJet280to120.Sumw2();
    TH1D ResponseJet2120to170("ResponseJet2120to170","ResponseJet2120to170",40,-0.2,0.2);
    ResponseJet2120to170.Sumw2();
    TH1D ResponseJet2170to300("ResponseJet2170to300","ResponseJet2170to300",40,-0.2,0.2);
    ResponseJet2170to300.Sumw2();
    TH1D ResponseJet2300to470("ResponseJet2300to470","ResponseJet2300to470",40,-0.2,0.2);
    ResponseJet2300to470.Sumw2();
    TH1D ResponseJet2470to600("ResponseJet2470to600","ResponseJet2470to600",40,-0.2,0.2);
    ResponseJet2470to600.Sumw2();
    TH1D ResponseJet2600to800("ResponseJet2600to800","ResponseJet2600to800",40,-0.2,0.2);
    ResponseJet2600to800.Sumw2();
    TH1D ResponseJet2800to1000("ResponseJet2800to1000","ResponseJet2800to1000",40,-0.2,0.2);
    ResponseJet2800to1000.Sumw2();
    TH1D ResponseJet21000to1400("ResponseJet21000to1400","ResponseJet21000to1400",40,-0.2,0.2);
    ResponseJet21000to1400.Sumw2();
    TH1D ResponseJet21400to1800("ResponseJet21400to1800","ResponseJet21400to1800",40,-0.2,0.2);
    ResponseJet21400to1800.Sumw2();
    TH1D ResponseJet21800to2400("ResponseJet21800to2400","ResponseJet21800to2400",40,-0.2,0.2);
    ResponseJet21800to2400.Sumw2();
    TH1D ResponseJet22400to3200("ResponseJet22400to3200","ResponseJet22400to3200",40,-0.2,0.2);
    ResponseJet22400to3200.Sumw2();
    TH1D ResponseJet23200("ResponseJet23200","ResponseJet23200",40,-0.2,0.2);
    ResponseJet23200.Sumw2();

    TH1D ResponseJet350to80("ResponseJet350to80","ResponseJet350to80",40,-0.2,0.2);
    ResponseJet350to80.Sumw2();
    TH1D ResponseJet380to120("ResponseJet380to120","ResponseJet380to120",40,-0.2,0.2);
    ResponseJet380to120.Sumw2();
    TH1D ResponseJet3120to170("ResponseJet3120to170","ResponseJet3120to170",40,-0.2,0.2);
    ResponseJet3120to170.Sumw2();
    TH1D ResponseJet3170to300("ResponseJet3170to300","ResponseJet3170to300",40,-0.2,0.2);
    ResponseJet3170to300.Sumw2();
    TH1D ResponseJet3300to470("ResponseJet3300to470","ResponseJet3300to470",40,-0.2,0.2);
    ResponseJet3300to470.Sumw2();
    TH1D ResponseJet3470to600("ResponseJet3470to600","ResponseJet3470to600",40,-0.2,0.2);
    ResponseJet3470to600.Sumw2();
    TH1D ResponseJet3600to800("ResponseJet3600to800","ResponseJet3600to800",40,-0.2,0.2);
    ResponseJet3600to800.Sumw2();
    TH1D ResponseJet3800to1000("ResponseJet3800to1000","ResponseJet3800to1000",40,-0.2,0.2);
    ResponseJet3800to1000.Sumw2();
    TH1D ResponseJet31000to1400("ResponseJet31000to1400","ResponseJet31000to1400",40,-0.2,0.2);
    ResponseJet31000to1400.Sumw2();
    TH1D ResponseJet31400to1800("ResponseJet31400to1800","ResponseJet31400to1800",40,-0.2,0.2);
    ResponseJet31400to1800.Sumw2();
    TH1D ResponseJet31800to2400("ResponseJet31800to2400","ResponseJet31800to2400",40,-0.2,0.2);
    ResponseJet31800to2400.Sumw2();
    TH1D ResponseJet32400to3200("ResponseJet32400to3200","ResponseJet32400to3200",40,-0.2,0.2);
    ResponseJet32400to3200.Sumw2();
    TH1D ResponseJet33200("ResponseJet33200","ResponseJet33200",40,-0.2,0.2);
    ResponseJet33200.Sumw2();

    float numberEntries = tree.GetEntries();

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
      double R_ValueJet1 = sqrt(pow(phi1Num[0]-genphi1Num[0],2)*pow(eta1Num[0]-geneta1Num[0],2));

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
        double SmallEtaResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        SmallEtaResponseJet150to80.Fill(SmallEtaResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        SmallEtaResponseJet180to120.Fill(SmallEtaResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        SmallEtaResponseJet1120to170.Fill(SmallEtaResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        SmallEtaResponseJet1170to300.Fill(SmallEtaResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        SmallEtaResponseJet1300to470.Fill(SmallEtaResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        SmallEtaResponseJet1470to600.Fill(SmallEtaResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        SmallEtaResponseJet1600to800.Fill(SmallEtaResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        SmallEtaResponseJet1800to1000.Fill(SmallEtaResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        SmallEtaResponseJet11000to1400.Fill(SmallEtaResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        SmallEtaResponseJet11400to1800.Fill(SmallEtaResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        SmallEtaResponseJet11800to2400.Fill(SmallEtaResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        SmallEtaResponseJet12400to3200.Fill(SmallEtaResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        SmallEtaResponseJet13200.Fill(SmallEtaResponseJet1);
        }
        }
        if(abs(geneta1Num[0])  >= 1.3 && abs(geneta1Num[0]) < 2.5){
            //calculate response
        double BigEtaResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt1Num[0] && genpt1Num[0] < 80){
        BigEtaResponseJet150to80.Fill(BigEtaResponseJet1);
        }
        if(80 <= genpt1Num[0] && genpt1Num[0] < 120){
        BigEtaResponseJet180to120.Fill(BigEtaResponseJet1);
        }
        if(120 <= genpt1Num[0] && genpt1Num[0] < 170){
        BigEtaResponseJet1120to170.Fill(BigEtaResponseJet1);
        }
        if(170 <= genpt1Num[0] && genpt1Num[0] < 300){
        BigEtaResponseJet1170to300.Fill(BigEtaResponseJet1);
        }
        if(300 <= genpt1Num[0] && genpt1Num[0] < 470){
        BigEtaResponseJet1300to470.Fill(BigEtaResponseJet1);
        }
        if(470 <= genpt1Num[0] && genpt1Num[0] < 600){
        BigEtaResponseJet1470to600.Fill(BigEtaResponseJet1);
        }
        if(600 <= genpt1Num[0] && genpt1Num[0] < 800){
        BigEtaResponseJet1600to800.Fill(BigEtaResponseJet1);
        }
        if(800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        BigEtaResponseJet1800to1000.Fill(BigEtaResponseJet1);
        }
        if(1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        BigEtaResponseJet11000to1400.Fill(BigEtaResponseJet1);
        }
        if(1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        BigEtaResponseJet11400to1800.Fill(BigEtaResponseJet1);
        }
        if(1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        BigEtaResponseJet11800to2400.Fill(BigEtaResponseJet1);
        }
        if(2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        BigEtaResponseJet12400to3200.Fill(BigEtaResponseJet1);
        }
        if(3200 <= genpt1Num[0]){
        BigEtaResponseJet13200.Fill(BigEtaResponseJet1);
        }
        }
      }

      //For Jet2
      //calculate R
      double R_ValueJet2 = sqrt(pow(phi2Num[0]-genphi2Num[0],2)*pow(eta2Num[0]-geneta2Num[0],2));

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
        double SmallEtaResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        SmallEtaResponseJet250to80.Fill(SmallEtaResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        SmallEtaResponseJet280to120.Fill(SmallEtaResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        SmallEtaResponseJet2120to170.Fill(SmallEtaResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        SmallEtaResponseJet2170to300.Fill(SmallEtaResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        SmallEtaResponseJet2300to470.Fill(SmallEtaResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        SmallEtaResponseJet2470to600.Fill(SmallEtaResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        SmallEtaResponseJet2600to800.Fill(SmallEtaResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        SmallEtaResponseJet2800to1000.Fill(SmallEtaResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        SmallEtaResponseJet21000to1400.Fill(SmallEtaResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        SmallEtaResponseJet21400to1800.Fill(SmallEtaResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        SmallEtaResponseJet21800to2400.Fill(SmallEtaResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        SmallEtaResponseJet22400to3200.Fill(SmallEtaResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        SmallEtaResponseJet23200.Fill(SmallEtaResponseJet2);
        }
        }
        if(abs(geneta2Num[0])  >= 1.3 && abs(geneta2Num[0]) < 2.5){
            //calculate response
        double BigEtaResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt2Num[0] && genpt2Num[0] < 80){
        BigEtaResponseJet250to80.Fill(BigEtaResponseJet2);
        }
        if(80 <= genpt2Num[0] && genpt2Num[0] < 120){
        BigEtaResponseJet280to120.Fill(BigEtaResponseJet2);
        }
        if(120 <= genpt2Num[0] && genpt2Num[0] < 170){
        BigEtaResponseJet2120to170.Fill(BigEtaResponseJet2);
        }
        if(170 <= genpt2Num[0] && genpt2Num[0] < 300){
        BigEtaResponseJet2170to300.Fill(BigEtaResponseJet2);
        }
        if(300 <= genpt2Num[0] && genpt2Num[0] < 470){
        BigEtaResponseJet2300to470.Fill(BigEtaResponseJet2);
        }
        if(470 <= genpt2Num[0] && genpt2Num[0] < 600){
        BigEtaResponseJet2470to600.Fill(BigEtaResponseJet2);
        }
        if(600 <= genpt2Num[0] && genpt2Num[0] < 800){
        BigEtaResponseJet2600to800.Fill(BigEtaResponseJet2);
        }
        if(800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        BigEtaResponseJet2800to1000.Fill(BigEtaResponseJet2);
        }
        if(1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        BigEtaResponseJet21000to1400.Fill(BigEtaResponseJet2);
        }
        if(1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        BigEtaResponseJet21400to1800.Fill(BigEtaResponseJet2);
        }
        if(1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        BigEtaResponseJet21800to2400.Fill(BigEtaResponseJet2);
        }
        if(2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        BigEtaResponseJet22400to3200.Fill(BigEtaResponseJet2);
        }
        if(3200 <= genpt2Num[0]){
        BigEtaResponseJet23200.Fill(BigEtaResponseJet2);
        }
        }
      }

      //For Jet3
      //calculate R
      double R_ValueJet3 = sqrt(pow(phi3Num[0]-genphi3Num[0],2)*pow(eta3Num[0]-geneta3Num[0],2));

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
        double SmallEtaResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        SmallEtaResponseJet350to80.Fill(SmallEtaResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        SmallEtaResponseJet380to120.Fill(SmallEtaResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        SmallEtaResponseJet3120to170.Fill(SmallEtaResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        SmallEtaResponseJet3170to300.Fill(SmallEtaResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        SmallEtaResponseJet3300to470.Fill(SmallEtaResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        SmallEtaResponseJet3470to600.Fill(SmallEtaResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        SmallEtaResponseJet3600to800.Fill(SmallEtaResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        SmallEtaResponseJet3800to1000.Fill(SmallEtaResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        SmallEtaResponseJet31000to1400.Fill(SmallEtaResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        SmallEtaResponseJet31400to1800.Fill(SmallEtaResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        SmallEtaResponseJet31800to2400.Fill(SmallEtaResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        SmallEtaResponseJet32400to3200.Fill(SmallEtaResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        SmallEtaResponseJet33200.Fill(SmallEtaResponseJet3);
        }
        }
        if(abs(geneta3Num[0])  >= 1.3 && abs(geneta3Num[0]) < 2.5){
            //calculate response
        double BigEtaResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= genpt3Num[0] && genpt3Num[0] < 80){
        BigEtaResponseJet350to80.Fill(BigEtaResponseJet3);
        }
        if(80 <= genpt3Num[0] && genpt3Num[0] < 120){
        BigEtaResponseJet380to120.Fill(BigEtaResponseJet3);
        }
        if(120 <= genpt3Num[0] && genpt3Num[0] < 170){
        BigEtaResponseJet3120to170.Fill(BigEtaResponseJet3);
        }
        if(170 <= genpt3Num[0] && genpt3Num[0] < 300){
        BigEtaResponseJet3170to300.Fill(BigEtaResponseJet3);
        }
        if(300 <= genpt3Num[0] && genpt3Num[0] < 470){
        BigEtaResponseJet3300to470.Fill(BigEtaResponseJet3);
        }
        if(470 <= genpt3Num[0] && genpt3Num[0] < 600){
        BigEtaResponseJet3470to600.Fill(BigEtaResponseJet3);
        }
        if(600 <= genpt3Num[0] && genpt3Num[0] < 800){
        BigEtaResponseJet3600to800.Fill(BigEtaResponseJet3);
        }
        if(800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        BigEtaResponseJet3800to1000.Fill(BigEtaResponseJet3);
        }
        if(1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        BigEtaResponseJet31000to1400.Fill(BigEtaResponseJet3);
        }
        if(1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        BigEtaResponseJet31400to1800.Fill(BigEtaResponseJet3);
        }
        if(1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        BigEtaResponseJet31800to2400.Fill(BigEtaResponseJet3);
        }
        if(2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        BigEtaResponseJet32400to3200.Fill(BigEtaResponseJet3);
        }
        if(3200 <= genpt3Num[0]){
        BigEtaResponseJet33200.Fill(BigEtaResponseJet3);
        }
        }
      }

    }

    //Neccesary so files dont get lost
    BigEtaResponseJet150to80.SetDirectory(0);
    BigEtaResponseJet180to120.SetDirectory(0);
    BigEtaResponseJet1120to170.SetDirectory(0);
    BigEtaResponseJet1170to300.SetDirectory(0);
    BigEtaResponseJet1300to470.SetDirectory(0);
    BigEtaResponseJet1470to600.SetDirectory(0);
    BigEtaResponseJet1600to800.SetDirectory(0);
    BigEtaResponseJet1800to1000.SetDirectory(0);
    BigEtaResponseJet11000to1400.SetDirectory(0);
    BigEtaResponseJet11400to1800.SetDirectory(0);
    BigEtaResponseJet11800to2400.SetDirectory(0);
    BigEtaResponseJet12400to3200.SetDirectory(0);
    BigEtaResponseJet13200.SetDirectory(0);
    BigEtaResponseJet250to80.SetDirectory(0);
    BigEtaResponseJet280to120.SetDirectory(0);
    BigEtaResponseJet2120to170.SetDirectory(0);
    BigEtaResponseJet2170to300.SetDirectory(0);
    BigEtaResponseJet2300to470.SetDirectory(0);
    BigEtaResponseJet2470to600.SetDirectory(0);
    BigEtaResponseJet2600to800.SetDirectory(0);
    BigEtaResponseJet2800to1000.SetDirectory(0);
    BigEtaResponseJet21000to1400.SetDirectory(0);
    BigEtaResponseJet21400to1800.SetDirectory(0);
    BigEtaResponseJet21800to2400.SetDirectory(0);
    BigEtaResponseJet22400to3200.SetDirectory(0);
    BigEtaResponseJet23200.SetDirectory(0);
    BigEtaResponseJet350to80.SetDirectory(0);
    BigEtaResponseJet380to120.SetDirectory(0);
    BigEtaResponseJet3120to170.SetDirectory(0);
    BigEtaResponseJet3170to300.SetDirectory(0);
    BigEtaResponseJet3300to470.SetDirectory(0);
    BigEtaResponseJet3470to600.SetDirectory(0);
    BigEtaResponseJet3600to800.SetDirectory(0);
    BigEtaResponseJet3800to1000.SetDirectory(0);
    BigEtaResponseJet31000to1400.SetDirectory(0);
    BigEtaResponseJet31400to1800.SetDirectory(0);
    BigEtaResponseJet31800to2400.SetDirectory(0);
    BigEtaResponseJet32400to3200.SetDirectory(0);
    BigEtaResponseJet33200.SetDirectory(0);
    SmallEtaResponseJet150to80.SetDirectory(0);
    SmallEtaResponseJet180to120.SetDirectory(0);
    SmallEtaResponseJet1120to170.SetDirectory(0);
    SmallEtaResponseJet1170to300.SetDirectory(0);
    SmallEtaResponseJet1300to470.SetDirectory(0);
    SmallEtaResponseJet1470to600.SetDirectory(0);
    SmallEtaResponseJet1600to800.SetDirectory(0);
    SmallEtaResponseJet1800to1000.SetDirectory(0);
    SmallEtaResponseJet11000to1400.SetDirectory(0);
    SmallEtaResponseJet11400to1800.SetDirectory(0);
    SmallEtaResponseJet11800to2400.SetDirectory(0);
    SmallEtaResponseJet12400to3200.SetDirectory(0);
    SmallEtaResponseJet13200.SetDirectory(0);
    SmallEtaResponseJet250to80.SetDirectory(0);
    SmallEtaResponseJet280to120.SetDirectory(0);
    SmallEtaResponseJet2120to170.SetDirectory(0);
    SmallEtaResponseJet2170to300.SetDirectory(0);
    SmallEtaResponseJet2300to470.SetDirectory(0);
    SmallEtaResponseJet2470to600.SetDirectory(0);
    SmallEtaResponseJet2600to800.SetDirectory(0);
    SmallEtaResponseJet2800to1000.SetDirectory(0);
    SmallEtaResponseJet21000to1400.SetDirectory(0);
    SmallEtaResponseJet21400to1800.SetDirectory(0);
    SmallEtaResponseJet21800to2400.SetDirectory(0);
    SmallEtaResponseJet22400to3200.SetDirectory(0);
    SmallEtaResponseJet23200.SetDirectory(0);
    SmallEtaResponseJet350to80.SetDirectory(0);
    SmallEtaResponseJet380to120.SetDirectory(0);
    SmallEtaResponseJet3120to170.SetDirectory(0);
    SmallEtaResponseJet3170to300.SetDirectory(0);
    SmallEtaResponseJet3300to470.SetDirectory(0);
    SmallEtaResponseJet3470to600.SetDirectory(0);
    SmallEtaResponseJet3600to800.SetDirectory(0);
    SmallEtaResponseJet3800to1000.SetDirectory(0);
    SmallEtaResponseJet31000to1400.SetDirectory(0);
    SmallEtaResponseJet31400to1800.SetDirectory(0);
    SmallEtaResponseJet31800to2400.SetDirectory(0);
    SmallEtaResponseJet32400to3200.SetDirectory(0);
    SmallEtaResponseJet33200.SetDirectory(0);
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
    SmallEtaResponseJet150to80.Write();
    SmallEtaResponseJet180to120.Write();
    SmallEtaResponseJet1120to170.Write();
    SmallEtaResponseJet1170to300.Write();
    SmallEtaResponseJet1300to470.Write();
    SmallEtaResponseJet1470to600.Write();
    SmallEtaResponseJet1600to800.Write();
    SmallEtaResponseJet1800to1000.Write();
    SmallEtaResponseJet11000to1400.Write();
    SmallEtaResponseJet11400to1800.Write();
    SmallEtaResponseJet11800to2400.Write();
    SmallEtaResponseJet12400to3200.Write();
    SmallEtaResponseJet13200.Write();
    BigEtaResponseJet150to80.Write();
    BigEtaResponseJet180to120.Write();
    BigEtaResponseJet1120to170.Write();
    BigEtaResponseJet1170to300.Write();
    BigEtaResponseJet1300to470.Write();
    BigEtaResponseJet1470to600.Write();
    BigEtaResponseJet1600to800.Write();
    BigEtaResponseJet1800to1000.Write();
    BigEtaResponseJet11000to1400.Write();
    BigEtaResponseJet11400to1800.Write();
    BigEtaResponseJet11800to2400.Write();
    BigEtaResponseJet12400to3200.Write();
    BigEtaResponseJet13200.Write();
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
    SmallEtaResponseJet250to80.Write();
    SmallEtaResponseJet280to120.Write();
    SmallEtaResponseJet2120to170.Write();
    SmallEtaResponseJet2170to300.Write();
    SmallEtaResponseJet2300to470.Write();
    SmallEtaResponseJet2470to600.Write();
    SmallEtaResponseJet2600to800.Write();
    SmallEtaResponseJet2800to1000.Write();
    SmallEtaResponseJet21000to1400.Write();
    SmallEtaResponseJet21400to1800.Write();
    SmallEtaResponseJet21800to2400.Write();
    SmallEtaResponseJet22400to3200.Write();
    SmallEtaResponseJet23200.Write();
    BigEtaResponseJet250to80.Write();
    BigEtaResponseJet280to120.Write();
    BigEtaResponseJet2120to170.Write();
    BigEtaResponseJet2170to300.Write();
    BigEtaResponseJet2300to470.Write();
    BigEtaResponseJet2470to600.Write();
    BigEtaResponseJet2600to800.Write();
    BigEtaResponseJet2800to1000.Write();
    BigEtaResponseJet21000to1400.Write();
    BigEtaResponseJet21400to1800.Write();
    BigEtaResponseJet21800to2400.Write();
    BigEtaResponseJet22400to3200.Write();
    BigEtaResponseJet23200.Write();
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
    SmallEtaResponseJet350to80.Write();
    SmallEtaResponseJet380to120.Write();
    SmallEtaResponseJet3120to170.Write();
    SmallEtaResponseJet3170to300.Write();
    SmallEtaResponseJet3300to470.Write();
    SmallEtaResponseJet3470to600.Write();
    SmallEtaResponseJet3600to800.Write();
    SmallEtaResponseJet3800to1000.Write();
    SmallEtaResponseJet31000to1400.Write();
    SmallEtaResponseJet31400to1800.Write();
    SmallEtaResponseJet31800to2400.Write();
    SmallEtaResponseJet32400to3200.Write();
    SmallEtaResponseJet33200.Write();
    BigEtaResponseJet350to80.Write();
    BigEtaResponseJet380to120.Write();
    BigEtaResponseJet3120to170.Write();
    BigEtaResponseJet3170to300.Write();
    BigEtaResponseJet3300to470.Write();
    BigEtaResponseJet3470to600.Write();
    BigEtaResponseJet3600to800.Write();
    BigEtaResponseJet3800to1000.Write();
    BigEtaResponseJet31000to1400.Write();
    BigEtaResponseJet31400to1800.Write();
    BigEtaResponseJet31800to2400.Write();
    BigEtaResponseJet32400to3200.Write();
    BigEtaResponseJet33200.Write();
    outHistFile3->Close();

  return 0;
}
