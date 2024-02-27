int RootToHist()
{

  string ranges[13] = {"50to80","80to120","120to170","170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","3200"};

  for (int i = 0; i < 13; i++)
  {
    string rootFile = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-"+ranges[i]+"_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM-15Jan2023.root";
    string outName = "/nfs/dust/cms/user/mueckejo/RootS2023/"+ranges[i]+"_PlotDijetAsymmetry_Run32023-15Jan2023_MC.root";

    TFile* inFile = TFile::Open(rootFile.c_str(),"READ");
    TTree* tree = (TTree*)inFile->Get("Events");

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float pt1rawNum[eventNum];
    float pt1nomNum[eventNum];
    float y1Num[eventNum];
    int TightID1[eventNum];
    float eta1Num[eventNum];
    float phi1Num[eventNum];


    tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree->SetBranchAddress("jetAK4_pt1_raw",&pt1rawNum);
    tree->SetBranchAddress("jetAK4_pt1_nom",&pt1nomNum);
    tree->SetBranchAddress("jetAK4_y1",&y1Num);
    tree->SetBranchAddress("jetAK4_TightID1",&TightID1);
    tree->SetBranchAddress("jetAK4_eta1",&eta1Num);
    tree->SetBranchAddress("jetAK4_phi1",&phi1Num);

    //variables of Jet2
    float pt2Num[eventNum];
    float pt2rawNum[eventNum];
    float pt2nomNum[eventNum];
    float y2Num[eventNum];
    int TightID2[eventNum];
    float eta2Num[eventNum];
    float phi2Num[eventNum];

    tree->SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree->SetBranchAddress("jetAK4_pt2_raw",&pt2rawNum);
    tree->SetBranchAddress("jetAK4_pt2_nom",&pt2nomNum);
    tree->SetBranchAddress("jetAK4_y2",&y2Num);
    tree->SetBranchAddress("jetAK4_TightID2",&TightID2);
    tree->SetBranchAddress("jetAK4_eta2",&eta2Num);
    tree->SetBranchAddress("jetAK4_phi2",&phi2Num);

    float mjjNum[eventNum];
    float mjjnomNum[eventNum];
    float mjjrawNum[eventNum];

    tree->SetBranchAddress("mjj",&mjjNum);
    tree->SetBranchAddress("mjj_nom",&mjjnomNum);
    tree->SetBranchAddress("mjj_raw",&mjjrawNum);

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

    TH1D PtAsymmetryRaw("PtAsymmetryRaw","PtAsymmetryRaw",50,0,1);
    PtAsymmetryRaw.Sumw2();
    TH1D PhiDifferenceRaw("PhiDifferenceRaw","PhiDifferenceRaw",50,0,180);
    PhiDifferenceRaw.Sumw2();
    TH1D EtaDifferenceRaw("EtaDifferenceRaw","EtaDifferenceRaw",50,-6,6);
    EtaDifferenceRaw.Sumw2();
    TH1D YDifferenceRaw("YDifferenceRaw","YDifferenceRaw",50,-6,6);
    YDifferenceRaw.Sumw2();
    TH1D ThetaDifferenceRaw("ThetaDifferenceRaw","ThetaDifferenceRaw",50,0,180);
    ThetaDifferenceRaw.Sumw2();

    TH1D PtAsymmetryNom("PtAsymmetryNom","PtAsymmetryNom",50,0,1);
    PtAsymmetryNom.Sumw2();
    TH1D PhiDifferenceNom("PhiDifferenceNom","PhiDifferenceNom",50,0,180);
    PhiDifferenceNom.Sumw2();
    TH1D EtaDifferenceNom("EtaDifferenceNom","EtaDifferenceNom",50,-6,6);
    EtaDifferenceNom.Sumw2();
    TH1D YDifferenceNom("YDifferenceNom","YDifferenceNom",50,-6,6);
    YDifferenceNom.Sumw2();
    TH1D ThetaDifferenceNom("ThetaDifferenceNom","ThetaDifferenceNom",50,0,180);
    ThetaDifferenceNom.Sumw2();

    std::cout << tree->GetEntries() << std::endl;
     float numberEntries = tree->GetEntries();
    //Fill the Hists with Root Tree Sim and Genjets
    for (Long64_t entry = 0; entry < tree->GetEntries(); ++entry)
    {
      tree->GetEntry(entry);

      if(entry % 100000 == 0)
      {
        std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
      }

    //Calculate chi
    double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

    //Calculate yboost
    double YBoostValue = (y1Num[0]+y2Num[0])/2;

    if (mjjNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
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
    if (mjjrawNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1[0] == 1 && TightID2[0] == 1){
        float deltaPhi = TMath::Abs(phi1Num[0]-phi2Num[0]);
        if(deltaPhi > TMath::Pi()){
          deltaPhi = TMath::TwoPi() - deltaPhi;
        }
        PhiDifferenceRaw.Fill(deltaPhi*radtodeg);

        double theta1 = 2*atan(exp(-eta1Num[0]));
        double theta2 = 2*atan(exp(-eta2Num[0]));

        float deltaTheta = TMath::Abs(theta1-theta2);
        if(deltaTheta > TMath::Pi()){
          deltaTheta = TMath::TwoPi() - deltaTheta;
        }
        ThetaDifferenceRaw.Fill(deltaTheta*radtodeg);


        PtAsymmetryRaw.Fill((pt1rawNum[0]-pt2rawNum[0])/(pt1rawNum[0]+pt2rawNum[0]));
        EtaDifferenceRaw.Fill(TMath::Abs(eta1Num[0]-eta2Num[0]));
        YDifferenceRaw.Fill(TMath::Abs(y1Num[0]-y2Num[0]));
      }
    }
    if (mjjnomNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1[0] == 1 && TightID2[0] == 1){
        float deltaPhi = TMath::Abs(phi1Num[0]-phi2Num[0]);
        if(deltaPhi > TMath::Pi()){
          deltaPhi = TMath::TwoPi() - deltaPhi;
        }
        PhiDifferenceNom.Fill(deltaPhi*radtodeg);

        double theta1 = 2*atan(exp(-eta1Num[0]));
        double theta2 = 2*atan(exp(-eta2Num[0]));

        float deltaTheta = TMath::Abs(theta1-theta2);
        if(deltaTheta > TMath::Pi()){
          deltaTheta = TMath::TwoPi() - deltaTheta;
        }
        ThetaDifferenceNom.Fill(deltaTheta*radtodeg);


        PtAsymmetryNom.Fill((pt1nomNum[0]-pt2nomNum[0])/(pt1nomNum[0]+pt2nomNum[0]));
        EtaDifferenceNom.Fill(TMath::Abs(eta1Num[0]-eta2Num[0]));
        YDifferenceNom.Fill(TMath::Abs(y1Num[0]-y2Num[0]));
      }
    }
    }

    //Neccesary so files dont get lost
    PtAsymmetry.SetDirectory(0);
    PhiDifference.SetDirectory(0);
    EtaDifference.SetDirectory(0);
    YDifference.SetDirectory(0);
    ThetaDifference.SetDirectory(0);
    PtAsymmetryRaw.SetDirectory(0);
    PhiDifferenceRaw.SetDirectory(0);
    EtaDifferenceRaw.SetDirectory(0);
    YDifferenceRaw.SetDirectory(0);
    ThetaDifferenceRaw.SetDirectory(0);
    PtAsymmetryNom.SetDirectory(0);
    PhiDifferenceNom.SetDirectory(0);
    EtaDifferenceNom.SetDirectory(0);
    YDifferenceNom.SetDirectory(0);
    ThetaDifferenceNom.SetDirectory(0);

    TFile* outHistFile = TFile::Open(outName.c_str(),"RECREATE");
    PtAsymmetry.Write();
    PhiDifference.Write();
    EtaDifference.Write();
    YDifference.Write();
    ThetaDifference.Write();
    PtAsymmetryRaw.Write();
    PhiDifferenceRaw.Write();
    EtaDifferenceRaw.Write();
    YDifferenceRaw.Write();
    ThetaDifferenceRaw.Write();
    PtAsymmetryNom.Write();
    PhiDifferenceNom.Write();
    EtaDifferenceNom.Write();
    YDifferenceNom.Write();
    ThetaDifferenceNom.Write();
    outHistFile->Close();
  }
  return 0;
}
