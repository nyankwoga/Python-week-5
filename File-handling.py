def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("First line\n")
            file.write("Second line\n")
            file.write("Third line\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File creation process completed.")


def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File reading process completed.")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Fourth line\n")
            file.write("Fifth line\n")
            file.write("Sixth line\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    finally:
        print("File appending process completed.")


def main():
    create_file()
    print()
    read_and_display_file()
    print()
    append_to_file()


if __name__ == "__main__":
    main()
