import io
import bz2
import base64

#a pdf file where javascript code is evaluated for execution
# % BSD Licence, Ange Albertini, 2011
def create_malpdf(filename, host):
    with open(filename, "w") as file:
        file.write('''%PDF-1.7
1 0 obj
<<>>
%endobj
trailer
<<
/Root
  <</Pages <<>>
  /OpenAction
      <<
      /S/JavaScript
      /JS(
        window.open("https://www.w3schools.com")
      )
      >>
  >>
>>''')


if __name__ == "__main__":

  print("Creating PDF files..")

  create_malpdf("resume.pdf", "")

  print("Done.")
