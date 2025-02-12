from main import *


def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(8, 2, 4) == 16
	assert simple_work_calc(50, 5, 3) == 380
	assert simple_work_calc(12, 3, 3) == 33


def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n * n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(16, 2, 4, lambda n: 5) == 19
	assert work_calc(25, 4, 5, lambda n: n + 2) == 71
	assert work_calc(50, 2, 5, lambda n: n // 2) == 47
	

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2
	res = compare_work(work_fn1, work_fn2)

	print(res)


def test_compare_span():
	print(1)
