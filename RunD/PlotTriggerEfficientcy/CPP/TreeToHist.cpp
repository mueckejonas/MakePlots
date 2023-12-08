int TreeToHist()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023D-22Sep2023_v1-v1_NANOAOD.root";
  char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023D-22Sep2023_v2-v1_NANOAOD.root";
  char rootFile3[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023D-22Sep2023_v1-v1_NANOAOD.root";
  char rootFile4[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023D-22Sep2023_v2-v1_NANOAOD.root";
  char outName[] = "/nfs/dust/cms/user/mueckejo/RootD/PlotTriggerEfficientcy_Run2023D.root";


  TChain tree("Events");   // name of the tree is the argument
  tree.Add(rootFile1);
  tree.Add(rootFile2);
  tree.Add(rootFile3);
  tree.Add(rootFile4);

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
  int HLT_PFJet40Num[eventNum];
  int HLT_PFJet60Num[eventNum];
  int HLT_PFJet80Num[eventNum];
  int HLT_PFJet110Num[eventNum];
  int HLT_PFJet140Num[eventNum];
  int HLT_PFJet200Num[eventNum];
  int HLT_PFJet260Num[eventNum];
  int HLT_PFJet320Num[eventNum];
  int HLT_PFJet400Num[eventNum];
  int HLT_PFJet450Num[eventNum];
  int HLT_PFJet500Num[eventNum];
  int HLT_PFJet550Num[eventNum];

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

  TH1D HLT_PFJet40("HLT_PFJet40","HLT_PFJet40",50,0,10000);
  HLT_PFJet40.Sumw2();
  TH1D HLT_PFJet60("HLT_PFJet60","HLT_PFJet60",50,0,10000);
  HLT_PFJet60.Sumw2();
  TH1D HLT_PFJet80("HLT_PFJet80","HLT_PFJet80",50,0,10000);
  HLT_PFJet80.Sumw2();
  TH1D HLT_PFJet110("HLT_PFJet110","HLT_PFJet110",50,0,10000);
  HLT_PFJet110.Sumw2();
  TH1D HLT_PFJet140("HLT_PFJet140","HLT_PFJet140",50,0,10000);
  HLT_PFJet140.Sumw2();
  TH1D HLT_PFJet200("HLT_PFJet200","HLT_PFJet200",50,0,10000);
  HLT_PFJet200.Sumw2();
  TH1D HLT_PFJet260("HLT_PFJet260","HLT_PFJet260",50,0,10000);
  HLT_PFJet260.Sumw2();
  TH1D HLT_PFJet320("HLT_PFJet320","HLT_PFJet320",50,0,10000);
  HLT_PFJet320.Sumw2();
  TH1D HLT_PFJet400("HLT_PFJet400","HLT_PFJet400",50,0,10000);
  HLT_PFJet400.Sumw2();
  TH1D HLT_PFJet450("HLT_PFJet450","HLT_PFJet450",50,0,10000);
  HLT_PFJet450.Sumw2();
  TH1D HLT_PFJet500("HLT_PFJet500","HLT_PFJet500",50,0,10000);
  HLT_PFJet500.Sumw2();
  TH1D HLT_PFJet550("HLT_PFJet550","HLT_PFJet550",50,0,10000);
  HLT_PFJet550.Sumw2();

  int HLT_PFHT180Num[eventNum];
  int HLT_PFHT250Num[eventNum];
  int HLT_PFHT350Num[eventNum];
  int HLT_PFHT370Num[eventNum];
  int HLT_PFHT430Num[eventNum];
  int HLT_PFHT510Num[eventNum];
  int HLT_PFHT590Num[eventNum];
  int HLT_PFHT680Num[eventNum];
  int HLT_PFHT780Num[eventNum];
  int HLT_PFHT890Num[eventNum];
  int HLT_PFHT1050Num[eventNum];

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

  TH1D HLT_PFHT180("HLT_PFHT180","HLT_PFHT180",50,0,10000);
  HLT_PFHT180.Sumw2();
  TH1D HLT_PFHT250("HLT_PFHT250","HLT_PFHT250",50,0,10000);
  HLT_PFHT250.Sumw2();
  TH1D HLT_PFHT350("HLT_PFHT350","HLT_PFHT350",50,0,10000);
  HLT_PFHT350.Sumw2();
  TH1D HLT_PFHT370("HLT_PFHT370","HLT_PFHT370",50,0,10000);
  HLT_PFHT370.Sumw2();
  TH1D HLT_PFHT430("HLT_PFHT430","HLT_PFHT430",50,0,10000);
  HLT_PFHT430.Sumw2();
  TH1D HLT_PFHT510("HLT_PFHT510","HLT_PFHT510",50,0,10000);
  HLT_PFHT510.Sumw2();
  TH1D HLT_PFHT590("HLT_PFHT590","HLT_PFHT590",50,0,10000);
  HLT_PFHT590.Sumw2();
  TH1D HLT_PFHT680("HLT_PFHT680","HLT_PFHT680",50,0,10000);
  HLT_PFHT680.Sumw2();
  TH1D HLT_PFHT780("HLT_PFHT780","HLT_PFHT780",50,0,10000);
  HLT_PFHT780.Sumw2();
  TH1D HLT_PFHT890("HLT_PFHT890","HLT_PFHT890",50,0,10000);
  HLT_PFHT890.Sumw2();
  TH1D HLT_PFHT1050("HLT_PFHT1050","HLT_PFHT1050",50,0,10000);
  HLT_PFHT1050.Sumw2();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);

    //Calculate Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
    Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();

        //fill HLT Hists
        if(HLT_PFJet40Num[0] == 1)
        {
          HLT_PFJet40.Fill(MjjValue);
        }
        if(HLT_PFJet60Num[0] == 1)
        {
          HLT_PFJet60.Fill(MjjValue);
        }
        if(HLT_PFJet80Num[0] == 1)
        {
          HLT_PFJet80.Fill(MjjValue);
        }
        if(HLT_PFJet110Num[0] == 1)
        {
          HLT_PFJet110.Fill(MjjValue);
        }
        if(HLT_PFJet140Num[0] == 1)
        {
          HLT_PFJet140.Fill(MjjValue);
        }
        if(HLT_PFJet200Num[0] == 1)
        {
          HLT_PFJet200.Fill(MjjValue);
        }
        if(HLT_PFJet260Num[0] == 1)
        {
          HLT_PFJet260.Fill(MjjValue);
        }
        if(HLT_PFJet320Num[0] == 1)
        {
          HLT_PFJet320.Fill(MjjValue);
        }
        if(HLT_PFJet400Num[0] == 1)
        {
          HLT_PFJet400.Fill(MjjValue);
        }
        if(HLT_PFJet450Num[0] == 1)
        {
          HLT_PFJet450.Fill(MjjValue);
        }
        if(HLT_PFJet500Num[0] == 1)
        {
          HLT_PFJet500.Fill(MjjValue);
        }
        if(HLT_PFJet550Num[0] == 1)
        {
          HLT_PFJet550.Fill(MjjValue);
        }

        //fill HLTPF Hists
        if(HLT_PFHT180Num[0] == 1)
        {
          HLT_PFHT180.Fill(MjjValue);
        }
        if(HLT_PFHT250Num[0] == 1)
        {
          HLT_PFHT250.Fill(MjjValue);
        }
        if(HLT_PFHT350Num[0] == 1)
        {
          HLT_PFHT350.Fill(MjjValue);
        }
        if(HLT_PFHT370Num[0] == 1)
        {
          HLT_PFHT370.Fill(MjjValue);
        }
        if(HLT_PFHT430Num[0] == 1)
        {
          HLT_PFHT430.Fill(MjjValue);
        }
        if(HLT_PFHT510Num[0] == 1)
        {
          HLT_PFHT510.Fill(MjjValue);
        }
        if(HLT_PFHT590Num[0] == 1)
        {
          HLT_PFHT590.Fill(MjjValue);
        }
        if(HLT_PFHT680Num[0] == 1)
        {
          HLT_PFHT680.Fill(MjjValue);
        }
        if(HLT_PFHT780Num[0] == 1)
        {
          HLT_PFHT780.Fill(MjjValue);
        }
        if(HLT_PFHT890Num[0] == 1)
        {
          HLT_PFHT890.Fill(MjjValue);
        }
        if(HLT_PFHT1050Num[0] == 1)
        {
          HLT_PFHT1050.Fill(MjjValue);
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
  outHistFile->Close();
  return 0;
}