# ARP_Poison


Un outil Python pour effectuer du spoofing ARP à des fins éducatives. Ce script permet de rediriger le trafic réseau en envoyant des réponses ARP falsifiées dans un petit reseau local.

## Auteur et Licence

- **Auteur** : Ray
- **Licence** :
## Prérequis

Assurez-vous d'avoir les bibliothèques suivantes installées :

- Python 3.x
- `nmap3`
- `scapy`
- `subprocess`

## Installation

1. Clonez ce dépôt (si applicable) ou téléchargez le fichier `spoof.py`.
2. Installez les dépendances nécessaires en exécutant la commande suivante :

```bash
pip install nmap3 scapy
```
Utilisation
Exécutez le script avec Python :

Exécution du script
Modifiez les valeurs codées en dur dans le fichier spoof.py si nécessaire :

Adresse IP de la victime (192.XXXXXXXX)
Adresse MAC de la victime (36:XXXXXXXX)
Adresse MAC de la passerelle (36:77:XXXXXX)

## Fonction

| Fonctionnalité                      | Description                                                          |
| ----------------------------------- | -------------------------------------------------------------------- |
| Détection de l’IP locale            | Récupère l’adresse IP locale du système.                             |
| Détection de la passerelle via DHCP | Utilise `nmap` (script DHCP) pour identifier la passerelle réseau.   |
| Récupération de l’adresse MAC       | Obtient la MAC associée à une IP donnée.                             |
| Envoi de réponses ARP falsifiées    | Envoie des paquets ARP pour influencer le routage local (ex : MITM). |

##
