# Mod Organizer 2 Profiles Modlist Sorting Script

This Python script helps you sort the `modlist.txt` file for Mod Organizer 2 profiles based on specific criteria. The script can sort the lines starting with "*Creation Club:" by the number inside the phrase and the length of the line. It can also reverse the sorting order for both the number and length.

## Requirements

- Python 3.x

## Usage

1. Place the `MO_sort.py` script in the same directory as your Mod Organizer 2 profiles' `modlist.txt` file. Backup it with another filename and rename the original to `input.txt`.

2. Run the script in your terminal/command prompt:

    ```bash
    python MO_sort.py
    ```

3. The script will prompt you with sorting options:
   - Type `1` if you want to keep the sort as it already is.
   - Type `2` if you want to ignore sorting based on numbers and only sort based on length.

4. The sorted output will be written to a new file called `output.txt` in the same directory.

5. Rename `output.txt` to `modlist.txt` and place it back in your Mod Organizer 2 profile directory, overwriting the original `modlist.txt` file.

6. Launch Mod Organizer 2, and the mods in your profile should now be sorted according to your chosen criteria.

## Note

- The script only sorts the lines starting with "*Creation Club:"; all other lines are kept in their relative position.

- The sorting is in descending order for both the number inside the phrase and the length of the line.

- The script tries to find the `modlist.txt` file in the same directory as the script. Ensure that you have both the script and the `modlist.txt` file in the correct directory before running the script.

- Before using the script, make sure to have a backup of your original `modlist.txt` file in case anything goes wrong during the sorting process.

## License

This script is provided under the MIT License. You can modify and distribute it as per the terms of the license.

