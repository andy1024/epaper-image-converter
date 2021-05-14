import re, ast

def read_consts(contents):
    constants = {}
    CONST_PATTERN=r'const unsigned char\s+(\w+)\[\d+\]\s+PROGMEM\s*=\s*{(.+?)}'
    REMOVE_COMMENTS=r'''/(?:\/\/(?:\\\n|[^\n])*\n)|(?:\/\*[\s\S]*?\*\/)|((?:R"([^(\\\s]{0,16})\([^)]*\)\2")|(?:@"[^"]*?")|(?:"(?:\?\?'|\\\\|\\"|\\\n|[^"])*?")|(?:'(?:\\\\|\\'|\\\n|[^'])*?'))/g'''
    contents = re.sub(REMOVE_COMMENTS, '', contents)
    for elem in re.split(';', contents):
        for name, value in re.findall(CONST_PATTERN, elem, flags=re.MULTILINE | re.DOTALL):
            value = '[' + value + ']'
            constants[name] = ast.literal_eval(value)
    return constants
