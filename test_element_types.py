
from atom_typer import uff_typer

def test_uff_typer_can_type_a_c():
    assert uff_typer.typeit(None)== ["C"]
