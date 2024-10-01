#extraction csv

chemin = G:\Mon Drive\bootcamp\Projet\Gestionnaire de budget version V1.0 Projet\dossier csv\Recette.csv
import csv
with open('chemin/Recette.csv', mode='r')as fichier_csv:
    reader = csv.Dictreader(fichier_csv)
    for ligne in reader:
        print(ligne)
   
    



def repartition_montant():
    montant = (pourcentage/100)*revenu