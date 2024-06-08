class DFA:
    def __init__(self, Q, Sigma, delta, q0, F):
        self.Q = Q
        self.Sigma = Sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def run(self, w):
        q = self.q0
        w = w.lower()
        try:
            while w != "":
                q = self.delta[(q, w[0])]
                w = w[1:]
            return q in self.F
        except KeyError:
            return False

# Define DFAs for HTML tags
D_a = DFA({0, 1, 2, 3}, 
          {'<', 'a', '>'}, 
          {(0, "<"): 1, (1, "a"): 2, (2, ">"): 3}, 
          0, 
          {3})
DC_a = DFA({0, 1, 2, 3, 4}, {'<', '/', 'a', '>'}, {(0, "<"): 1, (1, "/"): 2, (2, "a"): 3, (3, ">"): 4}, 0, {4})

D_p = DFA({0, 1, 2, 3}, {'<', 'p', '>'}, {(0, "<"): 1, (1, "p"): 2, (2, ">"): 3}, 0, {3})
DC_p = DFA({0, 1, 2, 3, 4}, {'<', '/', 'p', '>'}, {(0, "<"): 1, (1, "/"): 2, (2, "p"): 3, (3, ">"): 4}, 0, {4})

D_button = DFA({0, 1, 2, 3, 4, 5, 6, 7, 8},
               {'<', 'b', 'u', 't', 'o', 'n', '>'},
               {(0, "<"): 1, (1, "b"): 2, (2, "u"): 3, (3, "t"): 4, (4, "t"): 5, (5, "o"): 6, (6, "n"): 7, (7, ">"): 8},
               0,
               {8})
DC_button = DFA({0, 1, 2, 3, 4, 5, 6, 7, 8, 9},
                {'<', '/', 'b', 'u', 't', 'o', 'n', '>'},
                {(0, "<"): 1, (1, "/"): 2, (2, "b"): 3, (3, "u"): 4, (4, "t"): 5, (5, "t"): 6, (6, "o"): 7, (7, "n"): 8, (8, ">"): 9},
                0,
                {9})

D_div = DFA({0, 1, 2, 3, 4, 5}, {'<', 'd', 'i', 'v', '>'}, {(0, "<"): 1, (1, "d"): 2, (2, "i"): 3, (3, "v"): 4, (4, ">"): 5}, 0, {5})
DC_div = DFA({0, 1, 2, 3, 4, 5, 6}, {'<', '/', 'd', 'i', 'v', '>'}, {(0, "<"): 1, (1, "/"): 2, (2, "d"): 3, (3, "i"): 4, (4, "v"): 5, (5, ">"): 6}, 0, {6})

D_html = DFA({0, 1, 2, 3, 4, 5}, {'<', 'h', 't', 'm', 'l', '>'},
             {(0, "<"): 1, (1, "h"): 2, (2, "t"): 3, (3, "m"): 4, (4, "l"): 5, (5, ">"): 6}, 0, {6})
DC_html = DFA({0, 1, 2, 3, 4, 5, 6}, {'<', '/', 'h', 't', 'm', 'l', '>'},
              {(0, "<"): 1, (1, "/"): 2, (2, "h"): 3, (3, "t"): 4, (4, "m"): 5, (5, "l"): 6, (6, ">"): 7}, 0, {7})

D_body = DFA({0, 1, 2, 3, 4, 5, 6}, {'<', 'b', 'o', 'd', 'y', '>'},
             {(0, "<"): 1, (1, "b"): 2, (2, "o"): 3, (3, "d"): 4, (4, "y"): 5, (5, ">"): 6}, 0, {6})
DC_body = DFA({0, 1, 2, 3, 4, 5, 6, 7}, {'<', '/', 'b', 'o', 'd', 'y', '>'},
              {(0, "<"): 1, (1, "/"): 2, (2, "b"): 3, (3, "o"): 4, (4, "d"): 5, (5, "y"): 6, (6, ">"): 7}, 0, {7})

D_head = DFA({0, 1, 2, 3, 4, 5, 6}, {'<', 'h', 'e', 'a', 'd', '>'}, {(0, '<'): 1, (1, 'h'): 2, (2, 'e'): 3, (3, 'a'): 4, (4, 'd'): 5, (5, '>'): 6}, 0, {6})
DC_head = DFA({0, 1, 2, 3, 4, 5, 6, 7}, {'<', 'h', 'e', 'a', 'd', '>'}, {(0, '<'): 1, (1, '/'): 2, (2, 'h'): 3, (3, 'e'): 4, (4, 'a'): 5, (5, 'd'): 6, (6, '>'): 7}, 0, {7})

D_title = DFA({0, 1, 2, 3, 4, 5, 6, 7}, {'<', 't', 'i', 't', 'l', 'e', '>'}, {(0, '<'): 1, (1, 't'): 2, (2, 'i'): 3, (3, 't'): 4, (4, 'l'): 5, (5, 'e'): 6, (6, '>'): 7}, 0, {7})
DC_title = DFA({0, 1, 2, 3, 4, 5, 6, 7, 8}, {'<', '/', 't', 'i', 't', 'l', 'e', '>'}, {(0, '<'): 1, (1, '/'): 2, (2, 't'): 3, (3, 'i'): 4, (4, 't'): 5, (5, 'l'): 6, (6, 'e'): 7, (7, '>'): 8}, 0, {8})

# Tokenizer function
def tokenize(teks, dfas):
    tokens = []
    i = 0
    while i < len(teks):
        for dfa in dfas:
            token = cek_dfa(dfa, teks[i:])
            if token:
                tokens.append(token)
                i = i + len(token)
                break
        else:
            i += 1
    return tokens

def cek_dfa(dfa, text):
    for length in range(1, len(text) + 1):
        if dfa.run(text[:length]):
            return text[:length]
    return None


def parser(input,parse_table):
    stack = []
    stack.append('#')
    stack.append('S')
    input.append('EOS')
    i = 0
    while stack[-1]!='#':#selama atasnya bukan#
        baca = input[i] #LL(1)
        top = stack.pop()
        if top in parse_table: #kalau non terminal
            if baca in parse_table[top]:#kalau 'baca/symbol' ada di parse table dari produksi non terminal
                produksi = parse_table[top][baca] #produkksinya apa 
                if produksi !='':
                    stack.extend(reversed(produksi.split())) #push hasil produksi, tapi harus kebalik karena stack
            else:
                return False
        else: #jika terminal symbol
            if top ==baca:
                i= i+1 # input maju
            else:
                return False
    top = stack.pop()
    return stack == [] and top == "#"







# Define the grammar and parsing table
grammar = {
    'S': ['<html> A </html>'],
    'A': ['<head> B </head> C','C',''],
    'B': ['<title> </title>', ''],
    'C': ['<body> D </body>'],
    'D': ['<a> E </a> E', '<p> </p> E', '<button> E </button> E', '<div> E </div> E', ''],
    'E': ['D E', '']
}
parse_table = {
    'S': {
        '<html>': '<html> A </html>'
    },
    'A': {
        '<head>': '<head> B </head> C',
        '<body>': 'C',
        '</html>': '',
    },
    'B': {
        '<title>': '<title> </title>',
        '</head>': ''
    },
    'C': {
        '<body>': '<body> D </body>'
    },
    'D': {
        '<a>': '<a> E </a> E',
        '<p>': '<p> </p> E',
        '<button>': '<button> E </button> E',
        '<div>': '<div> E </div> E',
        '</body>': '',
        '</html>': ''
    },
    'E': {
        '<a>': 'D E',
        '<p>': 'D E',
        '<button>': 'D E',
        '<div>': 'D E',
        '</a>': '',
        '</p>': '',
        '</button>': '',
        '</div>': '',
        '</body>': '',
        '</html>': ''
    }
}

# Kumpulan DFA
dfas = [D_html, DC_html, D_body, DC_body, D_a, DC_a, D_p, DC_p, D_button, DC_button, D_div, DC_div, D_head, DC_head, D_title, DC_title]

# Test tokenize sama parser 
html = "<html><body><div><p>Hello</p></div></body></html>"

#tag-tag (html,p,a,div,button,body,head,title)
token_html = tokenize(html,dfas)
print(parser(token_html,parse_table))

#coba inputan file 
def read_html_file(filename):
    with open(filename, 'r') as file:
        html_content = file.read()
    return html_content
masukan = input("masukan file: ")
content = read_html_file(masukan)
tokens = tokenize(content,dfas)
print(tokens)
if parser(tokens,parse_table):
    print("Valid HTML file")
else:
    print("Invalid HTML file")
    
