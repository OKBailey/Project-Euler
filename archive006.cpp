#include <iostream>
using namespace std;

int main() {
 
  int limit = 100;
  int sum_of_squares, series_sum, square_of_sum;
  sum_of_squares = series_sum = square_of_sum = 0;
  
  int i = 1;
  while (i <= limit) {
    sum_of_squares = sum_of_squares + (i*i);
    series_sum +=i;
    i++;
  }
  square_of_sum = series_sum * series_sum;

  cout << square_of_sum - sum_of_squares;

  return 0;
}
