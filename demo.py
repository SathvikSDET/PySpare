import configparser
import os

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def get_credentials(config):
    # Read values directly from the config file without section headers
    username = config.get('DEFAULT', 'username', fallback=None)
    password = config.get('DEFAULT', 'password', fallback=None)
    return username, password

def main():
    # Get the current directory and build the path to config file inside 'config' folder
    config_file = os.path.join(os.getcwd(), "config", "config.properties")  # Path to your .properties file
    
    # Create a config parser object and read the file
    config = read_config(config_file)

    # Get username and password from the config
    username, password = get_credentials(config)
    
    # Print out the username and password or use them
    print(f"Username: {username}, Password: {password}")
    
    # Example of passing these values to another function
    login(username, password)

def login(username, password):
    # Simulate login process
    print(f"Logging in with username: {username} and password: {password}")

if __name__ == "__main__":
    main()
