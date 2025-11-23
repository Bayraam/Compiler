COPILOR - Kompajler projekat za bonus 10%

Autor: Harun
Datum: [23.11.2025

OPIS PROJEKTA:
-------------
Ovo je kompletan compiler/interpreter za mali programski jezik implementiran u Pythonu.
Projekat demonstrira razumijevanje ključnih koncepata compilera:
- Lexer (leksička analiza) - pretvara kod u tokene
- Parser (sintaksna analiza) - gradi AST (Abstract Syntax Tree)
- Interpreter (izvršavanje koda) - izvršava AST koristeći visitor pattern
- Bytecode compiler + VM - generiše i izvršava bytecode

UNIQUE FEATURE-E KOJE SAM DODAO:
--------------------------------
1. Modulo operator (%)
2. String interpolation sa ${} sintaksom (napredna funkcionalnost)
3. Ternary operator (condition ? true_val : false_val)
4. Range operator (..) - npr. 1..5 kreira listu [1,2,3,4,5]
5. // komentari (pored #)
6. Case-insensitive keywords (VAR, var, Var sve radi)
7. Aliasi: LET (VAR), FN (FUN), ELSEIF (ELIF)
8. Builtin aliasi: ECHO (PRINT), LENGTH (LEN), PI (MATH_PI)
9. Dodatne builtin funkcije: ABS, MIN, MAX, ROUND, SQRT, FLOOR, CEIL
10. Bytecode compiler i VM za code generation
11. Unit testovi (test_basic.py) - pokazuju razumijevanje koda
12. Detaljni komentari u kodu - objašnjavaju kako radi svaki dio

KAKO POKRENUTI:
--------------
1. Raspakuj ZIP fajl
2. Otvori terminal u folderu
3. Pokreni: python shell.py
4. U REPL-u: RUN("test_all.myopl") - za testove

ILI direktno:
- python test_basic.py - za unit testove
- python compile_bc.py examples/example_bc.myopl - za bytecode demo

Detaljnije uputstvo: UPUTSTVO.txt i KAKO_TESTIRATI.md

FAJLOVI:
-------
- basic.py - glavni kod (lexer, parser, interpreter) sa detaljnim komentarima
- shell.py - REPL konzola
- compile_bc.py, bytecode_vm.py, codegen.py - bytecode compiler sa komentarima
- test_basic.py - unit testovi (pokazuju razumijevanje)
- test_all.myopl - kompletan test svih funkcionalnosti
- examples/ - primjeri koda (uključujući complex_example.myopl)
- README.md - detaljna dokumentacija sa arhitekturom
- KAKO_TESTIRATI.md - vodič za testiranje
- strings_with_arrows.py - pomoćna funkcija za prikaz grešaka

TESTIRANJE:
----------
✅ Unit testovi: python test_basic.py (svi prolaze)
✅ Funkcionalni testovi: RUN("test_all.myopl") (svi prolaze)
✅ Bytecode testovi: python compile_bc.py examples/example_bc.myopl

Svi testovi prolaze uspješno!



