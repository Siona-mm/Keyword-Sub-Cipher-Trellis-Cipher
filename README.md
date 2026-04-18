# Trellis Cipher & Keyword Substitution Cipher


## Përshkrimi i Projektit

Projekti përmban dy metoda të pavarura enkriptimi/dekriptimi:

1. Trellis Cipher – një cipher bllok bazuar në një strukturë matricore 4x4 me mbushje alternative.
2. Keyword Substitution Cipher – një cipher zëvendësimi që përdor një fjalë-kyçe për të riorganizuar alfabetin (shkronja + numra).

Programi merr input nga përdoruesi, enkripton tekstin dhe pastaj e dekripton për të verifikuar korrektësinë.



## Detaje të Algoritmeve

### 1. Trellis Cipher (Bllok 4x4)

Përshkrimi:
Ky algoritëm punon duke ndarë tekstin në blloqe të madhësisë 16 karakteresh. Çdo bllok vendoset në një matricë 4x4 sipas një modeli "trellis" (rrjetë).

Si funksionon enkriptimi:
- Teksti konvertohet në uppercase dhe hapësirat zëvendësohen me `X`.
- Ndahen në blloqe à 16 karaktere (padding automatik nëse është e nevojshme).
- Në matricën 4x4:
  - Fillimisht mbushen pozitat çift (`(i + j) % 2 == 0`)
  - Pastaj mbushen pozitat tek (`(i + j) % 2 == 1`)
- Qelizat e mbetura plotësohen me `X`.
- Matrica lexohet rresht pas rreshti për të formuar ciphertext-in.

Si funksionon dekriptimi:
- Ndërtohet përsëri matrica 4x4 nga ciphertext-i.
- Lexohen fillimisht pozitat çift, pastaj pozitat tek.
- Në fund `X`-at zëvendësohen me hapësira.



### 2. Keyword Substitution Cipher (me shkronja + numra)

Përshkrimi:
Ky është një cipher monoalfabetik zëvendësimi i përmirësuar. Alfabeti origjinal (`A-Z` + `0-9`) riorganizohet duke përdorur një `keyword`.

Si funksionon:
- Keyword-i pastrohet nga përsëritjet dhe kthehet në uppercase.
- Ndërtohet çelësi i ri: `keyword + remaining letters/numbers`.
- Çdo karakter në tekst zëvendësohet me karakterin që ndodhet në të njëjtin pozicion në çelësin e ri.
- Dekriptimi bën procesin e kundërt duke përdorur pozicionin në çelës për të gjetur karakterin origjinal.

Shembull i çelësit:
- Keyword = `PYTHON`
- Çelësi = `PYTHONABCDEF...` (pa përsëritje + numrat në fund)


# Struktura e Projektit

- `KeyWordSubCipher.py` - Përmban logjikën e enkriptimit dhe dekriptimit të KeyWordSub.
- `TrellisCipher.py` - Përmban logjikën e enkriptimit dhe dekriptimit të Trellis.
- `README.md` - Dokumentacioni i plotë i projektit.


## Si të Ekzekutohet Programi

1. Hapni folderin ku ndodhet skripta.
2. Klikoni me të djathtin mbi file-in Python.
3. Zgjedhni "Run with Python" ose "Run Python File" 


### Kushtet Paraprake

Për të ekzekutuar këtë projekt, ju nevojitet:
- Python 3.7 ose më i ri.
- Nuk nevojiten librari të jashtme (Standard Library only).
   
