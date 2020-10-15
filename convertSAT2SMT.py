#coding: utf-8
import sys

def Convert_decl(line, ous):
    decls = line.split()
    nvars = int(decls[2])
    for i in range(nvars):
        ous.write("(declare-const p%d Bool)\n" % (i + 1))

def Convert_clause(line, ous):
    literals = line.split()
    assert (literals[-1] == '0')
    ous.write("(assert (or ")
    for p in literals:
        if p == '0':
           break
        if p[0] == '-':
           ous.write("(not p")
           ous.write(p[1:])
           ous.write(") ")
        else:
           ous.write("p")
           ous.write(p)
           ous.write(" ")
    ous.write("))\n")

def ConvertSATFile(file):
    ins = open(file)
    ous = open("%s.smt2" % file, 'w')
    ous.write("(set-logic QF_BV)\n")
    line = ''
    while True:
      line = ins.readline()
      if line.startswith('p'): break
    Convert_decl(line, ous)
    line = ins.readline()
    while line:
      Convert_clause(line, ous)
      line = ins.readline()
    ous.write("(check-sat)")
    ins.close()
    ous.close()


ConvertSATFile(sys.argv[1])