# KAKO PROVJERITI DA LI COPILOR RADI

## Brzi test (1 minuta)

1. Otvori terminal u folderu `compilor`
2. Pokreni: `python shell.py`
3. Upiši: `RUN("test_all.myopl")`
4. Trebao bi vidjeti sve testove kako prolaze

## Detaljniji testovi

### Test 1: Osnovna funkcionalnost
```
python shell.py
> RUN("venv/example.myopl")
```
Trebao bi vidjeti: "Greetings universe!" i "loop, spoop" 5 puta

### Test 2: Modulo operator
```
python shell.py
> LET x = 10 % 3
> PRINT(x)
```
Trebao bi vidjeti: 1

### Test 3: String interpolation
```
python shell.py
> VAR name = "world"
> PRINT("Hello ${name}!")
```
Trebao bi vidjeti: Hello world!

### Test 4: Novi builtin-ovi
```
python shell.py
> PRINT(ABS(-5))
> PRINT(MIN(3, 7))
> PRINT(MAX(3, 7))
```
Trebao bi vidjeti: 5, 3, 7

### Test 5: Bytecode compiler
```
python compile_bc.py examples/example_bc.myopl
```
Trebao bi vidjeti bytecode i rezultate: 7, 1, hello bytecode

## Sve testove odjednom
```
python shell.py
> RUN("test_all.myopl")
```

## Ako nešto ne radi
- Provjeri da li si u pravom folderu (compilor/)
- Provjeri da li imaš Python instaliran
- Provjeri da li fajlovi postoje (test_all.myopl, examples/, itd.)

