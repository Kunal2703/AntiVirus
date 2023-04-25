import hashlib
import os 

# Read list of malware hashes and virus info from files
malware_hashes = list(open("virusHash.unibit", "r").read().split('\n'))
virusInfo = list(open("virusInfo.unibit", "r").read().split('\n'))

# Define a function to calculate the SHA256 hash of a file
def sha256_hash(filename):
    try:
        # Open the file in binary mode and read its contents
        with open(filename, 'rb') as f:
            bytes = f.read()
            # Compute the SHA256 hash of the file's contents
            sha256hash = hashlib.sha256(bytes).hexdigest()
            f.close()
            # Print the hash to the console
            print(sha256hash)
        return(sha256hash)
    except:
        # Return an error message if there was a problem reading the file
        return("Virus Detected!!")

# Define a function to check if a file matches a known malware hash
def malware_checker(pathOfFile):
    # Make the malware_hashes and virusInfo lists global variables
    global malware_hashes
    global virusInfo
    
    # Compute the SHA256 hash of the file
    hash_malware_check = sha256_hash(pathOfFile)
    
    # Loop over the list of known malware hashes
    counter = 0 
    for i in malware_hashes:
        # If the file's hash matches a known malware hash, return the corresponding virus info
        if i == hash_malware_check:
            return virusInfo[counter]
        counter += 1
        
    # If the file's hash does not match any known malware hash, return 0
    return 0

# Define a function to scan a directory for viruses
virusName = []
virusPath = []


def virusScanner(path):
    # Create an empty list to store the paths of all files in the directory
    dir_list = list()
    
    # Recursively walk through the directory tree and add the paths of all files to the dir_list
    for(dirpath, dirnames, filenames) in os.walk(path):
        dir_list += [os.path.join(dirpath, file) for file in filenames]
    
    # Loop over the list of file paths and check each one for malware
    for i in dir_list:      
        print(i)       
        if malware_checker(i) != 0:
            # If the file is infected, add its virus info and path to the virusName and virusPath lists
            virusName.append(malware_checker(i)+" :: File :: "+i)
            virusPath.append(i)
            
# Define a function to remove viruses from a directory
def virusRemove(path):
    # Scan the directory for viruses and add their paths to the virusPath list
    virusScanner(path)
    # If any viruses were found, delete the infected files
    if virusPath:
        for i in virusPath:
            os.remove(i)
    else:
        # If no viruses were found, return 0
        return 0

    
#virusRemove("/Users/kunalsingh/Desktop/Sem-6")

#virusRemove(path)
#print(virusPath)
    