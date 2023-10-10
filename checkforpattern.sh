#!/bin/bash

# Define the path to the file
file_path="/Users/johnsontran/Desktop/Jenkins/Jenkins-Test/setDeploymentTagsOutput.txt"

# Check if the file exists
if [ -f "$file_path" ]; then
    # Use 'grep' to search for "error" in the file
    if grep -q "Absent" "$file_path"; then
        echo "Absent found in the Output!"
        exit 1  # Exit with a non-zero status to indicate failure
    else
        echo "No errors found in the file."
    fi
else
    echo "File not found: $file_path"
    exit 1  # Exit with a non-zero status to indicate failure
fi
