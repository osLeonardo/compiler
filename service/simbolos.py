class TabelaSimbolos:
    def __init__(self):
        self.table = {}

    def insert(self, name, category, type, level):
        if name in self.table:
            return f"Erro: identificador '{name}' já foi declarado como {self.table[name]['category']}."
        self.table[name] = {'category': category, 'type': type, 'level': level}
        return "OK"

    def lookup(self, name):
        if name not in self.table:
            return f"Erro: identificador '{name}' não foi declarado."
        return self.table[name]

    def remove(self, name):
        if name in self.table:
            del self.table[name]

    def check_scope(self, name, current_level):
        if name not in self.table or self.table[name]['level'] != current_level:
            return f"Erro: identificador '{name}' fora do escopo."
        return "OK"

    def get_all_symbols(self):
        return self.table