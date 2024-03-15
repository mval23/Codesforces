import os


def create_directory_and_files(directory_name, file_names):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Change directory to the newly created one
    os.chdir(directory_name)

    # Create Python files with names from the list
    for file_name in file_names:
        with open(file_name + ".py", "w") as file:
            file.write("")

    with open("jupyter.ipynb", "w") as file:
        file.write("")


directory_name = "module_5"
file_names = [
    "sumatoria_multiplos",
    "de_tin_marin",
    "teclado_numerico",
    "encontrando_mediana",
    "juego_eliminacion",
    "autografo_serena"
]

create_directory_and_files(directory_name, file_names)

# if __name__ == "__main__":
#     # Example usage
#     directory_name = input("Enter directory name: ")
#     file_names = input("Enter comma-separated list of file names: ").split(",")
#     create_directory_and_files(directory_name, file_names)
#     print("Directory '{}' created with Python files: {}".format(directory_name, file_names))
