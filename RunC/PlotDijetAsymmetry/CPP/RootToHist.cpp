int RootToHist()
{

    //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023C-22Sep2023_v1-v1_NANOAOD.root";
  char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023C-22Sep2023_v2-v1_NANOAOD.root";
  char rootFile3[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023C-22Sep2023_v3-v1_NANOAOD.root";
  char rootFile4[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023C-22Sep2023_v4-v1_NANOAOD.root";
  char rootFile5[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023C-22Sep2023_v1-v1_NANOAOD.root";
  char rootFile6[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023C-22Sep2023_v2-v1_NANOAOD.root";
  char rootFile7[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023C-22Sep2023_v3-v1_NANOAOD.root";
  char rootFile8[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023C-22Sep2023_v4-v1_NANOAOD.root";
  char outName[] = "/nfs/dust/cms/user/mueckejo/RootC/PlotDijetAsymmetry_Run2023C.root";


  TChain tree("Events");   // name of the tree is the argument
  tree.Add(rootFile1);
  tree.Add(rootFile2);
  tree.Add(rootFile3);
  tree.Add(rootFile4);
  tree.Add(rootFile5);
  tree.Add(rootFile6);
  tree.Add(rootFile7);
  tree.Add(rootFile8);

  //declare variables to Load from Root Tree
  const unsigned int eventNum = 1;
  //variables of Jet1
  float pt1Num[eventNum];
  float y1Num[eventNum];
  float eta1Num[eventNum];
  float phi1Num[eventNum];
  float mass1Num[eventNum];
  int TightID1[eventNum];

  tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree.SetBranchAddress("jetAK4_y1",&y1Num);
  tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
  tree.SetBranchAddress("jetAK4_mass1",&mass1Num);
  tree.SetBranchAddress("jetAK4_TightID1",&TightID1);

  //variables of Jet2
  float pt2Num[eventNum];
  float y2Num[eventNum];
  float eta2Num[eventNum];
  float phi2Num[eventNum];
  float mass2Num[eventNum];
  int TightID2[eventNum];

  tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
  tree.SetBranchAddress("jetAK4_y2",&y2Num);
  tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
  tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
  tree.SetBranchAddress("jetAK4_mass2",&mass2Num);
  tree.SetBranchAddress("jetAK4_TightID2",&TightID2);

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

    //Calculate Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
    Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();

    //Calculate chi
    double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

    //Calculate yboost
    double YBoostValue = (y1Num[0]+y2Num[0])/2;

    if (MjjValue > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1[0] == 1 && TightID2[0] == 1){
          float deltaPhi = TMath::Abs(phi1Num[0]-phi2Num[0]);
          if(deltaPhi > TMath::Pi()){
            deltaPhi = TMath::TwoPi() - deltaPhi;
          }
          PhiDifference.Fill(deltaPhi*radtodeg);

          double theta1 = 2*atan(exp(-eta1Num[0]));
          double theta2 = 2*atan(exp(-eta2Num[0]));

          float deltaTheta = TMath::Abs(theta1-theta2);
          if(deltaTheta > TMath::Pi()){
            deltaTheta = TMath::TwoPi() - deltaTheta;
          }
          ThetaDifference.Fill(deltaTheta*radtodeg);

          PtAsymmetry.Fill((pt1Num[0]-pt2Num[0])/(pt1Num[0]+pt2Num[0]));
          EtaDifference.Fill(TMath::Abs(eta1Num[0]-eta2Num[0]));
          YDifference.Fill(TMath::Abs(y1Num[0]-y2Num[0]));
        }
    }
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
