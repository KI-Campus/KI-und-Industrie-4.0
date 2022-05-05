# Definition der Merkmale

def extract_features(file_name):
    df = pd.read_csv(path + file_name, sep='\t', header=None)
    values = df.values
    
    features = np.array([])
    
    # Standardabweichung (für jeden der vier Sensoren) -> 4 Merkmale
    std = df.std().values
    features = np.append(features, std)
    
    # Durchschnittlicher Frequenzanteil >2kHz (für jeden der vier Sensoren) -> 4 Merkmale
    for i in range(0,4):
        f, t, Sxx = signal.spectrogram(values[:,i], fs)
        idx = np.where(f>2000)[0]
        sum_loc = np.sum(Sxx[:,idx[0]:],axis=0)
        features = np.append(features, np.mean(sum_loc))
    
    # Maximalwert (für jeden der vier Sensoren) -> 4 Merkmale
    maxi = df.abs().max().values
    features = np.append(features, maxi)
    
    # Quadratisches Mittel (für jeden der vier Sensoren) -> 4 Merkmale
    rms = np.sqrt(np.mean(np.power(values,2),0))
    features = np.append(features, rms)
    
    # Scheitelfaktor (für jeden der vier Sensoren) -> 4 Merkmale
    crest = maxi/rms
    features = np.append(features, crest)
    
    # Durchschnittliche Frequenz mit größter Amplitude (für jeden der vier Sensoren) -> 4 Merkmale
    for i in range(0,4):
        f, t, Sxx = signal.spectrogram(values[:,i], fs)
        max_loc = np.argmax(Sxx,0)
        features = np.append(features, np.mean(f[max_loc]))

    return features

# Extraktion der Merkmale für alle Dateien

n_files = 984
n_features = 24 # Hier die Zahl der Merkmale eintragen!

T = np.array([])
X = np.array([])

for dirpath, dirnames, files in os.walk(path):
    for file_name in files:
        features = extract_features(file_name)
        T = np.append(T, file_name.split('.'))
        X = np.append(X, features)
        
X = X.reshape(n_files,n_features)
T = np.array(T,dtype=float)
T = T.reshape(n_files,-1)

print('Merkmale Datei 1:', X[0])