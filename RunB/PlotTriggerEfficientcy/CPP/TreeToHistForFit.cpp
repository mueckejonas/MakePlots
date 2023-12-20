int TreeToHistForFit()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char outName[] = "/nfs/dust/cms/user/mueckejo/RootB/PlotFitFunctionTriggerEff_Run2023B.root";


  TChain tree("Events");   // name of the tree is the argument
  tree.Add(rootFile1);
  tree.Add(rootFile2);

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

  //variables of Jet3
  float pt3Num[eventNum];
  float y3Num[eventNum];
  float eta3Num[eventNum];
  float phi3Num[eventNum];
  float mass3Num[eventNum];
  int TightID3[eventNum];

  tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
  tree.SetBranchAddress("jetAK4_y3",&y3Num);
  tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
  tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
  tree.SetBranchAddress("jetAK4_mass3",&mass3Num);
  tree.SetBranchAddress("jetAK4_TightID3",&TightID3);

  //trigger efficienties
  bool HLT_PFJet40Num[eventNum];
  bool HLT_PFJet60Num[eventNum];
  bool HLT_PFJet80Num[eventNum];
  bool HLT_PFJet110Num[eventNum];
  bool HLT_PFJet140Num[eventNum];
  bool HLT_PFJet200Num[eventNum];
  bool HLT_PFJet260Num[eventNum];
  bool HLT_PFJet320Num[eventNum];
  bool HLT_PFJet400Num[eventNum];
  bool HLT_PFJet450Num[eventNum];
  bool HLT_PFJet500Num[eventNum];
  bool HLT_PFJet550Num[eventNum];

  tree.SetBranchAddress("HLT_PFJet40",&HLT_PFJet40Num);
  tree.SetBranchAddress("HLT_PFJet60",&HLT_PFJet60Num);
  tree.SetBranchAddress("HLT_PFJet80",&HLT_PFJet80Num);
  tree.SetBranchAddress("HLT_PFJet110",&HLT_PFJet110Num);
  tree.SetBranchAddress("HLT_PFJet140",&HLT_PFJet140Num);
  tree.SetBranchAddress("HLT_PFJet200",&HLT_PFJet200Num);
  tree.SetBranchAddress("HLT_PFJet260",&HLT_PFJet260Num);
  tree.SetBranchAddress("HLT_PFJet320",&HLT_PFJet320Num);
  tree.SetBranchAddress("HLT_PFJet400",&HLT_PFJet400Num);
  tree.SetBranchAddress("HLT_PFJet450",&HLT_PFJet450Num);
  tree.SetBranchAddress("HLT_PFJet500",&HLT_PFJet500Num);
  tree.SetBranchAddress("HLT_PFJet550",&HLT_PFJet550Num);

  TH1D Ref_HLT_PFJet40("Ref_HLT_PFJet40","Ref_HLT_PFJet40",30,2000,3000);
  Ref_HLT_PFJet40.Sumw2();
  TH1D Ref_HLT_PFJet60("Ref_HLT_PFJet60","Ref_HLT_PFJet60",30,2000,3000);
  Ref_HLT_PFJet60.Sumw2();
  TH1D Ref_HLT_PFJet80("Ref_HLT_PFJet80","Ref_HLT_PFJet80",30,2000,3000);
  Ref_HLT_PFJet80.Sumw2();
  TH1D Ref_HLT_PFJet110("Ref_HLT_PFJet110","Ref_HLT_PFJet110",30,2000,3000);
  Ref_HLT_PFJet110.Sumw2();
  TH1D Ref_HLT_PFJet140("Ref_HLT_PFJet140","Ref_HLT_PFJet140",30,2000,3000);
  Ref_HLT_PFJet140.Sumw2();
  TH1D Ref_HLT_PFJet200("Ref_HLT_PFJet200","Ref_HLT_PFJet200",30,2000,3000);
  Ref_HLT_PFJet200.Sumw2();
  TH1D Ref_HLT_PFJet260("Ref_HLT_PFJet260","Ref_HLT_PFJet260",30,2000,3000);
  Ref_HLT_PFJet260.Sumw2();
  TH1D Ref_HLT_PFJet320("Ref_HLT_PFJet320","Ref_HLT_PFJet320",30,2000,3000);
  Ref_HLT_PFJet320.Sumw2();
  TH1D Ref_HLT_PFJet400("Ref_HLT_PFJet400","Ref_HLT_PFJet400",30,2000,3000);
  Ref_HLT_PFJet400.Sumw2();
  TH1D Ref_HLT_PFJet450("Ref_HLT_PFJet450","Ref_HLT_PFJet450",30,2000,3000);
  Ref_HLT_PFJet450.Sumw2();
  TH1D Ref_HLT_PFJet500("Ref_HLT_PFJet500","Ref_HLT_PFJet500",30,2000,3000);
  Ref_HLT_PFJet500.Sumw2();
  TH1D Ref_HLT_PFJet550("Ref_HLT_PFJet550","Ref_HLT_PFJet550",30,2000,3000);
  Ref_HLT_PFJet550.Sumw2();
  gStyle->SetErrorX(0.);

  TH1D HLT_PFJet40("HLT_PFJet40","HLT_PFJet40",30,2000,3000);
  HLT_PFJet40.Sumw2();
  TH1D HLT_PFJet60("HLT_PFJet60","HLT_PFJet60",30,2000,3000);
  HLT_PFJet60.Sumw2();
  TH1D HLT_PFJet80("HLT_PFJet80","HLT_PFJet80",30,2000,3000);
  HLT_PFJet80.Sumw2();
  TH1D HLT_PFJet110("HLT_PFJet110","HLT_PFJet110",30,2000,3000);
  HLT_PFJet110.Sumw2();
  TH1D HLT_PFJet140("HLT_PFJet140","HLT_PFJet140",30,2000,3000);
  HLT_PFJet140.Sumw2();
  TH1D HLT_PFJet200("HLT_PFJet200","HLT_PFJet200",30,2000,3000);
  HLT_PFJet200.Sumw2();
  TH1D HLT_PFJet260("HLT_PFJet260","HLT_PFJet260",30,2000,3000);
  HLT_PFJet260.Sumw2();
  TH1D HLT_PFJet320("HLT_PFJet320","HLT_PFJet320",30,2000,3000);
  HLT_PFJet320.Sumw2();
  TH1D HLT_PFJet400("HLT_PFJet400","HLT_PFJet400",30,2000,3000);
  HLT_PFJet400.Sumw2();
  TH1D HLT_PFJet450("HLT_PFJet450","HLT_PFJet450",30,2000,3000);
  HLT_PFJet450.Sumw2();
  TH1D HLT_PFJet500("HLT_PFJet500","HLT_PFJet500",30,2000,3000);
  HLT_PFJet500.Sumw2();
  TH1D HLT_PFJet550("HLT_PFJet550","HLT_PFJet550",30,2000,3000);
  HLT_PFJet550.Sumw2();

  bool HLT_PFHT180Num[eventNum];
  bool HLT_PFHT250Num[eventNum];
  bool HLT_PFHT350Num[eventNum];
  bool HLT_PFHT370Num[eventNum];
  bool HLT_PFHT430Num[eventNum];
  bool HLT_PFHT510Num[eventNum];
  bool HLT_PFHT590Num[eventNum];
  bool HLT_PFHT680Num[eventNum];
  bool HLT_PFHT780Num[eventNum];
  bool HLT_PFHT890Num[eventNum];
  bool HLT_PFHT1050Num[eventNum];

  tree.SetBranchAddress("HLT_PFHT180",&HLT_PFHT180Num);
  tree.SetBranchAddress("HLT_PFHT250",&HLT_PFHT250Num);
  tree.SetBranchAddress("HLT_PFHT350",&HLT_PFHT350Num);
  tree.SetBranchAddress("HLT_PFHT370",&HLT_PFHT370Num);
  tree.SetBranchAddress("HLT_PFHT430",&HLT_PFHT430Num);
  tree.SetBranchAddress("HLT_PFHT510",&HLT_PFHT510Num);
  tree.SetBranchAddress("HLT_PFHT590",&HLT_PFHT590Num);
  tree.SetBranchAddress("HLT_PFHT680",&HLT_PFHT680Num);
  tree.SetBranchAddress("HLT_PFHT780",&HLT_PFHT780Num);
  tree.SetBranchAddress("HLT_PFHT890",&HLT_PFHT890Num);
  tree.SetBranchAddress("HLT_PFHT1050",&HLT_PFHT1050Num);

  TH1D Ref_HLT_PFHT180("Ref_HLT_PFHT180","Ref_HLT_PFHT180",30,2000,3000);
  Ref_HLT_PFHT180.Sumw2();
  TH1D Ref_HLT_PFHT250("Ref_HLT_PFHT250","Ref_HLT_PFHT250",30,2000,3000);
  Ref_HLT_PFHT250.Sumw2();
  TH1D Ref_HLT_PFHT350("Ref_HLT_PFHT350","Ref_HLT_PFHT350",30,2000,3000);
  Ref_HLT_PFHT350.Sumw2();
  TH1D Ref_HLT_PFHT370("Ref_HLT_PFHT370","Ref_HLT_PFHT370",30,2000,3000);
  Ref_HLT_PFHT370.Sumw2();
  TH1D Ref_HLT_PFHT430("Ref_HLT_PFHT430","Ref_HLT_PFHT430",30,2000,3000);
  Ref_HLT_PFHT430.Sumw2();
  TH1D Ref_HLT_PFHT510("Ref_HLT_PFHT510","Ref_HLT_PFHT510",30,2000,3000);
  Ref_HLT_PFHT510.Sumw2();
  TH1D Ref_HLT_PFHT590("Ref_HLT_PFHT590","Ref_HLT_PFHT590",30,2000,3000);
  Ref_HLT_PFHT590.Sumw2();
  TH1D Ref_HLT_PFHT680("Ref_HLT_PFHT680","Ref_HLT_PFHT680",30,2000,3000);
  Ref_HLT_PFHT680.Sumw2();
  TH1D Ref_HLT_PFHT780("Ref_HLT_PFHT780","Ref_HLT_PFHT780",30,2000,3000);
  Ref_HLT_PFHT780.Sumw2();
  TH1D Ref_HLT_PFHT890("Ref_HLT_PFHT890","Ref_HLT_PFHT890",30,2000,3000);
  Ref_HLT_PFHT890.Sumw2();
  TH1D Ref_HLT_PFHT1050("Ref_HLT_PFHT1050","Ref_HLT_PFHT1050",30,2000,3000);
  Ref_HLT_PFHT1050.Sumw2();

  TH1D HLT_PFHT180("HLT_PFHT180","HLT_PFHT180",30,2000,3000);
  HLT_PFHT180.Sumw2();
  TH1D HLT_PFHT250("HLT_PFHT250","HLT_PFHT250",30,2000,3000);
  HLT_PFHT250.Sumw2();
  TH1D HLT_PFHT350("HLT_PFHT350","HLT_PFHT350",30,2000,3000);
  HLT_PFHT350.Sumw2();
  TH1D HLT_PFHT370("HLT_PFHT370","HLT_PFHT370",30,2000,3000);
  HLT_PFHT370.Sumw2();
  TH1D HLT_PFHT430("HLT_PFHT430","HLT_PFHT430",30,2000,3000);
  HLT_PFHT430.Sumw2();
  TH1D HLT_PFHT510("HLT_PFHT510","HLT_PFHT510",30,2000,3000);
  HLT_PFHT510.Sumw2();
  TH1D HLT_PFHT590("HLT_PFHT590","HLT_PFHT590",30,2000,3000);
  HLT_PFHT590.Sumw2();
  TH1D HLT_PFHT680("HLT_PFHT680","HLT_PFHT680",30,2000,3000);
  HLT_PFHT680.Sumw2();
  TH1D HLT_PFHT780("HLT_PFHT780","HLT_PFHT780",30,2000,3000);
  HLT_PFHT780.Sumw2();
  TH1D HLT_PFHT890("HLT_PFHT890","HLT_PFHT890",30,2000,3000);
  HLT_PFHT890.Sumw2();
  TH1D HLT_PFHT1050("HLT_PFHT1050","HLT_PFHT1050",30,2000,3000);
  HLT_PFHT1050.Sumw2();

  float numberEntries = tree.GetEntries();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);
    //tree.GetEntries();
    if(entry % 100000 == 0)
    {
      std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
    }

    //Calculate chi
    double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

    //Calculate yboost
    double YBoostValue = (y1Num[0]+y2Num[0])/2;

    //Calculate Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
    Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();

    if (ChiValue < 16 && abs(YBoostValue) < 1.11 && 2000 <= MjjValue && MjjValue <= 3000){

    //fill HLT Hists
    Ref_HLT_PFJet40.Fill(MjjValue,HLT_PFJet40Num[0]);
    Ref_HLT_PFJet60.Fill(MjjValue,HLT_PFJet60Num[0]);
    Ref_HLT_PFJet80.Fill(MjjValue,HLT_PFJet80Num[0]);
    Ref_HLT_PFJet110.Fill(MjjValue,HLT_PFJet110Num[0]);
    Ref_HLT_PFJet140.Fill(MjjValue,HLT_PFJet140Num[0]);
    Ref_HLT_PFJet200.Fill(MjjValue,HLT_PFJet200Num[0]);
    Ref_HLT_PFJet260.Fill(MjjValue,HLT_PFJet260Num[0]);
    Ref_HLT_PFJet320.Fill(MjjValue,HLT_PFJet320Num[0]);
    Ref_HLT_PFJet400.Fill(MjjValue,HLT_PFJet400Num[0]);
    Ref_HLT_PFJet450.Fill(MjjValue,HLT_PFJet450Num[0]);
    Ref_HLT_PFJet500.Fill(MjjValue,HLT_PFJet500Num[0]);
    Ref_HLT_PFJet550.Fill(MjjValue,HLT_PFJet550Num[0]);

    HLT_PFJet60.Fill(MjjValue,HLT_PFJet60Num[0]*HLT_PFJet40Num[0]);
    HLT_PFJet80.Fill(MjjValue,HLT_PFJet80Num[0]*HLT_PFJet60Num[0]);
    HLT_PFJet110.Fill(MjjValue,HLT_PFJet110Num[0]*HLT_PFJet80Num[0]);
    HLT_PFJet140.Fill(MjjValue,HLT_PFJet140Num[0]*HLT_PFJet110Num[0]);
    HLT_PFJet200.Fill(MjjValue,HLT_PFJet200Num[0]*HLT_PFJet140Num[0]);
    HLT_PFJet260.Fill(MjjValue,HLT_PFJet260Num[0]*HLT_PFJet200Num[0]);
    HLT_PFJet320.Fill(MjjValue,HLT_PFJet320Num[0]*HLT_PFJet260Num[0]);
    HLT_PFJet400.Fill(MjjValue,HLT_PFJet400Num[0]*HLT_PFJet320Num[0]);
    HLT_PFJet450.Fill(MjjValue,HLT_PFJet450Num[0]*HLT_PFJet400Num[0]);
    HLT_PFJet500.Fill(MjjValue,HLT_PFJet500Num[0]*HLT_PFJet450Num[0]);
    HLT_PFJet550.Fill(MjjValue,HLT_PFJet550Num[0]*HLT_PFJet500Num[0]);

    //fill HLTPF Hists
    Ref_HLT_PFHT180.Fill(MjjValue,HLT_PFHT180Num[0]);
    Ref_HLT_PFHT250.Fill(MjjValue,HLT_PFHT250Num[0]);
    Ref_HLT_PFHT350.Fill(MjjValue,HLT_PFHT350Num[0]);
    Ref_HLT_PFHT370.Fill(MjjValue,HLT_PFHT370Num[0]);
    Ref_HLT_PFHT430.Fill(MjjValue,HLT_PFHT430Num[0]);
    Ref_HLT_PFHT510.Fill(MjjValue,HLT_PFHT510Num[0]);
    Ref_HLT_PFHT590.Fill(MjjValue,HLT_PFHT590Num[0]);
    Ref_HLT_PFHT680.Fill(MjjValue,HLT_PFHT680Num[0]);
    Ref_HLT_PFHT780.Fill(MjjValue,HLT_PFHT780Num[0]);
    Ref_HLT_PFHT890.Fill(MjjValue,HLT_PFHT890Num[0]);
    Ref_HLT_PFHT1050.Fill(MjjValue,HLT_PFHT1050Num[0]);

    HLT_PFHT250.Fill(MjjValue,HLT_PFHT250Num[0]*HLT_PFHT180Num[0]);
    HLT_PFHT350.Fill(MjjValue,HLT_PFHT350Num[0]*HLT_PFHT250Num[0]);
    HLT_PFHT370.Fill(MjjValue,HLT_PFHT370Num[0]*HLT_PFHT350Num[0]);
    HLT_PFHT430.Fill(MjjValue,HLT_PFHT430Num[0]*HLT_PFHT370Num[0]);
    HLT_PFHT510.Fill(MjjValue,HLT_PFHT510Num[0]*HLT_PFHT430Num[0]);
    HLT_PFHT590.Fill(MjjValue,HLT_PFHT590Num[0]*HLT_PFHT510Num[0]);
    HLT_PFHT680.Fill(MjjValue,HLT_PFHT680Num[0]*HLT_PFHT590Num[0]);
    HLT_PFHT780.Fill(MjjValue,HLT_PFHT780Num[0]*HLT_PFHT680Num[0]);
    HLT_PFHT890.Fill(MjjValue,HLT_PFHT890Num[0]*HLT_PFHT780Num[0]);
    HLT_PFHT1050.Fill(MjjValue,HLT_PFHT1050Num[0]*HLT_PFHT890Num[0]);
    }
  }

  //Neccesary so files dont get lost
  HLT_PFJet40.SetDirectory(0);
  HLT_PFJet60.SetDirectory(0);
  HLT_PFJet80.SetDirectory(0);
  HLT_PFJet110.SetDirectory(0);
  HLT_PFJet140.SetDirectory(0);
  HLT_PFJet200.SetDirectory(0);
  HLT_PFJet260.SetDirectory(0);
  HLT_PFJet320.SetDirectory(0);
  HLT_PFJet400.SetDirectory(0);
  HLT_PFJet450.SetDirectory(0);
  HLT_PFJet500.SetDirectory(0);
  HLT_PFJet550.SetDirectory(0);
  HLT_PFHT180.SetDirectory(0);
  HLT_PFHT250.SetDirectory(0);
  HLT_PFHT350.SetDirectory(0);
  HLT_PFHT370.SetDirectory(0);
  HLT_PFHT430.SetDirectory(0);
  HLT_PFHT510.SetDirectory(0);
  HLT_PFHT590.SetDirectory(0);
  HLT_PFHT680.SetDirectory(0);
  HLT_PFHT780.SetDirectory(0);
  HLT_PFHT890.SetDirectory(0);
  HLT_PFHT1050.SetDirectory(0);
  Ref_HLT_PFJet40.SetDirectory(0);
  Ref_HLT_PFJet60.SetDirectory(0);
  Ref_HLT_PFJet80.SetDirectory(0);
  Ref_HLT_PFJet110.SetDirectory(0);
  Ref_HLT_PFJet140.SetDirectory(0);
  Ref_HLT_PFJet200.SetDirectory(0);
  Ref_HLT_PFJet260.SetDirectory(0);
  Ref_HLT_PFJet320.SetDirectory(0);
  Ref_HLT_PFJet400.SetDirectory(0);
  Ref_HLT_PFJet450.SetDirectory(0);
  Ref_HLT_PFJet500.SetDirectory(0);
  Ref_HLT_PFJet550.SetDirectory(0);
  Ref_HLT_PFHT180.SetDirectory(0);
  Ref_HLT_PFHT250.SetDirectory(0);
  Ref_HLT_PFHT350.SetDirectory(0);
  Ref_HLT_PFHT370.SetDirectory(0);
  Ref_HLT_PFHT430.SetDirectory(0);
  Ref_HLT_PFHT510.SetDirectory(0);
  Ref_HLT_PFHT590.SetDirectory(0);
  Ref_HLT_PFHT680.SetDirectory(0);
  Ref_HLT_PFHT780.SetDirectory(0);
  Ref_HLT_PFHT890.SetDirectory(0);
  Ref_HLT_PFHT1050.SetDirectory(0);





  TFile* outHistFile = TFile::Open(outName,"RECREATE");
  //Write HLT Triggers Data to Root
  outHistFile->mkdir("HLT_PFJet");
  outHistFile->cd("HLT_PFJet");
  HLT_PFJet40.Write();
  HLT_PFJet60.Write();
  HLT_PFJet80.Write();
  HLT_PFJet110.Write();
  HLT_PFJet140.Write();
  HLT_PFJet200.Write();
  HLT_PFJet260.Write();
  HLT_PFJet320.Write();
  HLT_PFJet400.Write();
  HLT_PFJet450.Write();
  HLT_PFJet500.Write();
  HLT_PFJet550.Write();
  Ref_HLT_PFJet40.Write();
  Ref_HLT_PFJet60.Write();
  Ref_HLT_PFJet80.Write();
  Ref_HLT_PFJet110.Write();
  Ref_HLT_PFJet140.Write();
  Ref_HLT_PFJet200.Write();
  Ref_HLT_PFJet260.Write();
  Ref_HLT_PFJet320.Write();
  Ref_HLT_PFJet400.Write();
  Ref_HLT_PFJet450.Write();
  Ref_HLT_PFJet500.Write();
  Ref_HLT_PFJet550.Write();
  //Write Jet2 Data to Root
  outHistFile->mkdir("HLT_PFHT");
  outHistFile->cd("HLT_PFHT");
  HLT_PFHT180.Write();
  HLT_PFHT250.Write();
  HLT_PFHT350.Write();
  HLT_PFHT370.Write();
  HLT_PFHT430.Write();
  HLT_PFHT510.Write();
  HLT_PFHT590.Write();
  HLT_PFHT680.Write();
  HLT_PFHT780.Write();
  HLT_PFHT890.Write();
  HLT_PFHT1050.Write();
  Ref_HLT_PFHT180.Write();
  Ref_HLT_PFHT250.Write();
  Ref_HLT_PFHT350.Write();
  Ref_HLT_PFHT370.Write();
  Ref_HLT_PFHT430.Write();
  Ref_HLT_PFHT510.Write();
  Ref_HLT_PFHT590.Write();
  Ref_HLT_PFHT680.Write();
  Ref_HLT_PFHT780.Write();
  Ref_HLT_PFHT890.Write();
  Ref_HLT_PFHT1050.Write();
  outHistFile->Close();
  return 0;
}
