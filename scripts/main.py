from urllib.request import urlopen

with open("../data/tic-tac-toe.csv", "w") as output_file:
    output_file.write('TL,TM,TR,ML,MM,MR,BL,BM,BR,class\n')
    for line in urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/tic-tac-toe/tic-tac-toe.data"):
        decoded_line = line.decode('UTF-8').lower().strip()
        decoded_line = decoded_line.replace('positive', 'true')
        decoded_line = decoded_line.replace('negative', 'false')
        output_file.write(decoded_line + '\n')

    output_file.close()
