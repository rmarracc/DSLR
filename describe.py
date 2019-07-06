import numpy
import sys
import math
import pandas as pd

def	load_file(n):
	try:
		d = pd.read_csv(n, sep = ',')
	except:
		print ("dataset file missing")
		sys.exit()
	return (d)

def display_names(n, e):
	a = []
	l = []
	for i in range(len(n)):
		if ((type(n[i]) == float or type(n[i]) == int or type(n[i]) == numpy.int64) and not numpy.isnan(n[i])):
			l.append(len(e[i]) + 2)
			a.append(e[i])
	sys.stdout.write("{0: <7}".format(" "))
	for j in range(len(a)):
		sys.stdout.write("{0: >{width}}".format(a[j], width=l[j]))
	print ("")
	return (l)

def capped(a, b):
	c = b - a - 3
	if (c > 6):
		c = 6
	if (c < 0):
		c = 0
	return (c)

def padded_values(f, l, w):
	for j in range(len(f)):
		b = abs(f[j])
		if (b < 1):
			b = 1
		w.append(math.floor(math.log(b, 10)))
		if (f[j] < 0):
			w[j] += 1
		if (w[j] > l[j] - 1):
			sys.stdout.write("{0: >{width}}".format("*", width=l[j]))
		else:
			sys.stdout.write("{0: >{width}.{prec}f}".format(f[j], width=l[j], prec=capped(w[j], l[j])))
	print ("")

def get_count(a):
	r = 0
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r += a[i]
	return (r)

def get_mean(a):
	r = 0
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r += a[i]
	if (len(a) == 0):
		return (0)
	r /= len(a)
	return (r)

def get_min(a):
	r = 0
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			if (i == 0):
				r = a[i]
			else:
				if (r > a[i]):
					r = a[i]
	return (r)

def get_max(a):
	r = 0
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			if (i == 0):
				r = a[i]
			else:
				if (r < a[i]):
					r = a[i]
	return (r)

def get_q25(a):
	r = []
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r.append(a[i])
	r.sort()
	return (r[len(r) // 4])

def get_q50(a):
	r = []
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r.append(a[i])
	r.sort()
	return (r[len(r) // 2])

def get_q75(a):
	r = []
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r.append(a[i])
	r.sort()
	return (r[math.floor(len(r) * 0.75)])

def get_std(a):
	m = get_mean(a)
	r = 0
	for i in range(len(a)):
		if ((type(a[i]) == float or type(a[i]) == int or type(a[i]) == numpy.int64) and not numpy.isnan(a[i])):
			r += ((a[i] - m) * (a[i] - m))
	if (len(a) < 2):
		return (0)
	s = math.sqrt(r * (1 / (len(a) - 1)))
	return (s)

def process_f(n, e, l, a, func, s):
	f = []
	w = []
	for i in range(len(n)):
		if ((type(n[i]) == float or type(n[i]) == int or type(n[i]) == numpy.int64) and not numpy.isnan(n[i])):
			f.append(func(a[:, i]))
	sys.stdout.write("{0: <7}".format(s))
	padded_values(f, l, w)

def main():
	if (len(sys.argv) is not 2):
		print ("usage : python describe.py [dataset]")
		sys.exit()
	d = load_file(sys.argv[1])
	e = d.columns
	e = numpy.array(e)
	a = numpy.array(d)
	n = len(a)
	if (n < 2):
		print ("not enough data")
		sys.exit()
	l = display_names(a[0, :], e)
	process_f(a[0, :], e, l, a, get_count, "Count")
	process_f(a[0, :], e, l, a, get_mean, "Mean")
	process_f(a[0, :], e, l, a, get_std, "Std")
	process_f(a[0, :], e, l, a, get_min, "Min")
	process_f(a[0, :], e, l, a, get_q25, "25%")
	process_f(a[0, :], e, l, a, get_q50, "50%")
	process_f(a[0, :], e, l, a, get_q75, "75%")
	process_f(a[0, :], e, l, a, get_max, "Max")

if (__name__ == "__main__"):
	main()