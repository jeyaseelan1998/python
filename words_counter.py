def words_counter(content):
    """This function returns the dictionary which represents the repeatation of each word"""
    result = {}
    data = content.split()
    for word in data:
        if word.isalpha() and len(word) > 3:
            if not word in result:
                result[word] = 0
            result[word] += 1
    print(result)
    return result


content = "Visual Studio Code was recently released and I liked the look of it and the features it offered, so I figured I would give it a go.\n I downloaded the application from the downloads page, fired it up, messed around a bit with some of the features ... and then realized I had no idea how to actually execute any of my Python code!\nI really like the look and feel/usability/features of Visual Studio Code, but I can't seem to find out how to run my Python code, a real killer because that's what I program primarily in .\nIs there is a way to execute Python code in Visual Studio Code?"
words_counter(content)
