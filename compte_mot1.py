"""fichier compte_mot1.py"""
import pdb
import httplib
import time
import sys


FICHIER_LOG = open("fichier_log.txt", "w")
LOG = False


def count(adresse):
    """Fonction qui compte les mots de la page"""
    logger(FICHIER_LOG, " tentative de connection")
    pdb.set_trace()
    conn = httplib.HTTPConnection("cache.univ-st-etienne.fr", 3128)
    conn.request("GET", adresse)
    res = conn.getresponse()

    logger(FICHIER_LOG, " " + str(res.status) + " " + res.reason)

    logger(FICHIER_LOG, " recuperation de la page")

    page = res.read()

    logger(FICHIER_LOG, " recuperation de la page OK")

    logger(FICHIER_LOG, " debut de l'operation de decoupage")
    decoup = page.split(' ')

    logger(FICHIER_LOG, " fin de l'operation de decoupage")

    logger(FICHIER_LOG, " nombre de mot : " + str(len(decoup)))


def logger(fichier, message):
    """Fonction qui gere l'ecriture dans le fichier log"""
    if LOG:
        fichier.writelines(time.strftime('%d/%m/%y %H:%M', time.localtime()) +
        message + "\n")


if len(sys.argv) < 3:
    LOG = True
    logger(FICHIER_LOG, " debut de l'application")
    count(sys.argv[1])
else:
    logger(FICHIER_LOG, " erreur : nombre de parametre incorrect")
FICHIER_LOG.close()
