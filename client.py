import query


class Client:
    def __init__(self, data):
        self.name = data[0]
        self.phone = data[1]
        self.city = data[2]
        self.company = data[3]

    def insert(self):
        query.insert(f"""INSERT INTO contacts (name, phone, city, company) VALUES ('{self.name}', '{self.phone}', '{self.city}', '{self.company}');""")
