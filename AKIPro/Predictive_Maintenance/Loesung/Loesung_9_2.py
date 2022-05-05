# Eine Möglichkeit ist einen Alarm auszulösen, wenn alle Messungen innerhalb 
# einer Stunden (sechs aufeinander folgende Messungen) als Annomalie eingestuft werden

for i in range(5,len(time[test_idx])):
    # Ergänzen Sie hier ein Kriterium, wann ein Alarm ausgelöst werden soll
    if (annomaly[i-5:i].all()==True):
        print('Zeitpunkt:',date[test_idx][i])
        print('Warnung: Drohender Ausfall!')
        break