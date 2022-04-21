# PARTE 1: TOKENIZAR LA ENTRADA USANDO LEX
import ply.lex as lex
#pip install ply  #pip3 

# Paso 1: Proporcione una lista de tokens que defina
# todos los posibles nombres de token que puede producir
# el lexer.
# La lista de tokens también es utilizada YACC
# para identificar terminales.

tokens = (
   'NUMBER',
   'PLUS',
   'TIMES',
   'LPAREN',
   'RPAREN',
   'MINUS',
   'DIVIDE'
)

# Paso 2. Cada token se especifica escribiendo una regla
# de expresión regular, mediante declaraciones que usan
# un prefijo especial *t_* para indicar que define un token.

# Definición de tokens simples:

t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MINUS = r'\-'
t_DIVIDE = r'\/'

#MINUS, DIVIDE

# Definición de tokens que incluye código para
# complementar, por ejemplo, para la definición de número,
# se incluye su conversión a entero (para este caso):

def t_NUMBER(t):
    r'\d+' #\d equivalente a [0-9]
    t.value = int(t.value)
    return t


# Para incluir caracteres que hay que ignorar, en este caso,
# tabuladores y espacios.
t_ignore  = ' \t'


# Para el manejo de errores en las entradas
def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)


# Paso 3. Crear el objeto tipo lex (el tokenizador)
lexer = lex.lex()


# Hasta aquí se requiere sólo para tokenizar antes del parseo.
# En adelante, es para validar lo aquí incluido para tokenizar

# Paso 4. Definir o solicitar la entrada al usuario
# Se define una cadena de entrada, para este ejemplo.
# data puede ser una cadena obtenida de un archivo o directamente
# dada por un usuario desde la línea de comandos.
##
data = '4 / 2'
##
### Paso 5. Usar el objeto tipo lex para tokenizar la entrada
### Hacer que el objeto tipo lex identifique en la cadena de
### entrada los tokens definidos.
##
lexer.input(data)
##
### los tokens quedan en la variable lexer de tipo objeto Lexer,
### y se puede acceder a esos elementos de la siguiente manera:
##
print(lexer)
for tok in lexer:
    print(tok)

# La salida de cada tok tiene el siguiente formato:
# LexToken(type of token, token, line number, position)
