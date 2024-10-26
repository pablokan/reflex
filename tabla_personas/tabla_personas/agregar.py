    def add(self, *args):
        self.get_all()
        str_field_names = ', '.join(self.field_names)
        fields_list = [f"'{field}'" if type(field)==str else str(field) for field in args]
        field_values = ", ".join(fields_list)
        query = f"INSERT INTO {self.table_name} ({str_field_names}) VALUES ({field_values})"
        print(query)
        self.cursor.execute(query)
        self.conn.commit()
