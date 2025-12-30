from src.utils import copy_static

def main():
    copy_static("static", "public")
    print("Static files copied successfully!")

if __name__ == "__main__":
    main()