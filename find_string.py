"""
ejecutar la aplicación de consola"FINDSTR" y buscar sobre un archivo "test.txt"
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
    print(result)
    return result

def testEstoNoEs(text, filepath): #This test cases verifies that "esto no es" isn't present in a text file
    result = "PASS" if retFileContent(text, filepath) == 1 else "FAILED"
    print(result)
    return result
################################################################################
def suiteEsto():
    tcList = []
    tcList.append(testEstoEs("esto es", "test.txt"))
    tc_list.append(testEstoNoEs("esto no es", "test.txt"))
