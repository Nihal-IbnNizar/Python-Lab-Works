def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except IOError:
        print(f"Error: An I/O error occurred while copying contents.")

source_file = 'source.txt' 
destination_file = 'destination.txt' 

copy_file_contents(source_file, destination_file)
