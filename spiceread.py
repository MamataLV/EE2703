from sys import argv

if len(argv)!=2:
	print('Provide name of the file or too many arguments')

else:
	try:
		fname=argv[1]
		if '.netlist' in fname[-8:]:
			input_data=reversed(list(open(fname)))

			for line in input_data:
				if line.strip()=='.end':
					break
			for line in input_data:
				if line.strip()=='.circuit':
					break
				words=line.split()
				print(' '.join(words[::-1]))
			argv[1].close()
		else:
			print("Input file should be '*.netlist'")
	
	except IOError:
		print("File not found or path is incorrect")

	finally:
		exit()