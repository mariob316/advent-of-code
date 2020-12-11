from datetime import datetime
import subprocess
from pathlib import Path

class AOC():

    def __init__(self) -> None:
        self.input = []
        self.session = ""
        self.download_input()
        
    
    @property
    def day():
        pass
    
    def part1():
        pass
    
    def part2():
        pass

    def download_input(self):
        year = datetime.today().strftime('%Y')
        f_name = 'day' + ('0' if (self.day < 10) else '') + self.day + '.txt'
        if Path('input'/f_name).is_file:
            return Path('input'/f_name)
    
        cmd = f'curl https://adventofcode.com/{year}/day/{self.day}/input --cookie "session={self.session}"'
        output = subprocess.check_output(cmd, shell=True)
        with open('input/'+f_name, 'w+') as f:
            f.write(output.decode('utf-8'))
        

    