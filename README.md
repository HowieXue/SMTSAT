# SMTSAT 

SMT/SAT smt2/cnf converter

针对 SMT（Satisfiability Modulo Theories）和SAT （Boolean Satisfiability Problem）中，经常需要使用不同 的SAT和SMT solver (求解器)，这时候会经常有需求将SAT与SMT case文件互转。

所以写了python脚本自动化实现该功能。

- 需要注意的是， SAT只能与Bit-Vector的SMT相互转换，而针对int等则不能正确转换，这也是为什么有SMT的原因

Use case:

- python convertSAT2SMT.py bitvector_case2.cnf



- python convertSMT2SAT.py bitvecor_case2.smt2
