    def obtenerUsuarios(self):
        #fields_def = ['item TEXT', 'qty INTEGER', 'price REAL', 'pic TEXT']
        #d = Database('tienda', *fields_def)
        d = Database('tienda')
        self.cabecera = d.field_names
        self.gente = d.get_all()
