int RootToHist()
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
    char outNameJet1[] = "/nfs/dust/cms/user/mueckejo/RootS/PlotDijetAsymmetry_Run2023_Simulation.root";


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

  tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree.SetBranchAddress("jetAK4_y1",&y1Num);
  tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree.SetBranchAddress("jetAK4_phi1",&phi1Num);

  //variables of Jet2
  float pt2Num[eventNum];
  float y2Num[eventNum];
  float eta2Num[eventNum];
  float phi2Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
  tree.SetBranchAddress("jetAK4_y2",&y2Num);
  tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
  tree.SetBranchAddress("jetAK4_phi2",&phi2Num);

  //variables of Jet3
  float pt3Num[eventNum];
  float y3Num[eventNum];
  float eta3Num[eventNum];
  float phi3Num[eventNum];

  tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
  tree.SetBranchAddress("jetAK4_y3",&y3Num);
  tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
  tree.SetBranchAddress("jetAK4_phi3",&phi3Num);

  double pi = 3.14159265359;
  double radtodeg = 180.0/pi;

  TH1D PtAsymmetry("PtAsymmetry","PtAsymmetry",50,0,1);
  PtAsymmetry.Sumw2();
  TH1D PhiDifference("PhiDifference","PhiDifference",50,0,180);
  PhiDifference.Sumw2();
  TH1D EtaDifference("EtaDifference","EtaDifference",50,-6,6);
  EtaDifference.Sumw2();
  TH1D YDifference("YDifference","YDifference",50,-6,6);
  YDifference.Sumw2();
  TH1D ThetaDifference("ThetaDifference","ThetaDifference",50,0,180);
  ThetaDifference.Sumw2();

  float numberEntries = tree.GetEntries();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);

    if(entry % 100000 == 0)
    {
      std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
    }

    if (abs(phi1Num[0]) > pi/2 && abs(phi2Num[0]) > pi/2) {
      PhiDifference.Fill((abs(phi1Num[0])+abs(phi2Num[0])-pi)*radtodeg);
    } else {
      PhiDifference.Fill((abs(phi1Num[0])+abs(phi2Num[0]))*radtodeg);
    }

    double theta1 = 2*atan(exp(-eta1Num[0]));
    double theta2 = 2*atan(exp(-eta2Num[0]));

    if (theta1 > pi/2 && theta2 > pi/2) {
      ThetaDifference.Fill((theta1+theta2-pi)*radtodeg);
    } else {
      ThetaDifference.Fill((theta1+theta2)*radtodeg);
    }


    PtAsymmetry.Fill((pt1Num[0]-pt2Num[0])/(pt1Num[0]+pt2Num[0]));
    EtaDifference.Fill(eta1Num[0]-eta2Num[0]);
    YDifference.Fill(y1Num[0]-y2Num[0]);
  }

  //Neccesary so files dont get lost
  PtAsymmetry.SetDirectory(0);
  PhiDifference.SetDirectory(0);
  EtaDifference.SetDirectory(0);
  YDifference.SetDirectory(0);
  ThetaDifference.SetDirectory(0);

  TFile* outHistFile = TFile::Open(outName,"RECREATE");
  PtAsymmetry.Write();
  PhiDifference.Write();
  EtaDifference.Write();
  YDifference.Write();
  ThetaDifference.Write();
  outHistFile->Close();
  return 0;
}
