int TreeToHist()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFile1[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char rootFile2[] = "/nfs/dust/cms/user/hinzmann/run2023/JetMET1_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root";
  char outName[] = "/nfs/dust/cms/user/mueckejo/RootB/PlotDijetJetID_Run2023B.root";


   TChain tree("Events");   // name of the tree is the argument
   tree.Add(rootFile1);
   tree.Add(rootFile2);

  //declare variables to Load from Root Tree
  //variables of Jet1
  float pt1Num;
  float y1Num;
  float eta1Num;
  float phi1Num;
  float mass1Num;
  float jec1Num;
  float muf1Num;
  float nhf1Num;
  float chf1Num;
  float area1Num;
  float nemf1Num;
  float cemf1Num;
  float btagDeepFlavB1Num;
  int nConstituents1Num;
  int TightID1;

  tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
  tree.SetBranchAddress("jetAK4_y1",&y1Num);
  tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
  tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
  tree.SetBranchAddress("jetAK4_mass1",&mass1Num);
  tree.SetBranchAddress("jetAK4_jec1",&jec1Num);
  tree.SetBranchAddress("jetAK4_muf1",&muf1Num);
  tree.SetBranchAddress("jetAK4_nhf1",&nhf1Num);
  tree.SetBranchAddress("jetAK4_chf1",&chf1Num);
  tree.SetBranchAddress("jetAK4_area1",&area1Num);
  tree.SetBranchAddress("jetAK4_nemf1",&nemf1Num);
  tree.SetBranchAddress("jetAK4_cemf1",&cemf1Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB1",&btagDeepFlavB1Num);
  tree.SetBranchAddress("jetAK4_nConstituents1",&nConstituents1Num);
  tree.SetBranchAddress("jetAK4_TightID1",&TightID1);

  TH1D pt1("data_pt1","pt for jet1 data",20,0,4000);
  pt1.Sumw2();
  TH1D y1("data_y1","y for jet1 data",20,-6,6);
  y1.Sumw2();
  TH1D eta1("data_eta1","eta for jet1 data",20,-6,6);
  eta1.Sumw2();
  TH1D phi1("data_phi1","phi for jet1 data",20,-4,4);
  phi1.Sumw2();
  TH1D mass1("data_mass1","mass for jet1 data",20,0,500);
  mass1.Sumw2();
  TH1D jec1("data_jec1","jec for jet1 data",20,0.5,1.3);
  jec1.Sumw2();
  TH1D muf1("data_muf1","muf for jet1 data",20,0,1);
  muf1.Sumw2();
  TH1D nhf1("data_nhf1","nhf for jet1 data",20,0,1);
  nhf1.Sumw2();
  TH1D chf1("data_chf1","chf for jet1 data",20,0,1);
  chf1.Sumw2();
  TH1D area1("data_area1","area for jet1 data",20,0.2,1);
  area1.Sumw2();
  TH1D nemf1("data_nemf1","nemf for jet1 data",20,0,1);
  nemf1.Sumw2();
  TH1D cemf1("data_cemf1","cemf for jet1 data",20,0,1);
  cemf1.Sumw2();
  TH1D btagDeepFlavB1("data_btagDeepFlavB1","btagDeepFlavB for jet1 data",20,0,1);
  btagDeepFlavB1.Sumw2();
  TH1D nConstituents1("data_nConstituents1","nConstituents for jet1 data",20,0,100);
  nConstituents1.Sumw2();

  //variables of Jet2
  float pt2Num;
  float y2Num;
  float eta2Num;
  float phi2Num;
  float mass2Num;
  float jec2Num;
  float muf2Num;
  float nhf2Num;
  float chf2Num;
  float area2Num;
  float nemf2Num;
  float cemf2Num;
  float btagDeepFlavB2Num;
  int nConstituents2Num;
  int TightID2;

  tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
  tree.SetBranchAddress("jetAK4_y2",&y2Num);
  tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
  tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
  tree.SetBranchAddress("jetAK4_mass2",&mass2Num);
  tree.SetBranchAddress("jetAK4_jec2",&jec2Num);
  tree.SetBranchAddress("jetAK4_muf2",&muf2Num);
  tree.SetBranchAddress("jetAK4_nhf2",&nhf2Num);
  tree.SetBranchAddress("jetAK4_chf2",&chf2Num);
  tree.SetBranchAddress("jetAK4_area2",&area2Num);
  tree.SetBranchAddress("jetAK4_nemf2",&nemf2Num);
  tree.SetBranchAddress("jetAK4_cemf2",&cemf2Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB2",&btagDeepFlavB2Num);
  tree.SetBranchAddress("jetAK4_nConstituents2",&nConstituents2Num);
  tree.SetBranchAddress("jetAK4_TightID2",&TightID2);

  TH1D pt2("data_pt2","pt for jet2 data",20,0,4000);
  pt2.Sumw2();
  TH1D y2("data_y2","y for jet2 data",20,-6,6);
  y2.Sumw2();
  TH1D eta2("data_eta2","eta for jet2 data",20,-6,6);
  eta2.Sumw2();
  TH1D phi2("data_phi2","phi for jet2 data",20,-4,4);
  phi2.Sumw2();
  TH1D mass2("data_mass2","mass for jet2 data",20,0,500);
  mass2.Sumw2();
  TH1D jec2("data_jec2","jec for jet2 data",20,0.5,1.3);
  jec2.Sumw2();
  TH1D muf2("data_muf2","muf for jet2 data",20,0,1);
  muf2.Sumw2();
  TH1D nhf2("data_nhf2","nhf for jet2 data",20,0,1);
  nhf2.Sumw2();
  TH1D chf2("data_chf2","chf for jet2 data",20,0,1);
  chf2.Sumw2();
  TH1D area2("data_area2","area for jet2 data",20,0.2,1);
  area2.Sumw2();
  TH1D nemf2("data_nemf2","nemf for jet2 data",20,0,1);
  nemf2.Sumw2();
  TH1D cemf2("data_cemf2","cemf for jet2 data",20,0,1);
  cemf2.Sumw2();
  TH1D btagDeepFlavB2("data_btagDeepFlavB2","btagDeepFlavB for jet2 data",20,0,1);
  btagDeepFlavB2.Sumw2();
  TH1D nConstituents2("data_nConstituents2","nConstituents for jet2 data",20,0,100);
  nConstituents2.Sumw2();

  //variables of Jet3
  float pt3Num;
  float y3Num;
  float eta3Num;
  float phi3Num;
  float mass3Num;
  float jec3Num;
  float muf3Num;
  float nhf3Num;
  float chf3Num;
  float area3Num;
  float nemf3Num;
  float cemf3Num;
  float btagDeepFlavB3Num;
  int nConstituents3Num;
  int TightID3;

  tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
  tree.SetBranchAddress("jetAK4_y3",&y3Num);
  tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
  tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
  tree.SetBranchAddress("jetAK4_mass3",&mass3Num);
  tree.SetBranchAddress("jetAK4_jec3",&jec3Num);
  tree.SetBranchAddress("jetAK4_muf3",&muf3Num);
  tree.SetBranchAddress("jetAK4_nhf3",&nhf3Num);
  tree.SetBranchAddress("jetAK4_chf3",&chf3Num);
  tree.SetBranchAddress("jetAK4_area3",&area3Num);
  tree.SetBranchAddress("jetAK4_nemf3",&nemf3Num);
  tree.SetBranchAddress("jetAK4_cemf3",&cemf3Num);
  tree.SetBranchAddress("jetAK4_btagDeepFlavB3",&btagDeepFlavB3Num);
  tree.SetBranchAddress("jetAK4_nConstituents3",&nConstituents3Num);
  tree.SetBranchAddress("jetAK4_TightID3",&TightID3);

  TH1D pt3("data_pt3","pt for jet3 data",20,0,4000);
  pt3.Sumw2();
  TH1D y3("data_y3","y for jet3 data",20,-6,6);
  y3.Sumw2();
  TH1D eta3("data_eta3","eta for jet3 data",20,-6,6);
  eta3.Sumw2();
  TH1D phi3("data_phi3","phi for jet3 data",20,-4,4);
  phi3.Sumw2();
  TH1D mass3("data_mass3","mass for jet3 data",20,0,500);
  mass3.Sumw2();
  TH1D jec3("data_jec3","jec for jet3 data",20,0.5,1.3);
  jec3.Sumw2();
  TH1D muf3("data_muf3","muf for jet3 data",20,0,1);
  muf3.Sumw2();
  TH1D nhf3("data_nhf3","nhf for jet3 data",20,0,1);
  nhf3.Sumw2();
  TH1D chf3("data_chf3","chf for jet3 data",20,0,1);
  chf3.Sumw2();
  TH1D area3("data_area3","area for jet3 data",20,0.2,1);
  area3.Sumw2();
  TH1D nemf3("data_nemf3","nemf for jet3 data",20,0,1);
  nemf3.Sumw2();
  TH1D cemf3("data_cemf3","cemf for jet3 data",20,0,1);
  cemf3.Sumw2();
  TH1D btagDeepFlavB3("data_btagDeepFlavB3","btagDeepFlavB for jet3 data",20,0,1);
  btagDeepFlavB3.Sumw2();
  TH1D nConstituents3("data_nConstituents3","nConstituents for jet3 data",20,0,100);
  nConstituents3.Sumw2();

  //Create quantities calculated from variables
  TH1D MjjHist("data_mjj","Mjj [Gev]",20,0,10000);
  MjjHist.Sumw2();

  TH1D YBoostHist("data_yboost","YBoost",20,0,3);
  YBoostHist.Sumw2();

  TH1D ChiHist("data_chi","Chi",20,0,20);
  ChiHist.Sumw2();

  //Fill the Hists with Root Tree Data
  for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
  {
    tree.GetEntry(entry);

    //Calculate Mjj
    TLorentzVector Lorentz0, Lorentz1;
    Lorentz0.SetPtEtaPhiM(pt1Num,eta1Num,phi1Num,mass1Num);
    Lorentz1.SetPtEtaPhiM(pt2Num,eta2Num,phi2Num,mass2Num);
    TLorentzVector MjjSum = Lorentz0 + Lorentz1;
    double MjjValue = MjjSum.M();

    //Calculate chi
    double ChiValue = exp(abs(y1Num-y2Num));

    //Calculate yboost
    double YBoostValue = (y1Num+y2Num)/2;

    if (MjjValue > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
    {
      if(TightID1 == 1){
        //Fill Jet1
        pt1.Fill(pt1Num);
        y1.Fill(y1Num);
        eta1.Fill(eta1Num);
        phi1.Fill(phi1Num);
        mass1.Fill(mass1Num);
        jec1.Fill(jec1Num);
        muf1.Fill(muf1Num);
        nhf1.Fill(nhf1Num);
        chf1.Fill(chf1Num);
        area1.Fill(area1Num);
        nemf1.Fill(nemf1Num);
        cemf1.Fill(cemf1Num);
        btagDeepFlavB1.Fill(btagDeepFlavB1Num);
        nConstituents1.Fill(nConstituents1Num);
      }

      if(TightID2 == 1){
        //Fill Jet2
        pt2.Fill(pt2Num);
        y2.Fill(y2Num);
        eta2.Fill(eta2Num);
        phi2.Fill(phi2Num);
        mass2.Fill(mass2Num);
        jec2.Fill(jec2Num);
        muf2.Fill(muf2Num);
        nhf2.Fill(nhf2Num);
        chf2.Fill(chf2Num);
        area2.Fill(area2Num);
        nemf2.Fill(nemf2Num);
        cemf2.Fill(cemf2Num);
        btagDeepFlavB2.Fill(btagDeepFlavB2Num);
        nConstituents2.Fill(nConstituents2Num);
      }

      if(TightID3 == 1){
        //Fill Jet3
        pt3.Fill(pt3Num);
        y3.Fill(y3Num);
        eta3.Fill(eta3Num);
        phi3.Fill(phi3Num);
        mass3.Fill(mass3Num);
        jec3.Fill(jec3Num);
        muf3.Fill(muf3Num);
        nhf3.Fill(nhf3Num);
        chf3.Fill(chf3Num);
        area3.Fill(area3Num);
        nemf3.Fill(nemf3Num);
        cemf3.Fill(cemf3Num);
        btagDeepFlavB3.Fill(btagDeepFlavB3Num);
        nConstituents3.Fill(nConstituents3Num);
      }

      if(TightID1 == 1 && TightID2 == 1){
        //fill yboost
        YBoostHist.Fill(YBoostValue);

        //fill Mjj
        MjjHist.Fill(MjjValue);

        //fill chi
        ChiHist.Fill(ChiValue);
      }
    }
  }

  //Neccesary so files dont get lost
  pt1.SetDirectory(0);
  pt1.SetDirectory(0);
  y1.SetDirectory(0);
  eta1.SetDirectory(0);
  phi1.SetDirectory(0);
  mass1.SetDirectory(0);
  jec1.SetDirectory(0);
  muf1.SetDirectory(0);
  nhf1.SetDirectory(0);
  chf1.SetDirectory(0);
  area1.SetDirectory(0);
  nemf1.SetDirectory(0);
  cemf1.SetDirectory(0);
  btagDeepFlavB1.SetDirectory(0);
  nConstituents1.SetDirectory(0);
  pt2.SetDirectory(0);
  pt2.SetDirectory(0);
  y2.SetDirectory(0);
  eta2.SetDirectory(0);
  phi2.SetDirectory(0);
  mass2.SetDirectory(0);
  jec2.SetDirectory(0);
  muf2.SetDirectory(0);
  nhf2.SetDirectory(0);
  chf2.SetDirectory(0);
  area2.SetDirectory(0);
  nemf2.SetDirectory(0);
  cemf2.SetDirectory(0);
  btagDeepFlavB2.SetDirectory(0);
  nConstituents2.SetDirectory(0);
  pt3.SetDirectory(0);
  pt3.SetDirectory(0);
  y3.SetDirectory(0);
  eta3.SetDirectory(0);
  phi3.SetDirectory(0);
  mass3.SetDirectory(0);
  jec3.SetDirectory(0);
  muf3.SetDirectory(0);
  nhf3.SetDirectory(0);
  chf3.SetDirectory(0);
  area3.SetDirectory(0);
  nemf3.SetDirectory(0);
  cemf3.SetDirectory(0);
  btagDeepFlavB3.SetDirectory(0);
  nConstituents3.SetDirectory(0);
  MjjHist.SetDirectory(0);
  YBoostHist.SetDirectory(0);
  ChiHist.SetDirectory(0);

  TFile* outHistFile = TFile::Open(outName,"RECREATE");
  //Write Jet1 Data to Root
  outHistFile->mkdir("Jet1");
  outHistFile->cd("Jet1");
  pt1.Write();
  y1.Write();
  eta1.Write();
  phi1.Write();
  mass1.Write();
  jec1.Write();
  muf1.Write();
  nhf1.Write();
  chf1.Write();
  area1.Write();
  nemf1.Write();
  cemf1.Write();
  btagDeepFlavB1.Write();
  nConstituents1.Write();
  //Write Jet2 Data to Root
  outHistFile->mkdir("Jet2");
  outHistFile->cd("Jet2");
  pt2.Write();
  y2.Write();
  eta2.Write();
  phi2.Write();
  mass2.Write();
  jec2.Write();
  muf2.Write();
  nhf2.Write();
  chf2.Write();
  area2.Write();
  nemf2.Write();
  cemf2.Write();
  btagDeepFlavB2.Write();
  nConstituents2.Write();
  //Write Jet3 Data to Root
  outHistFile->mkdir("Jet3");
  outHistFile->cd("Jet3");
  pt3.Write();
  y3.Write();
  eta3.Write();
  phi3.Write();
  mass3.Write();
  jec3.Write();
  muf3.Write();
  nhf3.Write();
  chf3.Write();
  area3.Write();
  nemf3.Write();
  cemf3.Write();
  btagDeepFlavB3.Write();
  nConstituents3.Write();
  //Write quantities to Root
  outHistFile->mkdir("Kinematics");
  outHistFile->cd("Kinematics");
  MjjHist.Write();
  YBoostHist.Write();
  ChiHist.Write();
  outHistFile->Close();
  return 0;
}
