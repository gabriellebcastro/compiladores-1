import re

#formato desejado de token: <TIPO, VALOR>
#"if (x > 0) { y = x + 1; } else { y = x - 1; }"
"""int main() {
    if (x > 0) {
        return x;
    } else {
        return -1;
    }
}"""
script = """
x = 1;
print (x)
"""

types = [
    ('IF', re.compile(r'if')),
    ('ELSE', re.compile(r'else')),
    ('SOMA', re.compile(r'\+')),
    ('SUB', re.compile(r'-')),
    ('MUL', re.compile(r'\*')),
    ('DIV', re.compile(r'/')),
    ('ID', re.compile(r'[a-zA-Z][a-zA-Z0-9_]*')),
    ('NUM_INT', re.compile(r'[0-9]+')),
    ('ATRIB', re.compile(r'=')),
    ('LPAREN', re.compile(r'\(')),
    ('RPAREN', re.compile(r'\)')),
    ('EQUAL', re.compile(r'==')),
    ('PRINT', re.compile(r'print')),
    ('NEWLINE', re.compile(r'\n')),
    ('RIGHT', re.compile(r'{')),
    ('LEFT', re.compile(r'}')),
]

def lexer(script):
    num = 0

    while num < len(script):
        match = None
        for token, regex in types:
            match = regex.match(script, num)
            if match:  # Caracter reconhecido
                valor = match.group(0)
                num = match.end()

                print_token(token, valor)
                break

        if not match:  # Erro léxico
            if script[num] == " ":
                num += 1
            else:
                raise ValueError(f"Erro léxico: Caractere desconhecido ->", {script[num]})

print('Formato: <TIPO, VALOR>')
def print_token(token, value):
    print(f'<type: {token}, value: {value}> \n')

lexer(script)