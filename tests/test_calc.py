from minicalc import add, sub, mul, div, powi

def test_add():
	assert add(2, 3) == 5

def test_sub():
	assert sub(5, 1) == 4

def test_mul():
	assert mul(5, 1) == 5

def test_div():
	assert div(5, 1) == 5

def test_powi():
	assert powi(5, 1) == 5

