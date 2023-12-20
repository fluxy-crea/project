#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>

int main() {
  // Effectuer une requête GET
  cpr::Response response = cpr::Get(cpr::Url{"localhost:8000"});

  // Afficher la réponse brute du serveur
  std::cout << "Raw Response: " << response.text << std::endl;

  // Vérifier si la requête a réussi (code de statut 200)
  if (response.status_code == 200) {
    // Analyser la réponse JSON
    nlohmann::json jsonData = nlohmann::json::parse(response.text);

    // Accéder aux données JSON
    std::string title = jsonData["title"];
    bool completed = jsonData["completed"];

    // Afficher les données JSON
    std::cout << "Title: " << title << std::endl;
    std::cout << "Completed: " << (completed ? "true" : "false") << std::endl;
  } else {
    // Afficher une erreur si la requête échoue
    std::cerr << "Erreur lors de la requête GET. Code de statut : "
              << response.status_code << std::endl;
  }

  return 0;
}
