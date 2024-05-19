def bacafile(filesalah):
    try:
        with open(filesalah, 'r') as file:
            text = file.read().lower()
        return text
    except FileNotFoundError:
        print(f"Error: File '{filesalah}' tidak ditemukan atau tidak bisa dibaca.")
        return None

def membagi(text):
    words = text.split()
    return set(words)

def main():
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")
    
    text1 = bacafile(file1)
    text2 = bacafile(file2)
    
    if text1 is None or text2 is None:
        return
    
    kata1 = membagi(text1)
    kata2 = membagi(text2)
    
    gabungan_kata = kata1 | kata2
    
    print("Kata-kata yang muncul di kedua file:")
    for word in gabungan_kata:
        print(word)

if __name__ == "__main__":
    main()
