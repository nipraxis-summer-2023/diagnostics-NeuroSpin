Project OUTLIERS

(1) Adapt DVARS from exercices in findoutlie/metrics.py => DONE
(2) Fill in findoutlie/detectors.py for IQR (interquartile range) (but not only)
    - It is the region between the 75th and 25th percentile (meaning 75-25=50% of the data)
    - TO DO : lier le script 'metrics' (calcul DVARS) avec 'detectors' (calcul IQR)
(3) Fill in findoutlie/outfind.py 
    - Dans detect_outliers : il faut que l'on calcule une métrique (example : métrique 1 = FD de l'image pour chaque pas de temps = une liste de valeur, injectée dans une des fonctions de detectors) ; important: on appelle à fois les fonctions de '/metrics' et à la fois de '/detectors'
    - Dans detect_outliers : (au-dessus) on va pouvoir le faire pour d'autres métriques
(4) Test on one subject
(5) Test on the 9 other subjects 
(6) Add other image quality metrics: (cf. detect_outliers)
    ARTIFACTS MEASURE:
        - Framewise displacement: controls for movement => was the outlier detected because of a sudden move?
            FORMULA: FDi =∣Δxi∣+∣Δyi∣+∣Δzi∣+∣Δαi∣+∣Δβi∣+∣Δγi∣ (from Power et al., 2012)
                EXPLANATION: expresses instantaneous head-motion; i is the timepoint; x, y, z are the translational realignment parameters (RPs); α, β, γ are the rotational RPs
    TEMPORAL INFORMATION:
        - tSNR: gives information on the temporal evolution of the signal to noise ratio => was the outlier detected because of a disturbance in signal?
            FORMULA: tSNR = (Mean timecourse signal) / (SD timecourse noise) (from Krüger et al., 2001)
                EXPLANATION: Mean timecourse signal, is the average BOLD signal across time and SD timecourse noise, the SD of the corresponding voxel timecourse; higher values are better.
(7) Decision criteria: 
    Based on the combination of these 3 parameters:
    - DVARS
    - FD
    - tSNR
    And the combination of these 2 detectors:
    - IQR
    - ?

=> OBJECTIF : 3 métriques (DVARS, FD, tSNR?) + 2 detectors (IQR, ?)