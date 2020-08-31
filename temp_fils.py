import tempfile
#temp files are looked for in environment variables: TMPDIR, TEMP, TMP
#On windows, C:\TEMP, C:\TMP, \TEMP, and \TMP.
print("Temp dir location--> ", tempfile.gettempdir())
# if you want to write text data into a temp file, 
# we need to create the tempfile using the w+t mode
# instead of the default.
#my_file = tempfile.TemporaryFile('w+t')
my_folder = tempfile.TemporaryDirectory(prefix="UC_", suffix="_Python101")
my_file = tempfile.NamedTemporaryFile('w+t')
my_file = tempfile.NamedTemporaryFile(dir=my_folder.name, prefix="UC_", mode='w+t', suffix="_python101")
#my_file.name = "my_temporary_file.thingy"
try:
    #it's not a file yet, it is a temp object onthe filesystem
    print("The file is-->", my_file.name)
    my_file.write("Yo, this is what we do...")
    #go back to the beginning of the file and read data
    my_file.seek(0)
    data = my_file.read()
    print(data)
finally:
    my_file.close()
    print("Closed. Poof. Gone.")
    my_folder.cleanup()
    print("Cleaned Up. Poof. Gone.")