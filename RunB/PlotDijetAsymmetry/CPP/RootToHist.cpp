int RootToHist()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char outName[] = "/nfs/dust/cms/user/mueckejo/RootB/PlotDijetAsymmetry_Run2023B.root";


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

  TH1D PtAsymmetry("PtAsymmetry","PtAsymmetry",50,0,1);
  PtAsymmetry.Sumw2();
  TH1D PhiDifference("PhiDifference","PhiDifference",50,-360,360);
  PhiDifference.Sumw2();
  TH1D EtaDifference("EtaDifference","EtaDifference",50,-6,6);
  EtaDifference.Sumw2();
  TH1D YDifference("YDifference","YDifference",50,-4,4);
  YDifference.Sumw2();

  float numberEntries = tree.GetEntries();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);

    if(entry % 100000 == 0)
    {
      std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
    }

    PtAsymmetry.Fill((pt1Num[0]-pt2Num[0])/(pt1Num[0]+pt2Num[0]));
    PhiDifference.Fill(phi1Num[0]-phi2Num[0]);
    EtaDifference.Fill(eta1Num[0]-eta2Num[0]);
    YDifference.Fill(y1Num[0]-y2Num[0]);
  }

  //Neccesary so files dont get lost
  PtAsymmetry.SetDirectory(0);
  PhiDifference.SetDirectory(0);
  EtaDifference.SetDirectory(0);
  YDifference.SetDirectory(0);

  TFile* outHistFile = TFile::Open(outName,"RECREATE");
  PtAsymmetry.Write();
  PhiDifference.Write();
  EtaDifference.Write();
  YDifference.Write();
  outHistFile->Close();
  return 0;
}
