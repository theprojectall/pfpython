import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.cliente('15J','Marta','Perez'),
            db.cliente('48H','Manolo','López'),
            db.cliente('28Z','Ana','Garcia')
        ]
        def text_buscar_cliente(self):
            cliente_extistente = db.Clientes.buscar('15J')
            cliente_inextistente = db.Clientes.buscar('99X')
            self.assertIsNotNone(cliente_extistente)
            self.assertIsNone(cliente_inextistente)