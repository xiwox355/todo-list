taches = []

def ajouter_tache(tache):
    taches.append(tache)
    print(f"Tâche ajoutée : {tache}")

def lister_taches():
    print("\nListe des tâches :")
    if not taches:
        print("Aucune tâche.")
    for i, tache in enumerate(taches, 1):
        print(f"{i}. {tache}")

def supprimer_tache(index):
    try:
        tache_supprimee = taches.pop(index - 1)
        print(f"Tâche supprimée : {tache_supprimee}")
    except IndexError:
        print("Index invalide. Veuillez réessayer.")

def main():
    while True:
        print("\nOptions : [1] Ajouter une tâche [2] Lister les tâches [3] Supprimer une tâche [4] Quitter")
        choix = input("Choisissez une option : ")
        if choix == "1":
            tache = input("Entrez une tâche : ")
            ajouter_tache(tache)
        elif choix == "2":
            lister_taches()
        elif choix == "3":
            lister_taches()
            try:
                index = int(input("Entrez le numéro de la tâche à supprimer : "))
                supprimer_tache(index)
            except ValueError:
                print("Veuillez entrer un numéro valide.")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
