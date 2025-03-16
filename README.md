Dokumentacia:

1.)
Upravili sme si program z prvého zadania aby sme mohli vyhotoviť viacero fotografií. Následne sme nasnímali 10 fotografií šachovnice s rozmerom 7x5 políčok. Šachovnicu sme rôzne natáčali, odďaľovali a približovalin aby sme dosiahli čo najväčšiu rôznorodosť snímok. (Na správnu kalibráciu nebolo potrebných veľa obrázkov, stačilo ich aj 10. Dôležitá bola ich rôznorodosť a taktiež aby šachovnica zaberala vačšiu časť obrázka.)

2.)
Kameru je nutné nakalibrovať pretože môže nastať skreslenie. Tj napr. rovné čiary sa na krajoch obrázka môžu javiť ako zakrivené alebo niektoré oblasti na obrázku sa môžu javiť bližšie ako v skutočnosti sú. (Ide o radiálne  a tangenciálne skreslenie.
Preto je potrebné nájsť koeficienty skreslania a parametre kamery (vnútorné a vonkajšie).
Vnútorné:
Sú špecifické pre konkrétnu kameru (ohnisková vzdialenosť a optické centrá).
![image](https://github.com/user-attachments/assets/6e5ff4e5-dfc9-4250-b020-ffc89d50316d)


V zadaní nám bol poskytnutý návod na kalibráciu kamery. Do neho sme si zadali rozmery našej šachovnice a spustili ho.
Program nám vypísal maticu vnútorných parametrov a tak sme zistili fx,fy,cx,cy.

2.)
Vytvorili sme program na detekciu kružníc, ktorý kontinuálne sníma obraz.
V obraze používame slidre na úpravu parametrov pre detekciu hrán, minima detegovaných hrán, minimálneho a maximálneho polomeru vypísaných kružníc na obrázku.
Kružnice sa detegujú na grayscale obraze a vypisujú na RGB obrázok.
Pridali sme vypisovanie polomeru vykreslených kružníc na obrázku.

3.) Vytvorli sme si GitHub repozitár a do neho nahrali obrázky a program.
