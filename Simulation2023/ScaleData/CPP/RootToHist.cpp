int RootToHist()
{

  string ranges[13] = {"50to80","80to120","120to170","170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","3200"};

  for (int i = 0; i < 13; i++)
  {
    string rootFile = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-"+ranges[i]+"_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM-15Jan2023.root";
    string outName = "/nfs/dust/cms/user/mueckejo/RootS2023/"+ranges[i]+"_PlotSimulation_Run32023-15Jan2023_MC.root";

    TFile* inFile = TFile::Open(rootFile.c_str(),"READ");
    TTree* tree = (TTree*)inFile->Get("Events");

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float pt1rawNum[eventNum];
    float pt1nomNum[eventNum];
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
    float btagDeepFlavB1Num[eventNum];
    int nConstituents1Num[eventNum];
    int TightID1[eventNum];

    tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree->SetBranchAddress("jetAK4_pt1_raw",&pt1rawNum);
    tree->SetBranchAddress("jetAK4_pt1_nom",&pt1nomNum);
    tree->SetBranchAddress("jetAK4_y1",&y1Num);
    tree->SetBranchAddress("jetAK4_eta1",&eta1Num);
    tree->SetBranchAddress("jetAK4_phi1",&phi1Num);
    tree->SetBranchAddress("jetAK4_mass1",&mass1Num);
    tree->SetBranchAddress("jetAK4_jec1",&jec1Num);
    tree->SetBranchAddress("jetAK4_muf1",&muf1Num);
    tree->SetBranchAddress("jetAK4_nhf1",&nhf1Num);
    tree->SetBranchAddress("jetAK4_chf1",&chf1Num);
    tree->SetBranchAddress("jetAK4_area1",&area1Num);
    tree->SetBranchAddress("jetAK4_nemf1",&nemf1Num);
    tree->SetBranchAddress("jetAK4_cemf1",&cemf1Num);
    tree->SetBranchAddress("jetAK4_btagDeepFlavB1",&btagDeepFlavB1Num);
    tree->SetBranchAddress("jetAK4_nConstituents1",&nConstituents1Num);
    tree->SetBranchAddress("jetAK4_TightID1",&TightID1);

    TH1D pt1("Simpt1","pt for jet1 Sim",20,0,4000);
    pt1.Sumw2();
    TH1D pt1raw("Simpt1raw","ptraw for jet1 Sim",20,0,4000);
    pt1raw.Sumw2();
    TH1D pt1nom("Simpt1nom","ptnom for jet1 Sim",20,0,4000);
    pt1nom.Sumw2();

    TH1D y1("Simy1","y for jet1 Sim",20,-6,6);
    y1.Sumw2();
    TH1D y1raw("Simy1raw","y rawfor jet1 Sim",20,-6,6);
    y1raw.Sumw2();
    TH1D y1nom("Simy1nom","ynom for jet1 Sim",20,-6,6);
    y1nom.Sumw2();

    TH1D eta1("Simeta1","eta for jet1 Sim",20,-6,6);
    eta1.Sumw2();
    TH1D eta1raw("Simeta1raw","etaraw for jet1 Sim",20,-6,6);
    eta1raw.Sumw2();
    TH1D eta1nom("Simeta1nom","etanom for jet1 Sim",20,-6,6);
    eta1nom.Sumw2();

    TH1D phi1("Simphi1","phi for jet1 Sim",20,-4,4);
    phi1.Sumw2();
    TH1D phi1raw("Simphi1raw","phiraw for jet1 Sim",20,-4,4);
    phi1raw.Sumw2();
    TH1D phi1nom("Simphi1nom","phinom for jet1 Sim",20,-4,4);
    phi1nom.Sumw2();

    TH1D mass1("Simmass1","mass for jet1 Sim",20,0,500);
    mass1.Sumw2();
    TH1D mass1raw("Simmass1raw","massraw for jet1 Sim",20,0,500);
    mass1raw.Sumw2();
    TH1D mass1nom("Simmass1nom","massnom for jet1 Sim",20,0,500);
    mass1nom.Sumw2();

    TH1D jec1("Simjec1","jec for jet1 Sim",20,0.5,1.3);
    jec1.Sumw2();
    TH1D jec1raw("Simjec1raw","jecraw for jet1 Sim",20,0.5,1.3);
    jec1raw.Sumw2();
    TH1D jec1nom("Simjec1nom","jecnom for jet1 Sim",20,0.5,1.3);
    jec1nom.Sumw2();

    TH1D muf1("Simmuf1","muf for jet1 Sim",20,0,1);
    muf1.Sumw2();
    TH1D muf1raw("Simmuf1raw","mufraw for jet1 Sim",20,0,1);
    muf1raw.Sumw2();
    TH1D muf1nom("Simmuf1nom","mufnom for jet1 Sim",20,0,1);
    muf1nom.Sumw2();

    TH1D nhf1("Simnhf1","nhf for jet1 Sim",20,0,1);
    nhf1.Sumw2();
    TH1D nhf1raw("Simnhf1raw","nhfraw for jet1 Sim",20,0,1);
    nhf1raw.Sumw2();
    TH1D nhf1nom("Simnhf1nom","nhfnom for jet1 Sim",20,0,1);
    nhf1nom.Sumw2();

    TH1D chf1("Simchf1","chf for jet1 Sim",20,0,1);
    chf1.Sumw2();
    TH1D chf1raw("Simchf1raw","chfraw for jet1 Sim",20,0,1);
    chf1raw.Sumw2();
    TH1D chf1nom("Simchf1nom","chfnom for jet1 Sim",20,0,1);
    chf1nom.Sumw2();

    TH1D area1("Simarea1","area for jet1 Sim",20,0.2,1);
    area1.Sumw2();
    TH1D area1raw("Simarea1raw","arearaw for jet1 Sim",20,0.2,1);
    area1raw.Sumw2();
    TH1D area1nom("Simarea1nom","areanom for jet1 Sim",20,0.2,1);
    area1nom.Sumw2();

    TH1D nemf1("Simnemf1","nemf for jet1 Sim",20,0,1);
    nemf1.Sumw2();
    TH1D nemf1raw("Simnemf1raw","nemfraw for jet1 Sim",20,0,1);
    nemf1raw.Sumw2();
    TH1D nemf1nom("Simnemf1nom","nemfnom for jet1 Sim",20,0,1);
    nemf1nom.Sumw2();

    TH1D cemf1("Simcemf1","cemf for jet1 Sim",20,0,1);
    cemf1.Sumw2();
    TH1D cemf1raw("Simcemf1raw","cemfraw for jet1 Sim",20,0,1);
    cemf1raw.Sumw2();
    TH1D cemf1nom("Simcemf1nom","cemfnom for jet1 Sim",20,0,1);
    cemf1nom.Sumw2();

    TH1D btagDeepFlavB1("SimbtagDeepFlavB1","btagDeepFlavB for jet1 Sim",20,0,1);
    btagDeepFlavB1.Sumw2();
    TH1D btagDeepFlavB1raw("SimbtagDeepFlavB1raw","btagDeepFlavBraw for jet1 Sim",20,0,1);
    btagDeepFlavB1raw.Sumw2();
    TH1D btagDeepFlavB1nom("SimbtagDeepFlavB1nom","btagDeepFlavBnom for jet1 Sim",20,0,1);
    btagDeepFlavB1nom.Sumw2();

    TH1D nConstituents1("SimnConstituents1","nConstituents for jet1 Sim",20,0,100);
    nConstituents1.Sumw2();
    TH1D nConstituents1raw("SimnConstituents1raw","nConstituentsraw for jet1 Sim",20,0,100);
    nConstituents1raw.Sumw2();
    TH1D nConstituents1nom("SimnConstituents1nom","nConstituentsnom for jet1 Sim",20,0,100);
    nConstituents1nom.Sumw2();

    //variables of Jet2
    float pt2Num[eventNum];
    float pt2rawNum[eventNum];
    float pt2nomNum[eventNum];
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
    float btagDeepFlavB2Num[eventNum];
    int nConstituents2Num[eventNum];
    int TightID2[eventNum];

    tree->SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree->SetBranchAddress("jetAK4_pt2_raw",&pt2rawNum);
    tree->SetBranchAddress("jetAK4_pt2_nom",&pt2nomNum);
    tree->SetBranchAddress("jetAK4_y2",&y2Num);
    tree->SetBranchAddress("jetAK4_eta2",&eta2Num);
    tree->SetBranchAddress("jetAK4_phi2",&phi2Num);
    tree->SetBranchAddress("jetAK4_mass2",&mass2Num);
    tree->SetBranchAddress("jetAK4_jec2",&jec2Num);
    tree->SetBranchAddress("jetAK4_muf2",&muf2Num);
    tree->SetBranchAddress("jetAK4_nhf2",&nhf2Num);
    tree->SetBranchAddress("jetAK4_chf2",&chf2Num);
    tree->SetBranchAddress("jetAK4_area2",&area2Num);
    tree->SetBranchAddress("jetAK4_nemf2",&nemf2Num);
    tree->SetBranchAddress("jetAK4_cemf2",&cemf2Num);
    tree->SetBranchAddress("jetAK4_btagDeepFlavB2",&btagDeepFlavB2Num);
    tree->SetBranchAddress("jetAK4_nConstituents2",&nConstituents2Num);
    tree->SetBranchAddress("jetAK4_TightID2",&TightID2);

    TH1D pt2("Simpt2","pt for jet2 Sim",20,0,4000);
    pt2.Sumw2();
    TH1D pt2raw("Simpt2raw","ptraw for jet2 Sim",20,0,4000);
    pt2raw.Sumw2();
    TH1D pt2nom("Simpt2nom","ptnom for jet2 Sim",20,0,4000);
    pt2nom.Sumw2();

    TH1D y2("Simy2","y for jet2 Sim",20,-6,6);
    y2.Sumw2();
    TH1D y2raw("Simy2raw","y rawfor jet2 Sim",20,-6,6);
    y2raw.Sumw2();
    TH1D y2nom("Simy2nom","ynom for jet2 Sim",20,-6,6);
    y2nom.Sumw2();

    TH1D eta2("Simeta2","eta for jet2 Sim",20,-6,6);
    eta2.Sumw2();
    TH1D eta2raw("Simeta2raw","etaraw for jet2 Sim",20,-6,6);
    eta2raw.Sumw2();
    TH1D eta2nom("Simeta2nom","etanom for jet2 Sim",20,-6,6);
    eta2nom.Sumw2();

    TH1D phi2("Simphi2","phi for jet2 Sim",20,-4,4);
    phi2.Sumw2();
    TH1D phi2raw("Simphi2raw","phiraw for jet2 Sim",20,-4,4);
    phi2raw.Sumw2();
    TH1D phi2nom("Simphi2nom","phinom for jet2 Sim",20,-4,4);
    phi2nom.Sumw2();

    TH1D mass2("Simmass2","mass for jet2 Sim",20,0,500);
    mass2.Sumw2();
    TH1D mass2raw("Simmass2raw","massraw for jet2 Sim",20,0,500);
    mass2raw.Sumw2();
    TH1D mass2nom("Simmass2nom","massnom for jet2 Sim",20,0,500);
    mass2nom.Sumw2();

    TH1D jec2("Simjec2","jec for jet2 Sim",20,0.5,1.3);
    jec2.Sumw2();
    TH1D jec2raw("Simjec2raw","jecraw for jet2 Sim",20,0.5,1.3);
    jec2raw.Sumw2();
    TH1D jec2nom("Simjec2nom","jecnom for jet2 Sim",20,0.5,1.3);
    jec2nom.Sumw2();

    TH1D muf2("Simmuf2","muf for jet2 Sim",20,0,1);
    muf2.Sumw2();
    TH1D muf2raw("Simmuf2raw","mufraw for jet2 Sim",20,0,1);
    muf2raw.Sumw2();
    TH1D muf2nom("Simmuf2nom","mufnom for jet2 Sim",20,0,1);
    muf2nom.Sumw2();

    TH1D nhf2("Simnhf2","nhf for jet2 Sim",20,0,1);
    nhf2.Sumw2();
    TH1D nhf2raw("Simnhf2raw","nhfraw for jet2 Sim",20,0,1);
    nhf2raw.Sumw2();
    TH1D nhf2nom("Simnhf2nom","nhfnom for jet2 Sim",20,0,1);
    nhf2nom.Sumw2();

    TH1D chf2("Simchf2","chf for jet2 Sim",20,0,1);
    chf2.Sumw2();
    TH1D chf2raw("Simchf2raw","chfraw for jet2 Sim",20,0,1);
    chf2raw.Sumw2();
    TH1D chf2nom("Simchf2nom","chfnom for jet2 Sim",20,0,1);
    chf2nom.Sumw2();

    TH1D area2("Simarea2","area for jet2 Sim",20,0.2,1);
    area2.Sumw2();
    TH1D area2raw("Simarea2raw","arearaw for jet2 Sim",20,0.2,1);
    area2raw.Sumw2();
    TH1D area2nom("Simarea2nom","areanom for jet2 Sim",20,0.2,1);
    area2nom.Sumw2();

    TH1D nemf2("Simnemf2","nemf for jet2 Sim",20,0,1);
    nemf2.Sumw2();
    TH1D nemf2raw("Simnemf2raw","nemfraw for jet2 Sim",20,0,1);
    nemf2raw.Sumw2();
    TH1D nemf2nom("Simnemf2nom","nemfnom for jet2 Sim",20,0,1);
    nemf2nom.Sumw2();

    TH1D cemf2("Simcemf2","cemf for jet2 Sim",20,0,1);
    cemf2.Sumw2();
    TH1D cemf2raw("Simcemf2raw","cemfraw for jet2 Sim",20,0,1);
    cemf2raw.Sumw2();
    TH1D cemf2nom("Simcemf2nom","cemfnom for jet2 Sim",20,0,1);
    cemf2nom.Sumw2();

    TH1D btagDeepFlavB2("SimbtagDeepFlavB2","btagDeepFlavB for jet2 Sim",20,0,1);
    btagDeepFlavB2.Sumw2();
    TH1D btagDeepFlavB2raw("SimbtagDeepFlavB2raw","btagDeepFlavBraw for jet2 Sim",20,0,1);
    btagDeepFlavB2raw.Sumw2();
    TH1D btagDeepFlavB2nom("SimbtagDeepFlavB2nom","btagDeepFlavBnom for jet2 Sim",20,0,1);
    btagDeepFlavB2nom.Sumw2();

    TH1D nConstituents2("SimnConstituents2","nConstituents for jet2 Sim",20,0,100);
    nConstituents2.Sumw2();
    TH1D nConstituents2raw("SimnConstituents2raw","nConstituentsraw for jet2 Sim",20,0,100);
    nConstituents2raw.Sumw2();
    TH1D nConstituents2nom("SimnConstituents2nom","nConstituentsnom for jet2 Sim",20,0,100);
    nConstituents2nom.Sumw2();

    //variables of Jet3
    float pt3Num[eventNum];
    float pt3rawNum[eventNum];
    float pt3nomNum[eventNum];
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
    float btagDeepFlavB3Num[eventNum];
    int nConstituents3Num[eventNum];
    int TightID3[eventNum];

    tree->SetBranchAddress("jetAK4_pt3",&pt3Num);
    tree->SetBranchAddress("jetAK4_pt3_raw",&pt3rawNum);
    tree->SetBranchAddress("jetAK4_pt3_nom",&pt3nomNum);
    tree->SetBranchAddress("jetAK4_y3",&y3Num);
    tree->SetBranchAddress("jetAK4_eta3",&eta3Num);
    tree->SetBranchAddress("jetAK4_phi3",&phi3Num);
    tree->SetBranchAddress("jetAK4_mass3",&mass3Num);
    tree->SetBranchAddress("jetAK4_jec3",&jec3Num);
    tree->SetBranchAddress("jetAK4_muf3",&muf3Num);
    tree->SetBranchAddress("jetAK4_nhf3",&nhf3Num);
    tree->SetBranchAddress("jetAK4_chf3",&chf3Num);
    tree->SetBranchAddress("jetAK4_area3",&area3Num);
    tree->SetBranchAddress("jetAK4_nemf3",&nemf3Num);
    tree->SetBranchAddress("jetAK4_cemf3",&cemf3Num);
    tree->SetBranchAddress("jetAK4_btagDeepFlavB3",&btagDeepFlavB3Num);
    tree->SetBranchAddress("jetAK4_nConstituents3",&nConstituents3Num);
    tree->SetBranchAddress("jetAK4_TightID3",&TightID3);

    TH1D pt3("Simpt3","pt for jet3 Sim",20,0,4000);
    pt3.Sumw2();
    TH1D pt3raw("Simpt3raw","ptraw for jet3 Sim",20,0,4000);
    pt3raw.Sumw2();
    TH1D pt3nom("Simpt3nom","ptnom for jet3 Sim",20,0,4000);
    pt3nom.Sumw2();

    TH1D y3("Simy3","y for jet3 Sim",20,-6,6);
    y3.Sumw2();
    TH1D y3raw("Simy3raw","y rawfor jet3 Sim",20,-6,6);
    y3raw.Sumw2();
    TH1D y3nom("Simy3nom","ynom for jet3 Sim",20,-6,6);
    y3nom.Sumw2();

    TH1D eta3("Simeta3","eta for jet3 Sim",20,-6,6);
    eta3.Sumw2();
    TH1D eta3raw("Simeta3raw","etaraw for jet3 Sim",20,-6,6);
    eta3raw.Sumw2();
    TH1D eta3nom("Simeta3nom","etanom for jet3 Sim",20,-6,6);
    eta3nom.Sumw2();

    TH1D phi3("Simphi3","phi for jet3 Sim",20,-4,4);
    phi3.Sumw2();
    TH1D phi3raw("Simphi3raw","phiraw for jet3 Sim",20,-4,4);
    phi3raw.Sumw2();
    TH1D phi3nom("Simphi3nom","phinom for jet3 Sim",20,-4,4);
    phi3nom.Sumw2();

    TH1D mass3("Simmass3","mass for jet3 Sim",20,0,500);
    mass3.Sumw2();
    TH1D mass3raw("Simmass3raw","massraw for jet3 Sim",20,0,500);
    mass3raw.Sumw2();
    TH1D mass3nom("Simmass3nom","massnom for jet3 Sim",20,0,500);
    mass3nom.Sumw2();

    TH1D jec3("Simjec3","jec for jet3 Sim",20,0.5,1.3);
    jec3.Sumw2();
    TH1D jec3raw("Simjec3raw","jecraw for jet3 Sim",20,0.5,1.3);
    jec3raw.Sumw2();
    TH1D jec3nom("Simjec3nom","jecnom for jet3 Sim",20,0.5,1.3);
    jec3nom.Sumw2();

    TH1D muf3("Simmuf3","muf for jet3 Sim",20,0,1);
    muf3.Sumw2();
    TH1D muf3raw("Simmuf3raw","mufraw for jet3 Sim",20,0,1);
    muf3raw.Sumw2();
    TH1D muf3nom("Simmuf3nom","mufnom for jet3 Sim",20,0,1);
    muf3nom.Sumw2();

    TH1D nhf3("Simnhf3","nhf for jet3 Sim",20,0,1);
    nhf3.Sumw2();
    TH1D nhf3raw("Simnhf3raw","nhfraw for jet3 Sim",20,0,1);
    nhf3raw.Sumw2();
    TH1D nhf3nom("Simnhf3nom","nhfnom for jet3 Sim",20,0,1);
    nhf3nom.Sumw2();

    TH1D chf3("Simchf3","chf for jet3 Sim",20,0,1);
    chf3.Sumw2();
    TH1D chf3raw("Simchf3raw","chfraw for jet3 Sim",20,0,1);
    chf3raw.Sumw2();
    TH1D chf3nom("Simchf3nom","chfnom for jet3 Sim",20,0,1);
    chf3nom.Sumw2();

    TH1D area3("Simarea3","area for jet3 Sim",20,0.2,1);
    area3.Sumw2();
    TH1D area3raw("Simarea3raw","arearaw for jet3 Sim",20,0.2,1);
    area3raw.Sumw2();
    TH1D area3nom("Simarea3nom","areanom for jet3 Sim",20,0.2,1);
    area3nom.Sumw2();

    TH1D nemf3("Simnemf3","nemf for jet3 Sim",20,0,1);
    nemf3.Sumw2();
    TH1D nemf3raw("Simnemf3raw","nemfraw for jet3 Sim",20,0,1);
    nemf3raw.Sumw2();
    TH1D nemf3nom("Simnemf3nom","nemfnom for jet3 Sim",20,0,1);
    nemf3nom.Sumw2();

    TH1D cemf3("Simcemf3","cemf for jet3 Sim",20,0,1);
    cemf3.Sumw2();
    TH1D cemf3raw("Simcemf3raw","cemfraw for jet3 Sim",20,0,1);
    cemf3raw.Sumw2();
    TH1D cemf3nom("Simcemf3nom","cemfnom for jet3 Sim",20,0,1);
    cemf3nom.Sumw2();

    TH1D btagDeepFlavB3("SimbtagDeepFlavB3","btagDeepFlavB for jet3 Sim",20,0,1);
    btagDeepFlavB3.Sumw2();
    TH1D btagDeepFlavB3raw("SimbtagDeepFlavB3raw","btagDeepFlavBraw for jet3 Sim",20,0,1);
    btagDeepFlavB3raw.Sumw2();
    TH1D btagDeepFlavB3nom("SimbtagDeepFlavB3nom","btagDeepFlavBnom for jet3 Sim",20,0,1);
    btagDeepFlavB3nom.Sumw2();

    TH1D nConstituents3("SimnConstituents3","nConstituents for jet3 Sim",20,0,100);
    nConstituents3.Sumw2();
    TH1D nConstituents3raw("SimnConstituents3raw","nConstituentsraw for jet3 Sim",20,0,100);
    nConstituents3raw.Sumw2();
    TH1D nConstituents3nom("SimnConstituents3nom","nConstituentsnom for jet3 Sim",20,0,100);
    nConstituents3nom.Sumw2();

    float mjjNum[eventNum];
    float mjjnomNum[eventNum];
    float mjjrawNum[eventNum];

    tree->SetBranchAddress("mjj",&mjjNum);
    tree->SetBranchAddress("mjj_nom",&mjjnomNum);
    tree->SetBranchAddress("mjj_raw",&mjjrawNum);

    //Create quantities calculated from variables
    TH1D MjjHist("Simmjj","Mjj [Gev]",20,0,10000);
    MjjHist.Sumw2();
    TH1D MjjHistNom("Simmjjnom","Mjj [Gev]",20,0,10000);
    MjjHistNom.Sumw2();
    TH1D MjjHistRaw("Simmjjraw","Mjj [Gev]",20,0,10000);
    MjjHistRaw.Sumw2();

    TH1D YBoostHist("Simyboost","yboost",20,0,3);
    YBoostHist.Sumw2();
    TH1D YBoostHistNom("Simyboostnom","yboost",20,0,3);
    YBoostHistNom.Sumw2();
    TH1D YBoostHistRaw("Simyboostraw","yboost",20,0,3);
    YBoostHistRaw.Sumw2();

    TH1D ChiHist("Simchi","chi",20,0,20);
    ChiHist.Sumw2();
    TH1D ChiHistNom("Simchinom","chi",20,0,20);
    ChiHistNom.Sumw2();
    TH1D ChiHistRaw("Simchiraw","chi",20,0,20);
    ChiHistRaw.Sumw2();

    std::cout << tree->GetEntries() << std::endl;
    //Fill the Hists with Root Tree Sim and Genjets
    for (Long64_t entry = 0; entry < tree->GetEntries(); ++entry)
    {
      tree->GetEntry(entry);

      //Calculate Sim chi
      double ChiValue = exp(abs(y1Num[0]-y2Num[0]));

      //Calculate Sim yboost
      double YBoostValue = (y1Num[0]+y2Num[0])/2;

      if (mjjNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
      {
        //Fill SimJet1
        if(TightID1[0] == 1){
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
          btagDeepFlavB1.Fill(btagDeepFlavB1Num[0]);
          nConstituents1.Fill(nConstituents1Num[0]);
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
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
          btagDeepFlavB2.Fill(btagDeepFlavB2Num[0]);
          nConstituents2.Fill(nConstituents2Num[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
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
          btagDeepFlavB3.Fill(btagDeepFlavB3Num[0]);
          nConstituents3.Fill(nConstituents3Num[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill Simyboost
          YBoostHist.Fill(YBoostValue);

          //fill SimMjj
          MjjHist.Fill(mjjNum[0]);

          //fill Simchi
          ChiHist.Fill(ChiValue);
        }
      }

      if (mjjnomNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
      {
        //Fill SimJet1
        if(TightID1[0] == 1){
          pt1nom.Fill(pt1nomNum[0]);
          y1nom.Fill(y1Num[0]);
          eta1nom.Fill(eta1Num[0]);
          phi1nom.Fill(phi1Num[0]);
          mass1nom.Fill(mass1Num[0]);
          jec1nom.Fill(jec1Num[0]);
          muf1nom.Fill(muf1Num[0]);
          nhf1nom.Fill(nhf1Num[0]);
          chf1nom.Fill(chf1Num[0]);
          area1nom.Fill(area1Num[0]);
          nemf1nom.Fill(nemf1Num[0]);
          cemf1nom.Fill(cemf1Num[0]);
          btagDeepFlavB1nom.Fill(btagDeepFlavB1Num[0]);
          nConstituents1nom.Fill(nConstituents1Num[0]);
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
          pt2nom.Fill(pt2nomNum[0]);
          y2nom.Fill(y2Num[0]);
          eta2nom.Fill(eta2Num[0]);
          phi2nom.Fill(phi2Num[0]);
          mass2nom.Fill(mass2Num[0]);
          jec2nom.Fill(jec2Num[0]);
          muf2nom.Fill(muf2Num[0]);
          nhf2nom.Fill(nhf2Num[0]);
          chf2nom.Fill(chf2Num[0]);
          area2nom.Fill(area2Num[0]);
          nemf2nom.Fill(nemf2Num[0]);
          cemf2nom.Fill(cemf2Num[0]);
          btagDeepFlavB2nom.Fill(btagDeepFlavB2Num[0]);
          nConstituents2nom.Fill(nConstituents2Num[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
          pt3nom.Fill(pt3nomNum[0]);
          y3nom.Fill(y3Num[0]);
          eta3nom.Fill(eta3Num[0]);
          phi3nom.Fill(phi3Num[0]);
          mass3nom.Fill(mass3Num[0]);
          jec3nom.Fill(jec3Num[0]);
          muf3nom.Fill(muf3Num[0]);
          nhf3nom.Fill(nhf3Num[0]);
          chf3nom.Fill(chf3Num[0]);
          area3nom.Fill(area3Num[0]);
          nemf3nom.Fill(nemf3Num[0]);
          cemf3nom.Fill(cemf3Num[0]);
          btagDeepFlavB3nom.Fill(btagDeepFlavB3Num[0]);
          nConstituents3nom.Fill(nConstituents3Num[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill Simyboost
          YBoostHistNom.Fill(YBoostValue);

          //fill SimMjj
          MjjHistNom.Fill(mjjnomNum[0]);

          //fill Simchi
          ChiHistNom.Fill(ChiValue);
        }
      }

      if (mjjrawNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
      {
        //Fill SimJet1
        if(TightID1[0] == 1){
          pt1raw.Fill(pt1rawNum[0]);
          y1raw.Fill(y1Num[0]);
          eta1raw.Fill(eta1Num[0]);
          phi1raw.Fill(phi1Num[0]);
          mass1raw.Fill(mass1Num[0]);
          jec1raw.Fill(jec1Num[0]);
          muf1raw.Fill(muf1Num[0]);
          nhf1raw.Fill(nhf1Num[0]);
          chf1raw.Fill(chf1Num[0]);
          area1raw.Fill(area1Num[0]);
          nemf1raw.Fill(nemf1Num[0]);
          cemf1raw.Fill(cemf1Num[0]);
          btagDeepFlavB1raw.Fill(btagDeepFlavB1Num[0]);
          nConstituents1raw.Fill(nConstituents1Num[0]);
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
          pt2raw.Fill(pt2rawNum[0]);
          y2raw.Fill(y2Num[0]);
          eta2raw.Fill(eta2Num[0]);
          phi2raw.Fill(phi2Num[0]);
          mass2raw.Fill(mass2Num[0]);
          jec2raw.Fill(jec2Num[0]);
          muf2raw.Fill(muf2Num[0]);
          nhf2raw.Fill(nhf2Num[0]);
          chf2raw.Fill(chf2Num[0]);
          area2raw.Fill(area2Num[0]);
          nemf2raw.Fill(nemf2Num[0]);
          cemf2raw.Fill(cemf2Num[0]);
          btagDeepFlavB2raw.Fill(btagDeepFlavB2Num[0]);
          nConstituents2raw.Fill(nConstituents2Num[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
          pt3raw.Fill(pt3rawNum[0]);
          y3raw.Fill(y3Num[0]);
          eta3raw.Fill(eta3Num[0]);
          phi3raw.Fill(phi3Num[0]);
          mass3raw.Fill(mass3Num[0]);
          jec3raw.Fill(jec3Num[0]);
          muf3raw.Fill(muf3Num[0]);
          nhf3raw.Fill(nhf3Num[0]);
          chf3raw.Fill(chf3Num[0]);
          area3raw.Fill(area3Num[0]);
          nemf3raw.Fill(nemf3Num[0]);
          cemf3raw.Fill(cemf3Num[0]);
          btagDeepFlavB3raw.Fill(btagDeepFlavB3Num[0]);
          nConstituents3raw.Fill(nConstituents3Num[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill Simyboost
          YBoostHistRaw.Fill(YBoostValue);

          //fill SimMjj
          MjjHistRaw.Fill(mjjrawNum[0]);

          //fill Simchi
          ChiHistRaw.Fill(ChiValue);
        }
      }
    }

    //Neccesary so files dont get lost
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
    pt1raw.SetDirectory(0);
    y1raw.SetDirectory(0);
    eta1raw.SetDirectory(0);
    phi1raw.SetDirectory(0);
    mass1raw.SetDirectory(0);
    jec1raw.SetDirectory(0);
    muf1raw.SetDirectory(0);
    nhf1raw.SetDirectory(0);
    chf1raw.SetDirectory(0);
    area1raw.SetDirectory(0);
    nemf1raw.SetDirectory(0);
    cemf1raw.SetDirectory(0);
    btagDeepFlavB1raw.SetDirectory(0);
    nConstituents1raw.SetDirectory(0);
    pt2raw.SetDirectory(0);
    pt2raw.SetDirectory(0);
    y2raw.SetDirectory(0);
    eta2raw.SetDirectory(0);
    phi2raw.SetDirectory(0);
    mass2raw.SetDirectory(0);
    jec2raw.SetDirectory(0);
    muf2raw.SetDirectory(0);
    nhf2raw.SetDirectory(0);
    chf2raw.SetDirectory(0);
    area2raw.SetDirectory(0);
    nemf2raw.SetDirectory(0);
    cemf2raw.SetDirectory(0);
    btagDeepFlavB2raw.SetDirectory(0);
    nConstituents2raw.SetDirectory(0);
    pt3raw.SetDirectory(0);
    pt3raw.SetDirectory(0);
    y3raw.SetDirectory(0);
    eta3raw.SetDirectory(0);
    phi3raw.SetDirectory(0);
    mass3raw.SetDirectory(0);
    jec3raw.SetDirectory(0);
    muf3raw.SetDirectory(0);
    nhf3raw.SetDirectory(0);
    chf3raw.SetDirectory(0);
    area3raw.SetDirectory(0);
    nemf3raw.SetDirectory(0);
    cemf3raw.SetDirectory(0);
    btagDeepFlavB3raw.SetDirectory(0);
    nConstituents3raw.SetDirectory(0);
    MjjHistRaw.SetDirectory(0);
    YBoostHistRaw.SetDirectory(0);
    ChiHistRaw.SetDirectory(0);
    pt1nom.SetDirectory(0);
    y1nom.SetDirectory(0);
    eta1nom.SetDirectory(0);
    phi1nom.SetDirectory(0);
    mass1nom.SetDirectory(0);
    jec1nom.SetDirectory(0);
    muf1nom.SetDirectory(0);
    nhf1nom.SetDirectory(0);
    chf1nom.SetDirectory(0);
    area1nom.SetDirectory(0);
    nemf1nom.SetDirectory(0);
    cemf1nom.SetDirectory(0);
    btagDeepFlavB1nom.SetDirectory(0);
    nConstituents1nom.SetDirectory(0);
    pt2nom.SetDirectory(0);
    pt2nom.SetDirectory(0);
    y2nom.SetDirectory(0);
    eta2nom.SetDirectory(0);
    phi2nom.SetDirectory(0);
    mass2nom.SetDirectory(0);
    jec2nom.SetDirectory(0);
    muf2nom.SetDirectory(0);
    nhf2nom.SetDirectory(0);
    chf2nom.SetDirectory(0);
    area2nom.SetDirectory(0);
    nemf2nom.SetDirectory(0);
    cemf2nom.SetDirectory(0);
    btagDeepFlavB2nom.SetDirectory(0);
    nConstituents2nom.SetDirectory(0);
    pt3nom.SetDirectory(0);
    pt3nom.SetDirectory(0);
    y3nom.SetDirectory(0);
    eta3nom.SetDirectory(0);
    phi3nom.SetDirectory(0);
    mass3nom.SetDirectory(0);
    jec3nom.SetDirectory(0);
    muf3nom.SetDirectory(0);
    nhf3nom.SetDirectory(0);
    chf3nom.SetDirectory(0);
    area3nom.SetDirectory(0);
    nemf3nom.SetDirectory(0);
    cemf3nom.SetDirectory(0);
    btagDeepFlavB3nom.SetDirectory(0);
    nConstituents3nom.SetDirectory(0);
    MjjHistNom.SetDirectory(0);
    YBoostHistNom.SetDirectory(0);
    ChiHistNom.SetDirectory(0);



    TFile* outHistFile = TFile::Open(outName.c_str(),"RECREATE");
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
    pt2.Write();
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
    pt3.Write();
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
    MjjHist.Write();
    YBoostHist.Write();
    ChiHist.Write();
    pt1raw.Write();
    y1raw.Write();
    eta1raw.Write();
    phi1raw.Write();
    mass1raw.Write();
    jec1raw.Write();
    muf1raw.Write();
    nhf1raw.Write();
    chf1raw.Write();
    area1raw.Write();
    nemf1raw.Write();
    cemf1raw.Write();
    btagDeepFlavB1raw.Write();
    nConstituents1raw.Write();
    pt2raw.Write();
    pt2raw.Write();
    y2raw.Write();
    eta2raw.Write();
    phi2raw.Write();
    mass2raw.Write();
    jec2raw.Write();
    muf2raw.Write();
    nhf2raw.Write();
    chf2raw.Write();
    area2raw.Write();
    nemf2raw.Write();
    cemf2raw.Write();
    btagDeepFlavB2raw.Write();
    nConstituents2raw.Write();
    pt3raw.Write();
    pt3raw.Write();
    y3raw.Write();
    eta3raw.Write();
    phi3raw.Write();
    mass3raw.Write();
    jec3raw.Write();
    muf3raw.Write();
    nhf3raw.Write();
    chf3raw.Write();
    area3raw.Write();
    nemf3raw.Write();
    cemf3raw.Write();
    btagDeepFlavB3raw.Write();
    nConstituents3raw.Write();
    MjjHistRaw.Write();
    YBoostHistRaw.Write();
    ChiHistRaw.Write();
    pt1nom.Write();
    y1nom.Write();
    eta1nom.Write();
    phi1nom.Write();
    mass1nom.Write();
    jec1nom.Write();
    muf1nom.Write();
    nhf1nom.Write();
    chf1nom.Write();
    area1nom.Write();
    nemf1nom.Write();
    cemf1nom.Write();
    btagDeepFlavB1nom.Write();
    nConstituents1nom.Write();
    pt2nom.Write();
    pt2nom.Write();
    y2nom.Write();
    eta2nom.Write();
    phi2nom.Write();
    mass2nom.Write();
    jec2nom.Write();
    muf2nom.Write();
    nhf2nom.Write();
    chf2nom.Write();
    area2nom.Write();
    nemf2nom.Write();
    cemf2nom.Write();
    btagDeepFlavB2nom.Write();
    nConstituents2nom.Write();
    pt3nom.Write();
    pt3nom.Write();
    y3nom.Write();
    eta3nom.Write();
    phi3nom.Write();
    mass3nom.Write();
    jec3nom.Write();
    muf3nom.Write();
    nhf3nom.Write();
    chf3nom.Write();
    area3nom.Write();
    nemf3nom.Write();
    cemf3nom.Write();
    btagDeepFlavB3nom.Write();
    nConstituents3nom.Write();
    MjjHistNom.Write();
    YBoostHistNom.Write();
    ChiHistNom.Write();
    outHistFile->Close();
  }
  return 0;
}
