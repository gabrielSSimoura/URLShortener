import pyshorteners


s = pyshorteners.Shortener()
url = input("Enter the URL: ")
url = s.tinyurl.short(url)

print(url)




