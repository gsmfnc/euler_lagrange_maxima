import sys
import subprocess

def generateMainScript(path):
    mainScript = open("main_script.mac", "w")

    mainScript.write('reset()$\n')
    mainScript.write('clear(all)$\n')
    mainScript.write('kill(all)$\n')
    mainScript.write('batch("funzioni.mac")$\n')
    mainScript.write('batch("matrici_trasformazione.mac")$\n')
    mainScript.write('batch("calcolo_energia.mac")$\n')
    mainScript.write('batch("unit_test.mac")$\n')
    mainScript.write('\n\n\n')
    mainScript.write('"\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n'
        +
        'INIZIO SCRIPT DI TEST\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        +
        '\n\n\n"$')
    mainScript.write('\n\n\n')
    mainScript.write('batch("' + path + '")$')

    mainScript.close()

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing argument. (script filepath)")
    else:
        generateMainScript(sys.argv[1])
