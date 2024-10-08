import pytest


def test_lawn_grass_init(lawngrass_1):
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


def test_lawn_grass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 15000.0


def test_lawn_grass_add_not_grass(lawngrass_1, smartphone_1):
    with pytest.raises(TypeError):
        lawngrass_1 + smartphone_1
