import sys, getopt
import os.path
import urllib2
import time

def main(argv):
  fileInput = ""
  if len(sys.argv) < 3:
      print "usage is like checker.py -i <input file>"
      sys.exit(2)
  else:
    try:
      opts, args = getopt.getopt(argv, "i:", ["input="])
    except getopt.GetoptError:
      print "usage is like checker.py -i <input file>"
      sys.exit(2)

  for opt, arg in opts:
      if opt in ("-i", "--input"):
        fileName = arg

  checkFile(fileName)

def checkFile(fileName):
    if os.path.isfile(fileName):
      with open(fileName) as f:
        totalLine = 0
        processLine = 0
        outputLines = ""
        for line in f:
            totalLine = totalLine + 1
            fileResult = line.split("/")
            processed = fileResult[-1].split(".")
            if len(processed) > 1:
              processLine = processLine + 1
              time.sleep(0.1)
              if checkHTTPObject(line) == 200:
                outputLines =  "%s is accessible\n" %(line.rstrip())
              else:
                outputLines =  "%s is giving %s code\n" %(line.rstrip(), checkHTTPObject(line))

              with open("output.txt", "a") as outputFile:
                outputFile.write(outputLines)
                print outputLines.rstrip()

      print "Processing %s file, skipping folder and file without extension of total %s" %(processLine,totalLine,)
    else:
      print "Sorry can't find the file. Please check your input"
      sys.exit(2)


def checkHTTPObject(path):
    try:
      ret = urllib2.urlopen(path)
      return ret.code
    except urllib2.HTTPError as e:
      return e.code


if __name__  == "__main__":
    main(sys.argv[1:])
