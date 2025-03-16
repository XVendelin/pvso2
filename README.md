Dokumentacia:

1.)
Upravili sme si program z prvého zadania aby sme mohli vyhotoviť viacero fotografií. Následne sme nasnímali 10 fotografií šachovnice s rozmerom 7x5 políčok. Šachovnicu sme rôzne natáčali, odďaľovali a približovalin aby sme dosiahli čo najväčšiu rôznorodosť snímok. (Na správnu kalibráciu nebolo potrebných veľa obrázkov, stačilo ich aj 10. Dôležitá bola ich rôznorodosť a taktiež aby šachovnica zaberala vačšiu časť obrázka.)

2.)
Kameru je nutné nakalibrovať pretože môže nastať skreslenie. Tj napr. rovné čiary sa na krajoch obrázka môžu javiť ako zakrivené alebo niektoré oblasti na obrázku sa môžu javiť bližšie ako v skutočnosti sú. (Ide o radiálne  a tangenciálne skreslenie.
Preto je potrebné nájsť koeficienty skreslania a parametre kamery (vnútorné a vonkajšie).
Vnútorné:
Sú špecifické pre konkrétnu kameru (ohnisková vzdialenosť a stred snímky). Program v návode nám umožnil vyhlaďať tieto neznáme parametre a následne vytvoriť 3x3 maticu vnútorných parametrov (uložená na GitHube ako textový dokument).

![image](https://github.com/user-attachments/assets/6e5ff4e5-dfc9-4250-b020-ffc89d50316d)
  
	ohnisková vzdialenosť - fx,fy
	stred snímky - cx,cy

Vonkajšie:
Predstavujú rotačné a translačné vektory, ktoré umožňujú transformáciu súradníc bodu v 3D priestore na súradnice v obrazovom systéme.

![image](https://github.com/user-attachments/assets/d83cced9-a4ae-473b-bc8e-3c498e6b500e)

	– r - rotácia kamery
 	– t - translácia kamery
Kalibrácia sa musí vykonať na obrázkoch v šedých odtieňpch preto sme museli farebné obrázky zmeniť na čiernobiele. Spravili sme kalibráciu a výsledkom kalibrácie boli nasledujúce paramete:

	- mtx - matica vnútorných parametrov
	- dist - distortion coefficients
	- rvecs, tvecs - rotačné a translačné vektory

Tieto parametre sme si uložili do textového súboru.

3.)
Vytvorili sme program na detekciu kružníc používajúci Houghovu transformáciu, ktorý kontinuálne sníma obraz.
V obraze používame slidre na úpravu parametrov, umožňujú dynamickú zmenu parametrov detekcie kruhov:

	param1 – Prvý parameter Houghovho detekčného algoritmu (prah pre detekciu hrán)
	param2 – Druhý parameter Houghovho detekčného algoritmu (prah pre rozhodnutie, či nájdený kruh je platný)
	radius – Minimálny polomer detegovaných kruhov
	switch – Prepínač na zapnutie/vypnutie detekcie (ON/OFF)

Náš program beži v nekonečnej slučke až do momentu kedy je stlačený medzerník (vtedy sa vypne)
	
 	1) Program získava obrázok z kamery
	2) Spracuje ho:
 		uráví jeho veľkosť
		Prevedie ho na odtiene šedej
		Použije median blur na redukciu šumu
	3) Získa aktuálne nastavené hodnoty sliderov
	4) Ak je switch (ON) zapnutý, vykoná detekciu kruhov pomocou cv.HoughCircles()
 
 Výsledný obrázok s kruhmi (+ stred a polomer) sa zobrazí v okne. Obrázok je na rozdiel od odtieňov šedej zobrazovaný v RGB

4.) Vytvorli sme si GitHub repozitár a do neho nahrali obrázky a program.
