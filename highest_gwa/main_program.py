class GWAAnalyzer:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def find_highest_gwa(self):
        try:
            with open(self.input_filename, mode='r') as gwa_records:
                pass  # Logic coming next
        except FileNotFoundError:
            print("File not found.")