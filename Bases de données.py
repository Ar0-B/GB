# définir les charges

charge_variable={"nourriture":0,"loisir":0,"shopping":0,"coiffure":0,"autres":0}

charge_fixe={"loyer":0,"eau et éléctricité":0,"transport":0,"téléphone":0,"autres":0}

revenue_mensuel = float(input("Entrer votre revenue mensuel (€):"))

def repartition_globale():
    
    charge_globale = {"{charge_fixe}":0,"{charge_variable}":0,"charge_crucial":0,"epargne":0}
    while True:
        try:
            for charge in charge_globale:
                pourcentage = float(input(f"Entrer le pourcentage pour {charge} (%) ="))
                charge_globale[charge]= pourcentage
                total_pourcentage = sum(charge.values())
            if total_pourcentage != 100:
                print("Le pourcentage n'est pas correct.Réessayer encore")
                return False

            for cle,valeur in charge_globale.items():
                montant_reparti = (valeur/100)* revenue_mensuel
                print(f"{cle} = {montant_reparti}€ ({valeur}%)")
        except ValueError:
            return False


repartition_globale()