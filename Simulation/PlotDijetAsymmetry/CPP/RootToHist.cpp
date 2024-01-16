int RootToHist()
{

  string ranges[13] = {"50to80","80to120","120to170","170to300","300to470","470to600","600to800","800to1000","1000to1400","1400to1800","1800to2400","2400to3200","3200"};

  for (int i = 0; i < 13; i++)
  {
    string rootFile = "/nfs/dust/cms/user/hinzmann/run2023/QCD_PT-"+ranges[i]+"_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X_mcRun3_2023_realistic_v14-v2_NANOAODSIM.root";
    string outName = "/nfs/dust/cms/user/mueckejo/RootS/"+ranges[i]+"_PlotDijetAsymmetry_Run32023_MC.root";

    TFile* inFile = TFile::Open(rootFile.c_str(),"READ");
    TTree* tree = (TTree*)inFile->Get("Events");

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float y1Num[eventNum];
    float eta1Num[eventNum];
    float phi1Num[eventNum];

    tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree->SetBranchAddress("jetAK4_y1",&y1Num);
    tree->SetBranchAddress("jetAK4_eta1",&eta1Num);
    tree->SetBranchAddress("jetAK4_phi1",&phi1Num);

    //variables of Jet2
    float pt2Num[eventNum];
    float y2Num[eventNum];
    float eta2Num[eventNum];
    float phi2Num[eventNum];

    tree->SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree->SetBranchAddress("jetAK4_y2",&y2Num);
    tree->SetBranchAddress("jetAK4_eta2",&eta2Num);
    tree->SetBranchAddress("jetAK4_phi2",&phi2Num);

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

    std::cout << tree->GetEntries() << std::endl;
    //Fill the Hists with Root Tree Sim and Genjets
    for (Long64_t entry = 0; entry < tree->GetEntries(); ++entry)
    {
      tree->GetEntry(entry);

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

  TFile* outHistFile = TFile::Open(outName.c_str(),"RECREATE");
  PtAsymmetry.Write();
  PhiDifference.Write();
  EtaDifference.Write();
  YDifference.Write();
  ThetaDifference.Write();
  outHistFile->Close();
  return 0;
}
