int JetResolution()
{

    //define folders of Root Tree File and where to write Hist Files
    char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-50to80_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-80to120_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile3[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-120to170_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile4[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-170to300_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    /*
    char rootFile5[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-300to470_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile6[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-470to600_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile7[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-600to800_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile8[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-800to1000_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile9[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1000to1400_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile10[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1400to1800_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile11[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-1800to2400_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile12[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    char rootFile13[] = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-3200_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    */
    char outName[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotJetResolution_test_Run2023C.root";


    TChain tree("Events");   // name of the tree is the argument
    tree.Add(rootFile1);
    tree.Add(rootFile2);
    tree.Add(rootFile3);
    tree.Add(rootFile4);
    /*
    tree.Add(rootFile5);
    tree.Add(rootFile6);
    tree.Add(rootFile7);
    tree.Add(rootFile8);
    tree.Add(rootFile9);
    tree.Add(rootFile10);
    tree.Add(rootFile11);
    tree.Add(rootFile12);
    tree.Add(rootFile13);
    */

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


    TH1D Response20to40("Response20to40","Response20to40",20,20,40);
    Response20to40.Sumw2();
    TH1D Response40to60("Response40to60","Response40to60",20,40,60);
    Response40to60.Sumw2();
    TH1D Response60to80("Response60to80","Response60to80",20,60,80);
    Response60to80.Sumw2();
    TH1D Response80to100("Response80to100","Response80to100",20,80,100);
    Response20to40.Sumw2();
    TH1D Response100to120("Response100to120","Response100to120",20,100,120);
    Response100to120.Sumw2();

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
        //if(20 <= pt1Num[0] && pt1Num[0] < 40 && 20 <= genpt1Num[0] && genpt1Num[0] < 40){
        Response20to40.Fill(Response);
        //}
        if(40 <= pt1Num[0] && pt1Num[0] < 60 && 40 <= genpt1Num[0] && genpt1Num[0] < 60){
          Response40to60.Fill(Response);
        }
        if(60 <= pt1Num[0] && pt1Num[0] < 80 && 60 <= genpt1Num[0] && genpt1Num[0] < 80){
          Response60to80.Fill(Response);
        }
        if(80 <= pt1Num[0] && pt1Num[0] < 100 && 80 <= genpt1Num[0] && genpt1Num[0] < 100){
          Response80to100.Fill(Response);
        }
        if(100 <= pt1Num[0] && pt1Num[0] < 120 && 100 <= genpt1Num[0] && genpt1Num[0] < 120){
          Response100to120.Fill(Response);
        }
      }

    }

    //Neccesary so files dont get lost
    Response20to40.SetDirectory(0);
    Response40to60.SetDirectory(0);
    Response60to80.SetDirectory(0);
    Response80to100.SetDirectory(0);
    Response100to120.SetDirectory(0);


    TFile* outHistFile = TFile::Open(outName,"RECREATE");
    Response20to40.Write();
    Response40to60.Write();
    Response60to80.Write();
    Response80to100.Write();
    Response100to120.Write();
    outHistFile->Close();

  return 0;
}
