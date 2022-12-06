import pytest

# Regle 1 Nom de fichier devrait commnecer par le mot "test"
# Regle #2 Nom des methodes devrait commencer par le mot "test"

# def setup_module(module):
#     print("Ouverture la connexion BD")
#
# def teardown_module(module):
#     print("Cloture la connexion BD")
#
#
# #def setup_function(fonction):
#     print("Ouverture du site loginsalseforce")
#
#
# def teardown_function(function):
#   print("Fermeture du navigateur")
def get_data():
    return [
        ("hamid","123456"),
        ("hamid1", "123456A"),
        ("hamid2", "123456B"),
        ("hamid3", "123456C"),
        ("hamid4", "123456D"),
    ]
@pytest.mark.parametrize("username, password",get_data())
def test_login(username, password):
    print(username, "----", password,"----")

