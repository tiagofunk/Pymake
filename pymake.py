import os
import sys

def read_files( directory ):
    f = []
    for root, _, files in os.walk( directory ):
        for file in files:
            f.append( os.path.join(root, file) )
    return f

def filter_extensions(files,extension):
    return list(filter( lambda x : x.endswith(extension), files ))

def extract_path_and_file(file_path):
    file = file_path[ file_path.rfind("/")+1:file_path.rfind(".") ]
    path = file_path[ 0:file_path.rfind("/")+1 ]
    return path, file

def create_file_compile_command( path, file, arguments ):
    return f"{COMPILER} {arguments} {path}{file}.cpp -o {path}{file}.o"

def create_program_compile_command( files ):
    command = f"{COMPILER} -o {PROGRAM_PATH} "
    for f in files:
        command += f"{swap_extension(f)} "
    return command

def create_remove_file_command( file ):
    return f"rm {file}"

def swap_extension( file ):
    return file[0:-4] + ".o"

def execute( command ):
    print( f"Executando: {command}" )
    r = os.popen(command)
    result = r.readlines()
    r.close()
    if( result != [] ):
        print( result )
        return False
    return True

def compile_file( file, arguments ):
    path, file = extract_path_and_file( file )
    command = create_file_compile_command(path, file, arguments)
    return execute( command )

def compile_program(files):
    command = create_program_compile_command( files )
    return execute( command )   
    
def remove_file(file):
    command = create_remove_file_command( file )
    return execute( command )

def remove_program():
    if(os.path.exists( PROGRAM_PATH )):
        command = create_remove_file_command( PROGRAM_PATH )
        execute( command )

def build( files_arguments_exceptions ):
    errors_counts = 0
    files = read_files(FILES_DIR)
    files = filter_extensions(files, ".cpp")

    for f in files:
        path, file = extract_path_and_file( f )
        if file in files_arguments_exceptions:
            if not compile_file( f, f"{files_arguments_exceptions[file]} {ARGUMENTS}" ):
                errors_counts += 1
        else:
            if not compile_file( f, ARGUMENTS ):
                errors_counts += 1

    if errors_counts == 0:
        compile_program(files)

def clean():
    files = read_files(FILES_DIR)
    files = filter_extensions(files,".o")
    for f in files:
        remove_file( f )
    remove_program()


FILES_DIR = "./c/"
COMPILER = "g++"
ARGUMENTS = "-c -O3 -Wall -fmessage-length=0"
PROGRAM_NAME = "test"
PROGRAM_PATH = f"{FILES_DIR}{PROGRAM_NAME}"

files_arguments_exceptions = {
    "main": "-D REALIZE_TEST" 
}

if sys.argv[1] == "build":
   build( files_arguments_exceptions )
elif sys.argv[1] == "clean":
    clean()