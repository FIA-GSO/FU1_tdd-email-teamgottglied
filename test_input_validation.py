import pytest
from input_validation import is_valid_email
from input_validation import is_valid_password


@pytest.mark.parametrize("email", [
    ("test@email.com")
    , ("t.est@email.com")
    , ("test@em.ail.com")
    , ("test@email.co.uk")
    , ("te-st@email.com")
    , ("te_st@email.com")
    , ("test1@email.com")
])
def test_is_valid_email__gueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email

    # act
    response = is_valid_email(email)

    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    ("testemail.com")  # Fehlendes @-Zeichen
    , ("test@email")  # Fehlende Top-Level-Domain
    , ("test@em@ail.com")  # Mehrfaches @-Zeichen
])
def test_is_valid_email__ungueltige_Adressen(email):
    # arrange
    email_adress_to_be_tested = email

    # act
    response = is_valid_email(email)

    # assert
    assert response is False


@pytest.mark.parametrize("password",
                         [
                             "ein-sicheres-Passwort-hAh"
                             , "6v2§!faD"
                         ])
def test_is_valid_password__gueltige_Passwoerter(password):
    # act
    response = is_valid_password(password)

    # assert
    assert response is True


@pytest.mark.parametrize("password",
                         [
                             "kein-Sicheres-Passwort"
                             , "Abc3!"
                         ])
def test_is_valid_password__ungueltige_Passwoerter(password):
    # arrange
    password_to_be_tested = password

    # act
    response = is_valid_password(password_to_be_tested)

    # assert
    assert response is False
