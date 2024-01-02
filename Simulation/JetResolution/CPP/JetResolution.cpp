int JetResolution()
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
    char outName[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_test_Run2023C.root";


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

    TH1D Response50to80("Response50to80","Response50to80",40,-0.2,0.2);
    Response50to80.Sumw2();
    TH1D Response80to120("Response80to120","Response80to120",40,-0.2,0.2);
    Response80to120.Sumw2();
    TH1D Response120to170("Response120to170","Response120to170",40,-0.2,0.2);
    Response120to170.Sumw2();
    TH1D Response170to300("Response170to300","Response170to300",40,-0.2,0.2);
    Response170to300.Sumw2();
    TH1D Response300to470("Response300to470","Response300to470",40,-0.2,0.2);
    Response300to470.Sumw2();
    TH1D Response470to600("Response470to600","Response470to600",40,-0.2,0.2);
    Response470to600.Sumw2();
    TH1D Response600to800("Response600to800","Response600to800",40,-0.2,0.2);
    Response600to800.Sumw2();
    TH1D Response800to1000("Response800to1000","Response800to1000",40,-0.2,0.2);
    Response800to1000.Sumw2();
    TH1D Response1000to1400("Response1000to1400","Response1000to1400",40,-0.2,0.2);
    Response1000to1400.Sumw2();
    TH1D Response1400to1800("Response1400to1800","Response1400to1800",40,-0.2,0.2);
    Response1400to1800.Sumw2();
    TH1D Response1800to2400("Response1800to2400","Response1800to2400",40,-0.2,0.2);
    Response1800to2400.Sumw2();
    TH1D Response2400to3200("Response2400to3200","Response2400to3200",40,-0.2,0.2);
    Response2400to3200.Sumw2();
    TH1D Response3200("Response3200","Response3200",40,-0.2,0.2);
    Response3200.Sumw2();

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

      //calculate R
      double R_Value = sqrt(pow(phi1Num[0]-genphi1Num[0],2)*pow(eta1Num[0]-geneta1Num[0],2));

      if(R_Value < 0.2){
        //calculate response
        double Response = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= pt1Num[0] && pt1Num[0] < 80 && 50 <= genpt1Num[0] && genpt1Num[0] < 80){
        Response50to80.Fill(Response);
        }
        if(80 <= pt1Num[0] && pt1Num[0] < 120 && 80 <= genpt1Num[0] && genpt1Num[0] < 120){
        Response80to120.Fill(Response);
        }
        if(120 <= pt1Num[0] && pt1Num[0] < 170 && 120 <= genpt1Num[0] && genpt1Num[0] < 170){
        Response120to170.Fill(Response);
        }
        if(170 <= pt1Num[0] && pt1Num[0] < 300 && 170 <= genpt1Num[0] && genpt1Num[0] < 300){
        Response170to300.Fill(Response);
        }
        if(300 <= pt1Num[0] && pt1Num[0] < 470 && 300 <= genpt1Num[0] && genpt1Num[0] < 470){
        Response300to470.Fill(Response);
        }
        if(470 <= pt1Num[0] && pt1Num[0] < 600 && 470 <= genpt1Num[0] && genpt1Num[0] < 600){
        Response470to600.Fill(Response);
        }
        if(600 <= pt1Num[0] && pt1Num[0] < 800 && 600 <= genpt1Num[0] && genpt1Num[0] < 800){
        Response600to800.Fill(Response);
        }
        if(800 <= pt1Num[0] && pt1Num[0] < 1000 && 800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        Response800to1000.Fill(Response);
        }
        if(1000 <= pt1Num[0] && pt1Num[0] < 1400 && 1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        Response1000to1400.Fill(Response);
        }
        if(1400 <= pt1Num[0] && pt1Num[0] < 1800 && 1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        Response1400to1800.Fill(Response);
        }
        if(1800 <= pt1Num[0] && pt1Num[0] < 2400 && 1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        Response1800to2400.Fill(Response);
        }
        if(2400 <= pt1Num[0] && pt1Num[0] < 3200 && 2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        Response2400to3200.Fill(Response);
        }
        if(3200 <= pt1Num[0] && 3200 <= genpt1Num[0]){
        Response3200.Fill(Response);
        }
      }

    }

    //Neccesary so files dont get lost
    Response50to80.SetDirectory(0);
    Response80to120.SetDirectory(0);
    Response120to170.SetDirectory(0);
    Response170to300.SetDirectory(0);
    Response300to470.SetDirectory(0);
    Response470to600.SetDirectory(0);
    Response600to800.SetDirectory(0);
    Response800to1000.SetDirectory(0);
    Response1000to1400.SetDirectory(0);
    Response1400to1800.SetDirectory(0);
    Response1800to2400.SetDirectory(0);
    Response2400to3200.SetDirectory(0);
    Response3200.SetDirectory(0);


    TFile* outHistFile = TFile::Open(outName,"RECREATE");
    Response50to80.Write();
    Response80to120.Write();
    Response120to170.Write();
    Response170to300.Write();
    Response300to470.Write();
    Response470to600.Write();
    Response600to800.Write();
    Response800to1000.Write();
    Response1000to1400.Write();
    Response1400to1800.Write();
    Response1800to2400.Write();
    Response2400to3200.Write();
    Response3200.Write();
    outHistFile->Close();

  return 0;
}
