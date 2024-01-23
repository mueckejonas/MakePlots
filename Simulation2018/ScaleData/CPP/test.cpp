int test()
{

    string outName1 = "/nfs/dust/cms/user/mueckejo/RootS2018/100to200_PlotSimulation_Run22018_MC.root";

    TChain tree("tree");   // name of the tree is the argument
    tree.Add("/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT100to200_RunII_106X_v2_1_tree.root");
    tree.Add("/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT100to200_RunII_106X_v2_2_tree.root");
    tree.Add("/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT100to200_RunII_106X_v2_3_tree.root");

    //variables of Jet1
    float pt1Num;

    tree.SetBranchAddress("jetAK4_pt1",&pt1Num);

    TH1D pt1("Simpt1","pt for jet1 Sim",20,0,4000);
    pt1.Sumw2();

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

      pt1.Fill(pt1Num);
    }

    //Neccesary so files dont get lost
    pt1.SetDirectory(0);


    TFile* outHistFile1 = TFile::Open(outName1.c_str(),"RECREATE");
    //Write Jet1 Sim to Root
    outHistFile1->mkdir("Jet1");
    outHistFile1->cd("Jet1");
    pt1.Write();
    outHistFile1->Close();
  return 0;
}
