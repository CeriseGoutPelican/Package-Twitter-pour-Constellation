import twitter

""" FONCTION : basicInformations
    ============================
    Permet de récupérer les informations basiques à l'aide de l'API Twitter
    et la dépendance associée python-twitter

    Voir pour référence :
    API Twitter - https://apps.twitter.com/
    Python-Twitter - https://github.com/bear/python-twitter

    PARAMETRES :
    ============
    consumer_key : clef publique de l'application
    consumer_secret : clef privée de l'application
    access_token_key : jeu de clefs associé à un compte Twitter via oAuth
    access_token_secret : jeu de clefs associé à un compte Twitter via oAuth
"""
def basicInformations(ck, cs, atk, ats):
    api = twitter.Api(consumer_key = ck, consumer_secret = cs, access_token_key = atk, access_token_secret = ats) 

    return api.VerifyCredentials()