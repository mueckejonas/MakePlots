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


    tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree->SetBranchAddress("jetAK4_pt1_raw",&pt1rawNum);
    tree->SetBranchAddress("jetAK4_pt1_nom",&pt1nomNum);
    tree->SetBranchAddress("jetAK4_y1",&y1Num);
    tree->SetBranchAddress("jetAK4_TightID1",&TightID1);

    //variables of Jet2
    float pt2Num[eventNum];
    float pt2rawNum[eventNum];
    float pt2nomNum[eventNum];
    float y2Num[eventNum];
    int TightID2[eventNum];

    tree->SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree->SetBranchAddress("jetAK4_pt2_raw",&pt2rawNum);
    tree->SetBranchAddress("jetAK4_pt2_nom",&pt2nomNum);
    tree->SetBranchAddress("jetAK4_y2",&y2Num);
    tree->SetBranchAddress("jetAK4_TightID2",&TightID2);

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

    TH1D PtAsymmetryRaw("PtAsymmetryRaw","PtAsymmetryRaw",50,0,1);
    PtAsymmetryRaw.Sumw2();

    TH1D PtAsymmetryNom("PtAsymmetryNom","PtAsymmetryNom",50,0,1);
    PtAsymmetryNom.Sumw2();

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
        PtAsymmetry.Fill((pt1Num[0]-pt2Num[0])/(pt1Num[0]+pt2Num[0]));
      }
    }
    if (mjjrawNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1[0] == 1 && TightID2[0] == 1){
        PtAsymmetryRaw.Fill((pt1rawNum[0]-pt2rawNum[0])/(pt1rawNum[0]+pt2rawNum[0]));
      }
    }
    if (mjjnomNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1[0] == 1 && TightID2[0] == 1){
        PtAsymmetryNom.Fill((pt1nomNum[0]-pt2nomNum[0])/(pt1nomNum[0]+pt2nomNum[0]));
      }
    }
    }

    //Neccesary so files dont get lost
    PtAsymmetry.SetDirectory(0);
    PtAsymmetryRaw.SetDirectory(0);
    PtAsymmetryNom.SetDirectory(0);

    TFile* outHistFile = TFile::Open(outName.c_str(),"RECREATE");
    PtAsymmetry.Write();
    PtAsymmetryRaw.Write();
    PtAsymmetryNom.Write();
    outHistFile->Close();
  }
  return 0;
}
