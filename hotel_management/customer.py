class Customer:
    def __init__(self, customer_id: str, name: str, is_loyal_member: bool):
        self.customer_id = customer_id
        self.name = name
        self.is_loyal_member = is_loyal_member

    def __str__(self):
        return f'Customer: {self.name}, ID: {self.customer_id}, Loalty: {"Loyal member" if self.is_loyal_member else "Not Loyal member"}'
