import functions
import pytest
import math

@pytest.mark.parametrize("number,expected_result", [
    (100, 10),
    (4, 2)
])
def test_racine_carree(number,expected_result):
    assert functions.racine_carree(number) == expected_result

def test_plantage_racine_carree_type():
    with pytest.raises(TypeError):
        functions.racine_carree("lol")

def test_racine_carre_negatif():
    assert math.isnan(functions.racine_carree(-9))