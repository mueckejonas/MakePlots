int RootToHist()
{

  string ranges[13] = {"200to300","300to500","500to700","700to1000","1000to1500","1500to2000","2000toInf"};
  int rangesNums[13] = {23,25,20,20,6,4,2};

  for (int i = 0; i < 7; i++)
  {
    string outName1 = "/nfs/dust/cms/user/mueckejo/RootS2018/"+ranges[i]+"_PlotSimulation_Run22018_MC.root";
    string outName2 = "/nfs/dust/cms/user/mueckejo/RootS2018/"+ranges[i]+"_PlotSimulation_Run22018_Gen.root";


    TChain tree("tree");   // name of the tree is the argument
    for (int j = 0; j < rangesNums[i]; ++j){
      string inputtree = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT"+ranges[i]+"_RunII_106X_v2_"+to_string(j)+"_tree.root";
      tree.Add(inputtree.c_str());
    }

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float y1Num[eventNum];
    float eta1Num[eventNum];
    float phi1Num[eventNum];
    float mass1Num[eventNum];
    float jec1Num[eventNum];
    float muf1Num[eventNum];
    float nhf1Num[eventNum];
    float chf1Num[eventNum];
    float area1Num[eventNum];
    float nemf1Num[eventNum];
    float cemf1Num[eventNum];
    int TightID1[eventNum];

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
    tree.SetBranchAddress("jetAK4_IDTight1",&TightID1);

    TH1D pt1("Simpt1","pt for jet1 Sim",20,0,4000);
    pt1.Sumw2();
    TH1D y1("Simy1","y for jet1 Sim",20,-6,6);
    y1.Sumw2();
    TH1D eta1("Simeta1","eta for jet1 Sim",20,-6,6);
    eta1.Sumw2();
    TH1D phi1("Simphi1","phi for jet1 Sim",20,-4,4);
    phi1.Sumw2();
    TH1D mass1("Simmass1","mass for jet1 Sim",20,0,500);
    mass1.Sumw2();
    TH1D jec1("Simjec1","jec for jet1 Sim",20,0.5,1.3);
    jec1.Sumw2();
    TH1D muf1("Simmuf1","muf for jet1 Sim",20,0,1);
    muf1.Sumw2();
    TH1D nhf1("Simnhf1","nhf for jet1 Sim",20,0,1);
    nhf1.Sumw2();
    TH1D chf1("Simchf1","chf for jet1 Sim",20,0,1);
    chf1.Sumw2();
    TH1D area1("Simarea1","area for jet1 Sim",20,0.2,1);
    area1.Sumw2();
    TH1D nemf1("Simnemf1","nemf for jet1 Sim",20,0,1);
    nemf1.Sumw2();
    TH1D cemf1("Simcemf1","cemf for jet1 Sim",20,0,1);
    cemf1.Sumw2();

    //variables of Jet2
    float pt2Num[eventNum];
    float y2Num[eventNum];
    float eta2Num[eventNum];
    float phi2Num[eventNum];
    float mass2Num[eventNum];
    float jec2Num[eventNum];
    float muf2Num[eventNum];
    float nhf2Num[eventNum];
    float chf2Num[eventNum];
    float area2Num[eventNum];
    float nemf2Num[eventNum];
    float cemf2Num[eventNum];
    int TightID2[eventNum];

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
    tree.SetBranchAddress("jetAK4_IDTight2",&TightID2);

    TH1D pt2("Simpt2","pt for jet2 Sim",20,0,4000);
    pt2.Sumw2();
    TH1D y2("Simy2","y for jet2 Sim",20,-6,6);
    y2.Sumw2();
    TH1D eta2("Simeta2","eta for jet2 Sim",20,-6,6);
    eta2.Sumw2();
    TH1D phi2("Simphi2","phi for jet2 Sim",20,-4,4);
    phi2.Sumw2();
    TH1D mass2("Simmass2","mass for jet2 Sim",20,0,500);
    mass2.Sumw2();
    TH1D jec2("Simjec2","jec for jet2 Sim",20,0.5,1.3);
    jec2.Sumw2();
    TH1D muf2("Simmuf2","muf for jet2 Sim",20,0,1);
    muf2.Sumw2();
    TH1D nhf2("Simnhf2","nhf for jet2 Sim",20,0,1);
    nhf2.Sumw2();
    TH1D chf2("Simchf2","chf for jet2 Sim",20,0,1);
    chf2.Sumw2();
    TH1D area2("Simarea2","area for jet2 Sim",20,0.2,1);
    area2.Sumw2();
    TH1D nemf2("Simnemf2","nemf for jet2 Sim",20,0,1);
    nemf2.Sumw2();
    TH1D cemf2("Simcemf2","cemf for jet2 Sim",20,0,1);
    cemf2.Sumw2();

    //variables of Jet3
    float pt3Num[eventNum];
    float y3Num[eventNum];
    float eta3Num[eventNum];
    float phi3Num[eventNum];
    float mass3Num[eventNum];
    float jec3Num[eventNum];
    float muf3Num[eventNum];
    float nhf3Num[eventNum];
    float chf3Num[eventNum];
    float area3Num[eventNum];
    float nemf3Num[eventNum];
    float cemf3Num[eventNum];
    int TightID3[eventNum];

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
    tree.SetBranchAddress("jetAK4_IDTight3",&TightID3);

    TH1D pt3("Simpt3","pt for jet3 Sim",20,0,4000);
    pt3.Sumw2();
    TH1D y3("Simy3","y for jet3 Sim",20,-6,6);
    y3.Sumw2();
    TH1D eta3("Simeta3","eta for jet3 Sim",20,-6,6);
    eta3.Sumw2();
    TH1D phi3("Simphi3","phi for jet3 Sim",20,-4,4);
    phi3.Sumw2();
    TH1D mass3("Simmass3","mass for jet3 Sim",20,0,500);
    mass3.Sumw2();
    TH1D jec3("Simjec3","jec for jet3 Sim",20,0.5,1.3);
    jec3.Sumw2();
    TH1D muf3("Simmuf3","muf for jet3 Sim",20,0,1);
    muf3.Sumw2();
    TH1D nhf3("Simnhf3","nhf for jet3 Sim",20,0,1);
    nhf3.Sumw2();
    TH1D chf3("Simchf3","chf for jet3 Sim",20,0,1);
    chf3.Sumw2();
    TH1D area3("Simarea3","area for jet3 Sim",20,0.2,1);
    area3.Sumw2();
    TH1D nemf3("Simnemf3","nemf for jet3 Sim",20,0,1);
    nemf3.Sumw2();
    TH1D cemf3("Simcemf3","cemf for jet3 Sim",20,0,1);
    cemf3.Sumw2();

    //Create quantities calculated from variables
    TH1D MjjHist("Simmjj","Mjj [Gev]",20,0,10000);
    MjjHist.Sumw2();

    TH1D YBoostHist("Simyboost","YBoost",20,0,3);
    YBoostHist.Sumw2();

    TH1D ChiHist("Simchi","Chi",20,0,20);
    ChiHist.Sumw2();

    //variables of genJet
    float genpt1Num[eventNum];
    float geny1Num[eventNum];
    float geneta1Num[eventNum];
    float genphi1Num[eventNum];
    float genmass1Num[eventNum];
    float genpt2Num[eventNum];
    float geny2Num[eventNum];
    float geneta2Num[eventNum];
    float genphi2Num[eventNum];
    float genmass2Num[eventNum];
    float genpt3Num[eventNum];
    float geny3Num[eventNum];
    float geneta3Num[eventNum];
    float genphi3Num[eventNum];
    float genmass3Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt1",&genpt1Num);
    tree.SetBranchAddress("genJetAK4_y1",&geny1Num);
    tree.SetBranchAddress("genJetAK4_eta1",&geneta1Num);
    tree.SetBranchAddress("genJetAK4_phi1",&genphi1Num);
    tree.SetBranchAddress("genJetAK4_mass1",&genmass1Num);
    tree.SetBranchAddress("genJetAK4_pt2",&genpt2Num);
    tree.SetBranchAddress("genJetAK4_y2",&geny2Num);
    tree.SetBranchAddress("genJetAK4_eta2",&geneta2Num);
    tree.SetBranchAddress("genJetAK4_phi2",&genphi2Num);
    tree.SetBranchAddress("genJetAK4_mass2",&genmass2Num);
    tree.SetBranchAddress("genJetAK4_pt3",&genpt3Num);
    tree.SetBranchAddress("genJetAK4_y3",&geny3Num);
    tree.SetBranchAddress("genJetAK4_eta3",&geneta3Num);
    tree.SetBranchAddress("genJetAK4_phi3",&genphi3Num);
    tree.SetBranchAddress("genJetAK4_mass3",&genmass3Num);


    TH1D genpt1("Genpt1","pt for genJet1",20,0,4000);
    genpt1.Sumw2();
    TH1D geny1("Geny1","y for genJet1",20,-6,6);
    geny1.Sumw2();
    TH1D geneta1("Geneta1","eta for genJet1",20,-6,6);
    geneta1.Sumw2();
    TH1D genphi1("Genphi1","phi for genJet1",20,-4,4);
    genphi1.Sumw2();
    TH1D genmass1("Genmass1","mass for genJet1",20,0,500);
    genmass1.Sumw2();
    TH1D genpt2("Genpt2","pt for genJet2",20,0,4000);
    genpt2.Sumw2();
    TH1D geny2("Geny2","y for genJet2",20,-6,6);
    geny2.Sumw2();
    TH1D geneta2("Geneta2","eta for genJet2",20,-6,6);
    geneta2.Sumw2();
    TH1D genphi2("Genphi2","phi for genJet2",20,-4,4);
    genphi2.Sumw2();
    TH1D genmass2("Genmass2","mass for genJet2",20,0,500);
    genmass2.Sumw2();
    TH1D genpt3("Genpt3","pt for genJet3",20,0,4000);
    genpt3.Sumw2();
    TH1D geny3("Geny3","y for genJet3",20,-6,6);
    geny3.Sumw2();
    TH1D geneta3("Geneta3","eta for genJet3",20,-6,6);
    geneta3.Sumw2();
    TH1D genphi3("Genphi3","phi for genJet3",20,-4,4);
    genphi3.Sumw2();
    TH1D genmass3("Genmass3","mass for genJet3",20,0,500);
    genmass3.Sumw2();

    //caulculate qunatities from variables of gen jets
    TH1D genMjjHist("Genmjj","Mjj [Gev]",20,0,10000);
    genMjjHist.Sumw2();

    TH1D genYBoostHist("Genyboost","YBoost",20,0,3);
    genYBoostHist.Sumw2();

    TH1D genChiHist("Genchi","Chi",20,0,20);
    genChiHist.Sumw2();

    std::cout << tree.GetEntries() << std::endl;
    float numberEntries = tree.GetEntries();
    //Fill the Hists with Root Tree Sim and Genjets
    for (Long64_t entry = 0; entry < tree.GetEntries(); ++entry)
    {
      tree.GetEntry(entry);

      if(entry % 100000 == 0)
      {
        std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
      }

      //Calculate Sim Mjj
      TLorentzVector Lorentz0, Lorentz1;
      Lorentz0.SetPtEtaPhiM(pt1Num[0],eta1Num[0],phi1Num[0],mass1Num[0]);
      Lorentz1.SetPtEtaPhiM(pt2Num[0],eta2Num[0],phi2Num[0],mass2Num[0]);
      TLorentzVector MjjSum = Lorentz0 + Lorentz1;
      double MjjValue = MjjSum.M();

      //Calculate Sim chi
      double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

      //Calculate Sim yboost
      double YBoostValue = (y1Num[0]+y2Num[0])/2;

      //if (MjjValue > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)

        //Fill SimJet1
        //if(TightID1[0] == 1){
          pt1.Fill(pt1Num[0]);
          y1.Fill(y1Num[0]);
          eta1.Fill(eta1Num[0]);
          phi1.Fill(phi1Num[0]);
          mass1.Fill(mass1Num[0]);
          jec1.Fill(jec1Num[0]);
          muf1.Fill(muf1Num[0]);
          nhf1.Fill(nhf1Num[0]);
          chf1.Fill(chf1Num[0]);
          area1.Fill(area1Num[0]);
          nemf1.Fill(nemf1Num[0]);
          cemf1.Fill(cemf1Num[0]);


        //Fill SimJet2
        //if(TightID2[0] == 1){
          pt2.Fill(pt2Num[0]);
          y2.Fill(y2Num[0]);
          eta2.Fill(eta2Num[0]);
          phi2.Fill(phi2Num[0]);
          mass2.Fill(mass2Num[0]);
          jec2.Fill(jec2Num[0]);
          muf2.Fill(muf2Num[0]);
          nhf2.Fill(nhf2Num[0]);
          chf2.Fill(chf2Num[0]);
          area2.Fill(area2Num[0]);
          nemf2.Fill(nemf2Num[0]);
          cemf2.Fill(cemf2Num[0]);


        //Fill SimJet3
        //if(TightID3[0] == 1){
          pt3.Fill(pt3Num[0]);
          y3.Fill(y3Num[0]);
          eta3.Fill(eta3Num[0]);
          phi3.Fill(phi3Num[0]);
          mass3.Fill(mass3Num[0]);
          jec3.Fill(jec3Num[0]);
          muf3.Fill(muf3Num[0]);
          nhf3.Fill(nhf3Num[0]);
          chf3.Fill(chf3Num[0]);
          area3.Fill(area3Num[0]);
          nemf3.Fill(nemf3Num[0]);
          cemf3.Fill(cemf3Num[0]);


        //if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill Simyboost
          YBoostHist.Fill(YBoostValue);

          //fill SimMjj
          MjjHist.Fill(MjjValue);

          //fill Simchi
          ChiHist.Fill(ChiValue);



      //Calculate Mjj
      TLorentzVector genLorentz0, genLorentz1;
      genLorentz0.SetPtEtaPhiM(genpt1Num[0],geneta1Num[0],genphi1Num[0],genmass1Num[0]);
      genLorentz1.SetPtEtaPhiM(genpt2Num[0],geneta2Num[0],genphi2Num[0],genmass2Num[0]);
      TLorentzVector genMjjSum = genLorentz0 + genLorentz1;
      double genMjjValue = genMjjSum.M();

      //Calculate chi
      double genChiValue = exp(abs(geny1Num[0]-geny2Num[0]));

      //Calculate yboost
      double genYBoostValue = (geny1Num[0]+geny2Num[0])/2;

      //if (genMjjValue > 2500 && genChiValue < 16 && abs(genYBoostValue) < 1.11)

        //Fill genJet1
        genpt1.Fill(genpt1Num[0]);
        geny1.Fill(geny1Num[0]);
        geneta1.Fill(geneta1Num[0]);
        genphi1.Fill(genphi1Num[0]);
        genmass1.Fill(genmass1Num[0]);
        //Fill genJet2
        genpt2.Fill(genpt2Num[0]);
        geny2.Fill(geny2Num[0]);
        geneta2.Fill(geneta2Num[0]);
        genphi2.Fill(genphi2Num[0]);
        genmass2.Fill(genmass2Num[0]);
        //Fill genJet3
        genpt3.Fill(genpt3Num[0]);
        geny3.Fill(geny3Num[0]);
        geneta3.Fill(geneta3Num[0]);
        genphi3.Fill(genphi3Num[0]);
        genmass3.Fill(genmass3Num[0]);

        //Fill genmjj
        genMjjHist.Fill(genMjjValue);
        //fill genchi
        genChiHist.Fill(genChiValue);
        //fill genyboost
        genYBoostHist.Fill(genYBoostValue);

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
    MjjHist.SetDirectory(0);
    YBoostHist.SetDirectory(0);
    ChiHist.SetDirectory(0);
    genpt1.SetDirectory(0);
    genpt1.SetDirectory(0);
    geny1.SetDirectory(0);
    geneta1.SetDirectory(0);
    genphi1.SetDirectory(0);
    genmass1.SetDirectory(0);
    genpt2.SetDirectory(0);
    genpt2.SetDirectory(0);
    geny2.SetDirectory(0);
    geneta2.SetDirectory(0);
    genphi2.SetDirectory(0);
    genmass2.SetDirectory(0);
    genpt3.SetDirectory(0);
    genpt3.SetDirectory(0);
    geny3.SetDirectory(0);
    geneta3.SetDirectory(0);
    genphi3.SetDirectory(0);
    genmass3.SetDirectory(0);
    genMjjHist.SetDirectory(0);
    genYBoostHist.SetDirectory(0);
    genChiHist.SetDirectory(0);


    TFile* outHistFile1 = TFile::Open(outName1.c_str(),"RECREATE");
    //Write Jet1 Sim to Root
    outHistFile1->mkdir("Jet1");
    outHistFile1->cd("Jet1");
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
    //Write Jet2 Sim to Root
    outHistFile1->mkdir("Jet2");
    outHistFile1->cd("Jet2");
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
    //Write Jet3 Sim to Root
    outHistFile1->mkdir("Jet3");
    outHistFile1->cd("Jet3");
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
    //Write quantities to Root
    outHistFile1->mkdir("Kinematics");
    outHistFile1->cd("Kinematics");
    MjjHist.Write();
    YBoostHist.Write();
    ChiHist.Write();
    outHistFile1->Close();

    TFile* outHistFile2 = TFile::Open(outName2.c_str(),"RECREATE");
    //Write genJet1 to Root
    outHistFile2->mkdir("Jet1");
    outHistFile2->cd("Jet1");
    genpt1.Write();
    geny1.Write();
    geneta1.Write();
    genphi1.Write();
    genmass1.Write();
    //Write genJet2 to Root
    outHistFile2->mkdir("Jet2");
    outHistFile2->cd("Jet2");
    genpt2.Write();
    geny2.Write();
    geneta2.Write();
    genphi2.Write();
    genmass2.Write();
    //Write genJet3 to Root
    outHistFile2->mkdir("Jet3");
    outHistFile2->cd("Jet3");
    genpt3.Write();
    geny3.Write();
    geneta3.Write();
    genphi3.Write();
    genmass3.Write();
    //Write genjet quantities to Root
    outHistFile2->mkdir("Kinematics");
    outHistFile2->cd("Kinematics");
    genMjjHist.Write();
    genYBoostHist.Write();
    genChiHist.Write();
    outHistFile2->Close();
  }
  return 0;
}
