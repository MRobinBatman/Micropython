def Config(filename):
    # Create an empty dictionary to store the configuration values
    config = {}
    
    # Open the configuration file
    with open(filename) as f:
        # Read the contents of the file
        lines = f.read().splitlines()
        
        # Keep track of the current section
        section = None
        
        # Loop through each line in the file
        for line in lines:
            # Skip blank lines
            if not line.strip():
                continue
            
            # Check if the line is a section header
            if line.startswith('['):
                # Extract the section name from the line
                section = line[1:-1].strip()
                
                # Create a new dictionary for the section
                config[section] = {}
                
            # Check if the line is a key-value pair
            elif '=' in line:
                # Split the line into key and value
                key, value = [part.strip() for part in line.split('=', 1)]
                
                # Add the key-value pair to the current section
                config[section][key] = value
                
    # Return the dictionary of configuration values
    return config
"""
# Example usage:
config = Config('config.ini')

# Get values from the configuration file
value1 = config['Discord']['token']
value2 = config['Discord']['server']
value3 = config['Discord']['channel']


print('Token:', value1)
print('Server:', value2)
print('Channel:', value3)
"""

