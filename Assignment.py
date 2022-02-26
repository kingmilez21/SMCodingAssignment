# Python code to
# demonstrate readlines()
import glob
import sys
import statistics
from nltk.tokenize import WhitespaceTokenizer


def find_keyword(lines, keyword):
    found = []
    for line in lines:
        if keyword in line:
            found.append(line.strip())
    found.sort()
    return found


def duplicates(lines):
    seen = set()
    count = 0
    for line in lines:
        line_lower = line.lower().strip()
        if line_lower in seen:
            count += 1
        else:
            seen.add(line_lower)
    return count


def median(lines):
    length = []
    for line in lines:
        length.append(len(line.strip()))
    return statistics.median(length)


def median_token(lines):
    tk = WhitespaceTokenizer()
    length = []
    for line in lines:
        token = tk.tokenize(line)
        for lin in token:
            length.append(len(lin.strip()))
    return statistics.median(length)


def std_deviation(lines):
    length = []
    for line in lines:
        length.append(len(line))
    return statistics.stdev(length)


def std_deviation_token(lines):
    tk = WhitespaceTokenizer()
    length = []
    length_line = 0
    for line in lines:
        token = tk.tokenize(line)
        for lin in token:
            length_line += len(lin)
        length.append(length_line)
        length_line = 0
    return statistics.stdev(length)


def main():
    # for arg in sys.argv[1:]:
    #     print(arg)
    # put the additional file as a args and put into a list for time complexity
    # "How to not specfcy the fodler name"
    for name in glob.glob('C:/Users/ricks/SMCodingAssignment/SMCodingAssignment/*.txt'):
        with open(name) as fn:
            content = fn.readlines()
            avg = median(content)
            dup = duplicates(content)
            std = std_deviation(content)
            med_token = median_token(content)
            std_token = std_deviation_token(content)
            keyword = find_keyword(content, 'right')
            with open('C:/Users/ricks/SMCodingAssignment/SMCodingAssignment/Output/output.txt', 'w') as text_file:
                text_file.write("The number of duplicates: %d" % dup + '\n')
                text_file.write("The median: %d" % avg + '\n')
                text_file.write("The standard deviation: %d" % std + '\n')
                text_file.write("The median of token: %d" % med_token + '\n')
                text_file.write("The standard deviation deviation of token: %d" % std_token + '\n')
                for element in keyword:
                    text_file.write("%s" % element + '\n')


if __name__ == "__main__":
    main()
