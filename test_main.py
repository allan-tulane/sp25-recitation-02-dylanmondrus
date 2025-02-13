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
	
	sizes = [10, 20, 50, 100, 500, 1000]

	def f_c_small(n):
			return n ** 0.5  

	def f_c_equal(n):
			return n 

	def f_c_large(n):
			return n ** 1.5  

	def work_fn1(n):
			return work_calc(n, 2, 2, f_c_small)  

	def work_fn2(n):
			return work_calc(n, 2, 2, f_c_equal)  

	res1 = compare_work(work_fn1, work_fn2, sizes) 
	
	def work_fn3(n):
			return work_calc(n, 2, 2, f_c_large)  
	
	res2 = compare_work(work_fn2, work_fn3, sizes) 
	
	print("\nComparing small vs equal:")
	print_results(res1)
	print("\nComparing equal vs large:")
	print_results(res2)



def test_compare_span():

	sizes = [10, 20, 50, 100, 500, 1000]

	def f_c_small(n):
			return n ** 0.5  

	def f_c_equal(n):
			return n  

	def f_c_large(n):
			return n ** 1.5  

	def span_fn1(n):
			return span_calc(n, 2, 2, f_c_small) 

	def span_fn2(n):
			return span_calc(n, 2, 2, f_c_equal) 

	def span_fn3(n):
			return span_calc(n, 2, 2, f_c_large) 

	res = compare_work(span_fn1, span_fn2, sizes)

	print_results(res)
