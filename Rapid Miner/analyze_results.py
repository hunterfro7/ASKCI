import math

#Choose which exported confusion matrix files to use
baseline_files = ['dna_svm.csv','rna_svm.csv','drna_svm.csv','nondrna_svm.csv']
design_one_files = ['dna_dt.csv','rna_dt.csv','drna_dt.csv','nondrna_dt.csv']
design_two_files = ['dna_nb.csv','rna_nb.csv','drna_nb.csv','nondrna_nb.csv']
total_tp, total_mcc = 0, 0


def analyze_design(files):
	total_tp = 0
	total_mcc = 0
	results = []
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
	
		#print(f)
		#print("Sensitivity: " + str(sensitivity))
		#print("Specificity: " + str(specificity))
		#print("Predictive Accuracy: " + str(predictive_acc))
		clean_mcc = "{0:.3f}".format(mcc)
		#print("MCC: " + str(clean_mcc))
		#print('\n')
		results.append(str(sensitivity))
		results.append(str(specificity))
		results.append(str(predictive_acc))
		results.append(str(clean_mcc))

	accuracy = "{0:.1f}".format(100 * total_tp / 8795)	
	average_mcc = "{0:.3f}".format(total_mcc / 4)
	#print("Accuracy: " + str(accuracy))
	#print("Average MCC: " + str(average_mcc))
	results.append(str(average_mcc))
	results.append(str(accuracy))
	
	return results


outcome,quality = [''] * 19,[''] * 19
results_base, results_one, results_two = [],[],[]
results_best = ['']*18
results_base = analyze_design(baseline_files)
results_one = analyze_design(design_one_files)
results_two = analyze_design(design_two_files)
results_base.insert(0,'Baseline result')
results_one.insert(0, 'Design 1')
results_two.insert(0, 'Design 2')
results_best.insert(0,'Best Design')
outcome[0] = 'Outcome'
quality[0] = 'Quality Measure'

outcome[1] = 'DNA'
outcome[5] = 'RNA'
outcome[9] = 'DRNA'
outcome[13] = 'nonDRNA'
outcome[17] = 'averageMCC'
outcome[18] = 'accuracy'

for i in range(0,4):
	quality[1+(i*4)] = 'Sensitivity'
	quality[2+(i*4)] = 'Specificity'
	quality[3+(i*4)] = 'PredictiveACC'
	quality[4+(i*4)] = 'MCC	'

c_list = []
c_list.append(outcome)
c_list.append(quality)
c_list.append(results_base)
c_list.append(results_one)
c_list.append(results_two)
c_list.append(results_best)
for i in range(0,19):
	string = ''
	for c in c_list:
		if (i != 0) and (c == results_one or c == results_two):
			string = string + '	' + c[i] + '		'
		elif c != 3 or c != 4:
			string = string + c[i] + '		'
	print(string)
	









