import csv

csv_file = '03-Python_Instructions_PyBank_Resources_budget_data (2).csv'
csv_file_path = f'/Users/jasmin/UCI - Data Analytics/Homework Items/homework_jasmin/Python/{csv_file}'

months = []
amounts = []
with open(csv_file_path) as my_file:
	csv_reader = csv.reader(my_file, delimiter = ',')

#remember: f is to treat the whole argument as a literal string

	for row in csv_reader:
		month_year = row[0]
		months.append(month_year)
		amount_total = row[1]
		amounts.append(amount_total)

months.pop(0)		
amounts.pop(0)

print(f'Number of Months: {len(months)}')

profit_or_loss = []
for num in amounts:
	profit_or_loss.append(int(num))
print(f'Net Total of Profits/Losses: {sum(profit_or_loss)}')

average = sum(profit_or_loss)/len(months)
print(f'Average: {average}')

most_increase = max(profit_or_loss)
date_increase = profit_or_loss.index(most_increase)


most_decrease = min(profit_or_loss)
date_decrease = profit_or_loss.index(most_decrease)

print(f'Greeatest Increase in Profits: {months[date_increase]} ({most_increase})')
print(f'Greeatest Decrease in Profits: {months[date_decrease]} ({most_decrease})')

print('---------------------------------------------------')

import csv

csv_file_2 = '03-Python_Instructions_PyPoll_Resources_election_data.csv'
csv_file_path2 = f'/Users/jasmin/UCI - Data Analytics/Homework Items/homework_jasmin/Python/{csv_file_2}'



votes_per_candidate = {}
with open(csv_file_path2) as my_second_hw:
	vote_reader = csv.reader(my_second_hw, delimiter = ',')
	next(vote_reader)

	vote_tally = 0
	for vote in vote_reader:
		vote_tally +=1
		name = vote[2]
		if name in votes_per_candidate.keys():
			votes_per_candidate[name] +=1
		else:
			votes_per_candidate.update({name : 1})

	print(f'Total Number of Votes: {vote_tally}')

	highest_vote_count = 0
	winner = ''
	for candidate in votes_per_candidate:
		if votes_per_candidate[candidate] > highest_vote_count:
			highest_vote_count = votes_per_candidate[candidate]
			winner = candidate

	
		vote_percentage = votes_per_candidate[candidate]/vote_tally
		vote_percentage = int(vote_percentage * 100)
		#print(candidate +': ' + str(vote_percentage) + '% (' + str(votes_per_candidate[candidate]) + ')')
		print(f'{candidate} : {vote_percentage}% ({votes_per_candidate[candidate]})')
print(f'Winner: {winner}')
	

#print(votes_per_candidate)
#if 'key1' in dict.keys():

		



#		for name in vote_reader:
#			name = vote[2]
#			if name not in candidates:
#				candidates.append(name)
#			else:
#				vote_count[name] +=1

#print(candidates)


#curly bracket = dictionary = key-value pair(only inside dictionaries) example: 'pizza': 60


#anything you want to incriment, leave outside the loop
#correy_count = 0
#li_count = 0
#o_tooley_
#for name is csv:
	#person =name[2]
	#if person = 'Correy'
		#correy_count += 1
		#+1 is the same thing
		#elif person = 'Li'
		#li_count += 1

#names = []
#votes = {}
	#for name in csv:
	#for can in names:
		#person = name[2]
		#if person not in names:
			#names.append(person)

		#else:
			#votes[person] += 1
	#print(names)


#candidates.pop(0)
#print(f'List of Candidates: {candidates}')