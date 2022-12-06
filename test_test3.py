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

@pytest.fixture(scope="module")
def setup():
    print("Ouverture de la connexion BD")
    yield
    print("Fermeture de la BD")

@pytest.fixture(scope="function")
def before():
    print("Ouverture du navigateur")
    yield
    print("Fermeture du navigateur")


def test_login(setup, before):
    print("se connecter au site login saleseforce")

def test_createuser(setup, before):
    print("creer un utilisateur")

