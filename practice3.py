#EXERCISE 3 - Run timing

def run_timing():
    totalRuns = 0
    totalTime = 0
    while True:     
        timing = input('Enter 10 km run time: ').strip()
        
        if not timing:   
            break
        
        totalTime += float(timing)
        totalRuns += 1
    averageTime = totalTime / totalRuns
    print(f'Average of {averageTime}, over {totalRuns} runs')
    
run_timing()
