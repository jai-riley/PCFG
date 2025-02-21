def remove_lines_from_file(input_file, output_file, target_string):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            line_count = 0  # To count the lines processed
            removed_count = 0  # To count the lines removed
            for line in infile:
                line_count += 1
                print(f"Processing line {line_count}: {repr(line)}")  # Print the current line being processed
                
                if line.strip() not in target_string:  # Strips leading/trailing spaces before comparison
                    outfile.write(line)
                else:
                    removed_count += 1
                    print(f"Removed line {line_count}: {repr(line)}")  # Print removed lines

            print(f"Total lines processed: {line_count}")
            print(f"Total lines removed: {removed_count}")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_file = '/Users/jairiley/Desktop/BOW_Ngrams/corpus/pos_trees/wiki_validation_pos_trees.txt'
output_file = '/Users/jairiley/Desktop/BOW_Ngrams/corpus/pos_trees/wiki_validation_pos_trees_2.txt'
target_string = ['(FRAG (. .))','(INTJ (. .) (. .))','(INTJ (. .))']

print("Starting to process the file...")
remove_lines_from_file(input_file, output_file, target_string)
print("Done processing.")
