from math import sqrt

def top_matches(prefs,person,n=5,similarity=sim_pearson):
	scores= [(similarity(prefs,person,other), other) for other in prefs if other != person]
	scores.sort()
	scores.reverse()
	return scores[0:n]



# Returns a distance based similarity score
def sim_distance(prefs,person1,person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1;


	if len(si)==0: return 0

	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

	return 1/(1+sqrt(sum_of_squares))

# Returns the Pearson correlation coefficient as a similarity score
def sim_pearson(prefs,person1,person2):
	si={}
	for item = prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	n=len(si)

	if n==0: return 0;

	sum1 = sum([prefs[person1][item] for item in si])
	sum2 = sum([prefs[person2][item] for item in si])

	sum_of_squares1 = sum([pow(prefs[person1][item],2) for item in si])
	sum_of_squares2 = sum([pow(prefs[person2][item],2) for item in si])

	product_sum = sum(prefs[person1][item]*prefs[person2][item] for item in si)

	num = product_sum-(sum1*sum2/n)
	den = sqrt((sum_of_squares1-pow(sum1,2)/n)*(sum_of_squares2-pow(sum2,2)/n))

	if den==0: return 0

	return num/den

