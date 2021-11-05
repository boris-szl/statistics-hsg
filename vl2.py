
import math



körpergrösse = [185,173,163,191,188]
einkommen = [60000,60000,35000,90000,55000]

körpergrösse_einkommen = dict(zip(körpergrösse,einkommen))
print(körpergrösse_einkommen)


def createDictOfLists(list1, list2):
	return dict(zip(list1,list2))

def average(werte):
	summe = 0
	if isinstance(werte, list):
		for i in werte:
			summe += i
	average = (summe / len(werte))
	return average

def averagefordict(items):
	summe_key = 0
	summe_value = 0
	return 0

def averageForDictKeys(items):
	summe_key = 0
	for i,j in körpergrösse_einkommen.items():
		summe_key += i
	average_key = summe_key / len(körpergrösse_einkommen)
	return average_key

def averageForDictValues(items):
	summe_value = 0
	for i,j in körpergrösse_einkommen.items():
		summe_value += j
	average_value = summe_value / len(körpergrösse_einkommen)
	return average_value

def count_keys(dictionary):
	count = 0
	for i in enumerate(dictionary):
		count += 1
	return count

def count_values(dictionary):
	count = 0
	for key, value in enumerate(dictionary):
		count += 1
	return count

print(averageForDictKeys(körpergrösse_einkommen))
print(averageForDictValues(körpergrösse_einkommen))


def variance(werte):
	mu = average(werte)
	temp = 0
	for i in werte:
		temp += (i - mu)**2
	variance = temp / len(werte)
	return variance

print(variance(körpergrösse))

def sigma(variance):
	sigma = variance**(1/2)
	return sigma

print(sigma(variance(körpergrösse)))

def covariance(x,y):
	mu_x = average(x)
	mu_y = average(y)
	temp_dict = createDictOfLists(x,y)
	summe = 0
	for x,y in temp_dict.items():
		summe += (x - mu_x) * (y - mu_y)
	covariance = summe / len(temp_dict)
	return covariance

print(covariance(körpergrösse, einkommen))

def corr_coefficient(x,y):
	mu_x = average(x)
	mu_y = average(y)
	temp_dict = createDictOfLists(x,y)
	summe = 0
	for x,y in temp_dict.items():
		summe += (x - mu_x) * (y - mu_y)
	covariance = summe / len(temp_dict)
	var_x = variance(körpergrösse)
	var_y = variance(einkommen)
	sigma_x = var_x**(1/2)
	sigma_y = var_y**(1/2)
	corr_coefficient = covariance / (sigma_x * sigma_y)
	return corr_coefficient

print(corr_coefficient(körpergrösse, einkommen))

def weighted_average(list):
	summe = 0

with open('returns.txt', 'r') as returns:
	print(returns)







