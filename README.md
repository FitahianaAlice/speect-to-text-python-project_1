# Text-to-Speech Converter

Ce code est un petit programme qui permet de convertir du texte en parole en utilisant la bibliothèque Python `pyttsx3` et une interface graphique simple réalisée avec `tkinter`.

## Auteur
Ce code a été créé par RAZANAKOLONA Valisoa Fitahiana (fitahianaalice@gmail.com)


## Description
Le programme est destiné à convertir n'importe quel texte que l'utilisateur entre dans une zone de saisie en parole. Une fois que l'utilisateur a saisi le texte, il peut cliquer sur le bouton "Convertir", et le programme utilisera la bibliothèque `pyttsx3` pour lire le texte à voix haute.

## Fonctionnement
1. L'utilisateur est invité à saisir le texte souhaité dans le champ de saisie.
2. Une fois que le texte est entré, l'utilisateur clique sur le bouton "Convertir".
3. Le programme utilise la bibliothèque `pyttsx3` pour initialiser un moteur de synthèse vocale.
4. Le moteur de synthèse vocale lit le texte saisi par l'utilisateur à voix haute.
5. Le texte est prononcé en utilisant les paramètres par défaut du moteur de synthèse.

## Dépendances
Le programme a besoin de la bibliothèque `pyttsx3` pour fonctionner. Assurez-vous donc de l'avoir installée avant d'exécuter le code.

## Instructions
1. Assurez-vous d'avoir la bibliothèque `pyttsx3` installée sur votre système.
2. Copiez le code dans un fichier Python avec une extension `.py`.
3. Exécutez le fichier Python à l'aide de votre interpréteur Python.
4. Une fenêtre d'interface graphique apparaîtra.
5. Entrez le texte que vous souhaitez écouter dans la zone de saisie.
6. Cliquez sur le bouton "Convertir" pour entendre le texte saisi prononcé à voix haute.

Note : Ce programme est conçu pour des utilisations simples et peut être étendu avec des fonctionnalités supplémentaires telles que des options de voix, des contrôles de vitesse de lecture, etc., selon les besoins de l'utilisateur.

# Speech Recognition

Ce code est un programme qui permet d'utiliser la reconnaissance vocale pour écouter l'utilisateur et transcrire ce qu'il dit en texte. Le programme est développé en utilisant la bibliothèque Python `speech_recognition` (ou `speech_recognition`), et il propose une interface graphique réalisée avec `tkinter` pour lancer le processus de reconnaissance vocale.

## Description
Le programme offre la possibilité à l'utilisateur de cliquer sur un bouton intitulé "Start Listening" (Démarrer l'écoute). Une fois le bouton cliqué, le programme active le microphone de l'ordinateur et commence à écouter ce que l'utilisateur dit pendant une période de 20 secondes maximum.

## Fonctionnement
1. L'utilisateur lance l'application en exécutant le code.
2. Une fenêtre d'interface graphique apparaît avec un bouton "Start Listening".
3. Lorsque l'utilisateur clique sur le bouton, le programme commence à écouter l'entrée audio via le microphone.
4. Le programme utilise la bibliothèque `speech_recognition` pour reconnaître la parole de l'utilisateur et la convertir en texte.
5. Si l'écoute est réussie, une boîte de dialogue contextuelle s'affiche avec le texte transcrit.
6. Si aucune parole n'est détectée dans les 20 secondes, une boîte de dialogue d'avertissement s'affiche pour informer l'utilisateur qu'aucune parole n'a été détectée.
7. Si une erreur se produit lors de la reconnaissance vocale, une boîte de dialogue d'erreur s'affiche pour informer l'utilisateur et afficher le message d'erreur spécifique.

## Dépendances
Le programme a besoin de la bibliothèque `speech_recognition` et `tkinter` pour fonctionner. Assurez-vous donc de les avoir installées avant d'exécuter le code.

## Instructions
1. Assurez-vous d'avoir les bibliothèques `speech_recognition` et `tkinter` installées sur votre système.
2. Copiez le code dans un fichier Python avec une extension `.py`.
3. Exécutez le fichier Python à l'aide de votre interpréteur Python.
4. Une fenêtre d'interface graphique apparaîtra.
5. Cliquez sur le bouton "Start Listening".
6. Parlez clairement dans le microphone de votre ordinateur pendant la période d'écoute.
7. Une boîte de dialogue s'affichera avec le texte transcrit à partir de ce qui a été entendu, ou un avertissement s'il n'y a pas eu de détection vocale, ou une boîte de dialogue d'erreur en cas d'erreur lors de la reconnaissance vocale.
