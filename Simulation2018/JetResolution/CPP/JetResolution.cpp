int JetResolution()
{
    //define folders of Root Tree File and where to write Hist Files
    char rootFile1[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_1_tree.root";
    char rootFile2[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_2_tree.root";
    char rootFile3[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_3_tree.root";
    char rootFile4[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_4_tree.root";
    char rootFile5[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_5_tree.root";
    char rootFile6[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_6_tree.root";
    char rootFile7[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_7_tree.root";
    char rootFile8[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_8_tree.root";
    char rootFile9[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_9_tree.root";
    char rootFile10[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_10_tree.root";
    char rootFile11[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_11_tree.root";
    char rootFile12[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_12_tree.root";
    char rootFile13[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_13_tree.root";
    char rootFile14[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_14_tree.root";
    char rootFile15[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_15_tree.root";
    char rootFile16[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_16_tree.root";
    char rootFile17[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_17_tree.root";
    char rootFile18[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_18_tree.root";
    char rootFile19[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_19_tree.root";
    char rootFile20[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_20_tree.root";
    char rootFile21[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_21_tree.root";
    char rootFile22[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_22_tree.root";
    char rootFile23[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_23_tree.root";
    char rootFile24[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT200to300_RunII_106X_v2_0_tree.root";

    char rootFile25[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_1_tree.root";
    char rootFile26[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_2_tree.root";
    char rootFile27[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_3_tree.root";
    char rootFile28[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_4_tree.root";
    char rootFile29[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_5_tree.root";
    char rootFile30[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_6_tree.root";
    char rootFile31[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_7_tree.root";
    char rootFile32[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_8_tree.root";
    char rootFile33[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_9_tree.root";
    char rootFile34[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_10_tree.root";
    char rootFile35[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_11_tree.root";
    char rootFile36[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_12_tree.root";
    char rootFile37[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_13_tree.root";
    char rootFile38[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_14_tree.root";
    char rootFile39[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_15_tree.root";
    char rootFile40[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_16_tree.root";
    char rootFile41[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_17_tree.root";
    char rootFile42[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_18_tree.root";
    char rootFile43[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_19_tree.root";
    char rootFile44[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_20_tree.root";
    char rootFile45[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_21_tree.root";
    char rootFile46[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_22_tree.root";
    char rootFile47[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_23_tree.root";
    char rootFile48[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_24_tree.root";
    char rootFile49[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_25_tree.root";
    char rootFile50[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT300to500_RunII_106X_v2_0_tree.root";

    char rootFile51[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_1_tree.root";
    char rootFile52[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_2_tree.root";
    char rootFile53[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_3_tree.root";
    char rootFile54[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_4_tree.root";
    char rootFile55[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_5_tree.root";
    char rootFile56[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_6_tree.root";
    char rootFile57[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_7_tree.root";
    char rootFile58[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_8_tree.root";
    char rootFile59[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_9_tree.root";
    char rootFile60[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_10_tree.root";
    char rootFile61[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_11_tree.root";
    char rootFile62[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_12_tree.root";
    char rootFile63[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_13_tree.root";
    char rootFile64[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_14_tree.root";
    char rootFile65[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_15_tree.root";
    char rootFile66[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_16_tree.root";
    char rootFile67[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_17_tree.root";
    char rootFile68[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_18_tree.root";
    char rootFile69[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_19_tree.root";
    char rootFile70[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_20_tree.root";
    char rootFile71[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT500to700_RunII_106X_v2_0_tree.root";

    char rootFile72[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_1_tree.root";
    char rootFile73[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_2_tree.root";
    char rootFile74[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_3_tree.root";
    char rootFile75[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_4_tree.root";
    char rootFile76[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_5_tree.root";
    char rootFile77[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_6_tree.root";
    char rootFile78[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_7_tree.root";
    char rootFile79[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_8_tree.root";
    char rootFile80[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_9_tree.root";
    char rootFile81[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_10_tree.root";
    char rootFile82[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_11_tree.root";
    char rootFile83[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_12_tree.root";
    char rootFile84[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_13_tree.root";
    char rootFile85[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_14_tree.root";
    char rootFile86[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_15_tree.root";
    char rootFile87[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_16_tree.root";
    char rootFile88[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_17_tree.root";
    char rootFile89[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_18_tree.root";
    char rootFile90[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_19_tree.root";
    char rootFile91[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_20_tree.root";
    char rootFile92[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT700to1000_RunII_106X_v2_0_tree.root";

    char rootFile93[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_1_tree.root";
    char rootFile94[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_2_tree.root";
    char rootFile95[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_3_tree.root";
    char rootFile96[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_4_tree.root";
    char rootFile97[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_5_tree.root";
    char rootFile98[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_6_tree.root";
    char rootFile99[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1000to1500_RunII_106X_v2_0_tree.root";

    char rootFile100[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1500to2000_RunII_106X_v2_1_tree.root";
    char rootFile101[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1500to2000_RunII_106X_v2_2_tree.root";
    char rootFile102[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1500to2000_RunII_106X_v2_3_tree.root";
    char rootFile103[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1500to2000_RunII_106X_v2_4_tree.root";
    char rootFile104[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT1500to2000_RunII_106X_v2_0_tree.root";

    char rootFile105[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT2000toInf_RunII_106X_v2_0_tree.root";
    char rootFile106[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT2000toInf_RunII_106X_v2_1_tree.root";
    char rootFile107[] = "/pnfs/desy.de/cms/tier2/store/user/hinzmann/dijetangular/qcdUL18feb2023/dijetChiUL18_QCD_HT2000toInf_RunII_106X_v2_2_tree.root";

    char outNameJet1[] = "/nfs/dust/cms/user/mueckejo/RootS2018/PlotJetResolution_Jet1_Run22018_WholeEta.root";
    char outNameJet2[] = "/nfs/dust/cms/user/mueckejo/RootS2018/PlotJetResolution_Jet2_Run22018_WholeEta.root";
    char outNameJet3[] = "/nfs/dust/cms/user/mueckejo/RootS2018/PlotJetResolution_Jet3_Run22018_WholeEta.root";

    TChain tree("tree");   // name of the tree is the argument
    tree.Add(rootFile1);
    tree.Add(rootFile2);
    tree.Add(rootFile3);
    tree.Add(rootFile4);
    tree.Add(rootFile5);
    tree.Add(rootFile6);
    tree.Add(rootFile7);
    tree.Add(rootFile8);
    tree.Add(rootFile9);
    tree.Add(rootFile10);
    tree.Add(rootFile11);
    tree.Add(rootFile12);
    tree.Add(rootFile13);
    tree.Add(rootFile14);
    tree.Add(rootFile15);
    tree.Add(rootFile16);
    tree.Add(rootFile17);
    tree.Add(rootFile18);
    tree.Add(rootFile19);
    tree.Add(rootFile20);
    tree.Add(rootFile21);
    tree.Add(rootFile22);
    tree.Add(rootFile23);
    tree.Add(rootFile24);
    tree.Add(rootFile25);
    tree.Add(rootFile26);
    tree.Add(rootFile27);
    tree.Add(rootFile28);
    tree.Add(rootFile29);
    tree.Add(rootFile30);
    tree.Add(rootFile31);
    tree.Add(rootFile32);
    tree.Add(rootFile33);
    tree.Add(rootFile34);
    tree.Add(rootFile35);
    tree.Add(rootFile36);
    tree.Add(rootFile37);
    tree.Add(rootFile38);
    tree.Add(rootFile39);
    tree.Add(rootFile40);
    tree.Add(rootFile41);
    tree.Add(rootFile42);
    tree.Add(rootFile43);
    tree.Add(rootFile44);
    tree.Add(rootFile45);
    tree.Add(rootFile46);
    tree.Add(rootFile47);
    tree.Add(rootFile48);
    tree.Add(rootFile49);
    tree.Add(rootFile50);
    tree.Add(rootFile51);
    tree.Add(rootFile52);
    tree.Add(rootFile53);
    tree.Add(rootFile54);
    tree.Add(rootFile55);
    tree.Add(rootFile56);
    tree.Add(rootFile57);
    tree.Add(rootFile58);
    tree.Add(rootFile59);
    tree.Add(rootFile60);
    tree.Add(rootFile61);
    tree.Add(rootFile62);
    tree.Add(rootFile63);
    tree.Add(rootFile64);
    tree.Add(rootFile65);
    tree.Add(rootFile66);
    tree.Add(rootFile67);
    tree.Add(rootFile68);
    tree.Add(rootFile69);
    tree.Add(rootFile70);
    tree.Add(rootFile71);
    tree.Add(rootFile72);
    tree.Add(rootFile73);
    tree.Add(rootFile74);
    tree.Add(rootFile75);
    tree.Add(rootFile76);
    tree.Add(rootFile77);
    tree.Add(rootFile78);
    tree.Add(rootFile79);
    tree.Add(rootFile80);
    tree.Add(rootFile81);
    tree.Add(rootFile82);
    tree.Add(rootFile83);
    tree.Add(rootFile84);
    tree.Add(rootFile85);
    tree.Add(rootFile86);
    tree.Add(rootFile87);
    tree.Add(rootFile88);
    tree.Add(rootFile89);
    tree.Add(rootFile90);
    tree.Add(rootFile91);
    tree.Add(rootFile92);
    tree.Add(rootFile93);
    tree.Add(rootFile94);
    tree.Add(rootFile95);
    tree.Add(rootFile96);
    tree.Add(rootFile97);
    tree.Add(rootFile98);
    tree.Add(rootFile99);
    tree.Add(rootFile100);
    tree.Add(rootFile101);
    tree.Add(rootFile102);
    tree.Add(rootFile103);
    tree.Add(rootFile104);
    tree.Add(rootFile105);
    tree.Add(rootFile106);
    tree.Add(rootFile107);

    //declare variables to Load from Root Tree
    const unsigned int eventNum = 1;
    //variables of Jet1
    float pt1Num[eventNum];
    float y1Num[eventNum];
    float eta1Num[eventNum];
    float phi1Num[eventNum];
    float mass1Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt1",&pt1Num);
    tree.SetBranchAddress("jetAK4_y1",&y1Num);
    tree.SetBranchAddress("jetAK4_eta1",&eta1Num);
    tree.SetBranchAddress("jetAK4_phi1",&phi1Num);
    tree.SetBranchAddress("jetAK4_mass1",&mass1Num);

    //variables of genJet
    float genpt1Num[eventNum];
    float geny1Num[eventNum];
    float geneta1Num[eventNum];
    float genphi1Num[eventNum];
    float genmass1Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt1",&genpt1Num);
    tree.SetBranchAddress("genJetAK4_y1",&geny1Num);
    tree.SetBranchAddress("genJetAK4_eta1",&geneta1Num);
    tree.SetBranchAddress("genJetAK4_phi1",&genphi1Num);
    tree.SetBranchAddress("genJetAK4_mass1",&genmass1Num);

    TH1D ResponseJet150to80("ResponseJet150to80","ResponseJet150to80",40,-0.2,0.2);
    ResponseJet150to80.Sumw2();
    TH1D ResponseJet180to120("ResponseJet180to120","ResponseJet180to120",40,-0.2,0.2);
    ResponseJet180to120.Sumw2();
    TH1D ResponseJet1120to170("ResponseJet1120to170","ResponseJet1120to170",40,-0.2,0.2);
    ResponseJet1120to170.Sumw2();
    TH1D ResponseJet1170to300("ResponseJet1170to300","ResponseJet1170to300",40,-0.2,0.2);
    ResponseJet1170to300.Sumw2();
    TH1D ResponseJet1300to470("ResponseJet1300to470","ResponseJet1300to470",40,-0.2,0.2);
    ResponseJet1300to470.Sumw2();
    TH1D ResponseJet1470to600("ResponseJet1470to600","ResponseJet1470to600",40,-0.2,0.2);
    ResponseJet1470to600.Sumw2();
    TH1D ResponseJet1600to800("ResponseJet1600to800","ResponseJet1600to800",40,-0.2,0.2);
    ResponseJet1600to800.Sumw2();
    TH1D ResponseJet1800to1000("ResponseJet1800to1000","ResponseJet1800to1000",40,-0.2,0.2);
    ResponseJet1800to1000.Sumw2();
    TH1D ResponseJet11000to1400("ResponseJet11000to1400","ResponseJet11000to1400",40,-0.2,0.2);
    ResponseJet11000to1400.Sumw2();
    TH1D ResponseJet11400to1800("ResponseJet11400to1800","ResponseJet11400to1800",40,-0.2,0.2);
    ResponseJet11400to1800.Sumw2();
    TH1D ResponseJet11800to2400("ResponseJet11800to2400","ResponseJet11800to2400",40,-0.2,0.2);
    ResponseJet11800to2400.Sumw2();
    TH1D ResponseJet12400to3200("ResponseJet12400to3200","ResponseJet12400to3200",40,-0.2,0.2);
    ResponseJet12400to3200.Sumw2();
    TH1D ResponseJet13200("ResponseJet13200","ResponseJet13200",40,-0.2,0.2);
    ResponseJet13200.Sumw2();

    //variables of Jet2
    float pt2Num[eventNum];
    float y2Num[eventNum];
    float eta2Num[eventNum];
    float phi2Num[eventNum];
    float mass2Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt2",&pt2Num);
    tree.SetBranchAddress("jetAK4_y2",&y2Num);
    tree.SetBranchAddress("jetAK4_eta2",&eta2Num);
    tree.SetBranchAddress("jetAK4_phi2",&phi2Num);
    tree.SetBranchAddress("jetAK4_mass2",&mass2Num);

    //variables of genJet
    float genpt2Num[eventNum];
    float geny2Num[eventNum];
    float geneta2Num[eventNum];
    float genphi2Num[eventNum];
    float genmass2Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt2",&genpt2Num);
    tree.SetBranchAddress("genJetAK4_y2",&geny2Num);
    tree.SetBranchAddress("genJetAK4_eta2",&geneta2Num);
    tree.SetBranchAddress("genJetAK4_phi2",&genphi2Num);
    tree.SetBranchAddress("genJetAK4_mass2",&genmass2Num);

    TH1D ResponseJet250to80("ResponseJet250to80","ResponseJet250to80",40,-0.2,0.2);
    ResponseJet250to80.Sumw2();
    TH1D ResponseJet280to120("ResponseJet280to120","ResponseJet280to120",40,-0.2,0.2);
    ResponseJet280to120.Sumw2();
    TH1D ResponseJet2120to170("ResponseJet2120to170","ResponseJet2120to170",40,-0.2,0.2);
    ResponseJet2120to170.Sumw2();
    TH1D ResponseJet2170to300("ResponseJet2170to300","ResponseJet2170to300",40,-0.2,0.2);
    ResponseJet2170to300.Sumw2();
    TH1D ResponseJet2300to470("ResponseJet2300to470","ResponseJet2300to470",40,-0.2,0.2);
    ResponseJet2300to470.Sumw2();
    TH1D ResponseJet2470to600("ResponseJet2470to600","ResponseJet2470to600",40,-0.2,0.2);
    ResponseJet2470to600.Sumw2();
    TH1D ResponseJet2600to800("ResponseJet2600to800","ResponseJet2600to800",40,-0.2,0.2);
    ResponseJet2600to800.Sumw2();
    TH1D ResponseJet2800to1000("ResponseJet2800to1000","ResponseJet2800to1000",40,-0.2,0.2);
    ResponseJet2800to1000.Sumw2();
    TH1D ResponseJet21000to1400("ResponseJet21000to1400","ResponseJet21000to1400",40,-0.2,0.2);
    ResponseJet21000to1400.Sumw2();
    TH1D ResponseJet21400to1800("ResponseJet21400to1800","ResponseJet21400to1800",40,-0.2,0.2);
    ResponseJet21400to1800.Sumw2();
    TH1D ResponseJet21800to2400("ResponseJet21800to2400","ResponseJet21800to2400",40,-0.2,0.2);
    ResponseJet21800to2400.Sumw2();
    TH1D ResponseJet22400to3200("ResponseJet22400to3200","ResponseJet22400to3200",40,-0.2,0.2);
    ResponseJet22400to3200.Sumw2();
    TH1D ResponseJet23200("ResponseJet23200","ResponseJet23200",40,-0.2,0.2);
    ResponseJet23200.Sumw2();

    //variables of Jet3
    float pt3Num[eventNum];
    float y3Num[eventNum];
    float eta3Num[eventNum];
    float phi3Num[eventNum];
    float mass3Num[eventNum];

    tree.SetBranchAddress("jetAK4_pt3",&pt3Num);
    tree.SetBranchAddress("jetAK4_y3",&y3Num);
    tree.SetBranchAddress("jetAK4_eta3",&eta3Num);
    tree.SetBranchAddress("jetAK4_phi3",&phi3Num);
    tree.SetBranchAddress("jetAK4_mass3",&mass3Num);

    //variables of genJet
    float genpt3Num[eventNum];
    float geny3Num[eventNum];
    float geneta3Num[eventNum];
    float genphi3Num[eventNum];
    float genmass3Num[eventNum];

    tree.SetBranchAddress("genJetAK4_pt3",&genpt3Num);
    tree.SetBranchAddress("genJetAK4_y3",&geny3Num);
    tree.SetBranchAddress("genJetAK4_eta3",&geneta3Num);
    tree.SetBranchAddress("genJetAK4_phi3",&genphi3Num);
    tree.SetBranchAddress("genJetAK4_mass3",&genmass3Num);

    TH1D ResponseJet350to80("ResponseJet350to80","ResponseJet350to80",40,-0.2,0.2);
    ResponseJet350to80.Sumw2();
    TH1D ResponseJet380to120("ResponseJet380to120","ResponseJet380to120",40,-0.2,0.2);
    ResponseJet380to120.Sumw2();
    TH1D ResponseJet3120to170("ResponseJet3120to170","ResponseJet3120to170",40,-0.2,0.2);
    ResponseJet3120to170.Sumw2();
    TH1D ResponseJet3170to300("ResponseJet3170to300","ResponseJet3170to300",40,-0.2,0.2);
    ResponseJet3170to300.Sumw2();
    TH1D ResponseJet3300to470("ResponseJet3300to470","ResponseJet3300to470",40,-0.2,0.2);
    ResponseJet3300to470.Sumw2();
    TH1D ResponseJet3470to600("ResponseJet3470to600","ResponseJet3470to600",40,-0.2,0.2);
    ResponseJet3470to600.Sumw2();
    TH1D ResponseJet3600to800("ResponseJet3600to800","ResponseJet3600to800",40,-0.2,0.2);
    ResponseJet3600to800.Sumw2();
    TH1D ResponseJet3800to1000("ResponseJet3800to1000","ResponseJet3800to1000",40,-0.2,0.2);
    ResponseJet3800to1000.Sumw2();
    TH1D ResponseJet31000to1400("ResponseJet31000to1400","ResponseJet31000to1400",40,-0.2,0.2);
    ResponseJet31000to1400.Sumw2();
    TH1D ResponseJet31400to1800("ResponseJet31400to1800","ResponseJet31400to1800",40,-0.2,0.2);
    ResponseJet31400to1800.Sumw2();
    TH1D ResponseJet31800to2400("ResponseJet31800to2400","ResponseJet31800to2400",40,-0.2,0.2);
    ResponseJet31800to2400.Sumw2();
    TH1D ResponseJet32400to3200("ResponseJet32400to3200","ResponseJet32400to3200",40,-0.2,0.2);
    ResponseJet32400to3200.Sumw2();
    TH1D ResponseJet33200("ResponseJet33200","ResponseJet33200",40,-0.2,0.2);
    ResponseJet33200.Sumw2();

    float numberEntries = tree.GetEntries();

    std::cout << tree.GetEntries() << std::endl;
    //Fill the Hists with Root Tree Sim and Genjets
    //GetEntries();
    for (Long64_t entry = 0; entry <tree.GetEntries(); ++entry)
    {
      tree.GetEntry(entry);

      if(entry % 100000 == 0)
      {
        std::cout << to_string((entry/numberEntries)*100) << "% finished" << std::endl;
      }

      //For Jet1
      //calculate R
      double R_ValueJet1 = sqrt(pow(phi1Num[0]-genphi1Num[0],2)*pow(eta1Num[0]-geneta1Num[0],2));

      if(R_ValueJet1 < 0.2){
        //calculate response
        double ResponseJet1 = (pt1Num[0]-genpt1Num[0])/genpt1Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= pt1Num[0] && pt1Num[0] < 80 && 50 <= genpt1Num[0] && genpt1Num[0] < 80){
        ResponseJet150to80.Fill(ResponseJet1);
        }
        if(80 <= pt1Num[0] && pt1Num[0] < 120 && 80 <= genpt1Num[0] && genpt1Num[0] < 120){
        ResponseJet180to120.Fill(ResponseJet1);
        }
        if(120 <= pt1Num[0] && pt1Num[0] < 170 && 120 <= genpt1Num[0] && genpt1Num[0] < 170){
        ResponseJet1120to170.Fill(ResponseJet1);
        }
        if(170 <= pt1Num[0] && pt1Num[0] < 300 && 170 <= genpt1Num[0] && genpt1Num[0] < 300){
        ResponseJet1170to300.Fill(ResponseJet1);
        }
        if(300 <= pt1Num[0] && pt1Num[0] < 470 && 300 <= genpt1Num[0] && genpt1Num[0] < 470){
        ResponseJet1300to470.Fill(ResponseJet1);
        }
        if(470 <= pt1Num[0] && pt1Num[0] < 600 && 470 <= genpt1Num[0] && genpt1Num[0] < 600){
        ResponseJet1470to600.Fill(ResponseJet1);
        }
        if(600 <= pt1Num[0] && pt1Num[0] < 800 && 600 <= genpt1Num[0] && genpt1Num[0] < 800){
        ResponseJet1600to800.Fill(ResponseJet1);
        }
        if(800 <= pt1Num[0] && pt1Num[0] < 1000 && 800 <= genpt1Num[0] && genpt1Num[0] < 1000){
        ResponseJet1800to1000.Fill(ResponseJet1);
        }
        if(1000 <= pt1Num[0] && pt1Num[0] < 1400 && 1000 <= genpt1Num[0] && genpt1Num[0] < 1400){
        ResponseJet11000to1400.Fill(ResponseJet1);
        }
        if(1400 <= pt1Num[0] && pt1Num[0] < 1800 && 1400 <= genpt1Num[0] && genpt1Num[0] < 1800){
        ResponseJet11400to1800.Fill(ResponseJet1);
        }
        if(1800 <= pt1Num[0] && pt1Num[0] < 2400 && 1800 <= genpt1Num[0] && genpt1Num[0] < 2400){
        ResponseJet11800to2400.Fill(ResponseJet1);
        }
        if(2400 <= pt1Num[0] && pt1Num[0] < 3200 && 2400 <= genpt1Num[0] && genpt1Num[0] < 3200){
        ResponseJet12400to3200.Fill(ResponseJet1);
        }
        if(3200 <= pt1Num[0] && 3200 <= genpt1Num[0]){
        ResponseJet13200.Fill(ResponseJet1);
        }
      }

      //For Jet2
      //calculate R
      double R_ValueJet2 = sqrt(pow(phi2Num[0]-genphi2Num[0],2)*pow(eta2Num[0]-geneta2Num[0],2));

      if(R_ValueJet2 < 0.2){
        //calculate response
        double ResponseJet2 = (pt2Num[0]-genpt2Num[0])/genpt2Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= pt2Num[0] && pt2Num[0] < 80 && 50 <= genpt2Num[0] && genpt2Num[0] < 80){
        ResponseJet250to80.Fill(ResponseJet2);
        }
        if(80 <= pt2Num[0] && pt2Num[0] < 120 && 80 <= genpt2Num[0] && genpt2Num[0] < 120){
        ResponseJet280to120.Fill(ResponseJet2);
        }
        if(120 <= pt2Num[0] && pt2Num[0] < 170 && 120 <= genpt2Num[0] && genpt2Num[0] < 170){
        ResponseJet2120to170.Fill(ResponseJet2);
        }
        if(170 <= pt2Num[0] && pt2Num[0] < 300 && 170 <= genpt2Num[0] && genpt2Num[0] < 300){
        ResponseJet2170to300.Fill(ResponseJet2);
        }
        if(300 <= pt2Num[0] && pt2Num[0] < 470 && 300 <= genpt2Num[0] && genpt2Num[0] < 470){
        ResponseJet2300to470.Fill(ResponseJet2);
        }
        if(470 <= pt2Num[0] && pt2Num[0] < 600 && 470 <= genpt2Num[0] && genpt2Num[0] < 600){
        ResponseJet2470to600.Fill(ResponseJet2);
        }
        if(600 <= pt2Num[0] && pt2Num[0] < 800 && 600 <= genpt2Num[0] && genpt2Num[0] < 800){
        ResponseJet2600to800.Fill(ResponseJet2);
        }
        if(800 <= pt2Num[0] && pt2Num[0] < 1000 && 800 <= genpt2Num[0] && genpt2Num[0] < 1000){
        ResponseJet2800to1000.Fill(ResponseJet2);
        }
        if(1000 <= pt2Num[0] && pt2Num[0] < 1400 && 1000 <= genpt2Num[0] && genpt2Num[0] < 1400){
        ResponseJet21000to1400.Fill(ResponseJet2);
        }
        if(1400 <= pt2Num[0] && pt2Num[0] < 1800 && 1400 <= genpt2Num[0] && genpt2Num[0] < 1800){
        ResponseJet21400to1800.Fill(ResponseJet2);
        }
        if(1800 <= pt2Num[0] && pt2Num[0] < 2400 && 1800 <= genpt2Num[0] && genpt2Num[0] < 2400){
        ResponseJet21800to2400.Fill(ResponseJet2);
        }
        if(2400 <= pt2Num[0] && pt2Num[0] < 3200 && 2400 <= genpt2Num[0] && genpt2Num[0] < 3200){
        ResponseJet22400to3200.Fill(ResponseJet2);
        }
        if(3200 <= pt2Num[0] && 3200 <= genpt2Num[0]){
        ResponseJet23200.Fill(ResponseJet2);
        }
      }

      //For Jet3
      //calculate R
      double R_ValueJet3 = sqrt(pow(phi3Num[0]-genphi3Num[0],2)*pow(eta3Num[0]-geneta3Num[0],2));

      if(R_ValueJet3 < 0.2){
        //calculate response
        double ResponseJet3 = (pt3Num[0]-genpt3Num[0])/genpt3Num[0];

        //Fill hists with response for pt ranges of 20GeV from 0 to 1000
        if(50 <= pt3Num[0] && pt3Num[0] < 80 && 50 <= genpt3Num[0] && genpt3Num[0] < 80){
        ResponseJet350to80.Fill(ResponseJet3);
        }
        if(80 <= pt3Num[0] && pt3Num[0] < 120 && 80 <= genpt3Num[0] && genpt3Num[0] < 120){
        ResponseJet380to120.Fill(ResponseJet3);
        }
        if(120 <= pt3Num[0] && pt3Num[0] < 170 && 120 <= genpt3Num[0] && genpt3Num[0] < 170){
        ResponseJet3120to170.Fill(ResponseJet3);
        }
        if(170 <= pt3Num[0] && pt3Num[0] < 300 && 170 <= genpt3Num[0] && genpt3Num[0] < 300){
        ResponseJet3170to300.Fill(ResponseJet3);
        }
        if(300 <= pt3Num[0] && pt3Num[0] < 470 && 300 <= genpt3Num[0] && genpt3Num[0] < 470){
        ResponseJet3300to470.Fill(ResponseJet3);
        }
        if(470 <= pt3Num[0] && pt3Num[0] < 600 && 470 <= genpt3Num[0] && genpt3Num[0] < 600){
        ResponseJet3470to600.Fill(ResponseJet3);
        }
        if(600 <= pt3Num[0] && pt3Num[0] < 800 && 600 <= genpt3Num[0] && genpt3Num[0] < 800){
        ResponseJet3600to800.Fill(ResponseJet3);
        }
        if(800 <= pt3Num[0] && pt3Num[0] < 1000 && 800 <= genpt3Num[0] && genpt3Num[0] < 1000){
        ResponseJet3800to1000.Fill(ResponseJet3);
        }
        if(1000 <= pt3Num[0] && pt3Num[0] < 1400 && 1000 <= genpt3Num[0] && genpt3Num[0] < 1400){
        ResponseJet31000to1400.Fill(ResponseJet3);
        }
        if(1400 <= pt3Num[0] && pt3Num[0] < 1800 && 1400 <= genpt3Num[0] && genpt3Num[0] < 1800){
        ResponseJet31400to1800.Fill(ResponseJet3);
        }
        if(1800 <= pt3Num[0] && pt3Num[0] < 2400 && 1800 <= genpt3Num[0] && genpt3Num[0] < 2400){
        ResponseJet31800to2400.Fill(ResponseJet3);
        }
        if(2400 <= pt3Num[0] && pt3Num[0] < 3200 && 2400 <= genpt3Num[0] && genpt3Num[0] < 3200){
        ResponseJet32400to3200.Fill(ResponseJet3);
        }
        if(3200 <= pt3Num[0] && 3200 <= genpt3Num[0]){
        ResponseJet33200.Fill(ResponseJet3);
        }
      }

    }

    //Neccesary so files dont get lost
    ResponseJet150to80.SetDirectory(0);
    ResponseJet180to120.SetDirectory(0);
    ResponseJet1120to170.SetDirectory(0);
    ResponseJet1170to300.SetDirectory(0);
    ResponseJet1300to470.SetDirectory(0);
    ResponseJet1470to600.SetDirectory(0);
    ResponseJet1600to800.SetDirectory(0);
    ResponseJet1800to1000.SetDirectory(0);
    ResponseJet11000to1400.SetDirectory(0);
    ResponseJet11400to1800.SetDirectory(0);
    ResponseJet11800to2400.SetDirectory(0);
    ResponseJet12400to3200.SetDirectory(0);
    ResponseJet13200.SetDirectory(0);
    ResponseJet250to80.SetDirectory(0);
    ResponseJet280to120.SetDirectory(0);
    ResponseJet2120to170.SetDirectory(0);
    ResponseJet2170to300.SetDirectory(0);
    ResponseJet2300to470.SetDirectory(0);
    ResponseJet2470to600.SetDirectory(0);
    ResponseJet2600to800.SetDirectory(0);
    ResponseJet2800to1000.SetDirectory(0);
    ResponseJet21000to1400.SetDirectory(0);
    ResponseJet21400to1800.SetDirectory(0);
    ResponseJet21800to2400.SetDirectory(0);
    ResponseJet22400to3200.SetDirectory(0);
    ResponseJet23200.SetDirectory(0);
    ResponseJet350to80.SetDirectory(0);
    ResponseJet380to120.SetDirectory(0);
    ResponseJet3120to170.SetDirectory(0);
    ResponseJet3170to300.SetDirectory(0);
    ResponseJet3300to470.SetDirectory(0);
    ResponseJet3470to600.SetDirectory(0);
    ResponseJet3600to800.SetDirectory(0);
    ResponseJet3800to1000.SetDirectory(0);
    ResponseJet31000to1400.SetDirectory(0);
    ResponseJet31400to1800.SetDirectory(0);
    ResponseJet31800to2400.SetDirectory(0);
    ResponseJet32400to3200.SetDirectory(0);
    ResponseJet33200.SetDirectory(0);


    TFile* outHistFile1 = TFile::Open(outNameJet1,"RECREATE");
    ResponseJet150to80.Write();
    ResponseJet180to120.Write();
    ResponseJet1120to170.Write();
    ResponseJet1170to300.Write();
    ResponseJet1300to470.Write();
    ResponseJet1470to600.Write();
    ResponseJet1600to800.Write();
    ResponseJet1800to1000.Write();
    ResponseJet11000to1400.Write();
    ResponseJet11400to1800.Write();
    ResponseJet11800to2400.Write();
    ResponseJet12400to3200.Write();
    ResponseJet13200.Write();
    outHistFile1->Close();

    TFile* outHistFile2 = TFile::Open(outNameJet2,"RECREATE");
    ResponseJet250to80.Write();
    ResponseJet280to120.Write();
    ResponseJet2120to170.Write();
    ResponseJet2170to300.Write();
    ResponseJet2300to470.Write();
    ResponseJet2470to600.Write();
    ResponseJet2600to800.Write();
    ResponseJet2800to1000.Write();
    ResponseJet21000to1400.Write();
    ResponseJet21400to1800.Write();
    ResponseJet21800to2400.Write();
    ResponseJet22400to3200.Write();
    ResponseJet23200.Write();
    outHistFile2->Close();

    TFile* outHistFile3 = TFile::Open(outNameJet3,"RECREATE");
    ResponseJet350to80.Write();
    ResponseJet380to120.Write();
    ResponseJet3120to170.Write();
    ResponseJet3170to300.Write();
    ResponseJet3300to470.Write();
    ResponseJet3470to600.Write();
    ResponseJet3600to800.Write();
    ResponseJet3800to1000.Write();
    ResponseJet31000to1400.Write();
    ResponseJet31400to1800.Write();
    ResponseJet31800to2400.Write();
    ResponseJet32400to3200.Write();
    ResponseJet33200.Write();
    outHistFile3->Close();

  return 0;
}
