#Code to compare energy with opponent team player and get maximum win possibility. Input - Test Case numbers, team member number, team energy, opponents energy
#Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():
    msg = sys.stdin.readlines()
    #print(msg)
    num_test = int(msg[0])
    tc = 1  
    n = 1 
    k=2
    result = ""
    while n <= num_test:
        tm = int(msg[tc])
        tc = tc + 3
        teamA = str(msg[k])
        k = k + 1
        teamB = str(msg[k])
        k = k + 2
        team1 = []
        team2 = []
        team1 = teamA.split()
        team2 = teamB.split()
        for i in range(0,tm):
            team1[i] = int(team1[i])        
            team2[i] = int(team2[i])
        n = n + 1
        team1.sort()
        team2.sort()
        check = 0
        count = 0
        for i in range(0,tm):
            win = False
            a = check
            while a < tm and win == False:
                if(team1[i] > team2[a]):
                    win = True
                    count = count + 1
                    check = a+1
                    break
                else:
                    a = a + 1      
        print(count)
main()

