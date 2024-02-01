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
    float pt1numNum[eventNum];
    float y1Num[eventNum];
    int TightID1[eventNum];


    tree->SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree->SetBranchAddress("jetAK4_pt1_raw",&pt1rawNum);
    tree->SetBranchAddress("jetAK4_pt1_num",&pt1numNum);
    tree->SetBranchAddress("jetAK4_y1",&y1Num);
    tree->SetBranchAddress("jetAK4_TightID1",&TightID1);

    TH1D pt1("Simpt1","pt for jet1 Sim",20,0,4000);
    pt1.Sumw2();
    TH1D pt1raw("Simpt1raw","ptraw for jet1 Sim",20,0,4000);
    pt1raw.Sumw2();
    TH1D pt1num("Simpt1num","ptnum for jet1 Sim",20,0,4000);
    pt1num.Sumw2();

    //variables of Jet2
    float pt2Num[eventNum];
    float pt2rawNum[eventNum];
    float pt2numNum[eventNum];
    float y2Num[eventNum];
    int TightID2[eventNum];

    tree->SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree->SetBranchAddress("jetAK4_pt2_raw",&pt2rawNum);
    tree->SetBranchAddress("jetAK4_pt2_num",&pt2numNum);
    tree->SetBranchAddress("jetAK4_y2",&y2Num);
    tree->SetBranchAddress("jetAK4_TightID2",&TightID2);

    TH1D pt2("Simpt2","pt for jet2 Sim",20,0,4000);
    pt2.Sumw2();
    TH1D pt2raw("Simpt2raw","ptraw for jet1 Sim",20,0,4000);
    pt2raw.Sumw2();
    TH1D pt2num("Simpt2num","ptnum for jet1 Sim",20,0,4000);
    pt2num.Sumw2();

    //variables of Jet3
    float pt3Num[eventNum];
    float pt3rawNum[eventNum];
    float pt3numNum[eventNum];
    float y3Num[eventNum];
    int TightID3[eventNum];

    tree->SetBranchAddress("jetAK4_pt3",&pt3Num);
    tree->SetBranchAddress("jetAK4_pt3_raw",&pt3rawNum);
    tree->SetBranchAddress("jetAK4_pt3_num",&pt3numNum);
    tree->SetBranchAddress("jetAK4_y3",&y3Num);
    tree->SetBranchAddress("jetAK4_TightID3",&TightID3);

    TH1D pt3("Simpt3","pt for jet3 Sim",20,0,4000);
    pt3.Sumw2();
    TH1D pt3raw("Simpt3raw","ptraw for jet1 Sim",20,0,4000);
    pt3raw.Sumw2();
    TH1D pt3num("Simpt3num","ptnum for jet1 Sim",20,0,4000);
    pt3num.Sumw2();

    float mjjNum[eventNum];
    float mjjnumNum[eventNum];
    float mjjrawNum[eventNum];

    tree->SetBranchAddress("mjj",&mjjNum);
    tree->SetBranchAddress("mjj_num",&mjjnumNum);
    tree->SetBranchAddress("mjj_raw",&mjjrawNum);

    //Create quantities calculated from variables
    TH1D MjjHist("Simmjj","Mjj [Gev]",20,0,10000);
    MjjHist.Sumw2();
    TH1D MjjHistNum("Simmjjnum","Mjj [Gev]",20,0,10000);
    MjjHistNum.Sumw2();
    TH1D MjjHistRaw("Simmjjraw","Mjj [Gev]",20,0,10000);
    MjjHistRaw.Sumw2();

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
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
          pt2.Fill(pt2Num[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
          pt3.Fill(pt3Num[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill SimMjj
          MjjHist.Fill(mjjNum[0]);
        }
      }
      if (mjjnumNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
      {
        //Fill SimJet1
        if(TightID1[0] == 1){
          pt1num.Fill(pt1numNum[0]);
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
          pt2num.Fill(pt2numNum[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
          pt3num.Fill(pt3numNum[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill SimMjj
          MjjHistNum.Fill(mjjnumNum[0]);
        }
      }
      if (mjjrawNum[0] > 2500 && ChiValue < 16 && abs(YBoostValue) < 1.11)
      {
        //Fill SimJet1
        if(TightID1[0] == 1){
          pt1raw.Fill(pt1rawNum[0]);
        }

        //Fill SimJet2
        if(TightID2[0] == 1){
          pt2raw.Fill(pt2rawNum[0]);
        }

        //Fill SimJet3
        if(TightID3[0] == 1){
          pt3raw.Fill(pt3rawNum[0]);
        }

        if(TightID1[0] == 1 && TightID2[0] == 1){
          //fill SimMjj
          MjjHistRaw.Fill(mjjrawNum[0]);
        }
      }
    }

    //Neccesary so files dont get lost
    MjjHist.SetDirectory(0);
    MjjHistNum.SetDirectory(0);
    MjjHistRaw.SetDirectory(0);
    pt3.SetDirectory(0);
    pt3raw.SetDirectory(0);
    pt3num.SetDirectory(0);
    pt2.SetDirectory(0);
    pt2raw.SetDirectory(0);
    pt2num.SetDirectory(0);
    pt1.SetDirectory(0);
    pt1raw.SetDirectory(0);
    pt1num.SetDirectory(0);


    TFile* outHistFile = TFile::Open(outName.c_str(),"RECREATE");
    MjjHist.Write();
    MjjHistNum.Write();
    MjjHistRaw.Write();
    pt3.Write();
    pt3raw.Write();
    pt3num.Write();
    pt2.Write();
    pt2raw.Write();
    pt2num.Write();
    pt1.Write();
    pt1raw.Write();
    pt1num.Write();
    outHistFile->Close();
  }
  return 0;
}
