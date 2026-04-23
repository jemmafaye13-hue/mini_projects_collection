class NumberProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    def process_numbers(self):
        try:
            with open(self.input_file, 'r') as infile, open(self.output_file, 'w') as outfile:
                for line in infile:
                    num = int(line.strip())
                    if num % 2 == 0:
                        result = num ** 2  # Square if even
                    else:
                        result = num ** 3  # Cube if odd
                    outfile.write(str(result) + "\n")
            print("Processing complete!")
        except FileNotFoundError:
            print("Input file not found.")

if __name__ == "__main__":
    processor = NumberProcessor("numbers.txt", "double.txt")
    processor.process_numbers()