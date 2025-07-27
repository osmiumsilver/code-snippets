#include <iostream>

int main() {
  // 分配内存
  int* ptr = new int;
  *ptr = 10;

  // 释放内存
  delete ptr;

  // 尝试访问已释放的内存
  std::cout << *ptr << std::endl;  // UAF 漏洞发生在这里

  return 0;
}
