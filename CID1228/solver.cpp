#include <iostream>
#include <memory>
int main()
{
  int a = 99;
  auto b = [&a]{ return ++a; };
  std::cout << b() << std::endl;
  return 0;
}
