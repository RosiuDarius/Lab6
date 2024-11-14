# tests/test_client.py

import unittest
from operations.client_operations import GestorClienti, ClientExistsError, ClientNotFoundError
from domain.client import Client

class TestGestorClienti(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorClienti()

    def test_adauga_client(self):
        client = Client(1, "Ion Popescu", "1234567890123", 5)
        self.gestor.adauga_client(client)
        self.assertEqual(len(self.gestor.clienti), 1)

    def test_adauga_client_existenta(self):
        client = Client(1, "Ion Popescu", "1234567890123", 5)
        self.gestor.adauga_client(client)
        with self.assertRaises(ClientExistsError):
            self.gestor.adauga_client(client)

    def test_sterge_client(self):
        client = Client(1, "Ion Popescu", "1234567890123", 5)
        self.gestor.adauga_client(client)
        self.gestor.sterge_client(1)
        self.assertEqual(len(self.gestor.clienti), 0)

    def test_sterge_client_neexistent(self):
        with self.assertRaises(ClientNotFoundError):
            self.gestor.sterge_client(999)

    def test_cauta_client(self):
        client = Client(1, "Ion Popescu", "1234567890123", 5)
