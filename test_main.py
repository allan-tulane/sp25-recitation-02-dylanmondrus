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
	"""
	Compare empirical values of W(n) for different f(n) = n^c cases
	to justify theoretical predictions.
	"""
	# Define values of n to test
	sizes = [10, 20, 50, 100, 500, 1000]

	# Define different f(n) cases using def
	def f_c_small(n):
			return n ** 0.5  # c < log_b a (Expected O(n^log_b a))

	def f_c_equal(n):
			return n  # c = log_b a (Expected O(n log n))

	def f_c_large(n):
			return n ** 1.5  # c > log_b a (Expected O(n^c))

	# Create work functions for comparison
	def work_fn1(n):
			return work_calc(n, 2, 2, f_c_small)  # c < log_b a

	def work_fn2(n):
			return work_calc(n, 2, 2, f_c_equal)  # c = log_b a

	# Compare the work functions
	res = compare_work(work_fn1, work_fn2, sizes)

	# Print results in table format
	print_results(res)



def test_compare_span():
	print(1)

