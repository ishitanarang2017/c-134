import pandas as spd
import matplotlib.pyplot as plt
df = spd.read_csv("star_with_gravity.csv")
#print(df.head())
bools = []
for d in df.Distance:
    if d<100:
        bools.append(True)
    else:
        bools.append(False)
isdistance = spd.Series(bools)
stardist = df[isdistance]
stardist.reset_index(inplace=True,drop=True)
print(stardist.shape)
gravity_bold = []
for g in stardist.Gravity:
    if g<=350 and g>=150:
        gravity_bold.append(True)
    else:
        gravity_bold.append(False)
isgravity = spd.Series(gravity_bold)
finalstars = stardist[isgravity]
print(finalstars.shape)
finalstars.reset_index(inplace=True,drop=True)
finalstars.to_csv("filtered_stars.csv")