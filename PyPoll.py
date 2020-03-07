import pandas as pd

wr = open('/Users/enriquevazquez/Desktop/Python-/PyPoll/Results.txt', 'w' )
wr.write('Election Results\n------------------------------\n')
print('\nElection Results\n------------------------------')

csv_path = '/Users/enriquevazquez/Documents/BootCamp TEC/Bootcamp Program/Pandas/TDM-REV-DATA-PT-01-2020-U-C/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
csv_data = pd.read_csv(csv_path)
data_df = pd.DataFrame(csv_data)
data_df.head()

cand_count = data_df.groupby('Candidate')['Candidate'].count()
total = data_df['Candidate'].count()

wr.write('Total Votes : ' + str(total) + '\n------------------------------')
print('Total Votes : ' + str(total) + '\n------------------------------')

i=0

for i in range(len(cand_count)):
    print(f'{cand_count.index[i]}  : {str(round((cand_count[i]/total)*100,0))}% ({str(cand_count[i])})')
    wr.write('\n' + str(cand_count.index[i]) +  ' : ' + str(round((cand_count[i]/total)*100,0)) + '%  ' + '(' + str(cand_count[i]) + ')')
    i += 1
    
winner_num = data_df.groupby('Candidate')['Candidate'].count().max()

i = 0
for i in range(len(cand_count)):
    if cand_count[i] == winner_num:
        winner = cand_count.index[i]

print('\n------------------------------\nWinner : ' + str(winner) + '\n------------------------------')
wr.write('\n------------------------------\nWinner : ' + str(winner) + '\n------------------------------')