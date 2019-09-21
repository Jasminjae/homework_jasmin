import csv

csv_file = '04-Pandas_Instructions_HeroesOfPymoli_Resources_purchase_data.csv'
csv_path = f'/Users/jasmin/Data Analytics/Homework Items/homework_jasmin/Pandas/{csv_file}'

with open(csv_path) as my_data:
	my_csv = csv.reader(my_data, delimiter = ',')
	#.read_csv for reading csv in pandas

	total_player=[]
	for player in my_csv:
		total_player +=1
		name = player[0]
	print(total_player)