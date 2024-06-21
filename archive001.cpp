#include <iostream>
#include <list>
#include <numeric>
using namespace std;

int main() {
 
  int limit = 1000;
  list<int> multipleList;
  
  int i = 1;
  while (i < limit) {
    if (i % 3 == 0 || i % 5 == 0) {
     multipleList.push_back(i);   
    }
    i++;
  }
  
  int result = accumulate(multipleList.begin(), multipleList.end(), 0);
  
  cout << result;

  return 0;
}
