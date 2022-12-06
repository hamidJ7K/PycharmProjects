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


def test_login():
    url_attendue = "https://login.salesforce.com/"
    url_obtenue = "https://login.salesforce.com/"
    # if url_obtenue == url_attendue :
    #     print("TEST PASSED")
    # else :
    #     print("TEST FAILED!")
    print("debut de validation")
    #assert url_attendue == url_obtenue, "les url sont differentes"
    assert "login" in url_obtenue
    assert False, "Je force le test à echouer!" # hard assertion
    print("fin de validation!")



