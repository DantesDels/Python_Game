def display_main_menu():
    print(" === MENU PRINCIPAL ===\n\n")
    print("  1. Nouvelle Partie")
    print("  2. Continuer")
    print("  3. Sauvegarder la Partie")
    print("  4. Charger une Partie")
    print("  5. Quitter")

    choice = input("Sélectionnez une option : ")
    choice = choice.strip().lower()
    map = {
        '1': '1', 'nouvelle partie': '1', 'new game': '1', 'n': '1',
        '2': '2', 'continuer': '2', 'continue': '2', 'c': '2',
        '3': '3', 'sauvegarder': '3', 'save': '3', 's': '3',
        '4': '4', 'charger': '4', 'load': '4', 'l': '4',
        '5': '5', 'quitter': '5', 'quit': '5', 'q': '5'
    }
    choice = map.get(choice, choice)
    if choice not in ['1', '2', '3', '4', '5']:
        print("Choix invalide. Veuillez réessayer.\n")
        return display_main_menu()
    elif choice == '1':
        print("Démarrage d'une nouvelle partie...\n")
        # Initialiser un nouvel objet de jeu ici
    elif choice == '2':
        print("Reprise de la dernière partie sauvegardée...\n")
        # Continuer la partie en cours
    elif choice == '3':
        print("Sauvegarde de la partie en cours...\n")
        # Sauvegarder la partie en cours
    elif choice == '4':
        print("Chargement d'une partie sauvegardée...\n")
        # Charger une partie spécifique
    elif choice == '5':
        print("Merci d'avoir joué ! À bientôt.")
        exit()
    return choice
