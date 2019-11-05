import math

#Choose which exported confusion matrix files to use
files = ['dna_svm.csv','rna_svm.csv','drna_svm.csv','nondrna_svm.csv']
#files = ['dna_dt.csv','rna_dt.csv','drna_dt.csv','nondrna_dt.csv']
#files = ['dna_nb.csv','rna_nb.csv','drna_nb.csv','nondrna_nb.csv']
total_tp, total_mcc = 0, 0

for f in files:
	dna_nb_file = open(f, 'r')
	dna_nb_file_lines = dna_nb_file.readlines()
	dna_nb_file.close()
	line_one, line_two = dna_nb_file_lines[1].split(';'), dna_nb_file_lines[2].split(';')

	if line_one[0] == "\"pred True\"":
		tp = float(line_one[1])
		fn = float(line_one[2])
		fp = float(line_two[1])
		tn = float(line_two[2])
	elif line_one[0] == "\"pred False\"":
		tp = float(line_two[2])
		fn = float(line_two[1])
		fp = float(line_one[2])
		tn = float(line_one[1])
	
	if tp == 0:
		tp+=1
	elif fn == 0:
		fn+=1
	elif fp == 0:
		fp+=1
	elif tn == 0:
		tn+=1
	
	sensitivity = "{0:.1f}".format(100 * tp / (tp + fn))
	specificity = "{0:.1f}".format(100 * tn / (tn + fp))
	predictive_acc = "{0:.1f}".format(100 * (tp + tn)/(tp + fp + tn + fn))
	mcc = ((tp * tn) - (fp * fn)) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
	total_tp += tp
	total_mcc += mcc
	
	print(f)
	print("Sensitivity: " + str(sensitivity))
	print("Specificity: " + str(specificity))
	print("Predictive Accuracy: " + str(predictive_acc))
	print("MCC: " + str(mcc))
	print('\n')


accuracy = "{0:.1f}".format(100 * total_tp / 8795)	
average_mcc = "{0:.3f}".format(total_mcc / 4)
print("Accuracy: " + str(accuracy))
print("Average MCC: " + str(average_mcc))



