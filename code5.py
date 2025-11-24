def write_text(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    write_text("output.txt", "Sample output text")
    print("File written successfully!")
