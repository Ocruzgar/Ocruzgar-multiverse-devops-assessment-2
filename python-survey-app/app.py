import sys
from extract import get_input
from extract import get_output


def main(results_file):
    # function that receive a csv with the result of a survey, clean it and print it both in screen and in a file

    output_file = "clean_results.csv"
    get_input(results_file)
    get_output(output_file)



if __name__ == "__main__":
   main(sys.argv[1])