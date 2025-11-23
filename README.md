# Copilor - A Tiny Language and Compiler (Bonus 10%)

## 📋 Opis projekta

Copilor je kompletan compiler/interpreter za mali programski jezik implementiran u Pythonu. Projekat demonstrira razumijevanje ključnih koncepata compilera: leksička analiza (lexer), sintaksna analiza (parser), i izvršavanje koda (interpreter), kao i generisanje bytecode-a.

## 🏗️ Arhitektura projekta

Projekat je organizovan u nekoliko glavnih komponenti:

```
copilor/
├── basic.py          # Glavni modul: Lexer, Parser, Interpreter
├── codegen.py        # Bytecode code generator
├── bytecode_vm.py    # Virtual Machine za izvršavanje bytecode-a
├── compile_bc.py     # CLI za kompilaciju u bytecode
├── shell.py          # REPL (Read-Eval-Print Loop) konzola
├── test_basic.py     # Unit testovi
├── strings_with_arrows.py  # Pomoćna funkcija za prikaz grešaka
└── examples/         # Primjeri koda
```

### Kako radi kompajler:

1. **Lexer (Leksička analiza)**: 
   - Čita izvorni kod karakter po karakter
   - Grupiše karaktere u tokene (brojevi, stringovi, operatori, keywords)
   - Primjer: `"VAR x = 5"` → `[KEYWORD:VAR, IDENTIFIER:x, EQ, INT:5]`

2. **Parser (Sintaksna analiza)**:
   - Uzima tokene iz lexera
   - Provjerava da li tokeni slijede gramatička pravila
   - Gradi AST (Abstract Syntax Tree) - strukturu podataka koja predstavlja kod
   - Koristi recursive descent parsing

3. **Interpreter (Izvršavanje)**:
   - Obilazi AST koristeći visitor pattern
   - Izvršava naredbe i evaluira izraze
   - Upravlja memorijom kroz symbol table (varijable, funkcije)

4. **Bytecode Compiler + VM**:
   - Prolazi kroz AST i generiše bytecode instrukcije
   - VM izvršava bytecode koristeći stack-based pristup

## Šta projekat uključuje

### Osnovne komponente
- **Lexer (Leksička analiza)**: Pretvara izvorni kod u tokene
- **Parser (Sintaksna analiza)**: Gradi AST (Abstract Syntax Tree) iz tokena koristeći recursive descent parsing
- **Interpreter**: Obilazi AST i izvršava instrukcije koristeći visitor pattern
- **Bytecode Compiler + VM**: Generiše i izvršava jednostavan bytecode

### Jezičke funkcionalnosti
- Varijable, brojevi (int i float), stringovi, liste
- Funkcije (sa arrow syntax i tradicionalnom)
- Kontrolne strukture: IF/ELSEIF/ELSE, FOR, WHILE
- Logički operatori: AND, OR, NOT
- Aritmetički operatori: +, -, *, /, %, ^ (power)

### Originalni feature-i dodati u ovom projektu

1. **Modulo operator (%)**: `VAR x = 10 % 3  // x = 1`

2. **String interpolation**: 
   ```python
   VAR name = "World"
   PRINT("Hello ${name}!")  // Output: Hello World!
   ```

3. **Ternary operator**: 
   ```python
   VAR result = x > 0 ? "positive" : "negative"
   ```

4. **Range operator (..)**: 
   ```python
   VAR list = 1..5  // Creates [1, 2, 3, 4, 5]
   ```

5. **Case-insensitive keywords**: 
   ```python
   var x = 5  // VAR, var, Var sve radi
   ```

6. **Komentari**: Podržava i `#` i `//` stilove komentara

7. **Aliasi za ključne riječi**:
   - `LET` (umjesto `VAR`)
   - `FN` (umjesto `FUN`)
   - `ELSEIF` (umjesto `ELIF`)

8. **Builtin aliasi**:
   - `ECHO` (umjesto `PRINT`)
   - `LENGTH` (umjesto `LEN`)
   - `PI` (umjesto `MATH_PI`)

9. **Dodatne builtin funkcije**:
   - `ABS(value)` - apsolutna vrijednost
   - `MIN(a, b)` - minimum od dva broja
   - `MAX(a, b)` - maksimum od dva broja
   - `ROUND(value)` - zaokruživanje
   - `SQRT(value)` - kvadratni korijen
   - `FLOOR(value)` - zaokružuje na manji cijeli broj
   - `CEIL(value)` - zaokružuje na veći cijeli broj

10. **Bytecode compiler i VM**: Demonstracija code generation sa jednostavnom stack-based VM

11. **Unit testovi**: Kompletan set testova koji provjeravaju sve funkcionalnosti

## 🚀 Kako pokrenuti

### 1. REPL (Interactive Shell)
```bash
python shell.py
```
Zatim možete pisati kod direktno:
```
basic > VAR x = 5
basic > PRINT(x + 3)
8
```

### 2. Pokretanje fajla
```bash
python shell.py
```
U REPL-u:
```
basic > RUN("test_all.myopl")
```

### 3. Kompilacija u bytecode
```bash
python compile_bc.py examples/example_bc.myopl
```

### 4. Pokretanje unit testova
```bash
python test_basic.py
```

## Primjeri koda

### Osnovne operacije
```python
VAR x = 5
VAR y = 3
PRINT(x + y)  // Output: 8
```

### Modulo operator
```python
LET x = 10 % 3
ECHO(x)  // Output: 1
```

### String interpolation
```python
VAR name = "Copilor"
VAR num = 42
PRINT("Hello ${name}! Answer: ${num}")  // Output: Hello Copilor! Answer: 42
```

### Ternary operator
```python
VAR x = 5
VAR result = x > 0 ? "positive" : "negative"
PRINT(result)  // Output: positive
```

### Range operator
```python
VAR list = 1..5
PRINT(list)  // Output: [1, 2, 3, 4, 5]
```

### Arrow functions
```python
FN add(a, b) -> a + b
PRINT(add(2, 3))  // Output: 5
```

### Kontrolne strukture
```python
IF x > 0 THEN
    PRINT("positive")
ELSEIF x == 0 THEN
    PRINT("zero")
ELSE
    PRINT("negative")
END
```

### Dodatne builtin funkcije
```python
PRINT(ABS(-10))      // Output: 10
PRINT(MIN(5, 9))      // Output: 5
PRINT(MAX(5, 9))      // Output: 9
PRINT(ROUND(3.7))     // Output: 4
PRINT(SQRT(16))       // Output: 4.0
PRINT(FLOOR(3.9))     // Output: 3
PRINT(CEIL(3.1))      // Output: 4
```

### Kompleksniji primjer
Pogledaj `examples/complex_example.myopl` za kompletan primjer koji koristi sve funkcionalnosti.

### Case-insensitive keywords
```python
var test = "works"     // VAR, var, Var sve radi
PRINT(test)
```

## 🔧 Kako radi (kratak pregled)

1. **Lexer** pretvara tekst u tokene (sa podrškom za `${}` interpolaciju)
2. **Parser** gradi AST (abstract syntax tree) sa ternary operatorom
3. **Interpreter** obilazi AST i izvršava (sa novim builtin funkcijama)
4. **Codegen** prolazi kroz AST i emituje jednostavan bytecode koji izvršava mala stack-VM

## 📊 Testiranje

### Unit testovi
```bash
python test_basic.py
```

### Kompletan test suite
```bash
python shell.py
basic > RUN("test_all.myopl")
```




1. **String interpolation** - napredna funkcionalnost koja zahtijeva parsiranje izraza unutar stringa
2. **Ternary operator** - kompletan parser i evaluator implementiran
3. **Range operator** - originalna sintaksa za kreiranje lista
4. **Bytecode compiler** - pokazuje razumijevanje code generation koncepata
5. **Unit testovi** - pokazuje da razumijem kod i mogu ga testirati
6. **Dokumentacija** - detaljno objašnjenje arhitekture i kako sve radi


