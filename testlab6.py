import unittest
from lab6 import check_gas_supply


class TestGasNetwork(unittest.TestCase):

    def test_all_reachable(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = [
            ['Сховище_1', 'Львів'],
            ['Львів', 'Стрий']
        ]

        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, [])

    def test_some_unreachable(self):
        cities = ['Львів', 'Стрий', 'Долина']
        storages = ['Сховище_1']
        pipelines = [
            ['Сховище_1', 'Львів'],
            ['Львів', 'Стрий']
        ]

        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, [['Сховище_1', ['Долина']]])

    def test_multiple_storages(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [
            ['Сховище_1', 'Львів']
        ]

        result = check_gas_supply(cities, storages, pipelines)
        expected = [
            ['Сховище_1', ['Стрий']],
            ['Сховище_2', ['Львів', 'Стрий']]
        ]

        self.assertEqual(result, expected)

    def test_no_connections(self):
        cities = ['Львів']
        storages = ['Сховище_1']
        pipelines = []

        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, [['Сховище_1', ['Львів']]])


if __name__ == '__main__':
    unittest.main()
