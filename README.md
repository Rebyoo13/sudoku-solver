# Sudoku Solver 

Un proiect Python care rezolva automat Sudoku folosind backtracking.  
Include doua variante: `rows_col.py` (rezolvare in consola) si `autogui.py` (scrie automat solutia intr-o aplicatie externa).  

Demo:  
![Sudoku Screenshot](ss3.png)  

Link to project: [https://github.com/Rebyoo13/sudoku-solver](https://github.com/Rebyoo13/sudoku-solver)

---

## How It's Made
- Algoritm de backtracking pentru rezolvarea Sudoku.  
- Functia `possible(x, y, n)` verifica regulile Sudoku (linie, coloana, patrat 3x3).  
- `rows_col.py` afiseaza solutia in consola.  
- `autogui.py` scrie solutia automat folosind PyAutoGUI.  

---

## Usage

### 1. Rezolvare in consola
```bash
python rows_col.py
````

* Introdu fiecare rand al Sudoku ca un sir de 9 cifre.
* Foloseste `0` pentru celulele goale.
* Exemplu pentru un rand:

```
040000000
```

* Dupa ce ai introdus toate cele 9 randuri, scriptul va calcula solutia si o va afisa in consola.

### 2. Rezolvare cu scriere automata

```bash
python autogui.py
```

* Deschide Sudoku.com sau orice alta aplicatie Sudoku unde vrei sa scrii solutia.
* Asigura-te ca celula din stanga sus este selectata (cursorul activ).
* Introdu randurile unul cate unul (ex: `040000000`).
* Dupa 9 randuri, scriptul va calcula solutia si o va scrie automat in aplicatie, apasand tastele corespunzatoare si navigand intre celule.

> ⚠️ Atentie: Inainte de a rula `autogui.py`, nu folosi mouse-ul sau tastatura in timp ce scriptul scrie solutia, altfel poate da gres.

---

## Lessons Learned

* Intelegerea algoritmului de backtracking.
* Automatizarea tastaturii si mouse-ului cu PyAutoGUI.
* Structurarea unui proiect Python si creare README clar si profesional.

Rebyoo13 – [rebecadinu13@yahoo.com](mailto:rebecadinu13@yahoo.com)
Project Link: [https://github.com/Rebyoo13/sudoku-solver](https://github.com/Rebyoo13/sudoku-solver)

````
