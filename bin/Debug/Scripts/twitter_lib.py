import Constellation
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
    access_token_key : jeu de clefs associé à un compte Twitter via oAuth
    access_token_secret : jeu de clefs associé à un compte Twitter via oAuth
"""
def basicInformations(atk, ats):
    api = twitter.Api(consumer_key        = 'ygOLcfUomXDvSUfpinYvXg4Zz',                
                      consumer_secret     = 'OsOHpzzZTNIbzztnr1nmltmx2mg1iVcFi4eygNEpcEWB2lCEtv', 
                      access_token_key    = atk, 
                      access_token_secret = ats) 

    return api.VerifyCredentials()