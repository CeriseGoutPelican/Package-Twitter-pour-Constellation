import Constellation
import twitter_lib as Tw
import json
import time

def OnStart():

    # Récupération des informations de configuration (clé Twitter)
    if Constellation.GetSetting("twitter_access_token_key") <> None:
        Constellation.WriteInfo("Clés de configurations récupérées : (%s ; %s)" % (Constellation.GetSetting("twitter_access_token_key"), Constellation.GetSetting("twitter_access_token_secret")))
    else:
        #Constellation.RequestSettings()
        Constellation.WriteError("Problèm lors de la configuration du paquet")

    while(True):
        # Informations basiques liées à un compte Twitter :
        basicInformations   = Tw.basicInformations(Constellation.GetSetting("twitter_access_token_key"), Constellation.GetSetting("twitter_access_token_secret"))

        # Vérification de la connexion au serveur Twitter
        try:
            basicInformations.id
        except error:
            Constellation.WriteError("Impossible de se connecter au serveur Twitter...")
        else:
            # Push des données
            Constellation.WriteInfo("Connexion au serveur Twitter : récupération des informations de @%s terminée !" % basicInformations.screen_name)
            Constellation.PushStateObject(basicInformations.screen_name, basicInformations.AsDict(), lifetime = 30)

        time.sleep(30)

    pass

Constellation.Start(OnStart);