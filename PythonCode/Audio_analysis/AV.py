import subprocess

cmd = ['ffmpeg', '-i', '/Users/lisalocey/Desktop/HydroBIDE/results/movies/HydrobideVideo.mp4',
            '-i', '/Users/lisalocey/Desktop/HydroBIDE/results/movies/HydrobideSound.mp4',
            '-acodec', 'copy', '-vcodec', 'copy', '-f', 'avi',
            '/Users/lisalocey/Desktop/test.avi']

#process = subprocess.Popen(cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# and you can block util the cmd execute finish
#p.wait()

# or stdout, stderr = p.communicate()


#bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
#import subprocess
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
output = process.communicate()[0]