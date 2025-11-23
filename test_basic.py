"""
Unit testovi za Copilor compiler/interpreter.
Testiraju sve glavne funkcionalnosti jezika.
"""

import basic
import sys

def test_lexer():
    """Testira leksičku analizu (tokenizaciju)."""
    print("=== TEST: Lexer ===")
    
    # Test osnovnih tokena
    text = "VAR x = 5 + 3"
    lexer = basic.Lexer("<test>", text)
    tokens, error = lexer.make_tokens()
    
    assert error is None, f"Lexer greška: {error}"
    assert len(tokens) > 0, "Nema tokena"
    print("✅ Lexer radi")
    
def test_parser():
    """Testira sintaksnu analizu (parsing)."""
    print("=== TEST: Parser ===")
    
    text = "VAR x = 5 + 3"
    lexer = basic.Lexer("<test>", text)
    tokens, error = lexer.make_tokens()
    assert error is None
    
    parser = basic.Parser(tokens)
    ast = parser.parse()
    
    assert ast.error is None, f"Parser greška: {ast.error}"
    assert ast.node is not None, "AST je prazan"
    print("✅ Parser radi")
    
def test_interpreter():
    """Testira izvršavanje koda."""
    print("=== TEST: Interpreter ===")
    
    # Test osnovnih operacija
    result, error = basic.run("<test>", "VAR x = 5 + 3")
    assert error is None, f"Interpreter greška: {error}"
    print("✅ Interpreter radi")
    
def test_modulo():
    """Testira modulo operator."""
    print("=== TEST: Modulo operator ===")
    
    result, error = basic.run("<test>", "VAR x = 10 % 3")
    assert error is None
    assert result.elements[0].value == 1, f"Očekivano 1, dobijeno {result.elements[0].value}"
    print("✅ Modulo operator radi")
    
def test_string_interpolation():
    """Testira string interpolaciju."""
    print("=== TEST: String interpolation ===")
    
    result, error = basic.run("<test>", 'VAR name = "World"; VAR msg = "Hello ${name}!"')
    assert error is None
    print("✅ String interpolation radi")
    
def test_ternary():
    """Testira ternary operator."""
    print("=== TEST: Ternary operator ===")
    
    result, error = basic.run("<test>", 'VAR x = 5 > 3 ? "yes" : "no"')
    assert error is None
    assert result.elements[0].value == "yes", f"Očekivano 'yes', dobijeno {result.elements[0].value}"
    print("✅ Ternary operator radi")
    
def test_range():
    """Testira range operator."""
    print("=== TEST: Range operator ===")
    
    result, error = basic.run("<test>", "VAR list = 1..5")
    assert error is None
    assert len(result.elements[0].elements) == 5, "Lista treba imati 5 elemenata"
    print("✅ Range operator radi")
    
def test_aliases():
    """Testira alias-e za ključne riječi."""
    print("=== TEST: Aliases ===")
    
    result, error = basic.run("<test>", "LET x = 5; FN add(a, b) -> a + b; VAR sum = add(2, 3)")
    assert error is None
    print("✅ Aliases rade")
    
def test_builtin_functions():
    """Testira dodatne builtin funkcije."""
    print("=== TEST: Builtin funkcije ===")
    
    result, error = basic.run("<test>", "VAR x = ABS(-10); VAR y = MIN(5, 9); VAR z = MAX(5, 9); VAR w = ROUND(3.7)")
    assert error is None
    assert result.elements[0].value == 10, "ABS(-10) treba biti 10"
    assert result.elements[1].value == 5, "MIN(5, 9) treba biti 5"
    assert result.elements[2].value == 9, "MAX(5, 9) treba biti 9"
    assert result.elements[3].value == 4, "ROUND(3.7) treba biti 4"
    print("✅ Osnovne builtin funkcije rade")
    
    # Test nove funkcije
    result2, error2 = basic.run("<test>", "VAR s = SQRT(16); VAR f = FLOOR(3.9); VAR c = CEIL(3.1)")
    assert error2 is None
    assert abs(result2.elements[0].value - 4.0) < 0.001, "SQRT(16) treba biti 4.0"
    assert result2.elements[1].value == 3, "FLOOR(3.9) treba biti 3"
    assert result2.elements[2].value == 4, "CEIL(3.1) treba biti 4"
    print("✅ Nove builtin funkcije (SQRT, FLOOR, CEIL) rade")
    
def test_case_insensitive():
    """Testira case-insensitive keywords."""
    print("=== TEST: Case-insensitive keywords ===")
    
    result, error = basic.run("<test>", "var x = 5; VAR y = 10")
    assert error is None
    print("✅ Case-insensitive keywords rade")
    
def run_all_tests():
    """Pokreće sve testove."""
    print("\n" + "="*50)
    print("POKRETANJE UNIT TESTOVA")
    print("="*50 + "\n")
    
    tests = [
        test_lexer,
        test_parser,
        test_interpreter,
        test_modulo,
        test_string_interpolation,
        test_ternary,
        test_range,
        test_aliases,
        test_builtin_functions,
        test_case_insensitive,
    ]
    
    print(f"Ukupno testova: {len(tests)}\n")
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ Test neuspješan: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Greška u testu: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"REZULTATI: {passed} uspješno, {failed} neuspješno")
    print("="*50 + "\n")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

