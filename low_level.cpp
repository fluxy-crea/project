#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>

int main() {
  // Your low-level C++ code here

  // Example: Making an HTTP request using cpr
  cpr::Response response =
      cpr::Get(cpr::Url{"https://jsonplaceholder.typicode.com/todos/1"});

  // Example: Parsing JSON using nlohmann/json
  nlohmann::json json_data = nlohmann::json::parse(response.text);

  // Example: Displaying the parsed JSON data
  std::cout << "Title: " << json_data["title"] << std::endl;
  std::cout << "Completed: " << json_data["completed"] << std::endl;

  return 0;
}
