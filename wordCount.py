import string
import sys
def main(argv):
    """
    Takes all words from a file and writes them to a seperate file alphabetically along with their frequency.
    
    Reads a file line by line adding each previously unencountered word to a dictionary with a value of 1.
    If a word that has already been added to the dictionary is encountered again it's value is increased by 1.
    Before being added to the dictionary all characters are changed to lowercase. After having gone through
    the entire file the dictionary is then sorted and each tuple is printed in it's own individual line on a
    seperate file.
    Parameters:
    argv:  List of command lind arguments of which argv[1] and argv[2] are significant
    argv[1]: name of the input file which will be the bases for the dictionary
    argv[2]: name of the output file which is where the contents of the dictionary will be printed
    Returns:
    N/A
    """
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    word_list = {}
    temp = 0
    PunctuationTranslator = str.maketrans(string.punctuation,' '*len(string.punctuation)) 

    with open(inputfile) as file:
        for line in file:
            line =line.translate(PunctuationTranslator) # removes all punctuations replacing them with a space
            line = line.lower()    
            values = line.split()      
            for i in values:
                if i in word_list:
                    temp = word_list[i]
                    word_list[i] = temp + 1
                else:
                    word_list[i] = 1
    OutFile = open(outputfile, "w+")
    for i in sorted(word_list.keys()):
        curLine = i+" "+ str(word_list[i])
        OutFile.write(curLine + '\n')
    OutFile.close()

main(sys.argv)