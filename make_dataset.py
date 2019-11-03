from pandas import read_csv

seq, tag = list(), list()
with open('sequences_training.txt', 'r') as file:
    for line in file:
        words = line.split(',')
        tag.append(words[1][:-1])
    file.close()


train_df = read_csv('final_amino_acid_result.csv')
train_df['tags'] = tag
train_df['DNA'] = (train_df['tags'] == 'DNA')
train_df['RNA'] = (train_df['tags'] == 'RNA')
train_df['DRNA'] = (train_df['tags'] == 'DRNA')
train_df['nonDRNA'] = (train_df['tags'] == 'nonDRNA')
# comment out last 2 lines and include the following 2 lines to keep tag index
# train_df.set_index('tags', inplace=True)
# train_df.to_csv('amino_acid_indexed.csv')
train_df.drop(columns='tags', inplace=True)
train_df.to_csv('amino_acid_dataset.csv', index=False)
