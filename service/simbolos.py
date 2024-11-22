class TabelaSimbolos:
    def __init__(self):
        self.table = {}

    def insert(self, name, category, type, level):
        if name in self.table:
            return f"Erro: variável '{name}' já foi declarada."
        self.table[name] = {'category': category, 'type': type, 'level': level}
        return "OK"

    def lookup(self, name):
        if name not in self.table:
            return f"Erro: variável '{name}' não foi declarada."
        return self.table[name]

    def remove(self, name):
        if name in self.table:
            del self.table[name]

    def check_scope(self, name, current_level):
        if name not in self.table or self.table[name]['level'] != current_level:
            return f"Erro: variável '{name}' fora do escopo."
        return "OK"

    def get_all_symbols(self):
        return self.table