from app.io.input import console_input, file_input, pandas_input
from app.io.output import console_output, file_output


def main():
    input_path = "test_input.txt"
    output_path = "test_output.txt"
    inputted_text = console_input()
    inputted_file = file_input(input_path)
    inputted_pandas = pandas_input(input_path)

    console_output(inputted_text)
    console_output(inputted_file)
    console_output(inputted_pandas.to_string())

    file_output(output_path, inputted_text)
    file_output(output_path, inputted_file)
    file_output(output_path, inputted_pandas.to_string())


if __name__ == "__main__":
    main()
