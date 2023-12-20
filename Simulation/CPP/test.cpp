int test()
{
  //define folders of Root Tree File and where to write Hist Files
  char rootFileGen[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_PlotSimulation_WithScale_Jetresolution_Run32023_Gen.root";
  char rootFileMc[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_PlotSimulation_WithScale_Jetresolution_Run32023_MC.root";
  char outName[] = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/Sim/RootS/_PlotJetResolution_Run32023.root";

  TFile* inFile_Gen = TFile::Open(rootFileGen,"READ");
  TFile* inFile_MC = TFile::Open(rootFileMc,"READ");

  TH1D *pt1genhist = (TH1D*)inFile_Gen->Get("pt1gen_hist");
  TH1D* eta1genhist = (TH1D*)inFile_Gen->Get("eta1gen_hist");
  TH1D* phi1genhist = (TH1D*)inFile_Gen->Get("phi1gen_hist");

  TH1D* pt1simhist = (TH1D*)inFile_MC->Get("pt1sim_hist");
  TH1D* eta1simhist = (TH1D*)inFile_MC->Get("eta1sim_hist");
  TH1D* phi1simhist = (TH1D*)inFile_MC->Get("phi1sim_hist");


  std::cout << pt1genhist->GetEntries() << std::endl;









  return 0;
}
