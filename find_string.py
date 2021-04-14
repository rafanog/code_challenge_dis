"""
Ejecutar la aplicación de consola"FINDSTR" y buscar sobre un archivo "test.txt"
que tenga como contenido "esto es un archivo de ejemplo" estos dos strings:
"esto es" y "esto no es".
El resultado deberia ser algo como:
Test 1:
"esto es"        - esta presente en el archivo. PASS
Test 2:
"esto no es"  - no esta presente en el archivo. PASS
Success. Test 2/2 Ok.
"""
import os

def retFileContent(text, filepath): #This executes the findstr shell command
    return os.system("echo off && FINDSTR /C:\"{}\" {} > nul".format(text, filepath))
################################################################################
def testEstoEs(text, filepath): # This test case verifies that "esto es" is present in a text file
    result = "PASS" if retFileContent(text, filepath) == 0 else "FAILED"
    print("Test 1: \n\"esto es\"        - esta presente en el archivo. {}".format(result))
    return result

def testEstoNoEs(text, filepath): #This test cases verifies that "esto no es" isn't present in a text file
    result = "PASS" if retFileContent(text, filepath) == 1 else "FAILED"
    print("Test 1: \n\"esto no es\"        - no esta presente en el archivo. {}".format(result))
    return result
################################################################################
def suiteEsto():
    tcList = []
    tcPassed = 0
    tcFailed = 0
    counter = 0

    tcList.append(testEstoEs("esto es", "test.txt"))
    tcList.append(testEstoNoEs("esto no es", "test.txt"))

    for t in tcList:
        if tcList[counter] == "PASS":
            tcPassed += 1
        else:
            tcFailed += 1

        counter += 1

    if tcFailed > 0:
        print("Failed Tests {}/{} ERROR.".format(tcFailed, len(tcList)))

    print("Success Tests {}/{} OK".format(tcPassed, len(tcList)))
################################################################################

suiteEsto()
