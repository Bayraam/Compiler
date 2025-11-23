import sys
from pathlib import Path
from codegen import Codegen
from bytecode_vm import BytecodeVM


def main():
  if len(sys.argv) < 2:
    print('Usage: python compile_bc.py <file.myopl>')
    sys.exit(1)
  path = Path(sys.argv[1])
  text = path.read_text(encoding='utf-8')
  cg = Codegen()
  code, err = cg.compile(str(path), text)
  if err:
    print(err.as_string())
    sys.exit(2)
  # Print bytecode for inspection
  for i, (op, arg) in enumerate(code):
    if arg is None:
      print(f"{i:03}: {op}")
    else:
      print(f"{i:03}: {op} {arg}")
  # Execute
  print('--- VM OUTPUT ---')
  vm = BytecodeVM(code)
  vm.run()


if __name__ == '__main__':
  main()


