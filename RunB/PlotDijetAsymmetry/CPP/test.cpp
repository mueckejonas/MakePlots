int test()
{

double pi = 3.14159265358979323846;
double phi1 = 1.0;
double phi2 = 2.0;

double testvalue = TVector2::Phi_mpi_pi(abs(phi1)+abs(phi2));

std::cout << to_string(testvalue*180.0/pi) << std::endl;

return 0;
}
